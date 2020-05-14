from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Firefox()

browser.get(url)

p = browser.find_elements_by_tag_name('p')[-1]
num = p.text.split(': ')[-1]
a = browser.find_element_by_tag_name('a')

print(f'Expect number: {num}')

while True:
    a.click()
    p = browser.find_elements_by_tag_name('p')[-1].text
    value = p.split(': ')[-1]
    if value == num:
        break

print(f'text p: {value} text expect number: {num}')
print(f'The values are equals {value == num}')

# browser.quit()
