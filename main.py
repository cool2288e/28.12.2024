from PIL import Image
from PIL import ImageFilter

with Image.open("dexter.jpg") as image_original:
    image_original.show()

    image_gray = image_original.convert("L")
    image_gray.save("dexter_gray.jpg")
    image_gray.show()

    image_blur = image_original.filter(ImageFilter.BLUR)
    image_blur.save("dexter_blur.jpg")

    image_rotate = imaqge_original.transpose(Image.ROTATE_180)
    image_rotate.save("dexter_rotate.jpg")