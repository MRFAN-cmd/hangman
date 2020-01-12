import csv

movies=[["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("P132_3.csv","w",newline="") as f:
    w=csv.writer(f,delimiter=",")
    for z in movies:
        w.writerow(z)
