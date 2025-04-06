from bs4 import BeautifulSoup


def create_soup(html_str: str):
    return BeautifulSoup(html_str, "html5lib")
