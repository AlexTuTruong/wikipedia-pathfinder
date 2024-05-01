from bs4 import BeautifulSoup
import requests

def get_neighbours(url):
    """Gets neighbouring internal wikipedia articles"""

    response = requests.get(url, timeout = 30)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        hyperlinks = soup.find_all('a')

        neighbor_urls = set()
        for link in hyperlinks:
            href = link.get('href')

            if href and href.startswith('/wiki'):
                neighbor_urls.add('https://en.wikipedia.org' + href)

        return neighbor_urls

        # for n in neighbor_urls:
        #     if n == ('https://en.wikipedia.org/wiki/Workers%27_Party_of_Korea'):
        #         print(n)

    else:
        print('Failed to retreive HTML content. Status code: ', response.status_code)

# get_neighbours('https://en.wikipedia.org/wiki/Kim_Jong_Un')