    
import pandas as pd

# Google API
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
    
def send_to_sheets(dataframe):
    df = pd.read_csv("./output/request_response.csv", sep=";")
    df.to_excel('./output/data_values.xlsx', index=False)
    
    SERVICE_ACCOUNT_FILE = './res/credentials.json' # Credenciais
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # Lista com escopos necessários

    # Criando as credenciais com as informações das credenciais e os escopos
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Montando o serviço da API
    service = build('sheets', 'v4', credentials=creds)

    # Definindo as informações da planilha
    SPREADSHEET_ID = '1V1gBkvTv50ptqKcNwgEJYoDka3_rqJQCRJbgQOvqErs'
    SPREADSHEET_RANGE = 'faturamento!A1:H'

    # Cria a conexão com o serviço do Google Spreashets
    sheet = service.spreadsheets()

    body = {"values": df.values.tolist()}

    sheet.values().append(
    spreadsheetId = SPREADSHEET_ID,
    range = SPREADSHEET_RANGE,
    valueInputOption = "RAW",
    body = body
    ).execute()