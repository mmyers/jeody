import csv
import json
import os
import sys
from datetime import datetime


def getData(fileName):
    with open(fileName) as dataFile:
        data = json.load(dataFile)
        return data

class Question:
	def __init__(self, text, value, answer, theRound, showNumber, airDate, category):
		self.text = text
		self.value = value
		self.answer = answer
		self.theRound = theRound
		self.showNumber = showNumber
		self.airDate = airDate
		self.category = category

	def toJSON(self, number):
		return '{\"model\": \"viewer.question\", \"pk\": ' + str(number) + ", \"fields\": {\"text\": \"" + self.text + "\", \"value\": \"" + self.value + "\", \"answer\": \"" + self.answer + "\", \"theRound\": \"" + self.theRound + "\", \"showNumber\": \"" + self.showNumber + "\", \"airDate\": \"" + self.airDate.strftime("%Y-%m-%d") + "\", \"category\": " + str(self.category) + "}}"

class Category:
	def __init__(self, category):
		self.category = category

	def toJSON(self, number):
		return '{\"model\": \"viewer.category\", \"pk\": ' + str(number) + ", \"fields\": {\"category\": \"" + self.category + "\"}}"

def categoryPKByStr(data, strRep):
	for datum in data:
		if strRep == datum["fields"]["category"]:
			return datum["pk"]
	return 0

if len(sys.argv) < 3:
	print "Usage: python importdata.py path/to/csv/file questions/category"
	quit() 

if sys.argv[2] == "questions" and len(sys.argv) < 4:
	print "Usage: python importdata.py path/to/csv/file questions path/to/category.json"

if sys.argv[2] == "questions":
	data = getData('data.json')
	f = open('final.json', 'w')
	f.write('[')
	with open(sys.argv[1], 'rb') as csvfile:
		reader = csv.reader(csvfile)
		i = 0
		for row in reader:
			if 'Mystery Train' in row[6]:
				print row[6]
				print row[6].replace('\"', "")
			q = Question(text=row[5].replace('"', '\\"'), value=row[4].replace('\"', '"').replace('"', '\\"'), answer=row[6].replace('\\"', "").replace('\"', ""), theRound=row[2].replace('\"', '"').replace('"', '\\"'), showNumber=row[0].replace('\"', '"').replace('"', '\\"'), airDate=datetime.strptime(row[1], '%Y-%m-%d'), category=categoryPKByStr(data, row[3].replace('\"', '"').replace('"', '\\"')))
			f.write(q.toJSON(i))
			f.write(',')
			i += 1
elif sys.argv[2] == "category":
	f = open('data.json', 'w')
	f.write('[')
	with open(sys.argv[1], 'rb') as csvfile:
		reader = csv.reader(csvfile)
		i = 1
		for row in reader:
			c = Category(category=row[3].replace('\"', '"').replace('"', '\\"'))
			f.write(c.toJSON(i))
			f.write(',')
			i += 1

f.seek(-1, os.SEEK_END)
f.truncate()

f.write(']')

#for i in data:
	#f.write()

#c.executemany('INSERT INTO viewer_question (text, value, answer, theRound, showNumber, airDate, category) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
print "Completed import of data"
