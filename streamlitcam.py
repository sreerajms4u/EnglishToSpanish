
#python -m streamlit run cam.py
import cv2
import streamlit as st

imageName="Sreeeraj.jpg"

# Create two columns
col1, col2 = st.columns(2)

def drawBtn():
    option= ...
    st.button("Capture", on_click= capture_image)
def onCapture(opt):
    st.session_state["clicked"] = True
def capture_image():
    FRAME_IMGWINDOW = st.image([])
    ret, imgframe = camera.read()
    image =cv2.imwrite(imageName, imgframe)
    #img_file_buffer = st.camera_input("Take a picture")
    if image:
        # Add content to the left column
        with col2:
            st.header("Picture")
            FRAME_IMGWINDOW.image(imageName)

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
frame = ""
with col1:
    FRAME_VIDWINDOW = st.image([])
    st.header("Video")
    drawBtn()
    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Add content to the right column
        FRAME_VIDWINDOW.image(frame)    
    else:
        st.write('Stopped')