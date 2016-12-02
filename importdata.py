import csv
from datetime import datetime
import sqlite3
import sys
import os

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
		return '{\"model\": \"viewer.question\", \"pk\": ' + str(number) + ", \"fields\": {\"text\": \"" + self.text + "\", \"value\": \"" + self.value + "\", \"answer\": \"" + self.answer + "\", \"theRound\": \"" + self.theRound + "\", \"showNumber\": \"" + self.showNumber + "\", \"airDate\": \"" + self.airDate.strftime("%Y-%m-%d") + "\", \"category\": \"" + self.category + "\"}}"

if len(sys.argv) < 2:
	print "Usage: python importdata.py path/to/csv/file"
	quit() 

conn = sqlite3.connect('db.sqlite3')
conn.text_factory = str
c = conn.cursor()

data = []

f = open('data.json', 'w')
f.write('[')

with open(sys.argv[1], 'rb') as csvfile:
	reader = csv.reader(csvfile)
	#reader.next()
	i = 0
	for row in reader:
		#if 'Mystery Train' in row[6]:
			#print row[6]
			#print row[6].replace('\"', "")
		#q = Question(text=row[5].replace('"', '\\"'), value=row[4].replace('\"', '"').replace('"', '\\"'), answer=row[6].replace('\\"', "").replace('\"', ""), theRound=row[2].replace('\"', '"').replace('"', '\\"'), showNumber=row[0].replace('\"', '"').replace('"', '\\"'), airDate=datetime.strptime(row[1], '%Y-%m-%d'), category=row[3].replace('\"', '"').replace('"', '\\"'))
		q = Question(text=row[6].replace('"', '\\"').replace("\\'", "").replace("\'", ""), value=row[4].replace('\"', '"').replace('"', '\\"'), answer=row[7].replace('\\"', "").replace('\"', "").replace("\\'", "").replace("\'", ""), theRound=row[1].replace('\"', '"').replace('"', '\\"'), showNumber=row[0].replace('\"', '"').replace('"', '\\"'), airDate=datetime.strptime(row[1], '%Y-%m-%d'), category=row[3].replace('\"', '"').replace('"', '\\"'))

		f.write(q.toJSON(i))
		f.write(',')
		i += 1

f.seek(-1, os.SEEK_END)
f.truncate()

f.write(']')

#for i in data:
	#f.write()

#c.executemany('INSERT INTO viewer_question (text, value, answer, theRound, showNumber, airDate, category) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
print "Completed import of data"
