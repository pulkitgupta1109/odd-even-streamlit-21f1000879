import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Welcome All"

def main():
  st.title("TDS Assignment 8 - 21f1000879_Pulkit Submission")
  html_temp = """
  <div style="background-color:black;padding:10px">
  <h2 style="color:white;text-align:center;">Find whether the given number is odd or even, using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num = st.number_input("Enter number to check if it's even or odd", step=1)
  if num % 2 ==0:
       result="Even Number"
  else:
       result="Odd Number" 
  st.success('Given number is {}'.format(result))
  if st.button("Made By"):
      st.text("Pulkit")
      st.text("21f1000879")

if __name__=='__main__':
  main()
