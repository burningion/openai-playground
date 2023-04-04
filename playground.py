import os
import openai
from rich import print

# have this environment variable set
openai.api_key = os.getenv("OPENAI_API_KEY")

messagesList = []
messagesList.append({"role": "system", "content": "you are an experienced python backend developer who cares deeply about security"})
messagesList.append({"role": "user", "content": "write me a fastapi python program to accept file uploads and store them on amazon s3"})
response = openai.ChatCompletion.create(model="gpt-4", messages=messagesList)

resContent = response["choices"][0]["message"]["content"]
print(resContent)
messagesList.append({"role": "assistant", "content": resContent})
while True:
    next_prompt = input("enter next prompt (q to quit): ")
    if next_prompt == "q":
        import csv
        with open('chatlog.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, messagesList[0].keys())
            writer.writeheader()
            for message in messagesList:
                writer.writerow(message)
        exit()
    messagesList.append({"role": "user", "content": str(next_prompt)})
    response = openai.ChatCompletion.create(model="gpt-4", messages=messagesList)
    resContent = response["choices"][0]["message"]["content"]
    print(resContent)
    messagesList.append({"role": "assistant", "content": resContent})