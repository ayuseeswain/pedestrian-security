import os
from simple_image_download import simple_image_download as simp

# Create a "simple_images" folder in the same directory as this file, for generating image data into this folder
folder_name = "simple_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create an instance of the simple_image_download class
response = simp.simple_image_download

# Define a list of keywords for the types of images to be downloaded
# In this case, we're looking for images of "people walking on road"
keywords = ["people walking on road"]

# Loop through each keyword in the list
for kw in keywords:
    # For each keyword, call the download method of the response object
    # The first argument is the keyword, and the second is the number of images to download
    response().download(kw, 100)