import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title = "youtube video analyzer",
    layout = "centered"
)
st.title("YouTube Video Analyzer by AI")

@st.cache_resource
def get_agent():
    try:
        return build_youtube_agent()
    except:
        st.write("unexpected error")

agent = get_agent()

video_url = st.text_input("Enter YouTube Video Link",placeholder="Paste url here..")
button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyzie the video: {video_url}"
        )
    st.markdown("Analysis Video Report")
    st.markdown(response.content)
    st.success("Analysis done Successfully!")
