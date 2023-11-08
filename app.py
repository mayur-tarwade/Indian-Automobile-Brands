import streamlit as st

st.title('Greatest Indian Automobile Brands')
st.header('CARS 4 U')
option = st.sidebar.selectbox('INDIAN BRANDS',['TATA','Maruti','Mahindra'])
if option == 'TATA':
    st.subheader('TATA Cars')
    st.sidebar.image('image/Tata-Group-logo-3840x2160.png')
    st.sidebar.selectbox('TATA CARS',['Nexon','Safari','Tiago','Harrier'])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image('image/tata_nexon_ev_max-sixteen_nine.jpg')
        st.subheader('EV')
        st.metric('Rs',str(7.56) + ' Lac')
    with col2:
        st.image('image/19.jpg')
        st.subheader('XE')
        st.metric('Rs', str(6.95) + ' Lac')
    with col3:
        st.image('image/1642614440-nexon-ext-color-white.jpg')
        st.subheader('XM')
        st.metric('Rs', str(7.70) + ' Lac')
    with col4:
        st.image('image/Tata-Nexon-Kaziranga-Edition-Price.jpg')
        st.subheader('XZ')
        st.metric('Rs', str(8.70) + ' Lac')

elif option == 'Maruti':
    st.subheader('MARUTI CARS')
    st.sidebar.image('image/maruti-logo-maruti-icon-free-free-vector.jpg')
    st.sidebar.selectbox('Maruti Cars',['Wagonr','Alto','Celerio','Swift'])
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('image/WG.jpeg')
        st.subheader('Pet')
        st.metric('Rs', str(6.50) + ' Lac')
    with col2:
        st.image('image/WG.jpeg')
        st.subheader('Pet + CNG')
        st.metric('Rs', str(7.20) + ' Lac')
    with col3:
        st.image('image/WG.jpeg')
        st.subheader('VXI')
        st.metric('Rs', str(7.50) + ' Lac')
    with col4:
        st.image('image/WG.jpeg')
        st.subheader('LXI')
        st.metric('Rs', str(8.50) + ' Lac')
else:
    st.subheader('MAHINDRA CARS')
    st.sidebar.image('image/download.jpeg')
    st.sidebar.selectbox('Mahindra Cars',['XUV300','XUV400','XUV500','XUV700','Thar4X4'])
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('image/download (1).jpeg')
        st.subheader('W2 Pet')
        st.metric('Rs', str(7.99) + ' Lac')
    with col2:
        st.image('image/download (1).jpeg')
        st.subheader('W4 Pet')
        st.metric('Rs', str(8.66) + ' Lac')
    with col3:
        st.image('image/download (1).jpeg')
        st.subheader('W4 Diesel')
        st.metric('Rs', str(10.21) + ' Lac')
    with col4:
        st.image('image/download (1).jpeg')
        st.subheader('EV')
        st.metric('Rs', str(8.50) + ' Lac')

st.header("Other Automobile Brands")

st.sidebar.title('Menu')
st.sidebar.markdown ("""
- Home
- Who we are?
- Services
- Finance
- Contact
- Profile
""")
option = st.sidebar.selectbox('Select One',['Dealer','Quatation'])
st.sidebar.button('Select')
if option == 'Dealer':
    st.title('Dealers in the Town')
else:
    st.title('Quatations')