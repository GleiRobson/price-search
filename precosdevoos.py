#script python que me permite acompanhar o andamento dos preços de um voo especifico no google voos
#na pagina de preços de voos google flights

from selenium import webdriver
import time

#abrir navegador
navegador =  webdriver.Edge()
#ir para a pagina do google flights
link = "https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI1LTA5LTE4ag0IAhIJL20vMDJiZmY5cg0IAxIJL20vMDl3d2xqGioSCjIwMjUtMTAtMDlqDQgDEgkvbS8wOXd3bGpyDQgCEgkvbS8wMmJmZjlAAUgBcAGCAQsI____________AZgBAQ&hl=pt-BR"

navegador.get(link)
time.sleep(5)
#pegar o preço da passagem aerea mais barata

preco = navegador.find_element("class name", "jLMuyc").text
#verificar se o preço esta menor que 4500 reais

print(preco)

#armazenar o preco obtido em um arquivo de texto
with open("preco.txt", "w") as arquivo:
    arquivo.write(preco)
