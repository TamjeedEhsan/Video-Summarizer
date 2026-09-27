from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from PIL import Image
import os


# Load the BLIP processor
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Load the pretrained BLIP model
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def generate_caption(image_path):

    # Open the image
    image = Image.open(image_path).convert("RGB")

    # Prepare the image for the model
    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    # Generate a caption
    output = model.generate(**inputs)

    # Convert model output into readable text
    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption


def generate_video_captions(folder_path):

    captions = []

    # Get all frame filenames
    frame_files = sorted(os.listdir(folder_path))

    for frame_file in frame_files:

        # Only process JPG images
        if not frame_file.endswith(".jpg"):
            continue

        frame_path = os.path.join(
            folder_path,
            frame_file
        )

        # Generate caption
        caption = generate_caption(frame_path)

        print(frame_file, ":", caption)

        # Store caption
        captions.append(caption)

    return captions


# Load the BART tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "facebook/bart-large-cnn"
)

# Load the BART model
summary_model = AutoModelForSeq2SeqLM.from_pretrained(
    "facebook/bart-large-cnn"
)


def generate_summary(captions):

    # Combine all captions into one piece of text
    text = ". ".join(captions)

    # Convert text into tokens
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    # Generate the summary
    output = summary_model.generate(
        **inputs,
        max_length=100,
        min_length=20,
        do_sample=False
    )

    # Convert generated tokens into readable text
    summary = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    return summary