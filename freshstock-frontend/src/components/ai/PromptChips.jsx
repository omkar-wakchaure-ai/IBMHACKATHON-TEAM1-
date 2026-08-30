import React from 'react';
import { Sparkles } from 'lucide-react';

const PromptChips = ({ onSelectPrompt }) => {
  const prompts = [
    "Which products expire this week?",
    "Why is the tomato order high?",
    "Forecasted spend for next week?"
  ];

  return (
    <div className="flex flex-wrap gap-2 mt-4">
      {prompts.map((prompt, idx) => (
        <button
          key={idx}
          onClick={() => onSelectPrompt(prompt)}
          className="flex items-center space-x-1.5 px-3 py-1.5 bg-blue-50/50 hover:bg-blue-50 border border-blue-100 rounded-full text-xs font-medium text-blue-600 transition-colors"
        >
          <Sparkles size={12} className="text-blue-400" />
          <span>{prompt}</span>
        </button>
      ))}
    </div>
  );
};

export default PromptChips;
