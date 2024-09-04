from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Sample FAQs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to answer your FAQs.",]
    ],
    [
        r"how to use this product?",
        ["You can start by following the instructions provided in the user manual.",]
    ],
    [
        r"what is your purpose?",
        ["I am here to answer your questions and provide information.",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.respond(userText))

if __name__ == "__main__":
    app.run(debug=True)
