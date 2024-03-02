import streamlit as st
import pandas as pd
import numpy as np
from helpers import getPosts

#=============================================================================
# Upload Dataset Section
#=============================================================================
st.subheader("Upload Dataset")

# display file input button
uploaded_file = st.file_uploader("Choose a file", type="json")

# display an error message if the file is not JSON
if uploaded_file is not None:
    if not uploaded_file.name.endswith('.json'):
        st.error("Please upload a JSON file.")
st.divider()

#=============================================================================
# Topics & Questions Section
#=============================================================================
#-------------------
# Select Topics
#-------------------
options = st.multiselect(
    'Topics',
    ['Natural Recursion', 'Function Composition', 'Template Tags', 'Graphs'],
    ['Natural Recursion', 'Graphs'])


#-------------------
# Topics List & Post Numbers
#-------------------
topics = ["office hours", "Natural Recursion", "template", "midterm", "final exam"]
# setup the columns
topicsCol, postNumsCol = st.columns(2)
topicsCol.subheader("Most Frequent Topics:")
# postNumsCol.subheader("Posts:")

selectedTopic = topicsCol.radio("Select to view posts", topics)
postNums = getPosts(selectedTopic)
postNumsCol.subheader(f"Posts on {selectedTopic}:")
# postNumsCol.write(breeds)
for postNum in postNums:
    postNumsCol.write(postNum)

st.write("") # blank space

#-------------------
# Bar Chart
#-------------------
# we could have topic and number of posts?
color_data = {
    'Topics': topics,
    'PostCount': [15, 25, 10, 20, 5]  # Example counts
}

df = pd.DataFrame(color_data)
# df.set_index('Color', inplace=True)
st.bar_chart(df, x="Topics", y="PostCount", color="#0000FF", width=5) # display
