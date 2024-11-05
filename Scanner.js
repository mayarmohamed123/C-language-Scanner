document.getElementById("scanButton").addEventListener("click", () => {
  const code = document.getElementById("codeInput").value;
  const tokens = scanCode(code);
  document.getElementById("output").textContent = tokens
    .map((token) => `${token.type}: ${token.value}`)
    .join("\n");
});

function scanCode(code) {
  const patterns = [
    {
      type: "keyword",
      regex: /\b(for|int|return|if|else|while|char|float|double|void|main)\b/g,
    },
    { type: "identifier", regex: /\b[A-Za-z_][A-Za-z0-9_]*\b/g },
    { type: "operator", regex: /[+\-*/=<>!&|]+/g },
    { type: "numeric", regex: /\b\d+(\.\d+)?(e[+-]?\d+)?\b/g }, // Numeric constant including scientific notation
    { type: "charConst", regex: /'[^']'/g }, // Character constant
    { type: "specialChar", regex: /[{}();,]/g }, // Special characters
    { type: "comment", regex: /\/\/[^\n]*/g }, // Single-line comments
    { type: "whitespace", regex: /\s+/g }, // Whitespace
  ];

  const tokens = [];
  let lastIndex = 0;

  while (lastIndex < code.length) {
    let matchFound = false;

    for (const { type, regex } of patterns) {
      regex.lastIndex = lastIndex;
      const match = regex.exec(code);

      if (match && match.index === lastIndex) {
        // Only push non-whitespace tokens
        if (type !== "whitespace") {
          tokens.push({ type, value: match[0] });
        }
        lastIndex += match[0].length;
        matchFound = true;
        break;
      }
    }

    if (!matchFound) {
      lastIndex++; // Move past unrecognized character
    }
  }

  return tokens;
}
