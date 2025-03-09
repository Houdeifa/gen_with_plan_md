output_name = "plan.md"

tasks = """
    tasks:
     - the project is to create an android app using kivy with python
     - the app is a classic snake app which need to contain some menues
     - the game can have multpule "skins" which changes the style of the game once the game launched
     - in the app we have to have the ability to buy a skin
     - for the first version the buy button will add the same amount of money but next we will need to add a real paying api
"""
promt = ""
with open("prompt_creating_project.txt","r") as f:
    promt = f.read()

if promt == "":
    exit(0)

promt = promt.replace("[context]",tasks)

output = ""

import openai
openai.api_key = open("apikey_chatgpt.txt").read().strip()

result = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": promt
    }],
    stream=True,
)
	
# Print the ChatGPT response within a loop.
for chunk in result: 
    text = chunk.choices[0].delta.content
    print(chunk.choices[0].delta.content,end="")
    if isinstance(text,str):
        output += text

with open("plan.md","w+") as f:
    f.write(output)
