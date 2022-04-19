# imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# load picture
img=mpimg.imread('pic01.jpg')

# convert img to numpy array
img_np = np.array(img)

# size of array 
print(img_np.shape)

# iterate over pixel 
for x in range(img_np.shape[0]):
    for y in range(img_np.shape[1]):
        if np.sum(img_np[x,y,:]) > (765/4*3):
            print(' ',end = '')
        elif np.sum(img_np[x,y,:]) > (765/4*2):
            print('•',end = '')
        elif np.sum(img_np[x,y,:]) > (765/4*1):
            print('●',end = '')
        else:
            print('⓪',end = '')
    
    print('')

# convert numpy array to pic
plt.imshow(img_np, interpolation='nearest')
plt.show()

print('done',end = '')
print('Das ist meine Änderung')
