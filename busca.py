#!/usr/bin/python
import googlesearch
import os
import sys
import json
import requests


print("""\n

         ██╗ ██████╗ ████████╗ █████╗     ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗
         ██║██╔═══██╗╚══██╔══╝██╔══██╗    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝
         ██║██║   ██║   ██║   ███████║    ██║  ██║██║   ██║██████╔╝█████╔╝ ███████╗
    ██   ██║██║   ██║   ██║   ██╔══██║    ██║  ██║██║   ██║██╔══██╗██╔═██╗ ╚════██║
    ╚█████╔╝╚██████╔╝   ██║   ██║  ██║    ██████╔╝╚██████╔╝██║  ██║██║  ██╗███████║
     ╚════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                               

              Aplicação criada para pesquisas, utilizando dorks do google
                                   Criado por @JOTA 

                 Exclusivo para a turma do curso de Hacker Investigador!

                                    Version : 1.0
                                 Codename: Jota Dorks
                                                                                     """)

                                                                                                 
try:
    from googlesearch import search
except ImportError:
    print("Resultado não encontrado")
    
print("")    
print('[Exemplos de Dorks!]')
print('\n         | filetype:Pdf | site: | intitle: | intext: | inurl: | define: | info: | link: | weather: |') 

print("")   
query = input('\nDigite aqui: ')
print("\n")
print(f"Pesquisando...")

   
for resultado in search(query, tld='co.in'):
    
   
    print("|------------------------------------------------------------------------------------------------------------------------")   
    print (resultado)

print("\n:::Concluído:::")

query = input('\nDigite aqui: ')
for resultado in search(query, tld='co.in'):

    print("|------------------------------------------------------------------------------------------------------------------------")   
    print (resultado)

print("\n:::Finalizado:::\n")

