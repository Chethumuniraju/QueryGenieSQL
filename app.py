from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql, db):
    print(sql)
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()  # Always close the connection when you're done
    return rows

prompt=[
    """
    Yor are  an expert in converting English questions in SQL code!
    The SQL database has the name STUDENT and has the fallowing coloumns-NAME,CLASS,SECTION \nFor example 1-How many entries of records are present?,the SQL commad willlook like something like this SELECT COUNT(*) FROM STUDENT ; also the sql code should not have ``` in beginning or end and sql word in the  output , the same output only i will pass to my database to access

"""
]
    
st.set_page_config(page_title="I can Retrive any SQL query")
st.header("Gemini App to Retrive SQL Data")
input=st.text_input("Input Promt : ",key="input")

submit=st.button("Ask me query")

if submit :
    response=get_gemini_response(input,prompt)
    st.subheader("The response is")

    for row in read_sql_query(response,"student.db"):
      
        st.write(row)