import requests # type: ignore
import os, sys
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore

if len(sys.argv) < 2:
    print ('Usage: python scrap.py <group_name>')
    sys.exit()
else :
    group_name = sys.argv[1]


def get_page_contents(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        return page.text
    return None


def list_clubs(url):
    page_contents = get_page_contents(url) 
    if page_contents:
       links = get_clubs(page_contents)        
    for link in links:
        href = link.get('href')                        
        if href and href.startswith('https://sop.utoronto.ca/group/'):
            text = link.text            
            email = get_email(href)
            data.append([text, email])
            print(text)
        else:
            print('Content page is not a valid group : ', href)

def get_clubs(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')
    links = soup.find_all('a') # find all links
    return links

def get_email(url):
    page_contents = get_page_contents(url)
    if page_contents:
        soup = BeautifulSoup(page_contents, 'html.parser')
        email = soup.find('a', class_='block underline')
        if email:
            return email.text
    return None
    
if __name__ == '__main__':
    print("Starting the scraping...")
    # base url
    MAX_PAGE = 4
    baseUrl = 'https://sop.utoronto.ca/groups/?areas_of_interest=' + group_name + '&campus=st-george'
    data = []

    # loop through each page until there are no more pages
    page = 1
    while page < MAX_PAGE:
        url = baseUrl + '&pg=' + str(page)
        list_clubs(url)
        page = page + 1

    df = pd.DataFrame(data, columns=['Group Name', 'Primary Contact Email'])
    df.to_csv('uoftclubs24-'+ group_name +'-25contact.csv', doublequote=True)

    print("Completed")


