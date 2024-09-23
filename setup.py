import os
from datetime import datetime

login_email = os.getenv('LOGIN_EMAIL_SALAO99')
login_password = os.getenv('LOGIN_SENHA_SALAO99')
date_since = "01/01/2022"
date_until = datetime.now().strftime("%d/%m/%Y")

xpath_email_input = "//*[@id='xemail']"
xpath_password_input = "//*[@id='xsenha']"
xpath_login_button = "//*[@id='formLogin']/div[3]/div[2]/button"
xpath_exit_ad_button = '//*[@id="radix-0"]/div[1]/button'
xpath_remuneracoes_button = '//*[@id="root"]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/ul[2]/div[4]'
xpath_data_button = "/html/body/div[1]/div/div/main/div[2]/div/div[1]/div/div/div[2]/div/div[3]/div"
xpath_pesonalizar_data_button = "/html/body/div[4]/div[3]/li[4]"
xpath_date_since_input = "/html/body/div[1]/div[2]/div/div[3]/div/div[2]/form/div/div[1]/div/div/input"
xpath_date_until_input = "/html/body/div[1]/div[2]/div/div[3]/div/div[2]/form/div/div[2]/div/div/input"
xpath_confirm_date = "/html/body/div[1]/div[2]/div/div[3]/div/div[3]/button[2]"
xpath_detalhamento_button = "/html/body/div/div/div/main/div[2]/div/div[2]/div/div/div[3]/div[1]/div/div/div"
xpath_exibir_detalhes_button = "/html/body/div[4]/div[3]/ul/li[1]"
xpath_exportar_button = "/html/body/div/div[2]/div/div[3]/div/div/header/div/div/div/div[1]/button"
xpath_csv_button = "/html/body/div[4]/div[3]/ul/li[3]"
xpath_download_button = '//*[@id="root"]/div[2]/div[2]/div[3]/div/div/div[2]/div/a'
