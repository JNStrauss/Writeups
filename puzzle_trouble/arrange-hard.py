from PIL import Image
import numpy as np

im = Image.open("puzzle-trouble-hard.jpg")

width, height = im.size

col = 16
row = 16

init_order = []

order = np.array([['0902', '1106', '0610', '0510', '0414', '0205', '1003', '0314', '0110', '1508', '0615', '1015', '0209', '0509', '0704', '0311'],
                  ['0409', '1113', '0309', '0603', '0708', '1506', '0206', '0911', '0512', '1405', '0504', '0705', '1205', '1306', '0513', '1211'],
                  ['1301', '0402', '1204', '1102', '1504', '0113', '1114', '1411', '0508', '0703', '1109', '0806', '0215', '0105', '0710', '1514'],
                  ['0907', '0906', '0706', '0609', '0502', '1200', '0606', '0111', '0600', '1103', '1414', '0306', '0515', '0500', '0800', '0008'],
                  ['0300', '1105', '0503', '1511', '1004', '0905', '1502', '0302', '1403', '0015', '0313', '0411', '0305', '1404', '0914', '1313'],
                  ['0608', '1407', '1310', '0001', '1005', '0908', '0614', '1503', '1500', '0315', '0212', '1012', '0408', '0814', '0903', '0904'],
                  ['0410', '0103', '0812', '1309', '0915', '0003', '1101', '1509', '0612', '1110', '0511', '0412', '0403', '0012', '0108', '0200'],
                  ['0810', '0901', '1207', '1400', '0415', '1513', '0006', '1100', '1107', '1006', '0602', '0713', '0501', '0208', '0115', '1213'],
                  ['1203', '0213', '0803', '1000', '1111', '1115', '0613', '0009', '0605', '0805', '0107', '0601', '1415', '0910', '1303', '0913'],
                  ['0700', '0203', '0808', '1305', '1401', '0010', '0004', '1209', '0312', '0014', '0506', '0804', '0404', '0102', '0000', '0304'],
                  ['0813', '0809', '0303', '1208', '1201', '1406', '0802', '1302', '0202', '1104', '0002', '0101', '1515', '0711', '1409', '1312'],
                  ['0413', '1307', '0715', '0211', '0709', '0701', '0301', '1206', '0400', '1214', '0210', '0204', '0020', '0013', '0604', '0207'],
                  ['1512', '1413', '1011', '1510', '0114', '1314', '0201', '0807', '0005', '0815', '1210', '1108', '0607', '1001', '0811', '0100'],
                  ['0214', '1212', '0801', '1507', '0714', '1304', '0407', '0307', '1008', '1013', '1009', '1501', '0611', '1112', '0011', '0112'],
                  ['1007', '0912', '1215', '0507', '0514', '0405', '1412', '0707', '0308', '1014', '0505', '0007', '1300', '0702', '0712', '1315'],
                  ['0109', '1308', '1505', '1410', '0900', '0106', '0406', '1010', '1402', '0401', '1202', '0909', '1311', '1002', '1408', '0310']])

#iorder -= 1 # I started indexing the pieces with 1 instead of 0
def proper(n):
    #o = np.array(n[:, :2], dtype=int)
    #a = np.array(n[:, 2:], dtype=int)
    o = int(n[:2])
    a = int(n[2:])
    return o*16 + a

# Define the vectorized function using np.vectorize
proper_vec = np.vectorize(proper)

iorder = proper_vec(order)
#print(iorder)
order = iorder 

for i in range(row):
    for j in range(col):
        piece = im.crop((j*(width/col), i*(height/row), j*(width/col) + (width/col), i*(height/row) + (height/row)))
        init_order.append(piece)

# Get the size of each block

image_width, image_height = init_order[0].size

# Create an empty image to store the final result

final_image = Image.new(mode='RGB', size=(col * image_width, row * image_height))

# Iterate through the array and paste each block into the final image

for r in range(row):
    for c in range(col):
        x = c * image_width
        y = r * image_height
        #print(r,c, order[r,c])
        final_image.paste(init_order[order[r, c]], (x, y))
        #final_image.paste(order[r, c], (x, y))

# Save and show the final image

final_image.save('output.png')
#final_image.show()
