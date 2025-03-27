import PIL.Image
import streamlit as stlt
import PIL
import os
from pathlib import Path
import pandas

stlt.set_page_config(layout="wide")

col1, col2 = stlt.columns(2)

with col1:
    stlt.image("images/photo.jpg")

with col2:
    stlt.title("Ismail Jogiat")
    aboutme = """ 
                Hello, I'm Ismail. I'm just starting my journey in learning 
                Python development and programming. 
                I am eager to continue this journey and share the projects that 
                I've worked on and developed along the way.
                I will update this page as I work through various projects. 
                """
    stlt.info(aboutme)

statement1 = """
                Below you can find some of the Apps that I have built using Python. 
                Feel free to contact me for any details or if you have any questions!
                """

stlt.write(statement1)

col3, col4 = stlt.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, data_row in df[:10].iterrows():
        stlt.header(data_row["title"])
    

with col4:
    for index, data_row in df[10:].iterrows():
        stlt.header(data_row["title"])
                
                




