# Munch Scraping Scripts

## How To Use:

### Things to install:
Make sure you have Git installed, this is for interacting with Github.com.

[Instructions for installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Python is the language that was used for the scripts.
[Instructions for installing Python, Pip, Virtualenv](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/)

## Mac

### Navigating through files in the Terminal

Open your terminal once the above programs are completed and use Git commands to navigate to the folder you'd like the scripts to be in

[Git Commands](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html)

`cd nameoffolder` goes into a folder

`ls` shows what files are in the folder that you are currently in

### Download the project

Once you're in the folder, go to the top right of this webpage and click on the green "Clone or download" button. Make sure you "Use HTTP" if you have not set up your ssh key yet. Copy and Paste the link you'd like to use into the terminal along with `git clone`

`git clone https://github.com/jtung23/munchscraping.git`

`cd munchscraping` to go into downloaded folder

### Once in "munchscraping" Folder

#### If you want to work in a virtual environment (optional)
1. In the directory of the folder, from terminal `source env/bin/activate`. You should see a `(env)` to the left of your cmd line

#### If you don't want to use virtual env
2. Run `pip install -r requirements.txt`

3. `pip install geckodriver`

4. `python selscrape.py`

5. When the cmd line reads `DONE`, open spreadsheet.csv which can be found in the munchscraping folder to check.


## Modifying the file

- Replace the link in quotes on Line 22

	`site = "https://sfbay.craigslist.org/search/sfc/mar?query=social+media"`

	to use a different craigslist results page

- Replace the file name in quotes on Line 87
	
	`with open('spreadsheet.csv','w') as outfile:`

	to write/create to a new file.