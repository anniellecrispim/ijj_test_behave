from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = Firefox()

link = 'https://www.google.com/'
browser.get(link)


def send_keys_google():
    btn_search = browser.find_element(By.NAME, 'q')
    btn_search.send_keys('Instituto Joga Junto')
    btn_search.send_keys(Keys.ENTER)


def rearch_google_ijj(): #não tá legAl pois com reutilizavél 
    wait_menu_google = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'YmvwI')))    
    result_rearch = browser.find_elements(By.TAG_NAME, 'h3')
    for result in result_rearch:
        if result.text == 'Instituto Joga Junto':
            result.click()
            break

def send_messenger():
    input_name = browser.find_element(By.NAME, 'nome').send_keys('Nadinha')
    input_email = browser.find_element(By.NAME, 'email').send_keys('abcteste@gmail.com')
    subject = browser.find_element(By.NAME, 'assunto')
    input_body = browser.find_element(By.NAME, 'body').send_keys('Isso é um teste')
    select_subjects = Select(subject)
    select_subjects.select_by_visible_text('Ser facilitador')

send_keys_google()
rearch_google_ijj()
send_messenger()
browser.close()





