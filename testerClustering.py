from __future__ import division
import json

def jaccardDistance(str1, str2):
    intersect = set(str1).intersection(str2)
    union = set(str1).union(str2)
    return len(intersect)/len(union)

def getData(fileName):
    with open(fileName) as dataFile:
        data = json.load(dataFile)
        return data

def DBSCAN(data, epsilon, minPoints):
    NOISECLUSTER = 0
    clusterNum = 0
    visited = []
    pointToCluster = {}
    for question in data:
        if question['pk'] in visited:
            continue
        visited.append(question['pk'])
        neighborPoints = getClosePoints(data, question, epsilon)
        if len(neighborPoints) < minPoints:
            pointToCluster[question["pk"]] = NOISECLUSTER
        else:
            clusterNum += 1
            print "Expanding cluster"
            expandCluster(question, neighborPoints, clusterNum, epsilon, minPoints, pointToCluster, visited, data)

def expandCluster(point, neighboringPoints, clusterNumber, epsilon, minPoints, pointToCluster, visited, data):
    pointToCluster[point["pk"]] = clusterNumber
    for newPoint in neighboringPoints:
        if point["pk"] not in visited:
            visited.append(point["pk"])
            newNeighborPoints = getClosePoints(data, newPoint, epsilon)
            if len(newNeighborPoints) > minPoints:
                neighboringPoints.update(newNeighborPoints)
            if newPoint["pk"] not in pointToCluster:
                pointToCluster[newPoint["pk"]] = clusterNumber

def getClosePoints(data, point, epsilon):
    neighbors = set()
    for question in data:
        if question != point:
            if jaccardDistance(question['fields']['answer'], point['fields']['answer']) > epsilon:
                neighbors.add(question["pk"])

    return neighbors

if __name__ == "__main__":
    data = getData("data.json")
    data = data[:10000]
    DBSCAN(data, 0.6, 5)