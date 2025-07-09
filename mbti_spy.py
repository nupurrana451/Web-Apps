# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 20:13:55 2025

@author: nrna1
"""
import pickle

vectorizer_mbti=pickle.load(open("C:/Users/nrna1/anaconda3/envs/MachineLearning/vectorizer_mbti.sav",'rb'))
model_I_mbti=pickle.load(open("C:/Users/nrna1/anaconda3/envs/MachineLearning/model_I_mbti.sav",'rb'))
model_N_mbti=pickle.load(open("C:/Users/nrna1/anaconda3/envs/MachineLearning/model_N_mbti.sav",'rb'))
model_F_mbti=pickle.load(open("C:/Users/nrna1/anaconda3/envs/MachineLearning/model_F_mbti.sav",'rb'))
model_P_mbti=pickle.load(open("C:/Users/nrna1/anaconda3/envs/MachineLearning/model_P_mbti.sav",'rb'))

text="I like partying with my friends like crazy and meeting new people. I like to fantasize about future and work religiously for success in my career. I also want to help people in need and think about why are people the way they are."

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
print('Your personality type is likely:',mbti)