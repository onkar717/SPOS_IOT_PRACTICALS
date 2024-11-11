class Macro:
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def __str__(self):
        return f"Macro(Name: {self.name}, Parameters: {self.parameters}, Body: {self.body})"


class MacroProcessor:
    def __init__(self):
        self.macro_table = {}  # Macro table to hold macro definitions
        self.source_code = []   # Source code lines
        self.output_code = []   # Output code after macro expansion

    def pass_one(self, source_code):
        """Perform the first pass of the macro processor."""
        lines = source_code.splitlines()
        in_macro_definition = False
        current_macro = None

        for line in lines:
            line = line.strip()
            if not line or line.startswith(';'):  # Ignore empty lines and comments
                continue
            
            # Check for macro definition
            if line.startswith('MACRO'):
                in_macro_definition = True
                parts = line.split()
                macro_name = parts[1]
                parameters = parts[2:] if len(parts) > 2 else []
                current_macro = Macro(macro_name, parameters, [])
                continue
            
            # Check for macro end
            if in_macro_definition and line == 'ENDM':
                in_macro_definition = False
                if current_macro:
                    self.macro_table[current_macro.name] = current_macro
                continue
            
            # If we are in a macro definition, add the line to the macro body
            if in_macro_definition and current_macro:
                current_macro.body.append(line)
            else:
                # If not in a macro definition, add the line to the output code
                self.output_code.append(line)

    def display_macro_table(self):
        """Display the macro table."""
        print("\nMacro Table:")
        for macro_name, macro in self.macro_table.items():
            print(macro)

    def display_output_code(self):
        """Display the output code."""
        print("\nOutput Code:")
        for line in self.output_code:
            print(line)


# Example usage
if __name__ == "__main__":
    macro_processor = MacroProcessor()
    
    source_code = """
    ; This is a sample macro processor
    MACRO ADDITION A, B
        LOAD A
        ADD B
        STORE RESULT
    ENDM

    MACRO MULTIPLICATION A, B
        LOAD A
        MUL B
        STORE RESULT
    ENDM

    START:  ADDITION 5, 10
            MULTIPLICATION 2, 3
    """
    
    # Pass I
    macro_processor.pass_one(source_code)
    macro_processor.display_macro_table()
    macro_processor.display_output_code()
