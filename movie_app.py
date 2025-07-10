import pickle
import streamlit as st
import difflib

# Load the data
movie_model = pickle.load(open("movie_model.sav", "rb"))         # This should be a DataFrame with 'title' and 'index'
top_similar = pickle.load(open("top_similar.pkl", "rb"))         # Dictionary: {movie_index: [similar_index1, ...]}

# Function to generate recommendations
def movie_recs(movie_name):
    list_movies = movie_model['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_movies)
    
    if not find_close_match:
        return []

    close_match = find_close_match[0]
    index_movie = movie_model[movie_model['title'] == close_match]['index'].values[0]
    similar_indices = top_similar.get(index_movie, [])
    
    recommended = []
    for idx in similar_indices:
        title = movie_model[movie_model['index'] == idx]['title'].values[0]
        recommended.append(title)
    return recommended

# Streamlit App
def main():
    st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥")
    st.title("🎬 Movie Recommendation Engine")
    st.markdown("Enter a movie you like, and we'll recommend similar ones.")

    movie_name = st.text_input("🍿 Enter movie name:")

    if st.button("🔍 Get Recommendations"):
        if movie_name.strip():
            recommendations = movie_recs(movie_name)
            if recommendations:
                st.markdown("### 🎯 Top 30 Movie Recommendations:")
                for i, title in enumerate(recommendations, start=1):
                    st.write(f"{i}. {title}")
            else:
                st.warning("❌ Sorry, couldn't find a close match.")
        else:
            st.warning("⚠️ Please enter a movie name.")

if __name__ == '__main__':
    main()
