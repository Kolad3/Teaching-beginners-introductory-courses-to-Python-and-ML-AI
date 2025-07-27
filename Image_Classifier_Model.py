# This code implements an image classifier using the Hugging Face Transformers library.
# It classifies images into categories using a pre-trained model.

# Step 1: Install Hugging Face Transformers

# Step 2: Import pipeline
from transformers import pipeline
from PIL import Image

# Step 3: Load the image classifier model
classifier = pipeline("image-classification")

# Step 4: Load a sample image from the web
path = "C:\\Users\\DELL\\Documents\\Teens Empowerment\\cat_image.jpeg"      # Path to the image file in my personal computer, replace with your image path
                                                                            # If you want to use an image from the web, you can download it first or use a library like requests to fetch it from a URL.
                                                                            # For example, if you have an image URL, you can use requests to download it.
image = Image.open(path)

# Step 5: Classify the image
results = classifier(image)
for result in results:
    print(f"{result['label']}: {round(result['score']*100, 2)}%")
