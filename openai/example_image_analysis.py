import base64
from openai import OpenAI

def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
client = OpenAI(api_key='sk-SkyTNuAYmLQzGG0Urbc8Bxi6U_Z7CmA4cx1QRTYpHKT3BlbkFJu_9Vk9y16cF98A3e1_oT5fYc1ZYw601HAo33ul_UQA')
image_path = "C:\\Users\\edwar\\OneDrive\\Desktop\\openaitest.png"
base64_image = encode_image(image_path)
response = client.chat.completions.create(
    model='gpt-4o-mini-2024-07-18',
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'Please analyze the image from maplestory and provide the response in this format.'
                                         '1. Tell me what Percentage HP the character has'
                                         '2. Tell me what Percentage MP the character has'
                                         '3. Tell me how many red spots are in the mini map in the top left.'
                                         '4. There is a chatbox in the lower left side. My character name is Addwaah. If the most recent message is from someone else, can you give me an appropriate response?'},
                {'type': 'image_url',
                 'image_url': {
                     'url': f'data:image/jpeg;base64,{base64_image}'
                 },
                },
            ]
        }
    ]
)

print('Completion Tokens:', response.usage.completion_tokens)
print('Prompt Tokens:', response.usage.prompt_tokens)
print('Total Tokens:', response.usage.total_tokens)
print(response.choices[0])