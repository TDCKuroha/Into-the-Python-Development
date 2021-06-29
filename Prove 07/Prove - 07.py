from PIL import Image, ImageFilter

SIZE = (800, 600)
imagen_beach = Image.open("snowscape.jpg").resize(SIZE)
imagen_cactus = Image.open("black1.jpg").resize(SIZE)
img_green = imagen_cactus.filter(ImageFilter.GaussianBlur(0.24))

for y in range (imagen_cactus.height):
    for x in range(imagen_cactus.width):
        pixel_beache = imagen_beach.getpixel((x, y))
        r, g, b, = img_green.getpixel((x, y))
        if r < 125 and g >= 160 and b < 125:
            img_green.putpixel((x, y), pixel_beache)
       
img_green.show()
img_green.save("Overlay.jpg")















