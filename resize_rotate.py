from PIL import Image

img_dir = r"C:\Users\ranas\OneDrive\Desktop\EasyCSELearn\ComputerVisionA2Z\img\A0115_01_.jpg"

pil_img = Image.open(img_dir)

resize_img = pil_img.resize((128,128))
resize_img = resize_img.rotate(180)
resize_img.show()