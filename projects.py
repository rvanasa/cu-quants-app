import numpy as np
import pandas as pd
import streamlit as st

class Projects():
    
    def __init__(self):
    
        self.codebase_url = 'https://docs.google.com/spreadsheets/d/1seBg9Gu5S4xDxUjEwduufSQWTA15V3N-IdpzB5PEOnk/edit#gid=0'
        self.codebase_url = self.codebase_url.replace('/edit#gid=', '/export?format=csv&gid=')
        self.codebase_library = pd.read_csv(self.codebase_url)
        
    def get_list(self):
        st.write(self.codebase_library)
    
    def get_prepared(self):
        
        for i in range(len(self.codebase_library)):
            
            row = self.codebase_library.iloc[i]
            st.write(row[1], row[2], row[3], row[4])
            break
            