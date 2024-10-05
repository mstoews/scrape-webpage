import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import pandas as pd

def get_page_contents(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        return page.text
    return None

def get_clubs(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')    
    links = soup.find_all('a') # find all links
    return links

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
        
    else:
        print('Content page is not a valid group')


def get_email(url):
    page_contents = get_page_contents(url)
    if page_contents:
        soup = BeautifulSoup(page_contents, 'html.parser')
        email = soup.find('a', class_='block underline')
        if email:
            return email.text
    return None
    
if __name__ == '__main__':
    
    # base url
    MAX_PAGE = 6
    baseUrl = 'https://sop.utoronto.ca/groups/?areas_of_interest=leadership&campus=st-george&pg='
    data = []

    # loop through each page until there are no more pages
    page = 1
    while page < MAX_PAGE:
        url = baseUrl + str(page)
        list_clubs(url)
        page = page + 1

    df = pd.DataFrame(data, columns=['Group Name', 'Primary Contact Email'])
    df.to_csv('uoftclubs24-25contact.csv', index=False)

    print("EOF")


