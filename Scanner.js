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
      regex: /\b(int|return|if|else|while|for|char|float|double|void|main)\b/g,
    },
    { type: "identifier", regex: /\b[A-Za-z_][A-Za-z0-9_]*\b/g },
    { type: "operator", regex: /[+\-*/=<>!&|]/g },
    { type: "number", regex: /\b\d+(\.\d+)?\b/g },
    { type: "charConst", regex: /'[^']'/g },
    { type: "stringConst", regex: /"[^"]*"/g },
    { type: "specialChar", regex: /[{}();,]/g },
    { type: "comment", regex: /\/\/[^\n]*|\/\*[\s\S]*?\*\//g },
  ];

  const tokens = [];
  let lastIndex = 0;

  while (lastIndex < code.length) {
    let matchFound = false;

    for (const { type, regex } of patterns) {
      regex.lastIndex = lastIndex;
      const match = regex.exec(code);

      if (match && match.index === lastIndex) {
        tokens.push({ type, value: match[0] });
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
