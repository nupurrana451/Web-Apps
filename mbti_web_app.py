# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 20:30:28 2025

@author: nrna1
"""
import pickle
import streamlit as st
vectorizer_mbti=pickle.load(open('vectorizer_mbti.sav','rb'))
model_I_mbti=pickle.load(open('model_I_mbti.sav','rb'))
model_N_mbti=pickle.load(open('model_N_mbti.sav','rb'))
model_F_mbti=pickle.load(open('model_F_mbti.sav','rb'))
model_P_mbti=pickle.load(open('model_P_mbti.sav','rb'))

def predict_mbti(text):
    # Use global models and vectorizer
    X_vec = vectorizer_mbti.transform([text])
        # Define thresholds
    thresholds = {'I': 0.40, 'N': 0.35, 'F': 0.5, 'P': 0.5}
    def predict_trait(model, X, threshold):
      proba = model.predict_proba(X)[0, 1]
      return 1 if proba >= threshold else 0

        # Predict each trait
    I = predict_trait(model_I_mbti, X_vec, thresholds['I'])
    N = predict_trait(model_N_mbti, X_vec, thresholds['N'])
    F = predict_trait(model_F_mbti, X_vec, thresholds['F'])
    P = predict_trait(model_P_mbti, X_vec, thresholds['P'])

        # Combine into MBTI string
    mbti = (
        ('I' if I else 'E') +
        ('N' if N else 'S') +
        ('F' if F else 'T') +
        ('P' if P else 'J')
      )

    return mbti

def describe_mbti(mbti):
    descriptions = {
        "INTJ": "🎯 INTJ - The Architect: Strategic and logical, driven by long-term goals.",
        "INTP": "🧠 INTP - The Thinker: Curious, analytical, loves deep thinking.",
        "ENTJ": "📈 ENTJ - The Commander: Bold leader, strategic, and assertive.",
        "ENTP": "💡 ENTP - The Debater: Energetic, clever, loves new ideas.",
        "INFJ": "🌌 INFJ - The Advocate: Idealistic, deep, and empathetic.",
        "INFP": "💖 INFP - The Mediator: Creative and value-driven, cares deeply.",
        "ENFJ": "🌟 ENFJ - The Protagonist: Inspiring and caring leader.",
        "ENFP": "🌈 ENFP - The Campaigner: Free spirit, warm, full of ideas.",
        "ISTJ": "🗂️ ISTJ - The Logistician: Practical and reliable, values duty.",
        "ISFJ": "🛡️ ISFJ - The Defender: Caring and observant, protective of others.",
        "ESTJ": "🧱 ESTJ - The Executive: Organized, efficient, gets things done.",
        "ESFJ": "🤝 ESFJ - The Consul: Supportive, social, values harmony.",
        "ISTP": "🔧 ISTP - The Virtuoso: Action-oriented, loves building things.",
        "ISFP": "🎨 ISFP - The Adventurer: Gentle, creative, lives in the moment.",
        "ESTP": "⚡ ESTP - The Dynamo: Bold, fast-paced, enjoys challenge.",
        "ESFP": "🎉 ESFP - The Entertainer: Fun-loving and expressive.",
    }
    return descriptions.get(mbti, "🤔 Unknown MBTI type.")

# Streamlit App
def main():
    st.title('MBTI Personality Predictor')
    st.markdown("Tell us about yourself and find your MBTI type!")

    text = st.text_area('📝 Write a paragraph about yourself:', height=200)

    if st.button('🔍 Predict MBTI'):
        if text.strip() != "":
            mbti = predict_mbti(text)
            st.success(f"Your MBTI Type is: `{mbti}`")
            st.markdown(f"**{describe_mbti(mbti)}**")
        else:
            st.warning("Please enter some text first.")
        
if __name__=='__main__':
    main()
