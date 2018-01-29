# -*- coding: UTF-8 -*-
def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome
def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome = raw_input()
    posicao = nome.index(nome)
    print 'Por qual nome vc gostaria de alterar?'
    nomes[posicao] = raw_input()

def procurar(nomes):
    print 'Digite o nome a procurar:'
    nome = raw_input()
    if(nome in nomes):
        print "Nome %s está cadastrado" % (nome)
    else:
        print "Nome %s não está cadastrado" % (nome)

def menu():
    nomes = []
    escolha = ''
    while (escolha != '0'):
        print 'Digite 1 para cadastrar \n 0 para terminar \n 2 para listar nomes \n 3 para excluir \n 4 para alterar \n 5 para pesquisar'
        escolha = raw_input()
        if(escolha == '1'):
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            remover(nomes)
        if(escolha == '4'):
            alterar(nomes)
        if(escolha == '5'):
            procurar(nomes)
menu()
