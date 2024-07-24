// Chat.js
import React, { useState, useEffect } from 'react';

const Chat = ({ roomName }) => {
  const [socket, setSocket] = useState(null);
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');

  useEffect(() => {
    const newSocket = new WebSocket(`ws://localhost:8000/ws/chat/${roomName}/`);
    setSocket(newSocket);

    newSocket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      setMessages(prevMessages => [...prevMessages, data.message]);
    };

    return () => newSocket.close();
  }, [roomName]);

  const sendMessage = () => {
    if (socket && inputMessage) {
      socket.send(JSON.stringify({ message: inputMessage }));
      setInputMessage('');
    }
  };

  return (
    <div>
      <div>
        {messages.map((message, index) => (
          <p key={index}>{message}</p>
        ))}
      </div>
      <input
        value={inputMessage}
        onChange={(e) => setInputMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Chat;
