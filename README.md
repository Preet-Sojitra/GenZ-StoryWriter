# GenZ Story Writer

## Description

This project was created as a part of my Advance Python Lab course. This is a streamlit app that generates a story based on the user's input images. User can search for the images and select the images that they want to use for the story. User can select multiple images and the app will generate a story based on the images selected.

## Demo

View the demo of this app [here](https://youtu.be/3kPGzmmaWd4).

## Features

- User authentication
- User can search for the images using the search bar.
- User can select multiple images.
- User can generate a story based on the images selected.
- User can download the story as a pdf file.
- User gets a mail with the story as a pdf file.

## Tech Stack and Libraries Used

- **Web UI**: Streamlit
- **Authentication**: Pandas
- **Web Scrapping**: Beautiful Soup
- **Image Captioning**: [Vision Transformer GPT](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning)
- **Story Generation**: [Mistral-7b](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
- **PDF Generation**: Fpdf
- **Email Service**: SMTP

## Working

Under the hood, this is how this app works:

- User first logs in to the app using their credentials. If the user is not registered, they can register themselves. Authentication is implemented via reading and writing data to a csv file using `pandas` library.
- Once the user is logged in, they can search for the images using the search bar. We have implemented a web scraper that scrapes the images from the web.
- User then selects the images that they want to use for the story. The selected images are then downloaded and stored in the `tmp` folder.
- Those selected images are then passed to the `Vision Transformer GPT` model which generates the captions for the images.
- These captions are then passed to `generate_prompt` function which transforms these captions into appropriate prompts.
- This prompot is then passed to the `Mistral-7b` model which generates the story.
- As soon as the story is generated, it is displayed to the user and it is also sent to the user's mail via `SMTP` server.
- User can also download the story as a pdf file which is generated using `Fpdf` library.

## Try it locally

### Prerequisites

> Make sure you have python3 installed on your system. If not, you can download it from [here](https://www.python.org/downloads/). Once you have python3 installed, you can follow the steps below to try this app locally.

Before you try this app locally, you need to download the models and place them in the root directory of this project.

- Download the `Vision Transformer GPT` model from [here](https://drive.google.com/drive/folders/1N5soM8Y5EPBrGfxKGxQhkz2R19FHaCbi?usp=sharing) and place it in the root directory of this project. Download the `model_weights` folder and place it in the root directory of this project.

- Download the `Mistral-7b` model from [here](https://drive.google.com/drive/folders/1gbIBOmSF1RFpsaZV2IhrqcCHa65d9Y6j?usp=sharing) and place it in the root directory of this project. Download the `mistral-7b-instruct-v0.1.Q4_K_M.gguf` file and place it in the root directory of this project.

Now one last thing that you need to do is to create a `.env` file in the root directory of this project and add the following lines to it:

```bash
SENDER_EMAIL="your_email_address"
SENDER_EMAIL_PASSWORD="xxxx xxxx xxxx xxxx"
```

- Replace the `SENDER_EMAIL` with your email address.
- Replace the `SENDER_EMAIL_PASSWORD` with your email password.

  > NOTE: This is not your email password. This is the app password. Follow the steps that are mentioned [here](https://stackoverflow.com/a/72734404/16273741) to generate the app password. The app password is a 16 digit password and is of the form `xxxx xxxx xxxx xxxx`. Without this, email service will not work.

Now you are all set to try this app locally.

### Steps

Follow this steps to try this app locally:

1. Clone this repository.

```bash
git clone https://github.com/Preet-Sojitra/GenZ-StoryWriter
```

2. Navigate to the cloned repository.

```bash
cd GenZ-StoryWriter
```

> Creation and activation of virtual environment depends on the OS you are using. Follow the steps below according to your OS. You are recommened to refer the offical documentation to be on safer side. In case you face any issues, you can raise an issue.

3. Create a virtual environment.

```bash
python3 -m venv .venv
```

4. Activate the virtual environment.

   - If you are on Windows and using `cmd`:

   ```bash
   .venv\Scripts\activate.bat
   ```

   - If you are on Windows and using `powershell`:

   ```bash
   .venv\Scripts\activate.ps1
   ```

   - If you are on Linux or Mac:

   ```bash
   source .venv/bin/activate
   ```

   > Creation and activation of virtual environment is a one time process. You can skip these steps the next time you want to run the app locally.

5. Install the dependencies.

```bash
pip install -r requirements.txt
```

6. Run the app.

```bash
streamlit run Signup.py
```

> ❗**NOTE:** Mistral-7b model is a very large model and it takes a lot of time to load and generate the story. So, please be patient while the app is loading and generating the story. It will take minimum of 5 minutes to load and generate the story. Time taken to load and generate the story depends on your system configuration.

#### Work around for mistral-7b model taking much time:

We have implemented a work around for the mistral-7b model. We have made one `mock_story_generator.py` file which tries to replicate the mistral-7b model. It sends a dummy story (
dummy story is a story that is generated by the mistral-7b model only) after dealy of 8 seconds. So if you want to try the app without waiting for the mistral-7b model to load, you can use this work around.

To use this work around, you need to make some changes in the [pages/2_GenZ_Story_Writer.py](pages/2_GenZ_Story_Writer.py) file.

- Comment out the following lines:

```python
st.session_state.story = st.session_state.mistral_model.call_model(prompt)
```

and

- Uncomment the following lines:

```python
st.session_state.story = call_model(prompt)
```

Now run the app again.

## Future Plans

- Instead of using the web scraper, we can use stable diffusion models to generate the images.
- Enter one more field of text input to take prompt from the user. So that it can be used to tell the model in which direction the story should go.
- From story, generate a video using the images and the story.

## Originally Developed By

- Preet Sojitra
- Raj Randive
- Anuj Patel
- Kishan Pipariya
- Dhwani Chauhan
- Adhyayan Rana

## Contributing

Contributions are always welcome! Feel free to raise a PR for any kind of contributions.

If you have any queries, feel free to raise an issue.
