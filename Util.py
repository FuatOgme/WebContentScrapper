import urllib
from bs4 import BeautifulSoup

def WriteDoc(link):
   html = ""
   with urllib.request.urlopen(link) as response:
      html = response.read()
      soup = BeautifulSoup(html, 'html.parser')
      summary = soup.find('div',id='titleStoryLine').find('span',itemprop='description')

      text = summary.text.strip();
      return text

