import streamlit as st


def main():
    st.title("LOCAL MULTIMODAL GPT")
    Chat_contianer=st.container()

    user_input = st.text_input('type your message here', key="user_input")

    send_button=st.button('send', key='send_button')

    if send_button:
        llm_response= "this is a response from the LLM model"

        with Chat_contianer:
            st.chat_message('user').write(user_input)
            st.chat_message('AI').write('here is an answer')

if __name__=="__main__":
    main()