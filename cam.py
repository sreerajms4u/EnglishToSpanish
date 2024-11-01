"""Capture video from camera."""
import cv2 as cv

from transformers import pipeline
import streamlit as st

cap = cv.VideoCapture(0)
imageName = "Sree.jpg"
image=""
def capture_image(frame):
    image =cv.imwrite(imageName, frame)
    img_file_buffer = st.camera_input("Take a picture")
    if image:
        st.image(image)
"""
    if image is not None:
    # To read image file buffer as bytes:
        bytes_data = image.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
        st.write(type(bytes_data))
        """
    

def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text=image_to_text(
        url)[0]['generated_text']
    print(text)
    return text
def generate_story(scenario):
    generator = pipeline("text-generation", model="gpt2")
    result = generator(scenario, max_length=200, num_return_sequences=1)
    return result[0]["generated_text"]

def drawBtn():
    option= ...
    st.button("Find", on_click= onSearch, args= [option])
def onSearch(opt):
    st.session_state["clicked"] = True

def main():
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        text=""
        # Our operations on the frame come here
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('c'):
            capture_image(frame)
        if cv.waitKey(1) & 0xFF == ord('t'):
            text = img2text("Sree.jpg")
        if cv.waitKey(1) & 0xFF == ord('s'):
            story = generate_story(text)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

    st.set_page_config(page_title="imag 2 audio story")
    st.header("Turn an Imageinto an Audio story")
    #uploaded_file = st.file_uploader("Choose an image...",type="jpg")

    bytes_data = image.getvalue()
    with open(imageName,"wb") as file:
        file.write(bytes_data)
    scenario = img2text(image)
    story = generate_story(scenario)
    #text2speech(story)

    if st.session_state["clicked"]:
        st.success("Done!")

    if st.session_state["clicked"]:
        st.success("Done!")

    drawBtn()
    with st.expander("Content of the Image"):
        st.write(scenario)
    with st.expander("Story Of the Image"):
        st.write(story)

    st.audio("hello.mp3")


if __name__ == '__main__':
    main()

