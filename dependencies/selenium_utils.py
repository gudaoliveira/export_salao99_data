import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Configurando o webdriver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1280, 720)


def click_button(xpath, tempo_espera=1):
    """
    Clica em um determinado botão a partir do caminho (xpath) do elemento da página

    Parâmetros:
    xpath: Caminho para o objeto na página
    tempo_espera: Tempo de espera em segundos (1 segundo por padrão)

    IMPORTANTE: Defina o seu webdriver como "driver" ou edite a variável dentro dessa função
    """
    element = driver.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(tempo_espera)
    return


def input_text(xpath, text, tempo_espera=0.5):
    """
    Insere um texto em uma caixa de texto através do caminho (xpath) do elemento da página

    Parâmetros:
    xpath: Caminho para o objeto na página
    text: Texto a ser inserido
    tempo_espera: Tempo de espera em segundos (.5 segundo por padrão)

    IMPORTANTE: Defina o seu webdriver como "driver" ou edite a variável dentro dessa função
    """
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)
    time.sleep(tempo_espera)
    return


def wait_until_find(expected_xpath, tempo_espera=1):
    """
    Aguarda a interação do usuário na tela e volta a rodar o código quando algum elemento após a tela de interação aparece

    Ótimo para quando temos telas de login com CAPTCHA ou autenticação de dois fatores

    Parâmentros
    expected_xpath: O caminho (xpath) de algum elemento na tela que aparecerá depois da interação do usuário
    tempo_espera: Tempo de espera em segundos (3 segundos por padrão)

    IMPORTANTE: Defina o seu webdriver como "driver" ou edite a variável dentro dessa função
    """
    while True:
        try:
            # Tente encontrar um elemento que só está disponível após o login
            driver.find_element(By.XPATH, expected_xpath)
            print(f"{expected_xpath} encontrado")
            break  # Sai do loop se o elemento for encontrado
        except NoSuchElementException:
            print(f"Esperando o elemento {expected_xpath}")
            time.sleep(
                tempo_espera
            )  # Espera por 3 segundos antes de verificar novamente
    return
