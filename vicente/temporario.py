import tk
import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/las/USD-BRL, EUA-BRL, BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_ dolar requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EUBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
