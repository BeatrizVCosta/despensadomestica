import pickle
import datetime
# Adaptado de @flaviusgorgonio
import os
data=datetime.date.today()
# O TEMA DO MEU PROJETO É DESPENSA DOMÉSTICA
#dicionarios de cada tipo de produto
produtos={}
higiene={}
comidaas={}
#Adaptado de @marlisonss
#cor pra tela "sobre"
rosa = '\033[35m'
fim= '\033[0m'
#Recuperar os dados salvos no arquivo
try:
    arqProdutos = open("produtos.dat", "rb")
    banco = pickle.load(arqProdutos)
    produtos = banco[1]
    higiene = banco[2]
    comidaas = banco[3]
    arqProdutos.close()
except:
    arqProdutos = open("produtos.dat", "wb")
    arqProdutos.close()
    

#função para salvar os dados no arquivo em binário
def salvar():
  banco={
    1:produtos,
    2:higiene,
    3:comidaas
  }
  arqProdutos = open("produtos.dat", "wb")
  pickle.dump(banco,arqProdutos )
  arqProdutos.close()

def verifica_data():
  validade=""
  while validade=="":
    print("Digite a data de validade")
    dia=int(input("Dia:"))
    mes=int(input("Mês:"))
    ano=int(input("Ano:"))
    if dia>31 or dia<1 or mes>12 or mes<1:
      print("Data inválida!")
    elif ano==data.year:
      if mes==data.month and dia<data.day:
        validade=False
        return validade
      elif mes==data.month and dia==data.day:
        validade=False
        return validade
      elif mes<data.month:
        validade=False
        return validade
      else:
        validade="/".join([str(dia),str(mes),str(ano)])
        return validade
    elif ano<data.year:
      validade=False
      return validade
    elif ano>data.year:
      validade="/".join([str(dia),str(mes),str(ano)])
      return validade


def menu():
  os.system('clear')
  print("-----------------------------------------------------------------")
  print("|                    MENU PRINCIPAL                             |")
  print("-----------------------------------------------------------------")
  print("|                  0- SAIR                                      |")
  print("|                  1- COMIDAS                                   |")
  print("|                  2- HIGIENE PESSOAL                           |")
  print("|                  3- PRODUTOS DE LIMPEZA                       |")
  print("|                  4- LISTAR PRODUTOS                           |")
  print("|                  5- SOBRE A DESPENSA DOMÉSTICA                |")
  print("-----------------------------------------------------------------")
  escolha = int(input("Qual deseja acessar: "))
  return escolha
def sobre():
  os.system('clear')
  print("---------------------------------------------------------------------------")
  print("|                           DESPENSA DOMÉSTICA                            |")
  print("---------------------------------------------------------------------------")
  print("|     Esse projeto serve para o gerenciamento de uma despensa doméstica.  |")
  print("|     Nele é possível registrar, adicionar, remover                       |")
  print("|     e ver todos os produtos da sua despensa!                            |")
  print("|     A despensa foi separada em três tipos de produtos:                  |")
  print("|     1-  Comidas                                                         |")
  print("|     2-  Produtos de limpeza                                             |")
  print("|     3-  Produtos de higiene pessoal.                                    |")
  print(f"|     Projeto feito por : {rosa}Beatriz Vitória da Costa, BSI 2023.1{fim}            |")
  print("---------------------------------------------------------------------------")
  input("Tecle ENTER para continuar!")

def listar():
  if banco:
    if comidaas:
      print("-----------------------------------------------------------------")
      print("|                       Todas as comidas                        |")
      print("-----------------------------------------------------------------")
      for x in comidaas:
          print("Nome:",x," Validade:", comidaas[x][0]," Quantidade:", comidaas[x][1])
      print("-----------------------------------------------------------------")
    else :
      print("-----------------------------------------------------------------")
      print("|                  Nenhuma comida cadastrada!                   |")
      print("-----------------------------------------------------------------")
    if produtos:
      print("-----------------------------------------------------------------")
      print("|                 Todos os produtos de limpeza                  |")
      print("-----------------------------------------------------------------")
      for x in produtos:
          print("Nome:",x," Validade:", produtos[x][0]," Quantidade:", produtos[x][1])
      print("-----------------------------------------------------------------")
    else :
      print("-----------------------------------------------------------------")
      print("|            Nenhum produto de limpeza cadastrado!              |")
      print("-----------------------------------------------------------------")
    if higiene:
      print("-----------------------------------------------------------------")
      print("|              Todos os produtos de higiene pessoal             |")
      print("-----------------------------------------------------------------")
      for x in higiene:
          print("Nome:",x," Validade:", higiene[x][0]," Quantidade:", higiene[x][1])
      print("-----------------------------------------------------------------")
    else :
      print("-----------------------------------------------------------------")
      print("|            Nenhum produto de higiene cadastrado!              |")
      print("-----------------------------------------------------------------")
  input("Tecle ENTER para continuar!")
def comidas():
  os.system('clear')
  print("-----------------------------------------------------------------")
  print("|                        MENU COMIDAS                           |")
  print("-----------------------------------------------------------------")
  print("|               0- VOLTAR AO MENU PRINCIPAL                     |")
  print("|               1- CADASTRAR COMIDA                             |")
  print("|               2- PESQUISAR COMIDA                             |")
  print("|               3- ADICIONAR COMIDA                             |")
  print("|               4- RETIRAR COMIDA                               |")
  print("|               5- VER TODOS CADASTRADOS                        |")
  print("-----------------------------------------------------------------")
  escolha = int(input("Qual deseja acessar: "))
  return escolha

def higiene_pessoal():
  os.system('clear')
  print("-----------------------------------------------------------------")
  print("|                     MENU HIGIENE PESSOAL                       |")
  print("-----------------------------------------------------------------")
  print("|                  0- VOLTAR AO MENU PRINCIPAL                   |")
  print("|                  1- CADASTRAR PRODUTO                          |")
  print("|                  2- PESQUISAR PRODUTO                          |")
  print("|                  3- ADICIONAR PRODUTO                          |")
  print("|                  4- RETIRAR PRODUTO                            |")
  print("|                  5- VER TODOS CADASTRADOS                      |")
  print("-----------------------------------------------------------------")
  escolha = int(input("Qual deseja acessar: "))
  return escolha

def produtos_limpeza():
  os.system('clear')
  print("-----------------------------------------------------------------")
  print("|                     MENU PRODUTOS DE LIMPEZA                  |")
  print("-----------------------------------------------------------------")
  print("|                 0- VOLTAR AO MENU PRINCIPAL                   |")
  print("|                 1- CADASTRAR PRODUTO                          |")
  print("|                 2- PESQUISAR PRODUTO                          |")
  print("|                 3- ADICIONAR PRODUTO                          |")
  print("|                 4- RETIRAR PRODUTO                            |")
  print("|                 5- VER TODOS CADASTRADOS                      |")
  print("-----------------------------------------------------------------")
  escolha = int(input("Qual deseja acessar: "))
  return escolha
def cadastrar():
  nome = input("Digite o nome do produto: ")
  validade = verifica_data()
  quantidade = int(input("Digite a quantidade: "))
  if validade==False:
    print("-----------------------------------------------------------------")
    print("|              Produto Vencido!Não será adicionado!              |")
    print("-----------------------------------------------------------------")
  else:
    produtos[nome] = [validade,quantidade]
    print("-----------------------------------------------------------------")
    print("|              Produto adicionado com sucesso!                  |")
    print("-----------------------------------------------------------------")
    salvar()
  input("Tecle ENTER para continuar!")

def pesquisar():
  nome = input("Digite o nome do produto que deseja encontrar:")
  if nome in produtos:
    print("Nome:", nome," Validade:",produtos[nome][0]," Quantidade: ", produtos[nome][1])
  else:
    print("-----------------------------------------------------------------")
    print("|                    Produto não encontrado!                     |")
    print("-----------------------------------------------------------------")
  input("Tecle ENTER para continuar!")

def adicionar():
    nome = input("Digite o nome do produto que deseja atualizar:")
    if nome in produtos:
        quantidade = int(input("Digite a quantidade de produtos a serem adicionados: "))
        produtos[nome][1] += quantidade
        print("Produto atualizado com sucesso!")
        salvar()
    else:
      print("-----------------------------------------------------------------")
      print("|                    Produto não encontrado!                     |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")

def remover():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    if nome in produtos:
      quantidade = int(input("Digite a quantidade de produtos a serem removidos: "))
      produtos[nome][1] -= quantidade
      if produtos[nome][1]<=0:
        del produtos[nome]
        print("Produto apagado com sucesso!")
        salvar()
      else:
        print("Produtos removidos com sucesso!")
        salvar()
    else:
      print("-----------------------------------------------------------------")
      print("|                    Produto não encontrado!                     |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")

def ver_tudo():
    if produtos:
        print("-----------------------------------------------------------------")
        print("|              Todos os produtos de limpeza                      |")
        print("-----------------------------------------------------------------")
        for x in produtos:
          print("Nome:",x," Validade:", produtos[x][0]," Quantidade:", produtos[x][1])
        print("-----------------------------------------------------------------")
    else:
      print("-----------------------------------------------------------------")
      print("|             Ainda não há produtos cadastrados!                 |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")

def cadastrar_comidas():
  nome = input("Digite o nome do produto: ")
  validade = verifica_data()
  quantidade = int(input("Digite a quantidade: "))
  if validade==False:
    print("-----------------------------------------------------------------")
    print("|              Produto Vencido!Não será adicionado!              |")
    print("-----------------------------------------------------------------")
  else:
    comidaas[nome] = [validade,quantidade]
    print("-----------------------------------------------------------------")
    print("|              Produto adicionado com sucesso!                  |")
    print("-----------------------------------------------------------------")
    salvar()
  input("Tecle ENTER para continuar!")

def pesquisar_comidas():
  nome = input("Digite o nome do produto que deseja encontrar:")
  if nome in comidaas:
    print("Nome:", {nome} ," Validade:",comidaas[nome][0]," Quantidade: ",comidaas[nome][1])
  else:
      print("-----------------------------------------------------------------")
      print("|                    Produto não encontrado!                     |")
      print("-----------------------------------------------------------------")
  input("Tecle ENTER para continuar!")
  
def adicionar_comidas():
    nome = input("Digite o nome do produto que deseja  atualizar:")
    if nome in comidaas:
        quantidade = int(input("Digite a quantidade de produtos a serem adicionados: "))
        comidaas[nome][1] += quantidade
        print("Produto atualizado com sucesso!")
        salvar()
    else:
      print("-----------------------------------------------------------------")
      print("|                    Produto não encontrado!                     |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")

def remover_comidas():
    nome = input("Digite o nome do produto que deseja remover: ")
    if nome in comidaas:
      quantidade = int(input("Digite a quantidade de produtos a serem removidos: "))
      comidaas[nome][1] -= quantidade
      if comidaas[nome][1]<=0:
         del comidaas[nome]
         print("Produto apagado com sucesso!")
         salvar()
      else:
        print("Produtos removidos com sucesso!")
        salvar()
    else:
      print("-----------------------------------------------------------------")
      print("|                    Produto não encontrado!                     |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")

def ver_tudo_comidas():
    if comidaas:
        print("-----------------------------------------------------------------")
        print("|                       Todas as comidas                         |")
        print("-----------------------------------------------------------------")
        for x in comidaas:
          print("Nome:",x," Validade:", comidaas[x][0]," Quantidade:", comidaas[x][1])
        print("-----------------------------------------------------------------")
    else:
      print("-----------------------------------------------------------------")
      print("|             Ainda não há produtos cadastrados!                 |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")

def cadastrar_higiene():
  nome = input("Digite o nome do produto: ")
  validade = verifica_data()
  quantidade = int(input("Digite a quantidade: "))
  if validade==False:
    print("-----------------------------------------------------------------")
    print("|              Produto Vencido!Não será adicionado!              |")
    print("-----------------------------------------------------------------")
  else:
    higiene[nome] = [validade,quantidade]
    print("-----------------------------------------------------------------")
    print("|              Produto adicionado com sucesso!                  |")
    print("-----------------------------------------------------------------")
    salvar()
  input("Tecle ENTER para continuar!")

def pesquisar_higiene():
  nome = input("Digite o nome do produto que deseja encontrar:")
  if nome in higiene:
    print("Nome:", {nome} ," Validade:",higiene[nome][0]," Quantidade: ",higiene[nome][1])
  else:
      print("-----------------------------------------------------------------")
      print("|                    Produto não encontrado!                     |")
      print("-----------------------------------------------------------------")
  input("Tecle ENTER para continuar!")

def adicionar_higiene():
    nome = input("Digite o nome do produto que deseja  atualizar:")
    if nome in higiene:
        quantidade = int(input("Digite a quantidade de produtos a serem adicionados: "))
        higiene[nome][1] += quantidade
        print("Produto atualizado com sucesso!")
        salvar()
    else:
      print("-----------------------------------------------------------------")
      print("|                    Produto não encontrado!                     |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")

def remover_higiene():
    nome = input("Digite o nome do produto que deseja remover: ")
    if nome in higiene:
      quantidade = int(input("Digite a quantidade de produtos a serem removidos: "))
      higiene[nome][1] -= quantidade
      if higiene[nome][1]<=0:
         del higiene[nome]
         print("Produto apagado com sucesso!")
         salvar()
      else:
        print("Produtos removidos com sucesso!")
        salvar()
    else:
      print("-----------------------------------------------------------------")
      print("|                    Produto não encontrado!                     |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")
  
def ver_tudo_higiene():
    if higiene:
      print("-----------------------------------------------------------------")
      print("|          Todos os produtos de higiene pessoal                 |")
      print("-----------------------------------------------------------------")
      for x in higiene:
        print("Nome:",x," Validade:", higiene[x][0]," Quantidade:", higiene[x][1])
      print("-----------------------------------------------------------------")
    else:
      print("-----------------------------------------------------------------")
      print("|             Ainda não há produtos cadastrados!                 |")
      print("-----------------------------------------------------------------")
    input("Tecle ENTER para continuar!")

esc = menu()
while esc != 0:
  esc = menu()
  if esc == 1:
    esc2=comidas()
    while esc2!=0:
      if esc2==1:
         cadastrar_comidas() 
      elif esc2==2:
        pesquisar_comidas()
      elif esc2==3:
        ver_tudo_comidas()
        adicionar_comidas()
      elif esc2==4:
        ver_tudo_comidas()
        remover_comidas()
      elif esc2==5:
        ver_tudo_comidas()
      esc2=comidas()
  elif esc == 2:
    esc2=higiene_pessoal()
    while esc2!=0:
      if esc2==1:
        cadastrar_higiene()  
      elif esc2==2:
        pesquisar_higiene() 
      elif esc2==3:
        ver_tudo_higiene()
        adicionar_higiene() 
      elif esc2==4:
         ver_tudo_higiene()
         remover_higiene()
      elif esc2==5:
        ver_tudo_higiene()
      esc2=higiene_pessoal()
  elif esc == 3:
    esc2=produtos_limpeza()
    while esc2!=0:
      if esc2==1:
         cadastrar() 
      elif esc2==2:
        pesquisar() 
      elif esc2==3:
        ver_tudo()
        adicionar()
      elif esc2==4:
        ver_tudo()
        remover()
      elif esc2==5:
        ver_tudo()
      esc2=produtos_limpeza()
  elif esc == 4:
    listar()
  elif esc == 5:
    sobre()
  elif esc == 0:
    print("-----------------------------------------------------------------")
    print("|                              FIM                              |")
    print("-----------------------------------------------------------------")
    esc==0;
  else:
    print("-----------------------------------------------------------------")
    print("|                          Opção inválida!                      |")
    print("-----------------------------------------------------------------")
