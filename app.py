import streamlit as st
from Few_shots import FewShotPosts
from post_generator import generate_post

# Main app layout with UI improvements
def main():
    st.set_page_config(page_title="Codebasics LinkedIn Post Generator", layout="centered", initial_sidebar_state="collapsed")

    # Custom CSS for a more modern look
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #0077b5;
            color: white;
            border-radius: 8px;
            border: 1px solid #0077b5;
            padding: 10px 24px;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #005582;
            border: 1px solid #005582;
        }
        .main-header {
            color: #0077b5;
            text-align: center;
            font-size: 2.5em;
            font-weight: 600;
        }
        .sub-header {
            color: #4a4a4a;
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-header'>LinkedIn Post Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Craft engaging posts for your LinkedIn audience with the help of AI! 🤖</p>", unsafe_allow_html=True)

    try:
        fs = FewShotPosts()
        all_tags = fs.get_tags()
        influencer_options = list(fs.get_tags_per_influencer().keys())
        influencer_options.insert(0, "Any")
    except Exception as e:
        st.error(f"Failed to load post data. Please check the `preprocessed.json` file. Error: {e}")
        return

    # Use a container for a clean, bordered look
    with st.container(border=True):
        st.subheader("Post Preferences")

        # Use columns to align the input fields neatly
        col1, col2 = st.columns(2)
        with col1:
            selected_influencer = st.selectbox("Influencer Style", options=influencer_options, help="Choose an influencer style to emulate.")
            selected_length = st.selectbox("Post Length", options=["Short", "Medium", "Long"], help="Select the desired length of the post.")
        with col2:
            selected_engagement = st.selectbox("Engagement Weighting", options=["High", "Medium", "Low"], help="Prioritize posts that had higher engagement.")
            selected_language = st.selectbox("Language", options=["English", "Hinglish"], help="Choose the language for your post.")
        
        st.markdown("---")
        
        selected_tag = st.selectbox("Topic (Tag)", options=all_tags, help="Select the topic you want the post to be about.")

    st.markdown("---")

    # A single, prominent button for generation
    if st.button("Generate Post", use_container_width=True):
        with st.spinner("Generating your post..."):
            try:
                post = generate_post(
                    length=selected_length,
                    language=selected_language,
                    tag=selected_tag,
                    influencer=selected_influencer,
                    engagement_level=selected_engagement
                )
                
                # Display the generated post in a styled container
                st.markdown("<h3 style='color: #0077b5;'>Your Generated Post:</h3>", unsafe_allow_html=True)
                st.success("Post generated successfully! ✨")
                with st.container(border=True):
                    st.write(post)
            except Exception as e:
                st.error(f"An error occurred during post generation. Error: {e}")

# Run the app
if __name__ == "__main__":
    main()