from PIL import Image
from pylab import *
img_dir = r"C:\Users\ranas\OneDrive\Desktop\EasyCSELearn\ComputerVisionA2Z\img\A0115_01_.jpg"

pil_img = Image.open(img_dir)

img_arr = array(pil_img)

imshow(img_arr)

x = [ 100, 100, 400, 400]
y = [200,500,200,500]

plot(x, y , 'r*')
#plot(x[:2], y[:2])

title('With Matplotlib Image "myimg.jpg"')
show()