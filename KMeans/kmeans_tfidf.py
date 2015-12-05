from scipy.cluster.vq import kmeans2
import gzip
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from nltk import word_tokenize
import csv
from sklearn.decomposition import PCA
import numpy as np
from vaderSentiment.vaderSentiment import sentiment as vs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


lmtzr = WordNetLemmatizer()
stop = stopwords.words('english')

reviewlist=list()
ratinglist=list()
featureset=set()
featurelist=list()
reviewTextlist=list()
scorelist=list()

counter=0


g = open("path/to/test_data", 'r')
for l in g:
   	review = eval(l)
   	reviewText = review["reviewText"]
   	rating = review["overall"]
   	score=vs(reviewText)["compound"]
   	s = [lmtzr.lemmatize(i) for i in word_tokenize(reviewText) if i not in stop and i not in string.punctuation and i.isalpha()]
   	featureset=featureset.union(set(s))
featurelist=list(featureset)

for l in g:
    review = eval(l)
    reviewText = review["reviewText"]
    rating = review["overall"]
    s = [lmtzr.lemmatize(i) for i in word_tokenize(reviewText) if i not in stop and i not in string.punctuation and i.isalpha()]
    slist=[0]*len(featurelist)
    for item in s:
		slist[featurelist.index(item)]+=1
    		#print len(featurelist), len(slist), item
    reviewlist.append(slist)
    ratinglist.append(rating)
    reviewTextlist.append(reviewText)

reviewdata=np.array(reviewlist)
pca = PCA(n_components=5)
pca.fit(reviewdata)
newreviewdata = pca.transform(reviewdata)

centroids,labels=kmeans2(newreviewdata,5)

colors=['red','green','blue','yellow','black']
colorvalues=[colors[i] for i in labels]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(newreviewdata[:,0],newreviewdata[:,1],0,c=colorvalues,s=50)

plt.show()

with open("cluster-rating-tfidf.csv","wb") as f:
	csvwriter = csv.writer(f,delimiter="|")
	for i in range(len(labels)):
		csvwriter.writerow([labels[i],ratinglist[i],reviewTextlist[i]])




