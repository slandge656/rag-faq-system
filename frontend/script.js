async function askQuestion() {
  const query = document.getElementById("query").value;
  const response = await fetch("http://localhost:8000/query/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });
  const data = await response.json();
  document.getElementById("response").innerText =
    data.answer || "No answer found.";
}
