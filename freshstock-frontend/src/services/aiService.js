import { apiClient } from './api';

export const queryWatsonX = async (userPrompt, contextData) => {
  const response = await apiClient.post('/ai_assistant/query', {
    prompt: userPrompt,
    context: contextData
  });
  return response.data;
};
