import nltk
from nltk.chat.util import Chat, reflections

# Sample conversation pairs
pairs = [
    [
        r"(hi|hello|hey|hola|howdy)(.*)",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created for your project. You can call me ChatBot.",]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but I'm doing great! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem at all!", "No worries!", "It's okay!"]
    ],
    [
        r"(.*) (help|support) (.*)",
        ["I'm here to help! Please tell me what you need assistance with.",]
    ],
    [
        r"(.*) your name ?",
        ["My name is ChatBot. Nice to meet you!",]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer questions, and provide information.",]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you.",]
    ],
]

# Default responses for unrecognized inputs
fallback_responses = [
    "I didn't understand that. Could you please rephrase?",
    "I'm not sure how to respond to that.",
    "Can you please clarify your question?"
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def main():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"ChatBot: {response}")
        else:
            print(f"ChatBot: {fallback_responses}")

if __name__ == "__main__":
    main()
