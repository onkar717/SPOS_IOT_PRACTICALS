class Assembler:
    def __init__(self):
        self.symbol_table = {}  # Symbol table to hold labels and their addresses
        self.opcode_table = {   # Opcode table for instructions
            'LOAD': '0001',
            'STORE': '0010',
            'ADD': '0011',
            'SUB': '0100',
            'JMP': '0101',
            'JZ': '0110',
            'NOP': '1111'
        }
        self.directives = ['ORG', 'EQU']
        self.current_address = 0  # Current address in memory

    def first_pass(self, assembly_code):
        """Perform the first pass of the assembler."""
        lines = assembly_code.splitlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith(';'):  # Ignore empty lines and comments
                continue
            
            # Split the line into parts
            parts = line.split()
            label = None
            instruction = None
            operand = None
            
            # Check for label
            if parts[0].endswith(':'):
                label = parts[0][:-1]  # Remove the colon
                self.symbol_table[label] = self.current_address
                parts = parts[1:]  # Remove the label from parts
            
            # Check for directives
            if parts and parts[0] in self.directives:
                directive = parts[0]
                if directive == 'ORG':
                    self.current_address = int(parts[1])  # Set the current address
                elif directive == 'EQU':
                    # EQU directive handling can be added here
                    pass
                continue
            
            # Handle instructions
            if parts:
                instruction = parts[0]
                if instruction in self.opcode_table:
                    self.current_address += 1  # Increment address for each instruction

    def display_symbol_table(self):
        """Display the symbol table."""
        print("\nSymbol Table:")
        for label, address in self.symbol_table.items():
            print(f"{label}: {address}")

# Example usage
if __name__ == "__main__":
    assembler = Assembler()
    
    assembly_code = """
    START:  ORG 100
            LOAD A
            ADD B
            STORE C
    LOOP:   JMP START
            NOP
    A:      EQU 5
    B:      EQU 10
    C:      EQU 0
    """
    
    assembler.first_pass(assembly_code)
    assembler.display_symbol_table()
