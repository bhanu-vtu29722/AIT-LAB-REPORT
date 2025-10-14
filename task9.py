import openai


client = openai.OpenAI(api_key=" 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")
                       # Pass API key here

messages = []

system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type your query (type 'quit' to exit):")

while True:
    user_message = input()
    if user_message.lower() == "quit":
        print("Exiting chat...")
        break

    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print("\n" + reply + "\n")
