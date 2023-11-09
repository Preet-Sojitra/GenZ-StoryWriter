from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image


class ImageCaptioning:
    def __init__(self):
        self.model = VisionEncoderDecoderModel.from_pretrained("model_weights/model")
        self.feature_extractor = ViTImageProcessor.from_pretrained(
            "model_weights/features"
        )
        self.tokenizer = AutoTokenizer.from_pretrained("model_weights/tokenizer")

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)  # type: ignore

        print("Model has been initialized of Image Captioner ")

        max_length = 16
        num_beams = 4
        self.gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

    def captionIt(self, image_paths):
        images = []
        for image_path in image_paths:
            i_image = Image.open(image_path)
            if i_image.mode != "RGB":
                i_image = i_image.convert(mode="RGB")

            images.append(i_image)

        pixel_values = self.feature_extractor(images=images, return_tensors="pt").pixel_values  # type: ignore
        pixel_values = pixel_values.to(self.device)

        output_ids = self.model.generate(pixel_values, **self.gen_kwargs)  # type: ignore

        preds = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        preds = [pred.strip() for pred in preds]

        return preds
