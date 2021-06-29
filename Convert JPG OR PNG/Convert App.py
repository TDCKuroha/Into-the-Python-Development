from PIL import Image
import os
  
# importing the image 
im = Image.open("02.jpeg")
  
# converting to jpg
rgb_im = im.convert("RGB")
  
# exporting the image
rgb_im.save("geeksforgeeks_02.jpg")
