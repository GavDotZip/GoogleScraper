# This project takes a query and scrapes google for infromation on the query.
# For example; when you input: Irish Times
# The output will be: The Irish Times is an Irish daily broadsheet newspaper and online digital publication. -->
# It launched on 29 March 1859. The editor is Ruadhán Mac Cormaic. -->
# It is published every day except Sundays. The Irish Times is considered a newspaper of record for Ireland.

from bs4 import BeautifulSoup
import requests

# As per https://pypi.org/project/beautifulsoup4/ --> Beautiful Soup is a library that makes it easy to scrape information from web pages. -->
# It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


# take in a query and add "word1" + "word2" to the end of it accordingly
def google(query):
    query = query.replace(" ", "+")
    try:
        url = f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8'  # standard
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
    except:
        print("Ensure there is an internet connection") # if no connection available, no results found
    try:
        try:
            ans = soup.select('.RqBzHd')[0].getText().strip() # main classes in which Google results are stored

        except:
            try:
                title = soup.select('.AZCkJd')[0].getText().strip()
                try:
                    ans = soup.select('.e24Kjd')[0].getText().strip()
                except:
                    ans = ""
                ans = f'{title}\n{ans}'

            except:
                try:
                    ans = soup.select('.hgKElc')[0].getText().strip()
                except:
                    ans = soup.select('.kno-rdesc span')[0].getText().strip()
                    
    except: # if a result cannot be found, console will prompt user
        ans = "No result found. Refine search"
    return ans

# print result from scraper
result = google(str(input("Query\n")))
print(result)
