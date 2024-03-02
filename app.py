import streamlit as st
import pandas as pd
import subprocess
import platform
import random
import time


# st.write("Hello world")

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df
#=============================================================================
# Sidebar
#=============================================================================
# Using object notation
# st.page_link("pages/chatbot.py", label="Home", icon="🏠")

#=============================================================================
# Upload Dataset Section
#=============================================================================
st.subheader("Upload Dataset")
# Display file input button
uploaded_file = st.file_uploader("Choose a file")

# Display filename if a file is uploaded
if uploaded_file is not None:
    st.write("Selected file:", uploaded_file.name)

#=============================================================================
# Topics & Questions Section
#=============================================================================
st.subheader("Most Frequent Topics")
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df
