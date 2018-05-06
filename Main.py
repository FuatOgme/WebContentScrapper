from bs4 import BeautifulSoup
import urllib
import os
import Util


url = "https://www.imdb.com/chart/top"

html = ""
with urllib.request.urlopen(url) as response:
   html = response.read()

soup = BeautifulSoup(html,'html.parser')

baseUrl = 'https://www.imdb.com'
linkList = []
td_list =soup.findAll('td',class_ = 'titleColumn')
for td in td_list:
   elm_a = td.find('a')
   linkList.append(baseUrl + elm_a['href'])



i = 1
for link in linkList:
   path = "results" + os.sep + str(i) +"_.txt"
   text = Util.WriteDoc(link)
   with open(path, "w") as text_file:
      text_file.write(text)
   print(str(i) + 'yazılıyor..\r\n')
   i = i + 1

   # print(WriteDoc(link))
   # print('\r\n')



