import React, { useState } from 'react';
import { Send, Bot, User } from 'lucide-react';
import PromptChips from './PromptChips';

const ChatWidget = () => {
  const [messages, setMessages] = useState([
    { sender: 'ai', text: 'Hello! I am Granite, your AI Warehouse Assistant. How can I help optimize your stock today?' }
  ]);
  const [input, setInput] = useState('');

  const handleSend = (text = input) => {
    if (!text.trim()) return;
    setMessages(prev => [...prev, { sender: 'user', text }]);
    setInput('');
    
    // Dummy AI Response
    setTimeout(() => {
      setMessages(prev => [...prev, { 
        sender: 'ai', 
        text: 'Based on the predictive model, tomato demand is up 15% due to the upcoming festival weekend. I recommend securing stock immediately.' 
      }]);
    }, 1000);
  };

  return (
    <div className="flex flex-col h-[500px] w-full max-w-md bg-white rounded-2xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100 overflow-hidden">
      <div className="bg-blue-600 p-4 flex items-center space-x-3 text-white">
        <Bot size={24} />
        <div>
          <h3 className="font-semibold text-sm">IBM Granite Assistant</h3>
          <p className="text-blue-200 text-xs">Powered by watsonx.ai</p>
        </div>
      </div>
      
      <div className="flex-1 p-4 overflow-y-auto space-y-4 bg-gray-50/50">
        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[80%] p-3 rounded-2xl text-sm ${
              msg.sender === 'user' 
                ? 'bg-blue-600 text-white rounded-tr-none' 
                : 'bg-white border border-gray-100 text-gray-700 shadow-sm rounded-tl-none'
            }`}>
              {msg.text}
            </div>
          </div>
        ))}
      </div>
      
      <div className="p-4 bg-white border-t border-gray-50">
        <div className="flex items-center space-x-2 relative">
          <input 
            type="text" 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            placeholder="Ask about your inventory..."
            className="flex-1 pl-4 pr-10 py-3 bg-gray-50 border-none rounded-xl text-sm focus:ring-2 focus:ring-blue-100 outline-none transition-all"
          />
          <button 
            onClick={() => handleSend()}
            className="absolute right-2 p-1.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            <Send size={16} />
          </button>
        </div>
        <PromptChips onSelectPrompt={handleSend} />
      </div>
    </div>
  );
};

export default ChatWidget;
