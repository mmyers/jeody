#libraries used
import csv
import re
from nltk.stem import PorterStemmer
import math
import random
import sys, getopt


def main():
    inputfile = ''
    numK = ''
    argStor = []
    for arg in sys.argv[1:]:
        argStor.append(arg)
    inputfile = argStor[0]
    numK = argStor[1]
    program(inputfile, numK)


def program(path, k):
    #open file
    with open(path) as f:
        jeoInstancesOriginal = [list(line) for line in csv.reader(f)]
    jeoInstances = jeoInstancesOriginal
    jeoInstancesOriginal = [item[6] for item in jeoInstancesOriginal]
    jeoInstances = preProcessing(jeoInstances)
    jeoQuestions = [item[6] for item in jeoInstances]
    kCluster(jeoQuestions, 60, jeoInstancesOriginal)

def preProcessing(jeoInstances):
    
    #remove the header
    jeoInstances.pop(0)
    
    #first remove all of the non-alpha characters from each question and make lowercase
    regex = re.compile('[^a-zA-Z ]')
    
    #I used an online list of recognized stopwords
    stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "arent", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldnt", 'did', "didnt", 'do', 'does', "doesnt", 'doing', "dont", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadnt", 'has', "hasnt", 'have', "havent", 'having', 'he', "hed", "hes", 'her', 'here', "heres", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "id", "im", "ive", 'if', 'in', 'into', 'is', "isnt", 'it', 'its', 'itself', "lets", 'me', 'more', 'most', "mustnt", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shant", 'she', "shes", 'should', "shouldnt", 'so', 'some', 'such', 'than', 'that', "thats", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "theres", 'these', 'they', "theyd", "theyll", "theyre", "theyve", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "weve", 'were', "werent", 'what', "whats", 'when', "whens", 'where', "wheres", 'which', 'while', 'who', "whos", 'whom', 'why', "whys", 'with', "wont", 'would', "wouldnt", 'you', "youd", "youll", "youre", "youve", 'your', 'yours', 'yourself', 'yourselves', 'hrefhttpwwwjarchivecommediadjjpg']    
    
    port = PorterStemmer()
    for i in xrange(len(jeoInstances)):
        jeoInstances[i][6] = regex.sub('', jeoInstances[i][6]).lower()
        jeoInstances[i][6] = ' '.join([word for word in jeoInstances[i][6].split() if word not in stopwords])
        jeoInstances[i][6] = ",".join([port.stem(x) for x in jeoInstances[i][6].split()])
        jeoInstances[i][6] = jeoInstances[i][6].encode("utf-8").split(",")
    return jeoInstances

#-----This all relates to cosine similarity (below)-----
#for dot product
def dotProd(a1, b1):
    return sum(map(lambda x: x[0] * x[1], zip(a1, b1)))

#for actual cosine calculation
def cosine(a1, b1):
    prod = dotProd(a1, b1)
    first = math.sqrt(dotProd(a1, a1))
    second = math.sqrt(dotProd(b1, b1))
    return prod / (first * second)

#formatting to obtain overlap
def cosineSim(a,b):
    c = list(set().union(a,b))
    a1 = []
    b1 =[]
    for word in c:
        a1.append(a.count(word))
        b1.append(b.count(word))    
    return cosine(a1,b1)
#-----This all relates to cosine similarity (above)-----

def findMax(question, centers):
    storage = []
    for j in centers:
        storage.append(cosineSim(question,j))
    indexOfCluster = storage.index(max(storage))
    return indexOfCluster

#This isn't really K-Means anymore. It is a clustering algorithm that creates K clusters, based on max similarity between questions.
def kCluster(jeoQuestions, k, jeoInstancesOriginal):
    centers =[]
    clusters = []
    random_selection = random.sample(jeoQuestions, k)
    
    for number in random_selection:    
        centers.append(number)

    #initially, the cluster contains the indices of the center questions in the original dataset    
    for i in centers:
        clusters.append([jeoInstancesOriginal[jeoQuestions.index(i)]])
        
    for i in xrange(len(jeoQuestions)):
        clusterIndex = findMax(jeoQuestions[i], centers)
        print 
        #to update the centers, I add any new unique words to the center from the compared question
        centers[clusterIndex] = list(set().union(centers[clusterIndex],jeoQuestions[i]))
        #get the original questions back        
        clusters[clusterIndex].append(jeoInstancesOriginal[i])
                                  
    print clusters

if __name__ == "__main__":
    main()


