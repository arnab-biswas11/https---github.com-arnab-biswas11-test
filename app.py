import streamlit as st
import en_20230808
import spacy 

nlp = spacy.load("en_20230808")
st.write(nlp("this is a model"))
