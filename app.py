import streamlit as st
import random

# App Title
st.set_page_config(page_title="Growth Mindset App", layout="centered")
st.title("🚀 Adopt a Growth Mindset")

# Intro Section
st.markdown("""
A **growth mindset** is the belief that you can develop your abilities through dedication and hard work.  
It’s the foundation for learning, innovation, and success.
""")

# Key Points Section
st.header("🌱 Why Choose a Growth Mindset?")
st.markdown("""
- 💪 Embrace challenges  
- 🧠 Learn from mistakes  
- 🔁 Persist through difficulties  
- 🎉 Celebrate effort, not just results  
- 🌍 Keep an open mind  
""")

# Tips Section
st.header("📘 Tips to Build a Growth Mindset")
tips = [
    "Set learning goals, not just performance goals.",
    "Reflect on what you learned daily.",
    "Ask for feedback and use it to improve.",
    "Stay positive even when you struggle.",
    "Encourage your friends to grow too!"
]
for tip in tips:
    st.success(tip)

# Motivation Section
st.header("💬 Daily Motivation")
quotes = [
    "“Mistakes are proof you are trying.”",
    "“Every expert was once a beginner.”",
    "“Difficult roads often lead to beautiful destinations.”",
    "“Don’t stop until you’re proud.”",
    "“The only limit to your growth is your mindset.”"
]
if st.button("Show Me a Quote"):
    st.info(random.choice(quotes))

# Goal Tracker Section
st.header("🎯 Set Your Daily Goal")
goal = st.text_input("What's one thing you'll do today to grow?")
if goal:
    st.success(f"Great! Stay focused on: **{goal}**")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

