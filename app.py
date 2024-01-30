import streamlit as st
import en_20230808
import spacy 
import json
import requests
import pandas as pd
import pkg_resources

data = pkg_resources.resource_stream('en_20230808', 'meta.json')


nlp = spacy.load("en_20230808")
st.write(nlp("this is a model"))

with data as f:
    contents = json.load(f)

st.write(contents) 

# def load_lightcast_embeddings():
#     url = "https://skill-data-model.s3.ap-southeast-2.amazonaws.com/outputs/data/skill_ner_mapping/lightcast_embeddings.json"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data_lightcast_embeddings = json.loads(response.text)
#         return data_lightcast_embeddings
#     else:
#         st.error(f"Failed to fetch data from {url}. Status code: {response.status_code}")
#         return None

# def load_lightcast_hier_mapper():
#     url = "https://skill-data-model.s3.ap-southeast-2.amazonaws.com/outputs/data/skill_ner_mapping/lightcast_hier_mapper.json"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data_lightcast_hier_mapper = json.loads(response.text)
#         return data_lightcast_hier_mapper
#     else:
#         st.error(f"Failed to fetch data from {url}. Status code: {response.status_code}")
#         return None

# def load_lightcast_data_formatted():
#     url = "https://skill-data-model.s3.ap-southeast-2.amazonaws.com/outputs/data/skill_ner_mapping/lightcast_data_formatted.csv"
#     try:
#         df_lightcast_data_formatted = pd.read_csv(url)
#         return df_lightcast_data_formatted
#     except Exception as e:
#         st.error(f"Failed to fetch data from {url}. Error: {e}")
#         return None

# # Dropdown for user to select data category
# selected_category = st.selectbox("Select Data Category", ["Lightcast Embeddings", "Lightcast Hier Mapper", "Lightcast Data Formatted"])

# # Display selected data based on user's choice
# if selected_category == "Lightcast Embeddings":
#     data_lightcast_embeddings = load_lightcast_embeddings()
#     st.write("Data Lightcast Embeddings:", data_lightcast_embeddings)

# elif selected_category == "Lightcast Hier Mapper":
#     data_lightcast_hier_mapper = load_lightcast_hier_mapper()
#     st.write("Data Lightcast Hier Mapper:", data_lightcast_hier_mapper)

# if selected_category == "Lightcast Data Formatted":
#     df_lightcast_data_formatted = load_lightcast_data_formatted()
#     st.write("DataFrame Lightcast Data Formatted:", df_lightcast_data_formatted)
