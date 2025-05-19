from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # safer for deployment

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and empathetic mental health chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        bot_reply = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        bot_reply = "Sorry, I couldn't respond at the moment."

    return {'reply': bot_reply}

#if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

