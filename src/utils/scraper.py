import argparse
import requests
from bs4 import BeautifulSoup


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
            return title[:-len(' - Wikipedia')]
        else:
            return None
    else:
        print('Failed to retreive HTML content. Status code: ', response.status_code)


def main():
    """Main method to test the scraper"""

    parser = argparse.ArgumentParser(description='Find the shortest path between two Wikipedia articles.')

    parser.add_argument('url', type=str, help='URL of a Wikipedia article')

    args = parser.parse_args()
    print(get_neighbours(args.url))
    print(get_article_name(args.url))


if __name__ == "__main__":
    main()
