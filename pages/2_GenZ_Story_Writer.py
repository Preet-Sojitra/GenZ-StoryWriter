import streamlit as st
import time
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
from streamlit_image_select import image_select
from utils.pipeline import generate_prompt
from utils.ImageCaptioner import ImageCaptioning
from utils.createPDF import createPDF
from utils.sendEmail import send_mail
from utils.scrapImages import scrap_images, download_images
from utils.text_generator import MistralModel

dummy_story = """
Title: The Cartoon Character's Brushing Adventure

FADE IN:

INT. CARTOON CHARACTER'S ROOM - DAY

A cartoon character, wearing a hat and holding a toothbrush, stands in front of a mirror. He looks at himself in the mirror and starts brushing his teeth.

CARTOON CHARACTER (V.O.) Morning! Time to start my brushing adventure!

The cartoon character continues brushing his teeth for a few seconds, then suddenly stops and looks surprised. He puts down the toothbrush and turns to the camera.

CARTOON CHARACTER (V.O.) Oh no! My hat has fallen off!

He quickly reaches out and picks up the hat from the floor.

CARTOON CHARACTER (CONT'D) No problem! I'll just put this hat back on.

The cartoon character puts on the hat and continues brushing his teeth, this time with more care. He finishes brushing and turns to the camera once again.

CARTOON CHARACTER (V.O.) And that was my brushing adventure! Time to go out and have some fun!

FADE OUT.



"""

if "title" not in st.session_state:
    st.session_state.title = ""

if "images" not in st.session_state:
    st.session_state.images = []

if "selected_images" not in st.session_state:
    st.session_state.selected_images = []

if "story" not in st.session_state:
    st.session_state.story = ""

st.sidebar.success("Genz Story Writer Page")

st.title("GenZ Story Writer")

st.write(
    """
    ### What is this?
    This is a simple app that generates a story based on a few images.
    
    ### How does it work?
    1. Upload a few images
    2. Click the button
    3. Wait a few seconds
    4. Grab a cup of coffee
    5. Read the story
    
    ### How does it really work?
    Behind the scenes, the images are sent to a server that generates a story based on the images. The server uses a machine learning model to generate the story.
    """
)

# search bar for searching images
search_term = st.text_input("Search for images")
# enter number of images to download
num_images = st.number_input("Number of images to download", min_value=1, value=1)
search_button = st.button("Search")

if search_term and search_button and num_images > 0:
    # need to reset the images array, so that whenever user searches for the image again, he can see new images
    st.session_state.images = []

    st.write("Here are the images for your search term: ")

    # scrap the images
    image_links = scrap_images(search_term, num_images)
    # download the images
    download_images(image_links, "tmp/{}".format(search_term))

    # st.session_state.logger.log("Images scraped")

    # store the images
    for i in range(int(num_images)):
        st.session_state.images.append(f"tmp/{search_term}/image_{i + 1}.jpg")


if len(st.session_state.images) > 0:
    img = image_select(
        images=st.session_state.images,
        label="Select an image",
        use_container_width=False,
    )
    if st.button("Select this image "):
        st.session_state.selected_images.append(img)

    try:
        image_select(
            images=st.session_state.selected_images,
            label="You have selected {} images".format(
                len(st.session_state.selected_images)
            ),
            use_container_width=False,
        )
    except:
        pass

    clear = st.button("Clear all")
    if clear:
        st.session_state.selected_images = []
        st.session_state.images = []
        st.rerun()
        st.success("Images cleared successfully!")

if len(st.session_state.selected_images) > 0:
    st.write("### Click the button to generate a story")
    # print(st.session_state.selected_images)

    if st.button("Generate Story"):
        if "ic" not in st.session_state:
            st.session_state.ic = ImageCaptioning()

        if "mistral_model" not in st.session_state:
            st.session_state.mistral_model = MistralModel()

        captions = st.session_state.ic.captionIt(st.session_state.selected_images)
        st.session_state.logger.log("Captions for the images generated")

        st.write("### Here's the description of the images")
        st.warning(captions)

        prompt = generate_prompt(captions)
        st.session_state.story = st.session_state.mistral_model.call_model(prompt)

        # st.session_state.story = write_story(captions)
        # st.session_state.logger.log("Story generated")
        # st.session_state.story = dummy_story

        st.write("### Here is your story: ")
        st.success(st.session_state.story)
        # print(st.session_state.story)

        cleaned_story = [
            line.replace("''", "")
            for line in st.session_state.story.split("\n")  # type: ignore
            if line
        ]

        st.session_state.title = cleaned_story[0].split(": ")[1].replace('"', "")
        # print(st.session_state.title)

    if st.session_state.story:
        if "is_downloaded" not in st.session_state:
            st.session_state.is_downloaded = False

        if st.button("Download PDF"):
            createPDF(
                title=st.session_state.title,
                text=st.session_state.story,
                output_filename=f"/home/dell/Downloads/project/pdfs/{st.session_state.title}.pdf",
            )

            st.success("PDF downloaded successfully!")
            st.session_state.is_downloaded = True

        if st.session_state.is_downloaded:
            st.write("### Click the button to send the story to your email")

            send_to = st.text_input("Enter your email address")
            if st.button("Send Email"):
                # st.session_state.logger.log("Sending email")

                send_mail(
                    send_to,
                    f"/home/dell/Downloads/project/pdfs/{st.session_state.title}.pdf",
                )

                # st.session_state.logger.log("Email sent successfully!")

                st.success("Email sent successfully!")


else:
    st.write("### Please select an image first before generating a story")
