const input = document.getElementById("user-input");
const sendBtn = document.querySelector("button");

async function search() {
    const query = document.getElementById("query").value;
    const resultsDiv = document.getElementById("results");
    const loading = document.getElementById("loading");

    resultsDiv.innerHTML = "";
    loading.classList.remove("hidden");

    const response = await fetch("http://127.0.0.1:8000/search?q=" + query);
    const data = await response.json();

    loading.classList.add("hidden");

    // 👉 AI Answer (NEW)
    const answerDiv = document.createElement("div");
    answerDiv.className = "result";
    answerDiv.innerHTML = `
        <h2>🤖 AI Answer</h2>
        <p>${data.answer}</p>
    `;
    resultsDiv.appendChild(answerDiv);

    // 👉 Search Results
    data.results.forEach(item => {
        const div = document.createElement("div");
        div.className = "result";

        div.innerHTML = `
            <h3>${item.title}</h3>
            <p>${item.content}</p>
        `;

        resultsDiv.appendChild(div);
    });
}

function addMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");

  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);

  messageDiv.innerText = text;

  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  return messageDiv; // 🔥 important
}

async function typeText(element, text) {
  element.innerText = "";

  for (let i = 0; i < text.length; i++) {
    element.innerText += text[i];
    await new Promise(resolve => setTimeout(resolve, 45)); // speed control
  }
}

async function sendMessage() {
  
  const text = input.value;
  

  if (!text) return;

  // Disable input
  input.disabled = true;
  sendBtn.disabled = true;

  // Add user message
  addMessage(text, "user");
  input.value = "";

  // 🔥 Better placeholder
  const aiMessage = addMessage("▌", "ai");

  // 🔥 Session ID (dynamic)
  let sessionId = localStorage.getItem("session_id");
  if (!sessionId) {
    sessionId = Math.random().toString(36).substring(2);
    localStorage.setItem("session_id", sessionId);
  }

  try {
    let fullText = "";

    const eventSource = new EventSource(
      `http://127.0.0.1:8000/stream?message=${encodeURIComponent(text)}&session_id=${sessionId}`
    );

    eventSource.onmessage = (event) => {
      if (!event.data.includes("🤔")) {
         fullText += event.data;
}

      // 🔥 live typing with cursor
      aiMessage.innerText = fullText + " ▌";
    };

    eventSource.onerror = () => {
      eventSource.close();

      // remove cursor
      aiMessage.innerText = fullText;

      // enable input again
      input.disabled = false;
      sendBtn.disabled = false;
    };

  } catch (error) {
    aiMessage.innerText = "Error connecting to server";

    input.disabled = false;
    sendBtn.disabled = false;
  }
}

input.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});

  
document.getElementById("user-input")
  .addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
  });