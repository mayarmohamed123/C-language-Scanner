class TopDownParser:
    def __init__(self):
        self.grammar = {}
        self.first_terminals = {}

    def input_grammar(self):
        """Take grammar input dynamically from the user."""
        print("\U0001F447 Grammars \U0001F447")
        self.grammar = {}
        self.first_terminals = {}

        for non_terminal in ['S', 'B']:
            print(f"Enter two rules for non-terminal '{non_terminal}':")
            rules = []
            for i in range(2):
                rule = input(f"Rule {i + 1}: {non_terminal} -> ").strip()
                rules.append(rule)

            self.grammar[non_terminal] = rules

        if not self.validate_simple_grammar():
            print("The Grammar isn't simple.")
            return False

        print("The Grammar is simple and valid.")
        return True

    def validate_simple_grammar(self):
        """Check if the input grammar is simple."""
        for non_terminal, rules in self.grammar.items():
            first_letters = set()
            for rule in rules:
                if len(rule) == 0 or not rule[0].islower():
                    return False

                first_terminal = rule[0]
                if first_terminal in first_letters:
                    return False
                first_letters.add(first_terminal)

                self.first_terminals[non_terminal] = first_letters
        return True

    def parse(self, string, non_terminal):
        """Recursive Descent Parser."""
        if not string:
            return None

        for rule in self.grammar[non_terminal]:
            if string.startswith(rule[0]):
                remaining = string[len(rule[0]):]
                alpha = rule[1:]

                for char in alpha:
                    if char.isupper():
                        remaining = self.parse(remaining, char)
                        if remaining is None:
                            break
                    else:
                        if not remaining.startswith(char):
                            break
                        remaining = remaining[1:]

                else:
                    return remaining

        return None

    def input_sequence(self):
        """Take a sequence of characters and validate it."""
        sequence = input("Enter the string to be checked: ").strip()
        remaining = self.parse(sequence, 'S')

        if remaining == '':
            print("Your input String is Accepted.")
        else:
            print("Your input String is Rejected.")

    def run(self):
        """Infinite execution loop."""
        while True:
            print("=========================================")
            print("1-Another Grammar.")
            print("2-Another String.")
            print("3-Exit.")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                if not self.input_grammar():
                    continue
            elif choice == '2':
                if not self.grammar:
                    print("Please enter a valid grammar first.")
                    continue
                self.input_sequence()
            elif choice == '3':
                print("Exiting.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    parser = TopDownParser()
    parser.run()
