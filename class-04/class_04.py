from pprint import pprint
from selenium.webdriver import Firefox
from time import sleep


def get_links(browser, tag):
    element = browser.find_element_by_tag_name(tag)
    links = {}
    for a in browser.find_elements_by_tag_name('a'):
        links[a.text] = a.get_attribute('href')
    return links

url = 'https://selenium.dunossauro.live/aula_04.html'

browser = Firefox()

browser.get(url)

sleep(1)

pprint(get_links(browser, 'aside'))

links_exercises = get_links(browser, 'main')
pprint(links_exercises['Exercício 3'])

browser.quit()
