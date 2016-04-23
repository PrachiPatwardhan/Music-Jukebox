import requests
import bs4
import webbrowser
import csv

#accessing billboard website

res = requests.get("http://www.billboard.com/charts/hot-100")
html = res.content
soup = bs4.BeautifulSoup(html)
list1 = []
list2 = []
list4 = []
list5 = []
list6 = []

#searching for top ten songs

elems = soup.select('article h2')
str1 = "chart-row__song"
count = 1
count1 = 1

for item in elems:
	if str(item).find(str1) == 11 and count <= 10:
		list1.append(item)
		count = count + 1
	
for item in list1:
	str1 = str(item)
	str1 = str1[28:len(str1)-5]
	list5.append(str1)	

#searching for artists of top 10 songs

artist = soup.select('div a')
str2 = "chart-row__artist"

for item in artist:
	if str(item).find(str2) is not -1 and count1 <= 10:
		list2.append(item)
		count1 = count1 + 1

for item in list2:
	list3 = str(item).split()		
	l = len(list3)
	list4 = list3[5 : l - 1]
	str11 = " ".join(list4)
	list6.append(str11)

#writing it into a csv file

f = open("songlist.csv", 'wt')
qwriter = csv.writer(f)
row = zip(list5, list6)
for rows in row:
	qwriter.writerow(rows)
	

