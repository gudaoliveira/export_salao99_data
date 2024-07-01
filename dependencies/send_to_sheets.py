import os
import json
import pandas as pd

# Google API
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
    
def send_to_sheets(dataframe):

    SERVICE_ACCOUNT_FILE = 'C:\\_CREDENTIALS\\GSHEETS_API_CREDS_DUDA.json' # Credenciais
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # Lista com escopos necessários
    SPREADSHEET_ID = '1V1gBkvTv50ptqKcNwgEJYoDka3_rqJQCRJbgQOvqErs'
    SPREADSHEET_RANGE = 'faturamento!A2:H'

    # Criando as credenciais com as informações das credenciais e os escopos
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # Montando o serviço da API
    service = build('sheets', 'v4', credentials=creds)
    # Cria a conexão com o serviço do Google Spreashets
    sheet = service.spreadsheets()
    
    clear_body = {}
    body = {"values": dataframe.values.tolist()}

    # Limpa os dados
    sheet.values().clear(
    spreadsheetId = SPREADSHEET_ID,
    range = SPREADSHEET_RANGE,
    body = clear_body
    ).execute()
    
    # Cola os dados do CSV
    sheet.values().append(
    spreadsheetId=SPREADSHEET_ID,
    range=SPREADSHEET_RANGE,
    valueInputOption="RAW",
    body=body
    ).execute()