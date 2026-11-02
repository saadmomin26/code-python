from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-5-nano",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)
Client=OpenAI(
    api_key="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"
)

completion = Client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant, skilled in general task like alexa and google and cloud."},
        {"role": "user", "content": "what is coding."}
    ]
)

print(completion.choices[0].message.content)
