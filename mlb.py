Teams = ('ARI',
'ATL',
'BAL',
'BOS',
'CHC',
'CWS',
'CIN',
'CLE',
'COL',
'DET',
'FLA',
'HOU',
'KAN',
'LAA',
'LAD',
'MIL',
'MIN',
'NYM',
'NYY',
'OAK',
'PHI',
'PIT',
'SD',
'SF',
'SEA',
'STL',
'TB',
'TEX',
'TOR',
'WAS')

Divisions = {
	"National League East": (1,10,17,20,29),
	"National League Central": (4,6,15,21,25),
	"National League West": (0,8,14,22,23),
	"American League East": (2,3,18,26,28),
	"American League Central": (5,7,9,12,16),
	"American League West": (11,13,19,24,27)
}

import random as rand
import json

jsone = json.JSONEncoder()
jsond = json.JSONDecoder()


f = open('mlbdata.txt', 'r')
txt = f.read()
if txt == '':
	Data = {}
else:
	Data = jsond.decode(txt)

setteam = 'CLE'

def getteamscore(team):
	return .5*(Data[Teams[team] ]['W']-Data[Teams[team] ]['L'])

def randomnum(n1,n2):
	return int(rand.random()*(n2-n1)+n1)

def quicksort(lst,method):
	less = []
	equal = []
	greater = []
	if len(lst) > 1:
		pivot = method(lst[0])
		for x in lst:
			if method(x) > pivot:
				less.append(x)
			if method(x) == pivot:
				equal.append(x)
			if method(x) < pivot:
				greater.append(x)
		return quicksort(less,method)+equal+quicksort(greater,method)
	else:
		return lst

def simgame(win):
	lst = []
	for i in range(30):
		lst.append(i)
	lst1 = []
	lst2 = []
	for i in range(15):
		lst1.append(lst[0])
		ind = randomnum(1,len(lst)-1)
		lst2.append(lst[ind])
		lst.pop(ind)
		lst.pop(0)
	for i in range(len(lst1)):
		if Teams[lst1[i] ] == setteam:

			Data[setteam][win and 'W' or 'L'] += 1
			if (win and Data[setteam]['Streak'] < 0) or (not win and Data[setteam]['Streak'] > 0):
				Data[setteam]['Streak'] = 0
			Data[setteam]['Streak'] += win and 1 or -1

			Data[Teams[lst2[i] ] ][win and 'L' or 'W'] += 1
			if (win and Data[Teams[lst2[i] ] ]['Streak'] > 0) or (not win and Data[Teams[lst2[i] ]]['Streak'] < 0):
				Data[Teams[lst2[i] ] ]['Streak'] = 0
			Data[Teams[lst2[i] ] ]['Streak'] += win and -1 or 1

		elif Teams[lst2[i] ] == setteam:

			Data[setteam][win and 'W' or 'L'] += 1
			if (win and Data[setteam]['Streak'] < 0) or (not win and Data[setteam]['Streak'] > 0):
				Data[setteam]['Streak'] = 0
			Data[setteam]['Streak'] += win and 1 or -1

			Data[Teams[lst1[i] ] ][win and 'L' or 'W'] += 1
			if (win and Data[Teams[lst1[i] ] ]['Streak'] > 0) or (not win and Data[Teams[lst1[i] ] ]['Streak'] < 0):
				Data[Teams[lst1[i] ] ]['Streak'] = 0
			Data[Teams[lst1[i] ] ]['Streak'] += win and -1 or 1

		elif rand.random() < .5:

			Data[Teams[lst1[i] ] ]['W'] += 1
			if Data[Teams[lst1[i] ] ]['Streak'] < 0:
				Data[Teams[lst1[i] ] ]['Streak'] = 0
			Data[Teams[lst1[i] ] ]['Streak'] += 1

			Data[Teams[lst2[i] ]]['L'] += 1
			if Data[Teams[lst2[i] ] ]['Streak'] > 0:
				Data[Teams[lst2[i] ] ]['Streak'] = 0
			Data[Teams[lst2[i] ] ]['Streak'] -= 1

		else:

			Data[Teams[lst2[i] ]]['W'] += 1
			if Data[Teams[lst2[i] ] ]['Streak'] < 0:
				Data[Teams[lst2[i] ] ]['Streak'] = 0
			Data[Teams[lst2[i] ] ]['Streak'] += 1

			Data[Teams[lst1[i] ]]['L'] += 1
			if Data[Teams[lst1[i] ] ]['Streak'] > 0:
				Data[Teams[lst1[i] ] ]['Streak'] = 0
			Data[Teams[lst1[i] ] ]['Streak'] -= 1

def Save():
	f = open('mlbdata.txt', 'w')
	f.truncate()
	f.write(jsone.encode(Data))
	f.close()
	

while True:
	inp = raw_input("[1:Show Standings,w:Win,l:Loss] ")
	if inp == '1':
		print("Placement  Team  Wins  Losses  Games Behind  Streak")
		for division,r in Divisions.items():
			print(division)
			lst = quicksort(list(r),getteamscore)
			topscore = getteamscore(lst[0])
			for i in range(len(lst)):
				team = lst[i]
				wins = str(Data[Teams[team] ]['W'])
				losses = str(Data[Teams[team] ]['L'])
				gb = str(topscore-getteamscore(lst[i]))
				streak = ''
				if Data[Teams[team] ]['Streak'] > 0:
					streak += 'W'
				elif Data[Teams[team] ]['Streak'] < 0:
					streak += 'L'
				streak += str(abs(Data[Teams[team] ]['Streak']))
				print((' ')*3+str(i+1)+(' ')*5+Teams[team]+(' ')*(6-len(Teams[team]))+wins+(' ')*(6-len(wins))+losses+(' ')*(6-len(losses))+gb+(' ')*(6-len(gb))+streak)




	elif inp == 'w':
		simgame(True)
		Save()
	elif inp == 'l':
		simgame(False)
		Save()
	elif inp[0:4] == 'set ':
		t = inp[4:]
		if t in Data:
			setteam = t
		else:
			print("Error: Team "+t+" Does Not Exist")
	elif inp == 'reset':
		newData = {}
		for i in range(len(Teams)):
			newData[Teams[i] ] = {"W":0,"L":0,"Streak":0}
		Data = newData
		print("Successfully reset season!")
	elif inp == 'quit' or inp == 'exit' or inp == 'save':
		break
	else:
		print("Error: Invalid Input")

Save()













