import cv2
import numpy as np
import random 
img=cv2.imread("p.jpg") 

#resize image to make sure 4 pieces have the same dimension
image = cv2.resize(img, (400,400),interpolation=cv2.INTER_AREA)

height, width, channels = image.shape

frame_1=image[0:int(height/2),0:int(width/2)]
frame_2=image[0:int(height/2),int(width/2):int(width)]
frame_3=image[int(height/2):int(height),0:int(width/2)]
frame_4=image[int(height/2):int(height),int(width/2):int(width)]

new_image = np.empty_like(image)
random_array=[frame_1,frame_2,frame_3,frame_4]
r=random.sample(range(4), 4)
new_image[0:int(height/2),0:int(width/2)] = random_array[r[0]]
new_image[0:int(height/2),int(width/2):int(width)] = random_array[r[1]]
new_image[int(height/2):int(height),0:int(width/2)] = random_array[r[2]]
new_image[int(height/2):int(height),int(width/2):int(width)] = random_array[r[3]]

cv2.imshow("image",image)
cv2.imshow("new_image",new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()