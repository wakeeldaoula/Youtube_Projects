import nltk
from nltk.chat.util import Chat, reflections

# Define the conversation patterns and responses
conversation_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! It's nice to meet you.", "Hi %1! How can I assist you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Greetings! How can I help?"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but thanks for asking!", "I'm functioning well! How about you?"]
    ],
    [
        r"what is your name?",
        ["I am a friendly chatbot designed to assist you.", "You can call me your virtual assistant."]
    ],
    [
        r"what can you do?",
        ["I can chat with you, provide information, and help answer your questions!", 
         "I'm here to assist you with various queries."]
    ],
    [
        r"quit",
        ["Goodbye! Have a wonderful day!", "Take care! See you soon!"]
    ],
    [
        r"(.*)",
        ["I’m not sure how to respond to that. Can you elaborate?", "That’s interesting! Tell me more."]
    ]
]

# Initialize the chatbot
chatbot = Chat(conversation_pairs, reflections)

def start_chat():
    print("Hello! I'm a friendly chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()