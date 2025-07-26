# Step 1: Install Hugging Face Transformers

# Step 2: Import pipeline
from transformers import pipeline
from PIL import Image

# Step 3: Load the image classifier model
classifier = pipeline("image-classification")

# Step 4: Load a sample image from the web
path = "C:\\Users\\DELL\\Documents\\Teens Empowerment\\cat_image.jpeg"
image = Image.open(path)

# Step 5: Classify the image
results = classifier(image)
for result in results:
    print(f"{result['label']}: {round(result['score']*100, 2)}%")
