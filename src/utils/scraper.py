from bs4 import BeautifulSoup
import requests


def get_neighbours(url):
    """Gets neighbouring internal wikipedia articles"""

    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        hyperlinks = soup.find_all('a')

        neighbor_urls = set()
        for link in hyperlinks:
            href = link.get('href')

            if href and href.startswith('/wiki'):
                neighbor_urls.add('https://en.wikipedia.org' + href)

        return neighbor_urls

    else:
        print('Failed to retreive HTML content. Status code: ', response.status_code)


def get_article_name(url):
    """Get the article name of a given url"""
    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('title')

        if title_tag:
            title = title_tag.get_text()
            return title.rstrip(' - Wikipedia')
        else:
            return None
    else:
        print('Failed to retreive HTML content. Status code: ', response.status_code)


def main():
    """Main method to test the scraper"""

    test_url = 'https://en.wikipedia.org/wiki/Kim_Jong_Un'
    print(get_neighbours(test_url))
    print(get_article_name(test_url))


if __name__ == "__main__":
    main()
