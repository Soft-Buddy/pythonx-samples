import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'what is your name', ['I am a chatbot.', 'You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'your favorite (movie|book|song)', ['I am a chatbot and do not have preferences.']),
    (r'weather', ['I do not have real-time information. You can check a weather website.']),
    (r'(.*) age (.*)', ['I am just a computer program and do not have an age.']),
    (r'(.*) (love|like) (.*)', ['I am a machine and do not have feelings, but I am here to help!']),
    (r'how (can|do) you help', ['I can provide information, answer questions, or just chat with you.']),
    (r'what (can|do) you do', ['I can assist with a variety of topics, just ask me anything!']),
    (r'who created you', ['I was created by You.']),
    (r'where are you from', ['I am a computer program, so I do not have a specific location.']),
    (r'tell me a joke', ['Why did the computer go to therapy? It had too many bytes of emotional baggage!']),
    (r'favorite color', ['I do not have a favorite color.']),
    (r'tell me about yourself', ['I am a chatbot created with Python and NLTK.']),
    (r'(.*) thank you (.*)', ['You\'re welcome!', 'Anytime!']),
    (r'how (does|do) (.*) work', ['I can help answer questions, but specifics depend on the topic.']),
    (r'what time is it', ['I do not have access to real-time information, you can check your device.']),
    (r'who are you', ['I am a chatbot designed to assist and chat with users.']),
    (r'(.*)', ['I am sorry, I did not understand that.', 'Can you please rephrase?']),
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Run the chatbot
print("Hello! I am a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
