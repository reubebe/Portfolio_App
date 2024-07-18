import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG")

with col2:
    st.title("Reuben Newton Addison, PhD")
    content = """Hi, I am Reuben! An assistant professor of kinesiology by day and a Python programmer by night. 
As a researcher specializing in applied motor control and biomechanics, I found myself programming 
my own experiments, which sparked a keen interest in delving deeper into programming. Combining my 
existing passion for data analytics, I've decided to unite both realms, creating a shared foundation 
for making a meaningful impact. Leveraging my skills, I've successfully enhanced efficiency in my 
research workflow and aspire to pioneer the integration of analytics in the field of rehabilitation.

The first two apps I created were a result of a program I wrote during my postdoc at Mass General 
Hospital. I wrote the program to make it easier to assess voice quality as part of my research for 
individuals with laryngeal dystonia. The program made it easier to access multiple voice chunks at once. 
I then decided to convert the code into an app."""

st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3,empty_column, col4 = st.columns([1.5,0.5,1.5])
df  = pandas.read_csv("data.csv")

with col3:
    for index,row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index,row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

