import streamlit as st

st.markdown("# Character counter")

user_input = st.text_input("Input some text here and I'll count the characters")

if user_input:
    output = len(user_input)
    message = f"Your input is {output} characters long. You are awesome."

    # Create jumping animation for each character
    html_string = """
    <style>
    @keyframes jump {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }
    .jumping-text {
        font-size: 20px;
        font-weight: bold;
        display: inline-block;
    }
    .jump-char {
        display: inline-block;
        animation: jump 0.6s ease-in-out infinite;
    }
    </style>
    <div class="jumping-text">
    """

    # Wrap each character in a span with staggered animation delay
    for i, char in enumerate(message):
        delay = i * 0.05  # Stagger animation by 0.05s per character
        if char == " ":
            html_string += "&nbsp;"
        else:
            html_string += f'<span class="jump-char" style="animation-delay: {delay}s;">{char}</span>'

    html_string += "</div>"

    st.markdown(html_string, unsafe_allow_html=True)