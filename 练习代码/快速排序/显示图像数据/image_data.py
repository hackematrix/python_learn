from PIL import Image
import numpy as np

img=Image.open("D:\\piture\\161458933.jpg")

img_arr=np.array(img)
img_type=img_arr.dtype
img_shape=img_arr.shape

print(img_type)
print(img_shape)
