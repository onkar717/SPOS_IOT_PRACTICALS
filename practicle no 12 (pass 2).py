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
        self.intermediate_code = []  # Intermediate code from Pass-I
        self.current_address = 0  # Current address in memory

    def pass_one(self, assembly_code):
        """Perform the first pass of the assembler."""
        lines = assembly_code.splitlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith(';'):  # Ignore empty lines and comments
                continue
            
            # Split the line into parts
            parts = line.split()
            label = None
            
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
                    self.intermediate_code.append((instruction, parts[1:] if len(parts) > 1 else []))
                    self.current_address += 1  # Increment address for each instruction

    def pass_two(self):
        """Perform the second pass of the assembler."""
        machine_code = []
        for instruction, operands in self.intermediate_code:
            opcode = self.opcode_table[instruction]
            operand_code = ''
            for operand in operands:
                if operand in self.symbol_table:
                    # Resolve the address from the symbol table
                    operand_code += format(self.symbol_table[operand], '04b')  # Convert to 4-bit binary
                else:
                    # Handle immediate values or errors
                    operand_code += format(int(operand), '04b')  # Assuming operand is a number
            machine_code.append(f"{opcode} {operand_code}")

        return machine_code

    def display_symbol_table(self):
        """Display the symbol table."""
        print("\nSymbol Table:")
        for label, address in self.symbol_table.items():
            print(f"{label}: {address}")

    def display_intermediate_code(self):
        """Display the intermediate code."""
        print("\nIntermediate Code:")
        for instruction, operands in self.intermediate_code:
            print(f"{instruction} {' '.join(operands)}")

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
    
    # Pass I
    assembler.pass_one(assembly_code)
    assembler.display_symbol_table()
    assembler.display_intermediate_code()
    
    # Pass II
    machine_code = assembler.pass_two()
    print("\nMachine Code:")
    for code in machine_code:
        print(code)
