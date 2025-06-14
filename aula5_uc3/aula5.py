# criar conteudo

def criar_arquivo(nome_aqv: str, conteudo: str):
   """Cria um aquivo com nome e conteudo fornecido. """
   with open(nome_aqv, 'w') as arquivo:
       arquivo.write(conteudo)
       print ('arquivo criado com sucesso')

nome=input('digite o nome do arquivo: ')
criar_arquivo(f'./aula5_uc3/arquivos/{nome}.txt', "exemplo")


# ler o conteudo


def ler_arquivo(nome_aqv: str):
    """Retorna o conteudo de um aquivo fornecido. """
    with open(nome_aqv, 'r') as arquivo:
       return arquivo.read()


nome=input('digite o nome do arquivo: ')
print(ler_arquivo(f'./aula5_uc3/arquivos/{nome}.txt'))


# add conteudo


def add_conteudo(nome_arqv: str, conteudo: str):
   """Adicionar um conteudo a um arquivo. """
   with open(nome_arqv, 'a') as arquivo:
       arquivo.write('\n' + conteudo)
       print ('conteudo adicionado com sucesso')

nome=input('digite o nome do arquivo: ')
conteudo = input("digite o texto a ser adicionado: ")
add_conteudo(f'./aula5_uc3/arquivos/{nome}.txt', conteudo)


# contar as linhas


def contar_linhas(nome_aqv: str) -> int:
    """Retorna a quantidade de linhas de um aquivo fornecido. """
    with open(nome_aqv, 'r') as arquivo:
       return len(arquivo.readlines())
    


nome=input('digite o nome do arquivo: ')
print(contar_linhas(f'./aula5_uc3/arquivos/{nome}.txt'))



# verificar se uma palavra existe no conteudo


def seek_palavra(nome_aqv: str, palavra: str) ->bool:
    """Verifica se ha uma palvra em um aquivo. """
    with open(nome_aqv, 'r') as arquivo:
       return palavra in arquivo.read()


nome=input('digite o nome do arquivo: ')
print(seek_palavra(f'./aula5_uc3/arquivos/{nome}.txt', 'python'))


# Criar um arquivo com 3 linhas (um numero em cada)
# Crie uma função que some os numeros


def criar_arquivo(nome_aqv: str, conteudo: str):
   """Cria um aquivo com nome e conteudo fornecido. """
   with open(nome_aqv, 'w') as arquivo:
       arquivo.write(conteudo)
       print ('arquivo criado com sucesso')

nome=input('digite o nome do arquivo: ')
criar_arquivo(f'./aula5_uc3/arquivos/{nome}.txt', "5\n10\n15")


def somar_numeros(nome_aqv: str) ->int:
  """Retorna a soma dos numeros fornecidos fornecido. """
  with open(nome_aqv, 'r') as arquivo:
     return sum(int(linha.strip())for linha in arquivo)

nome=input('digite o nome do arquivo: ')
print(somar_numeros(f'./aula5_uc3/arquivos/{nome}.txt'))


# atualizar uma linha específica do arquivo


def atualizar_arquivo(nome_aqv: str, novo_conteudo: str, linha_alvo: str):
    """Retorna a soma dos numeros fornecidos fornecido. """
    with open(nome_aqv,'r') as arquivo:
        linhas = arquivo.readlines()
        if 0 <= linha_alvo < len(linhas):
            linhas[linha_alvo] = novo_conteudo + '\n'
    with open(nome_aqv,'w') as arq:
        arq.writelines(linhas)

nome=input('digite o nome do arquivo: ')
conteudo = input('informe o conteudo do arquivo')
linha=input('diga o numero de linhas do arquivo: ')
print(atualizar_arquivo(f'./aula5_uc3/arquivos/{nome}.txt',conteudo, linha))


# remover arquivo


import os


def delete_aqv(nome_aqv: str):
    """Excluir arquivo caso exista. """
    if os.path.exists(nome_aqv):
       os.remove(nome_aqv)
       print ("arquivo removido")
    else:
       print("arquivo não encontrado")
       

nome=input('digite o nome do arquivo que deseja remover: ')
delete_aqv(f'./aula5_uc3/arquivos/{nome}.txt')
