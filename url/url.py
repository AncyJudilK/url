import streamlit as st
import time

st.title("My Heart 💖")

# Container to hold the running text
placeholder = st.empty()

# Text to display
text = "I love you 💖"

# Running text effect
for _ in range(1):  # Run the animation once
    for i in range(len(text) + 1):
        placeholder.text(text[:i])  # Display the substring
        time.sleep(0.2)  # Pause for animation

# Create a downloadable text file
file_content = "I love you 💖"
file_name = "I_love_you.txt"

# Download button
st.download_button(
    label="Download 'I Love You' Text",
    data=file_content,
    file_name=file_name,
    mime="text/plain",
)





