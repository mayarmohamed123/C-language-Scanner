import re

def scan_code(code):
    patterns = [
        {'type': 'keyword', 'regex': r'\b(for|int|return|if|else|while|char|float|double|void|main)\b'},
        {'type': 'identifier', 'regex': r'\b[A-Za-z_][A-Za-z0-9_]*\b'}, 
        {'type': 'operator', 'regex': r'[+\-*/=<>!&|]+|=='}, 
        {'type': 'numeric', 'regex': r'\b\d+(\.\d+)?([eE][+-]?\d+)?\b'},  
        {'type': 'charConst', 'regex': r"'(\\.|[^'\\])'"}, 
        {'type': 'specialChar', 'regex': r'[{}();,]'}, 
        {'type': 'comment', 'regex': r'//[^\n]*|/\*[\s\S]*?\*/'}, 
        {'type': 'whitespace', 'regex': r'\s+'}, 
    ]

    tokens = []
    last_index = 0

    while last_index < len(code):
        match_found = False

        for pattern in patterns:
            regex = re.compile(pattern['regex'])
            match = regex.match(code, last_index)

            if match:
                tokens.append({'type': pattern['type'], 'value': match.group(0)})
                last_index += len(match.group(0))
                match_found = True
                break

        if not match_found:
            last_index += 1

    return tokens

# Example usage of the scanner
code_snippet = """
int main() {
    int count = 10;
    for (int i = 0; i < count; i++) {
        printf("Hello, World!");
    }
    return 0;
}
// This is a comment
/* This is a 
multi-line comment */
float number = 3.14e-2;
char c = 'A';
"""

tokens = scan_code(code_snippet)
for token in tokens:
    print(token)
