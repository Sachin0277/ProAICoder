import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system",
             "content": "You are a software developer experts that specializes in data structures and algorithms. You "
                        "are a highly experienced programmer who has experience at Google"}]


def CustomChatGPT(Problem_Statement):
    messages.append({"role": "user", "content": Problem_Statement})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="code", title="Pro AI Coder")

demo.launch(share=True)
