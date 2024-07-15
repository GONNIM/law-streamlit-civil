import streamlit as st

from dotenv import load_dotenv

from llm import get_ai_response
    
st.set_page_config(page_title="민법 챗봇", page_icon="🤖")

st.title("🤖 민법 챗봇")
st.caption("무엇이든 물어보세요! 계약, 소유, 상속, 채무 등 다양한 개인 권리와 의무에 대해...")

load_dotenv()

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_question := st.chat_input(placeholder="계약, 소유, 상속, 채무에 관련된 궁금한 내용들을 말씀해주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("답변을 생성하는 중입니다"):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
        st.session_state.message_list.append({"role": "ai", "content": ai_message})
