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
setteamnum = 7

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

def simplayoff(win):
	if 'Playoffs' in Data:
		world_series = {}
		for ind in range(2):
			division = ind == 0 and 'American' or 'National'
			lst = Data['Playoffs'][division]
			if len(lst) > 6 and lst[6]['TeamNum'] != -1: #world series
				world_series[division] = lst[6]

			elif len(lst) > 6 and lst[6]['TeamNum'] == -1: #division champ series
				if lst[4]['TeamNum'] == setteamnum:
					lst[win and 4 or 5]['Wins'] += 1
				elif lst[5]['TeamNum'] == setteamnum:
					lst[win and 5 or 4]['Wins'] += 1
				else:
					w = rand.random() < .5
					lst[w and 4 or 5]['Wins'] += 1
				for num in range(4,6):
					if lst[num]['Wins'] >= 4:
						lst[6]['TeamNum'] = lst[num]['TeamNum']
						break

			if len(lst) > 4 and lst[4]['TeamNum'] == -1:
				if lst[0]['TeamNum'] == setteamnum:
					n = 1
					if win:
						n = 0
					lst[n]['Wins'] += 1
				elif lst[1]['TeamNum'] == setteamnum:
					n = 0
					if win:
						n = 1
					lst[n]['Wins'] += 1
				else:
					w = rand.random() < .5
					lst[w and 0 or 1]['Wins'] += 1
				for num in range(0,2):
					if lst[num]['Wins'] >= 3:
						lst[4]['TeamNum'] = lst[num]['TeamNum']
						if lst[4]['TeamNum'] != -1 and lst[5]['TeamNum'] != -1:
							lst.append({"TeamNum": -1,"Wins": 0})
						break

			if len(lst) > 5 and lst[5]['TeamNum'] == -1:
				if lst[2]['TeamNum'] == setteamnum:
					lst[win and 2 or 3]['Wins'] += 1
				elif lst[3]['TeamNum'] == setteamnum:
					lst[win and 3 or 2]['Wins'] += 1
				else:
					w = rand.random() < .5
					lst[w and 2 or 3]['Wins'] += 1
				for num in range(2,4):
					if lst[num]['Wins'] >= 3:
						lst[5]['TeamNum'] = lst[num]['TeamNum']
						if lst[4]['TeamNum'] != -1 and lst[5]['TeamNum'] != -1:
							lst.append({"TeamNum": -1,"Wins": 0})
						break
			
			#Data['Playoffs'][division] = lst


		if 'American' in world_series and 'National' in world_series:
			if Data['Playoffs']['American'][6]['Wins'] >= 4 or Data['Playoffs']['National'][6]['Wins'] >= 4:
				print("A team has already won the World Series!")
			elif Data['Playoffs']['American'][6]['TeamNum'] == setteamnum:
				Data['Playoffs'][win and 'American' or 'National'][6]['Wins'] += 1
			elif Data['Playoffs']['National'][6]['TeamNum'] == setteamnum:
				Data['Playoffs'][win and 'National' or 'American'][6]['Wins'] += 1
			else:
				w = rand.random() < .5
				Data['Playoffs'][w and 'National' or 'American'][6]['Wins'] += 1


	else:
		print("Error: No Playoff Data; Run command '2' to Set up Playoff Bracket")

def Setup_Playoffs():
	Data['Playoffs'] = {}
	americanwc,awcwins = -1,-81 #wildcard top wins
	nationalwc,nwcwins = -1,-81
	americanlist = []
	nationallist = []
	for division,r in Divisions.items():
		lst = quicksort(list(r),getteamscore)
		print(division+" Champion: "+Teams[lst[0] ])
		if division[:8] == "American":
			americanlist.append(lst[0])
			wins = getteamscore(lst[1])
			if wins > awcwins:
				americanwc = lst[1]
				awcwins = wins
		else:
			nationallist.append(lst[0])
			wins = getteamscore(lst[1])
			if wins > nwcwins:
				nationalwc = lst[1]
				nwcwins = wins
	americanlist.append(americanwc)
	nationallist.append(nationalwc)
	print("American League Wildcard: "+Teams[americanwc])
	print("National League Wildcard: "+Teams[nationalwc])
	americanlist = quicksort(americanlist,getteamscore)
	nationallist = quicksort(nationallist,getteamscore)
	Data['Playoffs']['American'] = []
	Data['Playoffs']['National'] = []
	Data['Playoffs']['American'].append({"TeamNum": americanlist[0],"Wins": 0})
	Data['Playoffs']['American'].append({"TeamNum": americanlist[3],"Wins": 0})
	Data['Playoffs']['American'].append({"TeamNum": americanlist[1],"Wins": 0})
	Data['Playoffs']['American'].append({"TeamNum": americanlist[2],"Wins": 0})
	Data['Playoffs']['American'].append({"TeamNum": -1,"Wins": 0})
	Data['Playoffs']['American'].append({"TeamNum": -1,"Wins": 0})
	Data['Playoffs']['National'].append({"TeamNum": nationallist[0],"Wins": 0})
	Data['Playoffs']['National'].append({"TeamNum": nationallist[3],"Wins": 0})
	Data['Playoffs']['National'].append({"TeamNum": nationallist[1],"Wins": 0})
	Data['Playoffs']['National'].append({"TeamNum": nationallist[2],"Wins": 0})
	Data['Playoffs']['National'].append({"TeamNum": -1,"Wins": 0})
	Data['Playoffs']['National'].append({"TeamNum": -1,"Wins": 0})



def Save():
	f = open('mlbdata.txt', 'w')
	f.truncate()
	f.write(jsone.encode(Data))
	f.close()

def Backup_Save():
	f = open('mlbbackupsave.txt','w')
	f.truncate()
	f.write(jsone.encode(Data))
	f.close()

def Open_Backup_Save():
	f = open('mlbbackupsave.txt','r')
	txt = f.read()
	if txt == '':
		Data = {}
	else:
		Data = jsond.decode(txt)

	

while True:
	inp = raw_input("[1:Show Standings,2:Show Playoffs,w:Win,l:Loss] ")
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

	elif inp == '2':
		if "Playoffs" in Data:
			order = [0,4,1,6,2,5,3]
			for division,r in Data['Playoffs'].items():
				tlen = len(Data['Playoffs'][division])
				for i in range(7):
					index = order[i]
					if index < tlen and Data['Playoffs'][division][index]['TeamNum'] != -1:
						n = 8*(i%2)
						if i == 3:
							n = 8*2
						print(" "*(n)+Teams[Data['Playoffs'][division][index]['TeamNum'] ]+' '+str(Data['Playoffs'][division][index]['Wins']))
					else:
						print("")
				print("")
		else:
			Setup_Playoffs()
			print("Successfully Setup Playoff Bracket!")


	elif inp == 'w':
		simgame(True)
		Save()
	elif inp == 'l':
		simgame(False)
		Save()
	elif inp == 'pw':
		simplayoff(True)
		Save()
	elif inp == 'pl':
		simplayoff(False)
		Save()
	elif inp[0:4] == 'set ':
		t = inp[4:]
		if t in Data:
			setteam = t
			for i in range(len(Teams)):
				if Teams[i] == setteam:
					setteamnum = i
					break
		else:
			print("Error: Team "+t+" Does Not Exist")
	elif inp == 'reset':
		newData = {}
		for i in range(len(Teams)):
			newData[Teams[i] ] = {"W":0,"L":0,"Streak":0}
		Data = newData
		print("Successfully reset season!")
	elif inp == 'reset playoffs':
		del Data['Playoffs']
	elif inp == 'quit' or inp == 'exit' or inp == 'save':
		break
	elif inp == 'backup save':
		Backup_Save()
	elif inp == 'load backup':
		Open_Backup_Save()
	else:
		print("Error: Invalid Input")

Save()













