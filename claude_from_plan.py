import anthropic
import os
key = ""
with open("apikey.txt","r") as f:
    key = f.read()

if key == "":
    exit(0)
client = anthropic.Anthropic(api_key=key)

plan = ""
with open("plan.md","r",encoding='utf-8') as f:
    plan = f.read()

if plan == "":
    exit(0)

# message = client.messages.create(
#     model="claude-3-7-sonnet-20250219",
#     max_tokens=64000,
#     temperature=1,
#     stream=True,
#     system="you are a developper . please follow this plan.md file to create the project.",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": plan
#                 }
#             ]
#         }
#     ]
# )
whole_message = ""
old_message = ""
with client.messages.stream(
    max_tokens=64000,
    system="you are a developper . please follow this plan.md file to explain to me how to create the project.",
    messages=[{"role": "user", 
            "content": [
                {
                    "type": "text",
                    "text": plan
                }
            ]}],
    model="claude-3-7-sonnet-20250219",
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
        old_message += text
        whole_message += text
# old_message = ""
# with client.messages.stream(
#     max_tokens=64000,
#     system="you are a developper . please follow this plan.md file to explain to me how to create the project.",
#     messages=[
#         {"role": "assistant", 
#             "content": old_message},
#         {"role": "user", 
#             "content": "please continue"}],
#     model="claude-3-7-sonnet-20250219",
# ) as stream:
#     for text in stream.text_stream:
#         print(text, end="", flush=True)
#         old_message += text
#         whole_message + text

with open("generated.txt","w+",encoding="utf-8") as f:
    f.write(whole_message)
