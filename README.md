# Scraping the University of Toronto Groups Site

## Setup
All the commands should be completed with terminal window. If you do not know where the terminal window is just search for it on Windows, Linus or Mac. 

* Clone the repo with :
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

* if everything goes according to plan run the program. The data output is piped into a comma separated value file with the command. 

````bash
python scrap.py > result.csv
````

