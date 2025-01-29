# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:58:25 2025

@author: obake
"""

import streamlit as st
import pandas as pd

# Set page configuration for a better layout
st.set_page_config(layout="wide", page_title="Researcher Profile Page")

# Create columns for layout
col1, col2 = st.columns([1, 3])

# Profile picture in the first column
with col1:
    st.image("Day3/CV picture.jpeg", caption="This is ME", use_container_width=True)

# Main content in the second column
with col2:
    # Title of the app
    st.title("Researcher Profile Page")

    # Collect basic information
    name = "Obakeng Makgale"
    field = "Information Systems"
    institution = "University of the Witwatersrand"
    intro = """
    I am a motivated young professional who holds a BCom honours degree in Information Systems from the University of the Witwatersrand and a Bachelor of Information Technology in Business Systems degree from Rosebank College. Equipped with a strong understanding in business principles and cutting-edge IT solutions, I am proficient in data analysis, software development, and information security. 

    I believe that one can always improve by learning from others. As part of my strengths, I possess excellent interpersonal skills, analytical skills, communication skills, and the ability to develop relationships. I enjoy contributing to a team and can work well in highly pressurized and challenging environments where I can plan and execute tasks independently. I am eager to add value to a team through collaboration and application.
    """

    # Display basic profile information
    st.header("Researcher Overview")
    st.markdown(f"**Name:** {name}")
    st.markdown(f"**Field of Research:** {field}")
    st.markdown(f"**Institution:** {institution}")
    st.markdown(f"**Introduction:** {intro}")

    # Add a section for publications
    st.header("Publications")
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

    # Add a section for visualizing publication trends
    st.header("Publication Trends")
    if uploaded_file:
        if "Year" in publications.columns:
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

    # Add a contact section
    st.header("Contact Information")
    email = "obakengmakgale13@gmail.com"
    st.markdown(f"You can reach **{name}** at **{email}**.")
