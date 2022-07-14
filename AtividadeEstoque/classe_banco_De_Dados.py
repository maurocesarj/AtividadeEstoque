import mysql.connector
from classe_fabricante import *
from classe_produtos import *
from classe_historico_compras import *
from classe_historico_vendas import *
import datetime

class Banco:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='comerce_sports'
        )
        self.pls = []
        self.historicompra = []
        self.historivenda = []

        self.mycursor = self.conexao.cursor()
        self.Historico = Historico_Compras()
    # cadastrar fabricante
    def cadastrar_fabricante(self, cod, nome):
        objeto_fabricante = Fabricante(cod, nome)
        comando_sql = f'insert into Fabricante (nome_fabricante) value ("{objeto_fabricante.nome}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()

    # cadastrar produto
    def cadastrar_produto(self, cod, nome, fabricante, quantidade):
        objeto_produto = Produto(cod, nome, fabricante, quantidade)
        comando_sql = f'select nome_fabricante from Fabricante'
        self.mycursor.execute(comando_sql)
        luisa = self.mycursor.fetchall()
        for i in luisa:
            var1 = str(i)
            var1.replace(',', '')
            var2 = var1.replace('(', '')
            var3 = var2.replace(')', '')
            var4 = var3.replace(',', '')
            if fabricante in var4:
                comando_sql = f'insert into Produto (nome_produto, fabricante_produto, quantidade_produto) value ("{objeto_produto.nome}", "{objeto_produto.fabricante}", {objeto_produto.quantidade})'
                self.mycursor.execute(comando_sql)
                self.conexao.commit()
                break
            else:
                pass
        else:
            pass

    # listar produtos c/s codigo
    def listar_produtos(self, cod):
        if cod == '':
            comando_sql = f'select * from Produto'
            self.mycursor.execute(comando_sql)
            list = self.mycursor.fetchall()
            for i in list:
                exib = (f' {i} ').replace(',', ' | ').replace("'", '♦').replace('(', '╠{').replace(')', '}╣')
                self.pls.append(exib)
        else:
            comando_sql = f'select * from Produto where cod_produto = {cod}'
            self.mycursor.execute(comando_sql)
            list = self.mycursor.fetchall()
            for i in list:
                exib = (f' {i} ').replace(',', ' | ').replace("'", '♦').replace('(', '╠{').replace(')', '}╣')
                return exib

    # alterar dados
    def alterar_dados(self, atributo, valor, cod):
        comando_sql = f'update Produto set {atributo} = "{valor}" where cod_produto = {cod}'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()
        print('Alteração realizada com sucesso')

    def comprar_produtos(self, atributo, cod, quantidade):
        comando_sql = f'update Produto set {atributo} = quantidade_produto + {quantidade} where cod_produto = {cod}'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()
        hoje = datetime.date.today()
        print('Compra realizada com sucesso')
        historico_compra = Historico_Compras()
        comando_historico = f'insert into historico_compra (cod_produto_hc, data_hc, quantidade_produto_hc) value ("{cod}", "{hoje}", "{quantidade}")'
        self.mycursor.execute(comando_historico)
        self.conexao.commit()

    def vender_produtos(self, atributo, cod,  quantidade_final):
        comando_sql = f'select quantidade_produto from Produto where cod_produto = {cod}'
        self.mycursor.execute(comando_sql)
        quantidade_final1 = int(quantidade_final)
        luisa = self.mycursor.fetchall()
        for i in luisa:
            estoque1 = str(i)
            estoque1.replace(',', '')
            estoque2 = estoque1.replace('(', '')
            estoque3 = estoque2.replace(')', '')
            estoque4 = estoque3.replace(',', '')
            estoque5 = int(estoque4)
            if quantidade_final1 <= estoque5:
                comando_sql = f'update Produto set {atributo} = quantidade_produto - {quantidade_final} where cod_produto = {cod}'
                self.mycursor.execute(comando_sql)
                self.conexao.commit()
                hoje = datetime.date.today()
                print(f'Venda de {quantidade_final} Produto(s) realizada com sucesso')
                historico_venda = Historico_Vendas()
                comando_historico = f'insert into historico_venda (cod_produto_hv, data_hv, quantidade_produto_hv) value ("{cod}", "{hoje}", "{quantidade_final}")'
                self.mycursor.execute(comando_historico)
                self.conexao.commit()
            else:
                print('Você não consegue realizar esta venda, falta de estoque')

    def listar_historico_compra(self):
        comando_sql = f'select * from  historico_compra'
        self.mycursor.execute(comando_sql)
        luisa = self.mycursor.fetchall()
        for i in luisa:
            comprinha = ('COD PRODUTO:', i[1],'DATA:', i[2],'QUANTIDADE PRODUTO:', i[3])
            self.historicompra.append(comprinha)

    def listar_historico_venda(self):
        comando_sql = f'select * from  historico_venda'
        self.mycursor.execute(comando_sql)
        luisa = self.mycursor.fetchall()
        for i in luisa:
            vendinha = ('ID: ', i[0],
                  'COD PRODUTO: ', i[1],
                  'DATA: ', i[2],
                  'QUANT PRODUTO: ', i[3])
            self.historivenda.append(vendinha)