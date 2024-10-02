# Scraping the University of Toronto Groups Site

## Setup
All the commands should be completed with terminal window. If you do not know where the terminal window is just search for it on Windows, Linus or Mac. 

* clone the repo with :
````bash
git clone  https://github.com/mstoews/scrape-webpage.git 
````
* move into the directory

````bash
cd scrape-webpage
````

* install the requirements for python scraping which is basically beautifulsoup4 and requests

````bash
pip install -r ./requirements.txt
````

* if everything goes according to plan run the program. Data will be printed automatically in a csv format.

````bash
python scrap.py
````

## Code Review

### Main Function and funcion flow.
The main function starts with the starting page html page. The page is loaded and search is made for each group name. The email address is located on a separate link based upon the name of the group, get_clubs() function.  To do the scraping of the next associated page we use the function get_email(). Once have both the group name and the email address, they are added to the data array. Once we have looped through all the pages, which might take some time, we print the array using pandas dataframe. 

````
if __name__ == '__main__':
    
    # base url
    MAX_PAGE = 6
    baseUrl = 'https://sop.utoronto.ca/groups/?areas_of_interest=leadership&campus=st-george&pg='
    data = []

    # loop through each page until there are no more pages
    page = 1
    while page < MAX_PAGE:
        url = baseUrl + str(page)
        print_clubs(url)
        page = page + 1

    df = pd.DataFrame(data, columns=['Group Name', 'Primary Contact Email'])
    df.to_csv('uoftclubs24-25contact.csv', index=False)

    print("EOF")

````

### List Clubs and Emails
Create a list array of the club names and the matching email address. 

````
def list_clubs(url):
    page_contents = get_page_contents(url) 
    if page_contents:
       links = get_clubs(page_contents)        
    for link in links:
        href = link.get('href')                        
        if href and href.startswith('https://sop.utoronto.ca/group/'):
            text = link.text            
            email = getEmail(href)
            data.append([text, email])                
        
    else:
        print('Failed to get page contents.')

````