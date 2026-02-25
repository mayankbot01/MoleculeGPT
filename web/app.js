const chatContainer = document.getElementById('chat-container');
const taskInput = document.getElementById('task-input');
const sendBtn = document.getElementById('send-btn');

function addMessage(role, text) {
    const wrapper = document.createElement('div');
    wrapper.className = role === 'user' ? 'flex justify-end' : 'flex justify-start';
    
    const bubble = document.createElement('div');
    bubble.className = role === 'user' 
        ? 'bg-indigo-600 text-white p-3 rounded-lg chat-bubble shadow-sm' 
        : 'bg-indigo-100 text-indigo-800 p-3 rounded-lg chat-bubble shadow-sm';
    
    bubble.innerText = text;
    wrapper.appendChild(bubble);
    chatContainer.appendChild(wrapper);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

sendBtn.addEventListener('click', async () => {
    const task = taskInput.value.trim();
    if (!task) return;

    addMessage('user', task);
    taskInput.value = '';
    taskInput.disabled = true;
    sendBtn.disabled = true;

    try {
        const response = await fetch('/run', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ task: task })
        });

        if (!response.ok) {
            throw new Error('Failed to execute task');
        }

        const data = await response.json();
        addMessage('assistant', data.result);
    } catch (error) {
        addMessage('assistant', 'Error: ' + error.message);
    } finally {
        taskInput.disabled = false;
        sendBtn.disabled = false;
        taskInput.focus();
    }
});

taskInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendBtn.click();
});
