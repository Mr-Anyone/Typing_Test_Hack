from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

def information():
    url = 'https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find(class_ = 'table table-striped table-bordered')
    if table:
        tbody = table.find('tbody')
    else:
        print("Nothing to show")
    if tbody:
        tr = tbody.find_all('td')

    if tbody:
        province = []
        confirmed_cases = []
        probable_case = []
        add = 0
        for x in range(0, len(tr) -3, 3):
            province.append(tr[x].get_text())
            confirmed_cases.append(tr[x + 1 ].get_text())
            probable_case.append(tr[x + 2].get_text())
        return province, confirmed_cases, probable_case


def information_2():

    url = 'https://www.worldometers.info/coronavirus/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find(id = 'main_table_countries_today')
    body = table.find('tbody')
    information = body.find('tr')
    td = information.find_all('td')
    return td[0].get_text(), td[1].get_text()

a,b = information_2()
print(a,b)