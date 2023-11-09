import streamlit as st
import os
from streamlit_image_select import image_select
from utils.generate_prompt import generate_prompt
from utils.ImageCaptioner import ImageCaptioning
from utils.createPDF import createPDF
from utils.sendEmail import send_mail
from utils.scrapImages import scrap_images, download_images
from utils.script_generator import MistralModel
from utils.mock_story_generator import call_model

if "title" not in st.session_state:
    st.session_state.title = ""

if "images" not in st.session_state:
    st.session_state.images = []

if "selected_images" not in st.session_state:
    st.session_state.selected_images = []

if "story" not in st.session_state:
    st.session_state.story = ""

if "downloaded" not in st.session_state:
    st.session_state.downloaded = False

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
    
    ### Try it out!
    """
)

# search bar for searching images
search_term = st.text_input("Search for images", placeholder="Search image")
# enter number of images to download
num_images = st.number_input("Number of images to download", min_value=1, value=1)
search_button = st.button("Search")


# if search term is not empty and search button is clicked and number of images is greater than 0, then only search for images
if search_term and search_button and num_images > 0:
    # need to reset the images array, so that whenever user searches for the image again, he can see new images
    st.session_state.images = []

    with st.spinner("Please wait while we crawl the web for images"):
        # scrap the images
        image_links = scrap_images(search_term, num_images)
        # download the images
        download_images(image_links, "tmp/{}".format(search_term))

        if len(image_links) == 0:
            st.error("No images found for the search term")
            st.stop()

        # store the images in the session state, so that we can show them to the user
        for i in range(int(num_images)):
            st.session_state.images.append(f"tmp/{search_term}/image_{i + 1}.jpg")


# if there are images in the session state, then show them to the user
if len(st.session_state.images) > 0:
    st.write("Here are the images for your search term: ")
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

    clear = st.button("Clear all images")
    if clear:
        st.session_state.selected_images = []
        st.session_state.images = []
        st.rerun()
        st.success("Images cleared successfully!")

# if user has selected images, then show the button to generate the story
if len(st.session_state.selected_images) > 0:
    st.write("### It's time to generate a story!")
    # print(st.session_state.selected_images)

    st.write(
        "Enter email address. We will send the story to your email address after generating it."
    )
    send_to = st.text_input(
        "Enter your email address",
        label_visibility="collapsed",
        placeholder="Enter your email address",
    )

    if st.button("Generate Story"):
        if send_to == "":
            st.error("Please enter your email address")
        else:
            with st.spinner("Please wait while we generate a story for you"):
                if "ic" not in st.session_state:
                    st.session_state.ic = ImageCaptioning()

                if "mistral_model" not in st.session_state:
                    st.session_state.mistral_model = MistralModel()

                captions = st.session_state.ic.captionIt(
                    st.session_state.selected_images
                )

                st.write("### Here's the description of the images")
                st.warning(captions)

                prompt = generate_prompt(captions)
                st.session_state.story = st.session_state.mistral_model.call_model(
                    prompt
                )

                # Below line is for testing purposes only. It calls the mock story generator. Mock story generator tries to replicate the behaviour of the mistral model. It returns a dummy story after a delay of 8 seconds. Since the mistral model takes much time to generate the story, we are using the mock story generator to replicate the behaviour of the mistral model for testing purposes. Uncomment the below line and comment the above line to use the mock story generator for testing.

                # st.session_state.story = call_model(prompt)

                print(st.session_state.story)

    if st.session_state.story:
        st.write("### Here is your story: ")
        st.success(st.session_state.story)

        cleaned_story = [
            line.replace("''", "")
            for line in st.session_state.story.split("\n")  # type: ignore
            if line
        ]
        st.session_state.title = cleaned_story[0].split(": ")[1].replace('"', "")

        # show the download button only if the story is generated
        if st.button("Download PDF"):
            createPDF(
                title=st.session_state.title,
                text=st.session_state.story,
                output_filename=f"pdfs/{st.session_state.title}.pdf",
            )

            st.success("PDF downloaded successfully!")

        # keep track of whether the email is sent or not. So that we don't send the email again and again
        if "email_sent" not in st.session_state:
            st.session_state.email_sent = False

        if not st.session_state.email_sent:
            # save the story in a tmp pdf file, so that it can be sent to the user via email
            createPDF(
                title=st.session_state.title,
                text=st.session_state.story,
                output_filename=f"tmp_pdfs/{st.session_state.title}.pdf",
            )

            # Mail the story to the user
            try:
                send_mail(send_to, f"tmp_pdfs/{st.session_state.title}.pdf")
            except:
                st.error(
                    "Email could not be sent. Try entering a valid email address or try again later."
                )

            st.session_state.email_sent = True

            # Now delete the pdf file
            os.remove(f"tmp_pdfs/{st.session_state.title}.pdf")

else:
    st.write("### Please select an image first before generating a story")
