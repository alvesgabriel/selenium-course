from selenium.webdriver import Firefox


url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Firefox()

browser.get(url)

elements = {
    'h1': {}
}

ps = browser.find_elements_by_tag_name('p')
for p in ps:
    elements['h1'][p.get_attribute('atributo')] = p.text

print(elements)

browser.quit()
