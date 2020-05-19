from selenium.webdriver import Firefox
from time import sleep


url = 'https://selenium.dunossauro.live/aula_04_b.html'

browser = Firefox()

browser.get(url)

divs = browser.find_elements_by_tag_name('div')

for div in divs:
    sleep(1)
    div.click()

for _ in divs:
    sleep(1)
    browser.back()

for _ in divs:
    sleep(1)
    browser.foward()

# browser.quit()
