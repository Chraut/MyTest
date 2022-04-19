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

#img_np = np.array([[1, 2, 3], [4, 5, 6]])

# iterate over pixel 
'''
for x in img_np:
    for y in x:
        y[0] = 255
        y[1] = 255
'''

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

"""
# show image
plt.imshow(img)
plt.show()
"""

print('done',end = '')
print('Das ist meine Änderung')
