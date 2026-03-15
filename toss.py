import streamlit as st
import random
import time 

st.title ( "DRAGON OR TIGER" )

if st.button ("bet now " , type = "primary"):
    placeholder = st.empty ()

    with open ("joker.mp4" , "rb") as f :
        vid = f.read() 

        placeholder.video( vid , autoplay = True)

        time.sleep (5)

        placeholder.empty()

        result = random.choice (["DRAGON " , "TIGER "])

        if result == "TIGER":
            st.image ("tiger.png ", width = 300)

        else:
            st.image ("dragon.png " , width = 300 )
            