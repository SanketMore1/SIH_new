import streamlit as st
import train
import test
from os.path import exists
import os


if exists("requirements.txt"):
    os.system("pip3 install -r requirements.txt")
    os.remove("requirements.txt")


if exists("model_sgd.h5"):
    st.markdown("<h1 style='text-align: center;'>Model Exists,Can Use the existing model for prediction </h1>", unsafe_allow_html=True)   
       
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
st.header("Select your choice")
choice=st.radio("",("Train the model","Test the model"))
if choice == 'Train the model':
    st.markdown("<h1 style='text-align: center; color:gray'>Training Section</h1>", unsafe_allow_html=True)
    train.train()
elif choice == 'Test the model':
    st.markdown("<h1 style='text-align: center; color:gray'>Testing Section</h1>", unsafe_allow_html=True)
    if exists("model_sgd.h5"):
        test.test()
    else:
        st.markdown("<h1 style='text-align: center;'>No Model Have been Trained please train the model first</h1>", unsafe_allow_html=True)
            
        
    


