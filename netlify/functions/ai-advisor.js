exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: JSON.stringify({ error: 'Method not allowed' }) };
  }
  try {
    const { mealName } = JSON.parse(event.body);
    const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
    
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1500,
        messages: [{
          role: 'user',
          content: `As a nutrition expert, analyze "${mealName}" and provide healthy alternatives.`
        }]
      })
    });
    
    const data = await response.json();
    return {
      statusCode: 200,
      body: JSON.stringify({ success: true, advice: data.content?.[0]?.text })
    };
  } catch (error) {
    return { statusCode: 500, body: JSON.stringify({ error: error.message }) };
  }
};