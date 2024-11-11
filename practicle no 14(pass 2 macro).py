class MacroProcessor:
    def __init__(self):
        # Macro table to store macro definitions
        self.macro_table = {}
        # Source code lines
        self.source_code = []
        # Expanded code lines
        self.expanded_code = []

    def add_macro(self, macro_name, macro_body):
        """Add a macro definition to the macro table."""
        self.macro_table[macro_name] = macro_body

    def load_source_code(self, source_lines):
        """Load source code lines."""
        self.source_code = source_lines

    def expand_macros(self):
        """Expand macros in the source code."""
        for line in self.source_code:
            line = line.strip()
            if line.startswith("MACRO"):
                # Skip macro definition lines
                continue
            elif line in self.macro_table:
                # If line is a macro, expand it
                self.expanded_code.extend(self.macro_table[line])
            else:
                # Otherwise, just add the line as it is
                self.expanded_code.append(line)

    def get_expanded_code(self):
        """Return the expanded code."""
        return self.expanded_code


# Example usage
if __name__ == "__main__":
    # Create a macro processor instance
    macro_processor = MacroProcessor()

    # Define macros
    macro_processor.add_macro("PRINT_HELLO", [
        "LOAD R1, 'Hello, World!'",
        "CALL PRINT"
    ])
    macro_processor.add_macro("ADD_NUMBERS", [
        "LOAD R1, A",
        "LOAD R2, B",
        "ADD R1, R2",
        "STORE R1, C"
    ])

    # Load source code
    source_code = [
        "MACRO PRINT_HELLO",
        "ENDMACRO",
        "MACRO ADD_NUMBERS",
        "ENDMACRO",
        "PRINT_HELLO",
        "ADD_NUMBERS",
        "END"
    ]
    macro_processor.load_source_code(source_code)

    # Expand macros
    macro_processor.expand_macros()

    # Get and print the expanded code
    expanded_code = macro_processor.get_expanded_code()
    print("Expanded Code:")
    for line in expanded_code:
        print(line)
