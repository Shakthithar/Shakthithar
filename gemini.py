import google.generativeai as genai

# Set your API key
API_KEY = "AIzaSyC8PKlS5Ippsf9QPdj7G6kG76D-RrxxaTA"
genai.configure(api_key=API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro')  # Use the Gemini Pro model

# Chatbot function
def chatbot():
    print("Chatbot: Hello! How can I assist you today? (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        # Send user input to the model
        response = model.generate_content(user_input)
        
        # Print the chatbot's response
        print(f"Chatbot: {response.text}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()