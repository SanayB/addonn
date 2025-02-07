import pandas as pd
import numpy as np
import streamlit as st

st.title('Welcome Everyone we are learning python')
st.write("Python requires Practice!!")


data=pd.DataFrame({
    'c1':[10,20,30,40],
    'c2':['A','B','C','D']
})

st.write(data)

chart_data=np.random.rand(20,3)

st.line_chart(chart_data)