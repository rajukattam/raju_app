import streamlit as st 
import numpy as np
import pandas as pd  

st.title('HI MY FELLOWS')
st.subheader('Today im gonna teach you to use the streamlit')
st.markdown('[Google](htpps://www.google.com)')
st.latex(r'\begin{pmatrix}a&b\\c&d\end{pmatrix}')
#st.balloons()
st.latex(r'\begin{pmatrix}a&b\\c&d\end{pmatrix}')
st.markdown('[Youtube](https://www.youtube.com)')
st.sidebar.title('EEE SR University')
st.sidebar.title('Result')
genre = st.sidebar.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", ":rainbow[***Drama***]", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ])
st.markdown('## HI HELLO')
code = '''
def hello_world():
   return('hello world')

print(hello_world(hello))
'''
st.code(code)
if st.checkbox('True'):
    st.write('clicked')
    #print('clicked')
else:
    st.text('not clicked')
    #print('not cliked')    
st.image('Harley davidson-1.jpg')
st.markdown('https://youtu.be/11nGRskQs7g?si=IbWafpeRHkBcTl78')