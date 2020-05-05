#!/Users/thor/opt/anaconda3/bin/python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("res.html"), "html.parser")

table = soup.find('table')
table_body = table.find('tbody')
data = []
#
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

for item in data:
    print(item)
