import requests
from bs4 import BeautifulSoup
import urllib.parse
import os


def scrap_images(query, num_images):
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        image_links = []

        for img in soup.find_all("img"):
            image_links.append(img.get("src"))

        # print(f"Found {len(image_links)} images.")
        # print(image_links)

        if num_images == 1:
            return image_links[1:2]
        else:
            return image_links[1 : num_images + 1]
    else:
        print("Failed to retrieve search results.")
        return []


def download_images(image_links, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for i, image_link in enumerate(image_links):
        try:
            image_data = requests.get(image_link).content
            with open(os.path.join(output_folder, f"image_{i + 1}.jpg"), "wb") as f:
                f.write(image_data)
            print(f"Downloaded image {i + 1}")

        except Exception as e:
            print(f"Failed to download image {i + 1}: {str(e)}")
