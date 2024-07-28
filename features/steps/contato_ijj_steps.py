from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que estou na página do instituto joga junto')
def step_enter_on_page_ijj(context):

    title = context.browser.title
    assert 'Instituto Joga Junto' in title, 'Título não encontrado'


@when(u'preencho o formulário de contato')
def step_preencher_formulário(context):
    input_name = context.browser.find_element(By.NAME, 'nome').send_keys('Nadinha')
    input_email = context.browser.find_element(By.NAME, 'email').send_keys('abcteste@gmail.com')
    subject = context.browser.find_element(By.NAME, 'assunto')
    input_body = context.browser.find_element(By.NAME, 'body').send_keys('Isso é um teste')
    
    select_subjects = Select(subject)
    select_subjects.select_by_visible_text('Ser facilitador')

#falta um assert verificando se o que foi enviado foi "quero ser um facilitador"

@when(u'aperto o botão de enviar')
def step_submit(context):
    button_submit = context.browser.find_element(By.XPATH, '//*[@id="Contato"]/div[1]/form/button').submit()


@then(u'os dados são recebidos com sucesso')
def step_dados_recebidos(context):
    #import ipdb;ipdb.sset_trace()
    wait = WebDriverWait(context.browser, 10)

    alert = wait.until(EC.alert_is_present())
    #print(alert)
    alert_text = alert.text
    verify_text = "Dados recebidos!"
    assert 'Dados recebidos!' in alert.text

    alert.accept()