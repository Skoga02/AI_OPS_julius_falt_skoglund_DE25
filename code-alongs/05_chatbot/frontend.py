import streamlit as st
import httpx

# Every time you start streamlit a new session starts
def init_session_states():
    if "messages" not in st.session_state:
        st.session_state.messages = [] # if session empty list = empty

    if "message_history" not in st.session_state:
        st.session_state.message_history = [] # if session empty list = empty

# Loops thru the empty list in seesion messages (Takes content into markdown)
def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"]) 


def handle_user_input():
    if prompt := st.chat_input("Talk to the JokeBot"):
        st.session_state.messages.append({"role": "user", "content": prompt}) # Prompt becomes content (Displays chat messages)
        # Post to API
        response = httpx.post(
            "http://127.0.0.1:8000/chat",
            json={
                "question": prompt, "message_history": st.session_state.message_history
            }, timeout=60
        ).json()

        st.session_state.message_history = response.get("message_history")

        bot_response = response.get("response")
        st.write(bot_response)
        # Saves response 
        response = f"Ro Båt: {bot_response}"

        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(response)
        # Stores messages in session_state
        st.session_state.messages.append({"role": "assistant", "content": response})


def layout():
    st.markdown("# Chat with Ro Båt")
    st.write(
        "RO BÅT is a funny robot that can help you out with programming tasks. However he doesn't directly answer your question, usually he asks another question back."
    )

    display_chat_messages()
    handle_user_input()

# Entry point 
if __name__ == "__main__":
    init_session_states()
    layout()