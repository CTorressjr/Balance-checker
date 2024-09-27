import pandas as pd
import os

pasta = r"C:\Users\PC\Desktop\EFD CONTRIBUICOES MEDICALMAIS"

dados = []
arq_n_processados = []
linhapis = '|M205|12|810908|'
linhacofins = '|M605|12|217208|'

def pis():

    arquivos = os.listdir(pasta)

    valortotalpis = 0

    for arquivo in arquivos:

        caminho_arquivo = os.path.join(pasta, arquivo)

        with open (caminho_arquivo, 'r', encoding='ISO-8859-1') as arqtxt:
            conteudo = arqtxt.readlines()
            for linhavalorpis in conteudo:

                if linhapis in linhavalorpis:
                    
                    linhavalorpis = linhavalorpis.split('|')
                    valorpis = linhavalorpis[4]
                    valorpis = float(valorpis.replace(',', '.'))                    
                    valortotalpis += valorpis
                    
    print(round(valortotalpis))                 
                

def cofins():

    arquivos = os.listdir(pasta)

    valortotalcofins = 0

    for arquivo in arquivos:

        caminho_arquivo = os.path.join(pasta, arquivo)

        with open (caminho_arquivo, 'r', encoding='ISO-8859-1') as arqtxt:
            conteudo = arqtxt.readlines()
            for linhavalorcofins in conteudo:

                if linhacofins in linhavalorcofins:
                    
                    linhavalorcofins = linhavalorcofins.split('|')
                    valorcofins = linhavalorcofins[4]
                    valorcofins = float(valorcofins.replace(',', '.'))                    
                    valortotalcofins += valorcofins
                    
    print(valortotalcofins)



pis() 
cofins()   