# Munch Scraping Scripts

## How To Use:

### Things to install:
Make sure you have Git installed, this is for 
[Instructions for installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

[Instructions for installing Python, Pip, Virtualenv](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/)
### Mac

### Navigating through files in the Terminal

`cd` goes into a folder
`ls` shows what files are in the folder that you are currently in

### Once in "munchscraping" Folder
1. In the directory of the folder, run `source env/bin/activate`. You should see a `(env)` to the left of your cmd line

2. Run `pip install -r requirements.txt`

3. `pip install geckodriver`

4. `python selscrape.py`

5. When the cmd line reads `DONE`, open spreadsheet.csv in a program to check


## Modifying the file

- Replace the link in quotes on Line 22

	`site = "https://sfbay.craigslist.org/search/sfc/mar?query=social+media"`

	to use a different craigslist results page

- Replace the file name in quotes on Line 87
	
	`with open('spreadsheet.csv','w') as outfile:`

	to write/create to a new file.