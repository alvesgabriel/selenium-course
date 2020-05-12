from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Firefox()

browser.get(url)

sleep(1)

a = browser.find_element_by_tag_name('a')
p = browser.find_element_by_tag_name('p')

for click in range(1, 11):
    a.click()
    p = browser.find_elements_by_tag_name('p')[-1]
    print(f'text p: {p.text} text click: {click}')
    print(f'The values are equals {p.text == str(click)}')

browser.quit()
