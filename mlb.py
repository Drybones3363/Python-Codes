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

import json
jsone = json.JSONEncoder()
jsond = json.JSONDecoder()

'''
for i,k in Divisions.items():
	print(i)
	for e in range(len(k)):
		print(Teams[k[e] ])
'''
f = open('mlbdata.txt', 'r')
Data = jsond.decode(f.read())

while True:
	inp = input("[1:Show Standings,2:...,3:...] ")
	if inp == '1':
		print("Team","Wins","Losses","Streak")
		for e,r in Divisions.items():
			print(e)
			lst = list(r)
			for i in range(len(lst)):
				



	elif inp == '2':



	elif inp == '3':


	elif inp == 'reset':
		newData = {}
		for i in range(len(Teams)):
			newData[Teams[i] ] = {"W":0,"L":0,"Streak":0}
		Data = newData
	elif inp == 'quit' or inp == 'exit':
		break
	else:
		print("Error: Invalid Input")

f = open('mlbdata.txt', 'w')
f.truncate()
f.write(jsone.encode(Data))
f.close()














