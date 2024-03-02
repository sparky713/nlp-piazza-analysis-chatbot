import streamlit as st
import pandas as pd
import numpy as np
import subprocess
import platform
import random

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


# List of animals
topics = ["office hours", "Natural Recursion", "template", "midterm", "final exam"]

# Layout with two columns
# topicsCol, postNumsCol = st.columns([1, 2])
topicsCol, postNumsCol = st.columns(2)
topicsCol.subheader("Most Frequent Topics:")
# postNumsCol.subheader("Posts:")

# Display all topics in the left column
selectedTopic = topicsCol.radio("Select to view posts", topics)

# Display posts based on the selected topic
postNums = getPosts(selectedTopic)
postNumsCol.subheader(f"Posts on {selectedTopic}:")
# postNumsCol.write(breeds)
for postNum in postNums:
    postNumsCol.write(postNum)



#-------------------
# Topics List & Post Numbers
#-------------------
# def handle_click(item):
#     st.write("You clicked:", item)
# topicsCol, postNumsCol = st.columns(2)
# with topicsCol:
#     st.subheader("Most Frequent Topics:")

#     # Sample list of items
#     topics = ["office hours", "recursion", "template", "midterm", "final exam"]

#     # Define a JavaScript function to handle item clicks
#     javascript = """
#     <script>
#     function handleClick(item) {
#         alert("You clicked on " + item);
#     }
#     </script>
#     """
#     # Display the JavaScript function
#     st.markdown(javascript, unsafe_allow_html=True)

#     for topic in topics:
#         st.markdown(f"<div style='cursor:pointer;' onclick='handleClick(\"{topic}\")'>{topic}</div>", unsafe_allow_html=True)
#         st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)



# with postNumsCol:
#     st.subheader("Posts:")
#     items = ["@1", "@2", "@3", "@4", "@5", "@6", "@7", "@8", "@9", "@10", "@11", "@12", "@13", "@14", "@15"]

#     # Define a JavaScript function to handle item clicks
#     javascript = """
#     <script>
#     function handleClick(item) {
#         alert("You clicked on " + item);
#     }
#     </script>
#     """
#     # Display the JavaScript function
#     st.markdown(javascript, unsafe_allow_html=True)

#     # Display the list items with click event handlers and dividers
#     # with st.markdown("<div style='height: 200px; overflow-y: auto;'>", unsafe_allow_html=True):
#     for item in items:
#         st.markdown(f"<div style='cursor:pointer;' onclick='handleClick(\"{item}\")'>{item}</div>", unsafe_allow_html=True)
#         st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
#     # st.markdown("</div>", unsafe_allow_html=True)
    



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


