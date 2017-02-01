#  Function of this script: to get the results of survey automatically
#  In order to fit all kinds of survey, we need to change parameters of the input, changing the axis area.
#  This script deals with four questions, put them into a list, the jpg file is a scan of survey
#  Author: Zizhuo Ren
from PIL import Image
from operator import itemgetter
im = Image.open("/Users/zizhuoren/Desktop/file-page1 2.jpg")
im.show()
import numpy as np
import csv
import pandas as pd
def image2pixelarray(filepath):
    """
    Parameters
    ----------
    filepath : str
        Path to an image file

    Returns
    -------
    list
        A list of lists which make it simple to access the greyscale value by
        im[y][x]
    """
    im = Image.open(filepath).convert('L')
    (width, height) = im.size
    greyscale_map = list(im.getdata())
    greyscale_map = np.array(greyscale_map)
    greyscale_map = greyscale_map.reshape((height, width))
    return greyscale_map

# Open a picture file
temp = image2pixelarray("/Users/zizhuoren/Desktop/file-page1 2.jpg")
# y is 1164 - 1184, x1 is 339 - 359 , x2 is 753 - 773

# Deal with the first survey x axis is 444 - 463, y1 is 775 - 795, y2 is 837 - 857 
# y3 is 898 - 918
#start1
value_list1 = [] 
axis_sum1_1 = 0
axis_sum2_1 = 0
axis_sum3_1 = 0
for i in range(775, 796):
    axis_sum1_1 += sum(temp[i][444: 463])
for j in range(837, 857):
    axis_sum2_1 += sum(temp[j][444: 463])
for k in range(898, 918):
    axis_sum3_1 += sum(temp[k][444: 463])
value_list1.append(axis_sum1_1)
value_list1.append(axis_sum2_1)
value_list1.append(axis_sum3_1)
result1 = min(enumerate(value_list1), key=itemgetter(1))[0] + 1

value_list2 = [] 
axis_sum1_2 = 0
axis_sum2_2 = 0
for i in range(1164, 1184):
    axis_sum1_2 += sum(temp[i][339: 359])
for j in range(1164, 1184):
    axis_sum2_2 += sum(temp[j][753: 773])

value_list2.append(axis_sum1_2)
value_list2.append(axis_sum2_2)

result2 = min(enumerate(value_list2), key=itemgetter(1))[0] + 1

#Deal with the first survey x axis is 444 - 463, y1 is 1491 - 1510, y2 is 837 - 857 
# y3 is 898 - 918
#start1
value_list3 = [] 
axis_sum1_3 = 0
axis_sum2_3 = 0
axis_sum3_3 = 0
for i in range(1491, 1510):
    axis_sum1_3 += sum(temp[i][444: 463])
for j in range(1554, 1574):
    axis_sum2_3 += sum(temp[j][444: 463])
for k in range(1614, 1634):
    axis_sum3_3 += sum(temp[k][444: 463])
value_list3.append(axis_sum1_3)
value_list3.append(axis_sum2_3)
value_list3.append(axis_sum3_3)
result3 = min(enumerate(value_list3), key=itemgetter(1))[0] + 1

# Deal with the first survey x axis is 444 - 463, y1 is 1491 - 1510, y2 is 837 - 857 
# y3 is 898 - 918
#start1
value_list4 = [] 
axis_sum1_4 = 0
axis_sum2_4 = 0
axis_sum3_4 = 0
for i in range(1858, 1878):
    axis_sum1_4 += sum(temp[i][444: 463])
for j in range(1921, 1941):
    axis_sum2_4 += sum(temp[j][444: 463])
for k in range(1982, 2002):
    axis_sum3_4 += sum(temp[k][444: 463])
value_list4.append(axis_sum1_4)
value_list4.append(axis_sum2_4)
value_list4.append(axis_sum3_4)
result4 = min(enumerate(value_list4), key=itemgetter(1))[0] + 1
print ([result1,result2, result3, result4])