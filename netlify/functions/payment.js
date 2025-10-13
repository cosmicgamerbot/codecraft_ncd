exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: JSON.stringify({ error: 'Method not allowed' }) };
  }
  try {
    const { amount, method } = JSON.parse(event.body);
    await new Promise(resolve => setTimeout(resolve, 2000));
    const transactionId = `TXN${Date.now()}`;
    return {
      statusCode: 200,
      body: JSON.stringify({
        success: true,
        transactionId,
        amount,
        method
      })
    };
  } catch (error) {
    return { statusCode: 500, body: JSON.stringify({ error: error.message }) };
  }
};