import pymongo
import pandas as pd


class BancoDeDados:

    def __init__(self):
        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")['exercicio_banco']['pessoa']

    def inserir_pessoa(self, dados: dict):
        self.conexao.insert_one(dados)

    def alterar_pessoa(self, dados: dict, novos_dados: dict):
        self.conexao.update_one(dados, {'$set': novos_dados})

    def deletar_pessoa(self, dados: dict):
        self.conexao.delete_one(dados)

    def consultar_pessoas(self):
        print(pd.DataFrame(self.conexao.find()))


# teste = BancoDeDados()
# teste.inserir_pessoa(dict(nome='Augusto Soares', idade=38, peso=91.4, altura=1.92))
# teste.alterar_pessoa(dict(nome='Augusto Soares'), dict(idade=41, peso=87.9, altura=1.93)
# teste.deletar_pessoa((dict(nome='João da Costa')))
# teste.consultar_pessoas()