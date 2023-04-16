import requests
import pandas
from bs4 import BeautifulSoup

def my_func(download_name: str, url: str = "https://www.scrapethissite.com/pages/"):
    # Define all constants
    # URL = "https://www.scrapethissite.com/pages/"
    

    # Hit the URL
    resp = requests.get(url)
    # print(resp.content)

    # Convert the content to BeautifulSoup object
    soup = BeautifulSoup(resp.content, features='html.parser')
    # print(soup)

    # Extract all the divs with class = page
    all_divs = soup.find_all("div", class_ = "page")
    # print(all_divs)
    href_list = []
    title_list = []
    description_list = []

    for div in all_divs:
        # Get the first a tag
        a_tag = div.find("a")
        # In the a tag, get href(link)
        href = a_tag.get("href")
        href_list.append("https://www.scrapethissite.com"+href)
        # print(href)
        # In the a tag, get text(title)
        title = a_tag.text
        title_list.append(title)
        # print(titles)
        # Get the first p tag
        description_tag = div.find("p")
        # In the p tag, get text(description)
        description = description_tag.text.strip()
        description_list.append(description)
        # print(description)

    # print(title_list)

    # dictionary
    data = {
        "title": title_list,
        "href": href_list,
        "description": description_list
    }

    df = pandas.DataFrame(data)

    # Download the data as csv
    # saving the dataframe 
    df.to_csv("Data/"+download_name+'.csv') 

my_func("scrapped_data", "https://www.scrapethissite.com/pages/simple/")