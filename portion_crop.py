from PIL import Image

img_dir = r"C:\Users\ranas\OneDrive\Desktop\EasyCSELearn\ComputerVisionA2Z\img\A0115_01_.jpg"

pil_img = Image.open(img_dir)

crop_area = (348,185, 501, 432)


cropped_img = pil_img.crop(crop_area)

cropped_img.show()
