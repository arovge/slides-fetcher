#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# get the url into the soup
#url = input('url: ')
url = 'http://jayurbain.com/msoe/cs4881/outline.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# find the table that we should parse
table = soup.find('table')
inner_table = table.find('table')
if inner_table is not None:
    table = inner_table

# some tables may not have a tbody
tbody = table.find('tbody')
if tbody is not None:
    table = tbody

# what to store each week of content in
weeks = []
rows = table.find_all('tr')
# remove the first index
del rows[0]

# loop through all rows and begin processing
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        links = cell.find_all('a')
        
        for link in links:
            if link.name == 'a':
                print(link.get_text())
        # print(cell)
    # if first_cell_text.isdigit():
    #     weeks.append({
    #         'week': int(first_cell_text),
    #         cells[1].get_text(): cells[2].get_text()
    #     })
    # else:
    #     weeks[-1][cells[0].get_text()] = cells[1].get_text()
    # print(f'{row}\n\n')
    
    # cells = row.find_all('td')
    # weeks.append({
    #     week: int(first_cell_text),

    # })
    # cells = row.find('td')
    # print(cells)
    # print(f'{cells[0].get_text()} and {cells[1].get_text()}')
# for week in weeks:
#     print(week)
    