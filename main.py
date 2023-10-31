import openai 
import streamlit as st
with st.sidebar:
    openai_api_key = st.text_input("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", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("✍️বাংলা GPT SCMS") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "আপনাকে কিভাবে সাহায্য করতে পারি?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("অনুগ্রহ করে আপনার Animerz প্রমাণীকরণ কী লিখুন")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
