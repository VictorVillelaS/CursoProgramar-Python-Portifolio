from MODELS.preferenciasDeFamiliaresVO import PreferenciasDeFamiliaresVO
from openpyxl import Workbook
from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from io import BytesIO


class ExporterBLL:
    def __init__(self):
        pass

    @staticmethod
    def criarTabelaExcel(valores: list[PreferenciasDeFamiliaresVO]):
        # workbook, ou arquivo excel
        wb = Workbook()

        # worksheet, ou tabela de um arquivo excel
        ws = wb.active
        ws.title = "Preferencias de Familiares"

        # cria título das colunas
        lista_headers = ["Familiar", "Preferencia", "Intensidade", "Observacao"]
        ws.append(lista_headers)

        # adiciona valores
        for i in range(len(valores)):
            valor = valores[i]
            atributos = [valor.objFamiliar.nome, valor.objPreferencia.descricao, valor.intensidade, valor.observacao]
            ws.append(atributos)

        return wb

    @staticmethod
    def exportarTabelaExcel(valores: list[PreferenciasDeFamiliaresVO], path: str):
        tabela = ExporterBLL.criarTabelaExcel(valores)
        tabela.save(path)

    @staticmethod
    def exportarTabelaEmail(valores: list[PreferenciasDeFamiliaresVO], file_paths: tuple[str]):
        # Lê as informações do arquivo 'login_info' para o envio do email
        with open('login_info.txt', 'r') as arquivo:
            remetente, senha, destinatario = arquivo.readlines()

        # Monta a mensagem para ser enviada
        mensagem = MIMEMultipart()
        mensagem['From'] = remetente
        mensagem['To'] = destinatario
        mensagem['Subject'] = "Tabela 'preferências de familiares'"

        mensagem.attach(MIMEText('Segue planilha com preferências do familiar.', 'plain'))

        # Adiciona as planilhas como anexos da mensagem
        for file_path in file_paths:
            nome_arquivo = file_path.split('/')[-1]
            with open(file_path, 'rb') as arquivo:
                anexo = MIMEApplication(arquivo.read(), _subtype="xlsx")
                anexo.add_header('Content-Disposition', f'attachment; filename={nome_arquivo}')
                mensagem.attach(anexo)

        # Loga a conta do remetente para envio do email
        # Sinceramente, esse código está ruim, mas serve para esse propósito
        # Para um guia melhor e mais complexo, ver https://realpython.com/python-send-email/
        servidor_smtp = 'smtp.gmail.com'
        porta_smtp = 587
        server = smtplib.SMTP(servidor_smtp, porta_smtp)
        server.starttls()

        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, mensagem.as_string())

        server.quit()
        print("Email enviado!")
