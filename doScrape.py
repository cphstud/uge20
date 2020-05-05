#!/Users/thor/opt/anaconda3/bin/python
from bs4 import BeautifulSoup
import sys

source=sys.argv[1]
datatype=sys.argv[2]
soup = BeautifulSoup(open(source), "html.parser")

table = soup.find('table')
#table = soup.find("table", {"class":"table-sm personligerekorder table table-striped- table-bordered table-hover table-checkable responsive no-wrap"})

table_body = table.find('tbody')
data = []
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

for item in data:
    print(item)
