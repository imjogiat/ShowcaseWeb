import streamlit as stlt
import PIL
import os

stlt.set_page_config(layout="wide")

col1, col2 = stlt.columns(2)

with col1:
    stlt.image("images/photo.jpg")

with col2:
    stlt.title("Ismail Jogiat")
    aboutme = """ 
                Hello, I'm Ismail. I'm just starting my journey in learning Python development and programming. 
                I am eager to continue this journey and share the projects that I've worked on and developed along the way.
                I will update this page as I work through various projects. 
                """
    stlt.info(aboutme)



