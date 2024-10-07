# Scraping the University of Toronto Groups Site
## Setup
All the commands should be completed with terminal window. If you do not know where the terminal window is just search for it on Windows, Linus or Mac. 

### Git and Github (gh)
The first step requires git. If you do not have git installed on your mac or linux machine, you can install it with homebrew. If you do not have homebrew, you need to install it with the following command.

If you have git skip to the clone step


````bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo >> /home/mst/.bashrc
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/mst/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
````

then install git and gh. (gh is the command line for gh and very useful.)

````bash
brew install git; brew install gh
````

### Installing the requirements

In order to run the python script you must have python. Seems obvious but there are actually two versions of python. Version 2 and 3. Depending upon which is installed on your mac or linux machine you need to adjust the command line to run successfully. 

````bash
python -V
````
If the command fails, the try 

````bash
python3 -V
````
if the works set you must adjust the pip and python commands to pip3 and python3 

### Installation
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

* if everything goes according to plan run the program. Data will be printed automatically in a csv format. You must pass a parameter to the scrap.py file to tell which group to use.

````bash
python scrap.py work-career-development
````



## Code Review
### Main Function and function flow.
The main function starts with the starting page html page. The page is loaded and search is made for each group name. The email address is located on a separate link based upon the name of the group, get_clubs() function.  To do the scraping of the next associated page we use the function get_email(). Once have both the group name and the email address, they are added to the data array. Once we have looped through all the pages, which might take some time, we print the array using pandas dataframe. 

```py
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
```

### List Clubs and Emails
Create a list array of the club names and the matching email address. 

```py
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

```


## Virtual Environments
### Running code in the environment
```bash
 virtualenv -p /usr/local/bin/python3 venv
 source venv/bin/activate 
 pip3 install -r ./requirements.txt
 python3 scrap.py
 deactivate
 ```

