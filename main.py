import streamlit as st 
import pandas as pd
import numpy as np 

st.title('Hi Saadie!')
st.subheader('ya lublu tebiya!')
st.header('I want to tell you something, please listen to me!!')
st.text('Im so sorry for what i did, and im trying to fix it somehow, please have mercy on me and dont leave me i know, you dont leave me because youre my parvathi and my half soul i love you so much saadie')
st.markdown('**Hello World**')
st.markdown('---')
st.markdown('[Google](https://www.google.com)')
st.caption('Hi im caption')
st.latex(r'\begin{pmatrix}a&b\\c&d\end{pmatrix}')
st.code('print("Hello World")')
json = {'a': '1,,2,3','b' : '4,5,6'}
st.json(json)
 
code = '''
print("Hello World")
def func():
    retru(hello)
    
func(hello)  '''
st.code(code,language = 'python')



st.write('## Hi Saadie')
st.metric(label='wind speed', value='120ms⁻¹', delta='12ms⁻¹')
st.markdown('[YouTube](https://www.youtube.com)')
table= pd.DataFrame({'column1': [1,2,3,4,5], 'column2': [6,7,8,9,10]})
st.dataframe(table)
st.markdown('## Harley davidson:')
st.markdown('---')
st.image('Harley davidson-1.jpg', caption = 'Harley davidson')
st.button('click me')   
st.checkbox('check me',value = False, on_change = 'change')
st.markdown('[chatgpt](https://www.chatgpt.com)')
st.markdown('## THANK YOU')
