import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "kitchener"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)