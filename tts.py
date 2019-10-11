from bs4 import BeautifulSoup
import requests

class Voices:
    class EN_UK_Lola:
        id_name = 'en-GB-Standard-A'
        name = 'Lola'
        country = 'UK'
    
    class EN_UK_Donald:
        id_name = 'en-GB-Standard-B'
        name = 'Lola'
        country = 'UK'
    
    class EN_UK_Gabriela:
        id_name = 'en-GB-Standard-C'
        name = 'Gabriela'
        country = 'UK'
    
    class EN_UK_Daniel:
        id_name = 'en-GB-Standard-D'
        name = 'Daniel'
        country = 'UK'
    
    class EN_AU_Kia:
        id_name = 'en-AU-Standard-A'
        name = 'Kia'
        country = 'AU'
    
    class EN_AU_William:
        id_name = 'en-AU-Standard-B'
        name = 'William'
        country = 'AU'
    
    class EN_AU_Olivia:
        id_name = 'en-AU-Standard-C'
        name = 'Olivia'
        country = 'AU'
    
    class EN_AU_Noah:
        id_name = 'en-AU-Standard-D'
        name = 'Noah'
        country = 'AU'

class TTS:
    def __init__(self, voice : Voices, text : str):
        self.voice = voice
        self.text = text

        page = requests.post('https://notevibes.com/', data = {
            'content': text,
            'voice': voice.id_name,
            'speed': '1',
            'pitch': '0',
            'submit': '1',
            'recaptcha_response': '03AOLTBLR1v2NWmD88AJkb8FZimVzM2zhdHtfwQ_1rt4ENlPYIMGwvEBfGOCCgOy0wjpbNwZoPB12bkoqpnuEArcWh5mXeGuwz4E5cy_gaAs4CCyysyBezfBW92H66ucl5keNRal0IhMSzkeFoXyFSR5ZrYahXdmfLAUlgmZEbj535zTXlYBs80D2VZitJxkxXXzly8ekMG7GgpvsrQU0TC5UeywKDNpNF3PBM4bwxdcgPm46OGgpE7pOIT-NYAz6Ar9nGmOm9_xGERxnvfAeyb1zobr2d2vHcnmcCtYBHpldg0iplAmQnFBgacb8sMMJQHKlJ_Slkq2xgBxK1CuAifh31EU5rpEGteVALpAFKuCDEp7FAgGx56OMh87T5TLEVG_WPBs7qs0NFc2JmaxTAcYz8iy1WLlpNllWE-V8-3yvFjj5Juzz9tKHRiy993nfEGo2OQPvegWsXIy6OWuW4rWhvg360zQkGeYc39zpwijY8ekzjjvH8TlxIXbmG0ilLHVPlXiCNdOcvzj9ww3Jq7dBOCLBkZL36yg'
        }, headers = {
            'User-Agent': 'Reddit TTS Engine (NathanBitTheMoon)'
        })]

        soup = BeautifulSoup(page.content, features = "html.parser")
        self.url = soup.find_all('div', {'class': 'btn btn-primary btn-lg'})[0].find_all('a')[0]['href']

