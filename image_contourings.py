from PIL import Image
from pylab import  *
img_dir = r"C:\Users\ranas\OneDrive\Desktop\EasyCSELearn\ComputerVisionA2Z\img\A0115_01_.jpg"

pil_img = Image.open(img_dir).convert('L')

img_arr = array(pil_img)

figure()

gray()

contour(img_arr, origin="image")

axis('equal')

axis('off')

show()