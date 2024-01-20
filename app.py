import streamlit as st


def clear_input_field():
    st.session_state.user_question=st.session_state.user_input
    st.session_state.user_input= ""

def set_send_input():
    st.session_state.send_input = True
    clear_input_field()

def main():
    st.title("LOCAL MULTIMODAL GPT")
    Chat_contianer=st.container()

    if "send_input" not in st.session_state:
        st.session_state.send_input=False
        st.session_state.user_question= ""


    user_input = st.text_input('type your message here', key="user_input", on_change=set_send_input)

    send_button=st.button('send', key='send_button')

    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            llm_response= "this is a response from the LLM model"

            with Chat_contianer:
                st.chat_message('user').write(st.session_state.user_question)
                st.chat_message('AI').write('here is an answer')

if __name__=="__main__":
    main()