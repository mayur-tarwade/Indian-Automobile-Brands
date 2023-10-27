import streamlit as st

st.title('CARS for You...')
option = st.selectbox('Indian Brands',['TATA','Maruti','Mahindra'])
if option == 'TATA':
    st.selectbox('TATA Cars',['Nexon','Safari','Tiago','Harrier'])
elif option == 'Maruti':
    st.selectbox('Maruti Cars',['Wagnor','Alto','Clerio','Swift'])
else:
    st.selectbox('Mahibdra Cars',['XUV300','XUV400','XUV500','XUV700','Thar4X4'])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image('tiago-exterior-right-front-three-quarter-25.jpeg')
with col2:
    st.write('One of the best option in TATA Car family available is Tata Tiago Just go for it and it wont disappoint you')
with col3:
    st.write('Welcome to Maharashtra. Search Tata car in Maharashtra')
with col4:
    st.write('Welcome to Pune. Search Tata car in Pune')