# Aaron Chang (33197863)
# Tun Myat (51705354)

import sys
import pylab
import networkx as nx
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

if os.path.exists("result.csv"):
	os.remove("result.csv")

csv_name = sys.argv[1]


with open(csv_name) as csvfile:
	reader = csv.reader(csvfile)

	G = nx.Graph()
	
	for row in reader:
		# G.add_edge(row[0], row[1], weight=float(row[2]))
		G.add_edge(row[0], row[1], weight=float(row[2]), color=row[3])


print(nx.info(G))

nx.draw(G)

# show the graph in picture
# plt.show()

A = input("Please type the node A: ")
B = input("Please type the node B: ")
C = input("Please type the number of nodes C: ")
D = float(input("Please type the total weight of the edges D: "))

path_count = 0

for path in nx.all_simple_paths(G, source=A, target=B):
	
	i=0
	weight = float(0)

	while(i<len(path)-1):
		weight += float(G[path[i]][path[i+1]]['weight'])
		i+=1
	
	if abs(weight-float(D)) <= 0.01 and len(path) == int(C):
		if path_count == 0:
			print()
			print("All the possible paths that satisfy the conditions")
		path_count += 1
		print(path)
	
		path_name = ['path',path_count]
		
		with open("result.csv", 'a', newline='') as csvfile:
			
			csvwriter_title = csv.writer(csvfile,delimiter='_')
			csvwriter_title.writerow(path_name)
			
			csvwriter = csv.writer(csvfile)
			x=0
			while x < len(path)-1:
				csvwriter.writerows(zip(path[x], path[x+1]))
				x+=1
		
if(path_count == 0):
	print("There is no result.")
	print("NULL")
	
