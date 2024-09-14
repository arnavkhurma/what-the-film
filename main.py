import streamlit as st
from propelauth import auth
import cv2 as cv

st.set_page_config(layout="wide")


user = auth.get_user()
if user is None:
    st.error('Unauthorized')
    st.stop()

with st.sidebar:
    st.image("static/logo.jpeg")
    st.markdown("---")
    url = "https://www.streamlit.io"
    if user is None:
        st.markdown(f'<a href="{url}" style="color: black; text-decoration: none; font-weight: bold; font-size: 130%;">LOGIN</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{url}" style="color: black; text-decoration: none; font-weight: bold; font-size: 130%;">SIGN UP</a>', unsafe_allow_html=True)
        st.markdown(f'<a style="color: black; text-decoration: none; font-size: 70%;">* Secure Login with PropelAuth</a>', unsafe_allow_html=True)
    else:
        st.text("Logged in as " + user.email)
        st.link_button('MY ACCOUNT', auth.get_account_url(), use_container_width=True)
        st.link_button('PAST SEARCHES', auth.get_account_url(), use_container_width=True)
        st.link_button('LOG OUT', auth.get_account_url(), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    model_Picture=None
    st.header("Upload / Take an Image")
    picture = st.camera_input("")
    st.markdown("---")
    df = st.file_uploader(label='')

with col2:
    result_found = False
    if result_found:
        st.header("Right Half")
        st.write("This is the content of the right half.")
        st.image("https://via.placeholder.com/150", caption="Right Image")

# Add custom CSS for file uploader and mobile responsiveness
st.markdown(
    """
    <style>
    [data-testid='stFileUploader'] {
        width: 100%;
    }
    @media only screen and (max-width: 768px) {
        .css-1lcbmhc {  /* column width */
            flex-direction: column;  /* Stack the columns */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)
