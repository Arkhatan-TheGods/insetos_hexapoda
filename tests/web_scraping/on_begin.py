import requests
from bs4 import BeautifulSoup
# import json

"""foram importados os módulos, agora criar processos divididos de baixar a página, transformar em beautifulsoup, depois criar uma ferramenta de buscar todos os elementos html, depois outra função de busca."""


def main_link():
    link = 'https://pt.wikipedia.org/wiki/Hexapoda'
    return link


def wikipedia_link():
    link = 'https://pt.wikipedia.org'
    return link


def requesting():
    link = main_link()
    page = requests.get(link)
    return page


def show_content():
    page = requesting()
    content = page.content
    return content


def content_to_bs():
    content = show_content()
    bs = BeautifulSoup(content, 'html.parser')
    return bs


def find_all_tags(tag: str):  # faz uma busca por todas as tags
    bs = content_to_bs()
    target = tag
    find = bs.find_all(target)
    found = find
    return found


def tags_to_text(tag: str):  # extrai texto de tags buscada no parâmetro
    bs = content_to_bs()
    target = tag
    find = bs.find_all(target)
    for pos, each_tag in enumerate(find):
        print(pos, str(each_tag.get_text()))


"""próximo objetivo, achar a posição da tag conhecida como tbody para depois pegar as classes e subdivisões dos hexapoda, como exemplo: Collembola, Protura, Diplura... """


def show_links():  # mostra os links de todos as tags <a> com href
    bs = content_to_bs()
    find = bs.find_all('a', href=True)
    for pos, links in enumerate(find):
        print(pos, links.get('href'))
# show_links()


def scientific_classification():
    for pos, element in enumerate(find_all_tags('tbody')):
        if pos == 2:
            result = (str(element.get_text()).replace('\n', '').split())
    return result


def cladograma_list():
    for pos, element in enumerate(find_all_tags('tbody')):
        if pos == 3:
            results = (element.get_text().replace('\n', '').split())
    return results
# tags_to_text('tbody')


"""o que eu devo fazer? criar um filtro para separar a tag e classe: <div class="mw-parser-output">"""


def filter_target_div():
    bs = content_to_bs()
    principal = bs.find('div', attrs={'class': 'mw-parser-output'})
    print(principal)
    return principal
# filter_target_div()


"""criar um filtrador de links para que possam ser possíveis a extração contínua das outras páginas em seguidas sendo assim não quebra o processo contínuo de extrair dados úteis."""

with open('hexapoda.txt', 'w') as file:
    file.write(str(cladograma_list()))
