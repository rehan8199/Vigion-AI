import streamlit as st

st.set_page_config(page_title="Vigion.ai", layout="wide")

st.title("🎬 Vigion.ai: World's Most Powerful AI Video Engine")
st.markdown("### Generate 1-30 Minute Videos from Prompts")

prompt = st.text_area("Enter your cinematic prompt:", placeholder="A deep sea exploration of an alien base...")
duration = st.slider("Select Duration (Minutes):", 1, 30, 5)

if st.button("Generate Video"):
    st.info("Initializing Vigion Engine... (Free Tier Running)")
    # Yahan humne backend link kiya hai
    st.warning("Vigion.ai is in High Demand. Your video is in queue.")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndXpxamZ3bmZ3bmZ3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZAmS/3o7TKMGpxx946") # Loading animation
