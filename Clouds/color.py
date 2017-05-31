
from __future__ import division
print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time
import argparse
#import utils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-c", "--clusters", required = True, type = int,
	help = "# of clusters")
args = vars(ap.parse_args())

# Load the Summer Palace photo
china = cv2.imread(args["image"])
china = cv2.cvtColor(china, cv2.COLOR_BGR2RGB)
# load_sample_image("china.jpg")
n_colors = args["clusters"]
# Convert to floats instead of the default 8 bits integer coding. Dividing by
# 255 is important so that plt.imshow behaves works well on float data (need to
# be in the range [0-1])
china = np.array(china, dtype=np.float64) / 255

plt.figure(1)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Original image (Full colors)')
plt.imshow(china)

# Load Image and transform to a 2D numpy array.
w, h, d = original_shape = tuple(china.shape)
assert d == 3
image_array = np.reshape(china, (w * h, d))

print("Fitting model on a small sub-sample of the data")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0)[:1000]
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)
print("done in %0.3fs." % (time() - t0))

# Get labels for all points
print("Predicting color indices on the full image (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print("done in %0.3fs." % (time() - t0))


codebook_random = shuffle(image_array, random_state=0)[:n_colors + 1]
print("Predicting color indices on the full image (random)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random,
                                          image_array,
                                          axis=0)
print("done in %0.3fs." % (time() - t0))

#-------------------------------------------------------------------
x = (kmeans.cluster_centers_)*255
print x
i = 0
select = range(n_colors)
clusters = np.arange(n_colors)
CM = np.array([int("000000",16),int("030303",16),int("050505",16),int("080808",16),int("0a0a0a",16),
int("0d0d0d",16),int("0f0f0f",16),int("121212",16),int("141414",16),int("171717",16),int("1a1a1a",16),
int("1c1c1c",16),int("1f1f1f",16),int("212121",16),int("242424",16),int("262626",16),int("292929",16),
int("2b2b2b",16),int("2e2e2e",16),int("303030",16),int("333333",16),int("363636",16),int("383838",16),
int("3b3b3b",16),int("3d3d3d",16),int("404040",16),int("424242",16),int("454545",16),int("474747",16),
int("4a4a4a",16),int("4d4d4d",16),int("4f4f4f",16),int("525252",16),int("555555",16),int("575757",16),
int("595959",16),int("5c5c5c",16),int("5e5e5e",16),int("616161",16),int("636363",16),int("666666",16),
int("696969",16),int("6b6b6b",16),int("6e6e6e",16),int("707070",16),int("737373",16),int("757575",16),
int("787878",16),int("7a7a7a",16),int("7d7d7d",16),int("808080",16),int("7f7f7f",16),int("808080",16),
int("828282",16),int("858585",16),int("878787",16),int("8a8a8a",16),int("8c8c8c",16),int("8f8f8f",16),
int("919191",16),int("949494",16),int("969696",16),int("999999",16),int("9c9c9c",16),int("9e9e9e",16),
int("a1a1a1",16),int("a3a3a3",16),int("a6a6a6",16),int("a9a9a9",16),int("a8a8a8",16),int("ababab",16),
int("aaaaaa",16),int("adadad",16),int("b0b0b0",16),int("b3b3b3",16),int("b5b5b5",16),int("b8b8b8",16),
int("bababa",16),int("bdbdbd",16),int("c0c0c0",16),int("bebebe",16),int("bfbfbf",16),int("c2c2c2",16),
int("c4c4c4",16),int("c7c7c7",16),int("c9c9c9",16),int("cdcdcd",16),int("cccccc",16),int("cfcfcf",16),
int("d1d1d1",16),int("d4d4d4",16),int("d3d3d3",16),int("d6d6d6",16),int("d9d9d9",16),int("dcdcdc",16),
int("dbdbdb",16),int("dedede",16),int("e0e0e0",16),int("e3e3e3",16),int("e5e5e5",16),int("e8e8e8",16),
int("ebebeb",16),int("ededed",16),int("f0f0f0",16),int("f2f2f2",16),int("f5f5f5",16),int("f7f7f7",16),
int("fafafa",16),int("fcfcfc",16),int("ffffff",16),int("8b8989",16),int("cdc9c9",16),int("eee9e9",16),
#--------------Up here are all the white to black colors (Grays) --------------------------------------
int("4cb7a5",16),int("2faa96",16),int("dbfef8",16),int("daf4f0",16),int("108070",16),int("2a8e82",16),
int("353f3e",16),int("36dbca",16),int("40e0d0",16),int("99cdc9",16),int("45c3b8",16),int("03a89e",16),
int("457371",16),int("01c5bb",16),int("90fefb",16),int("068481",16),int("838b8b",16),int("7a8b8b",16),
int("c1cdcd",16),int("668b8b",16),int("b4cdcd",16),int("2f4f4f",16),int("2f4f4f",16),int("5f9f9f",16),
int("c0d9d9",16),int("528b8b",16),int("e0eeee",16),int("96cdcd",16),int("388e8e",16),int("79cdcd",16),
int("d1eeee",16),int("8fd8d8",16),int("66cccc",16),int("adeaea",16),int("70dbdb",16),int("aeeeee",16),
int("afeeee",16),int("8deeee",16),int("37fdfc",16),int("008080",16),int("008b8b",16),int("00cdcd",16),
int("00eeee",16),int("00ffff",16),int("97ffff",16),int("bbffff",16),int("e0ffff",16),int("f0ffff",16),
int("00ced1",16),int("5f9ea0",16),int("00867b",16),int("00c5cd",16),int("00e5ee",16),int("00f5ff",16),
int("67e6ec",16),int("4a77aa",16),int("05edff",16),int("53868b",16),int("73b1b7",16),int("05e9ff",16),
int("7ac5cd",16),int("8ee5ee",16),int("05b8cc",16),int("98f5ff",16),int("b0e0e6",16),int("c1f0f6",16),
int("39b7cd",16),int("65909a",16),int("0ebfe9",16),int("c3e4ed",16),int("68838b",16),int("63d1f4",16),
int("9ac0cd",16),int("50a6c2",16),int("add8e6",16),int("b2dfee",16),int("00688b",16),int("009acd",16),
int("0099cc",16),int("00b2cc",16),int("00b2ee",16),int("00bfff",16),int("bfefff",16),int("33a1c9",16),
int("507786",16),int("87ceeb",16),int("38b0de",16),int("0bb5ff",16),int("42c0fb",16),int("6996ad",16),
int("539dc2",16),int("236b8e",16),int("3299cc",16),int("0198e1",16),int("33a1de",16),int("607b8b",16),
int("35586c",16),int("5d92b1",16),int("8db6cd",16),int("325c74",16),int("a4d3ee",16),int("82cffd",16),
int("67c8ff",16),int("b0e2ff",16),int("87cefa",16),int("6ca6cd",16),int("4a708b",16),int("9bc4e2",16),
int("7ec0ee",16),int("87ceff",16),int("517693",16),int("5d7b93",16),int("42647f",16),int("4682b4",16),
int("4f91cd",16),int("5cacee",16),int("63b8ff",16),int("525c65",16),int("36648b",16),int("62b1f6",16),
int("f0f8ff",16),int("4e78a0",16),int("4e78a0",16),int("0d4f8b",16),int("708090",16),int("778899",16),
int("6183a6",16),int("9fb6cd",16),int("7d9ec0",16),int("104e8b",16),int("1874cd",16),int("1c86ee",16),
int("60affe",16),int("007fff",16),int("1e90ff",16),int("6c7b8b",16),int("b7c3d0",16),int("739ac5",16),
int("75a1d0",16),int("b9d3ee",16),int("499df5",16),int("c6e2ff",16),int("3b6aa0",16),int("7aa9dd",16),
int("0276fd",16),int("003f87",16),int("6e7b8b",16),int("506987",16),int("a2b5cd",16),int("4372aa",16),
int("26466d",16),int("1d7cf2",16),int("687c97",16),int("344152",16),int("50729f",16),int("4973ab",16),
int("b0c4de",16),int("3063a5",16),int("bcd2ee",16),int("7eb6ff",16),int("cae1ff",16),int("4d71a3",16),
int("2b4f81",16),int("4981ce",16),int("88ace0",16),int("5993e5",16),int("3a66a7",16),int("3579dc",16),
int("5190ed",16),int("42526c",16),int("4d6fac",16),int("2c5197",16),int("6495ed",16),int("6d9bf1",16),
int("5b90f6",16),int("1464f4",16),int("3a5894",16),int("7093d8",16),int("1b3f8b",16),int("5971ad",16),
int("0147fa",16),int("3d59ab",16),int("27408b",16),int("3a5fcd",16),int("4169e1",16),int("436eee",16),
int("003eff",16),int("4876ff",16),int("a9acb6",16),int("22316c",16),int("162252",16),int("3b4990",16),
int("283a90",16),int("6f7285",16),int("838ede",16),int("e6e8fa",16),int("7d7f94",16),int("2e37fe",16),
int("2f2f4f",16),int("42426f",16),int("8f8fbc",16),int("5959ab",16),int("7171c6",16),int("d9d9f3",16),
int("23238e",16),int("3232cc",16),int("3232cd",16),int("191970",16),int("e6e6fa",16),int("000033",16),
int("000080",16),int("00008b",16),int("00009c",16),int("0000cd",16),int("0000ee",16),int("0000ff",16),
int("3333ff",16),int("4d4dff",16),int("6666ff",16),int("aaaaff",16),int("ccccff",16),int("f8f8ff",16),
int("5b59ba",16),int("120a8f",16),int("302b54",16),int("483d8b",16),int("473c8b",16),int("3b3178",16),
int("6a5acd",16),int("5969cd",16),int("7a67ee",16),int("8470ff",16),int("836fff",16),int("7b68ee",16),
int("3300ff",16),int("ffffff",16)])

AC = np.array([115,119,122,125,129,133,134,135,136,138,141,142,147,148,149,150,158,159,160,168,
173,177,182,185,187,194,196,201,207,208,209,210,212,213,216,224,230,234,237,248,252,259,273,285,
286,308,321,332,334,336,341,348])#131,133,148,[238,272,277]---fault of E photo, 313,344---Fault II phot

DC = np.array([115,119,122,125,127,129,134,135,136,138,141,147,149,150,158,159,160,168,
173,177,182,185,187,194,196,201,207,208,209,210,212,215,224,230,234,237,248,249,259,271,273,285,
286,313,316,321,334,341,348])


#Define clusters

while (i<n_colors):
	R = round(x[i,0])
	G = round(x[i,1])
	B = round(x[i,2])
	#define decimal
	clusters[i] = (R*65536)+(G*256)+B
	
	#define clouds
	NCM = np.absolute(CM-clusters[i])
	M = NCM.min()
	W = zip(*np.where(NCM == M))
	Wx = zip(*np.where(W[0][0] == AC))
	print W
	#print NCM[0]
	print Wx
	print clusters[i]
#-----------------------------------------------------------------------------------
	if ((R>240 and G>240) or (R>240 and B>240) or (B>240 and G>240) and (B>235 and G>235 and R>235)):
		print "The",i," Cluster is: sky"
		select[i]=1
	elif (W[0][0]<113) and abs(B-G)<=20 and abs(B-R)<=20 and abs(R-G)<=20:
		print "The",i," Cluster is: a cloud"
		print abs(B-G)
		print abs(B-R)
		print abs(R-G)
		select[i]=0
	elif (Wx != [] and abs(B-G)<=34 and abs(B-R)<=34 and abs(R-G)<=34):
		print "The",i," Cluster is: a cloud"
		select[i]=0
		print abs(B-G)
		print abs(B-R)
		print abs(R-G)
	else:
		print "The",i," Cluster is: sky"
		select[i]=1
		print abs(B-G)
		print abs(B-R)
		print abs(R-G)
	i = i+1

print select
print labels
'''
c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
cf = 0

while (cf < len(labels)):
	if (labels[cf] == 0):
		c0 = c0+1
	elif (labels[cf] == 1):
		c1 = c1+1
	elif (labels[cf] == 2):
		c2 = c2+1
	elif (labels[cf] == 3):
		c3 = c3+1
	elif (labels[cf] == 4):
		c4 = c4+1
	elif (labels[cf] == 5):
		c5 = c5+1
	elif (labels[cf] == 6):
		c6 = c6+1
	elif (labels[cf] == 7):
		c7 = c7+1
	elif (labels[cf] == 8):
		c8 = c8+1
	else:
		c9 = c9+1
	cf = cf+1

print "The cluster 0 percentage is: " ,(c0/len(labels))*100
print "The cluster 1 percentage is: " ,(c1/len(labels))*100
print "The cluster 2 percentage is: " ,(c2/len(labels))*100
print "The cluster 3 percentage is: " ,(c3/len(labels))*100
print "The cluster 4 percentage is: " ,(c4/len(labels))*100
print "The cluster 5 percentage is: " ,(c5/len(labels))*100
print "The cluster 6 percentage is: " ,(c6/len(labels))*100
print "The cluster 7 percentage is: " ,(c7/len(labels))*100
print "The cluster 8 percentage is: " ,(c8/len(labels))*100
print "The cluster 9 percentage is: " ,(c9/len(labels))*100
'''
cloud = 0
sky = 0
m = 0

while (m < len(labels)):
	if (select[labels[m]] == 0):
		cloud = cloud+1
	else:
		sky = sky+1
	m = m+1

d=0
while (d<len(labels)):
	c = labels[d]
	labels[d] = select[c]
	d = d+1


print "The cloud percentage is: " ,(cloud/len(labels))*100
print "The sky percentage is: " ,(sky/len(labels))*100

kmeans.cluster_centers_[0] = [1, 1, 1]
kmeans.cluster_centers_[1] = [0, 0, 0]
#print kmeans.cluster_centers_

def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

# Display all results, alongside original image
plt.figure(1)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Original image (Full colors)')
plt.imshow(china)

plt.figure(2)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Quantized image (Selected colors, K-Means)')
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))
plt.savefig('/home/pi/DriverS/Clouds/Images/Result/cloud.jpg')

'''plt.figure(3)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Quantized image (Selected colors, Random)')
plt.imshow(recreate_image(codebook_random, labels_random, w, h))'''
plt.show()

#python color.py --image /home/pi/DriverS/Clouds/Images/Test/cloud.jpg --clusters 10
