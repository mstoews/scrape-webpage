import requests
from bs4 import BeautifulSoup


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
    # print(soup.prettify())
    links = soup.find_all('a') # find all links
    #clubs = soup.find_all('a', class_='text-primary') # find all names for the links
    return links

def print_clubs(url):
    page_contents = get_page_contents(url) 

    if page_contents:
        links = get_clubs(page_contents)
        for link in links:
            href = link.get('href')                        
            if href and href.startswith('https://sop.utoronto.ca/group/'):
                text = link.text            
                email = getEmail(href)
                print(text,',', email)
        
        #for i in range(len(links)):
        #    print(links[i].text)     
        
        #for i in range(len(clubs)):
        #    print(clubs[i].text)            
    else:
        print('Failed to get page contents.')


def getEmail(url):
    page_contents = get_page_contents(url)
    if page_contents:
        soup = BeautifulSoup(page_contents, 'html.parser')
        email = soup.find('a', class_='block underline')
        if email:
            return email.text
    return None
    
if __name__ == '__main__':
    # 1. expand the main page to where all of the clubs are listed

    baseUrl = 'https://sop.utoronto.ca/groups/?areas_of_interest=leadership&campus=st-george&pg='

    url = baseUrl + '1'
    print_clubs(url)
    url = baseUrl + '2'
    print_clubs(url)
    url = baseUrl + '3'
    print_clubs(url)
    url = baseUrl + '4'
    print_clubs(url)
    print("Scraping completed and saved to uoftclubs24-25contact.csv")


