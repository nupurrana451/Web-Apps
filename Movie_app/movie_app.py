# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 17:05:07 2025

@author: nrna1
"""

import pickle
import streamlit as st
import difflib
movie_model=pickle.load(open("C:/Users/nrna1/anaconda3/envs/MachineLearning/movie_model.sav",'rb'))
similarity_df=pickle.load(open("C:/Users/nrna1/anaconda3/envs/MachineLearning/similarity.sav",'rb'))
def movie_recs(movie_name):
    list_movies=movie_model['title'].tolist()
    find_close_match=difflib.get_close_matches(movie_name,list_movies)
    close_match=find_close_match[0]
    index_movie=movie_model[movie_model['title']==close_match]['index'].values[0]
    similarity_score=list(enumerate(similarity_df[index_movie]))
    sort_sim_mov=sorted(similarity_score,key=lambda x:x[1],reverse=True)
    recommended = []
    for movie in sort_sim_mov[1:31]:  # Skip the input movie
        index = movie[0]
        title = movie_model[movie_model['index'] == index]['title'].values[0]
        recommended.append(title)
    return recommended

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
        st.warning("Please enter a movie name.")
        
if __name__=='__main__':
    main()