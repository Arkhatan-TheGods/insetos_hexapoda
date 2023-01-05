import requests
import pytest
import json
from bs4 import BeautifulSoup

hexapoda_link = 'https://pt.wikipedia.org/wiki/Hexapoda'


def header():
    page = requests.get('https://pt.wikipedia.org/wiki/Hexapoda')
    content = BeautifulSoup(page.content, 'html.parser')
    # show_content = content.prettify()
    # print(show_content)
    return content


header()


def find_all_element(element: str):
    finding = str(element)
    content = header()
    list(content.children)
    print(content.find_all(finding))


# @pytest.fixture
# def setup_header():
#     page = requests.get('https://pt.wikipedia.org/wiki/Hexapoda')
#     content = BeautifulSoup(page.content, 'html.parser')
#     return content


# def test_show_content():
#     content = setup_header()
#     print(content)
