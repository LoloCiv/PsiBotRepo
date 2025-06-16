const chatContainer = document.getElementById('chat-container');
const userInput      = document.getElementById('user-input');
const sendBtn        = document.getElementById('send-button');

// Añade una burbuja al chat
function addMessage(text, sender) {
  const div = document.createElement('div');
  div.className = `message ${sender}`;
  div.textContent = text;
  chatContainer.appendChild(div);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Llama al backend
async function sendMessage() {
  const text = userInput.value.trim();
  if (!text) return;

  addMessage(text, 'user');
  userInput.value = '';
  userInput.focus();

  try {
    const res   = await fetch('/chat', {
      method : 'POST',
      headers: { 'Content-Type': 'application/json' },
      body   : JSON.stringify({ mensaje: text })
    });
    const data  = await res.json();
    addMessage(data.respuesta || '⚠️ Error de respuesta.', 'bot');
  } catch (err) {
    console.error(err);
    addMessage('⚠️ Error al conectar con el servidor.', 'bot');
  }
}

// Eventos
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', e => {
  if (e.key === 'Enter') sendMessage();
});
