from PIL import Image

img_dir = r"C:\Users\ranas\OneDrive\Desktop\EasyCSELearn\ComputerVisionA2Z\img\A0115_01_.jpg"

pil_img = Image.open(img_dir)

pil_img.show()

gray_img = pil_img.convert("L")

gray_img.show()