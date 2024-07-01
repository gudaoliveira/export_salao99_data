import io
import requests
import pandas as pd

from setup import *
from dependencies.selenium_utils import *
from dependencies.send_to_sheets import *

def main():

    # Acessa a página
    pagina_login = "https://www.salao99.com.br/conta/login?continuacao=https%3A%2F%2Fsalao99.com.br%2Fenterprise%2Fsistema%2Fpainel"
    driver.get(pagina_login)
    wait_until_find(xpath_email_input)

    input_text(xpath_email_input, login_email)
    input_text(xpath_password_input, login_password)
    click_button(xpath_login_button)

    wait_until_find(xpath_exit_ad_button)
    click_button(xpath_exit_ad_button)

    wait_until_find(xpath_remuneracoes_button)
    click_button(xpath_remuneracoes_button)

    wait_until_find(xpath_data_button)
    click_button(xpath_data_button)
    time.sleep(1)
    click_button(xpath_pesonalizar_data_button)

    wait_until_find(xpath_date_since_input)
    input_text(xpath_date_since_input, date_since)
    input_text(xpath_date_until_input, date_until)

    # Realizando o clique com javascript
    confirm_date_element = driver.find_element(By.XPATH, xpath_confirm_date)
    driver.execute_script("arguments[0].click();", confirm_date_element)
    wait_until_find(xpath_detalhamento_button)

    # Realizando o clique com javascript
    detalhamento_button_element = driver.find_element(By.XPATH, xpath_detalhamento_button)
    driver.execute_script("arguments[0].click();", detalhamento_button_element)

    wait_until_find(xpath_exibir_detalhes_button)
    click_button(xpath_exibir_detalhes_button)

    wait_until_find(xpath_exportar_button)
    click_button(xpath_exportar_button)

    wait_until_find(xpath_csv_button)
    click_button(xpath_csv_button)

    wait_until_find(xpath_download_button)
    element_download_button = driver.find_element(By.XPATH, xpath_download_button)
    download_url = element_download_button.get_attribute("href")
    
    driver.quit()
    
    csv_file = requests.get(download_url)
    csv_file.raise_for_status()
    csv_content = csv_file.text
    
    with open("./output/request_response.csv", "w", encoding="utf-8") as file:
        file.write(csv_content)
        
    df = pd.read_csv("./output/request_response.csv", sep=";")
    df = df.astype(str)
    df.to_excel('./output/data_values.xlsx', index=False)
        
    #Envia para o sheets 
    send_to_sheets(df)
    
    print("Atualização concluída com sucesso")
    
if __name__ == "__main__":
    main()