import groq

client = groq.Client(api_key="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") #You can take your own free api key from groq.com

def get_ai_response(user):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role":"user", "content":user}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f'Error: {e}'

if __name__ == "__main__":
    print("Welcome to your AI chatbot! Type 'exit to quit'")
    while True:
        user_input = input('\nYou: ')
        if user_input.lower() in ['exit', 'quit', 'stop']:
            print("\nGoodbye! :) ")
            break
        response = get_ai_response(user_input)
        print("AI:", response)


