from classe_banco_De_Dados import *
from tkinter import *
banco_dados_mauro = Banco()



def format_cpf(event = None):
    text = entry_cpf_login.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    entry_cpf_login.delete(0, "end")
    entry_cpf_login.insert(0, new_text)

win = Tk() # criação janelas e frames
win.title('KARASUNO') # definindo nome da janela
inicio = Frame(win) # frame do banner inicial
login = Frame(win) # frame do banner login
registro_novo_usuario = Frame(win) # frame do banner novo usuario
painel_controle = Frame(win) # frame do banner painel controle
historico = Frame(win) # frame do banner do historico
alterar = Frame(win) # frame do banner para alterar nome
listar = Frame(win) # frame do banner para listar produtos
cadastrar = Frame(win) # frame do banner cadastrar produtos e fabricantes
venda = Frame(win) # frame do banner venda e compra de produtos

# Definir imagens de Frames

# imagem de capa
img_inicial = PhotoImage(file="img estoque/banner_capa.png")
label_inicial = Label(inicio, image=img_inicial)
label_inicial.pack()
# imagem de login
img_login = PhotoImage(file="img estoque/banner_login.png")
label_login = Label(login, image=img_login)
label_login.pack()
# imagem de registro novo usuario
img_novousu = PhotoImage(file="img estoque/banner_registro.png")
label_novousu = Label(registro_novo_usuario, image=img_novousu)
label_novousu.pack()
# imagem de painel controle
img_painelcontrole = PhotoImage(file="img estoque/banner_painel_controle.png")
label_painelcontrole = Label(painel_controle, image=img_painelcontrole)
label_painelcontrole.pack()
# imagem historico
img_historico = PhotoImage(file="img estoque/banner_historicos.png")
label_historico = Label(historico, image=img_historico)
label_historico.pack()
# imagem alterar
img_alterar = PhotoImage(file="img estoque/banner_alterar_nome.png")
label_alterar = Label(alterar, image=img_alterar)
label_alterar.pack()
# imagem listar
img_listar = PhotoImage(file="img estoque/banner_listar.png")
label_listar = Label(listar, image=img_listar)
label_listar.pack()
# imagem cadastro
img_cadas = PhotoImage(file="img estoque/banner_cadastrar.png")
label_cadas = Label(cadastrar, image=img_cadas)
label_cadas.pack()
# imagem venda e compra
img_venda = PhotoImage(file="img estoque/banner_venda_compra.png")
label_venda = Label(venda, image=img_venda)
label_venda.pack()




# Criação de botoes e Entrys
# Tela inicial
continuar = Button(inicio, text='CONTINUAR', font='Arial 20 bold', foreground='#070A0E', bd=0, background='white', cursor='hand2', padx=20, pady=7, command=lambda: [inicio.pack_forget(), login.pack()])
continuar.place(x=1220,y=762)

# Tela de login
entry_cpf_login = Entry(login, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=40, bd=0)
entry_cpf_login.place(x=948, y=330)
entry_senha_login = Entry(login, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', show='*',width=40, bd=0)
entry_senha_login.place(x=948, y=471)
continuar = Button(login, text='CONTINUAR', font='Arial 31 bold', foreground='white', bd=0, activebackground='#070A0E',background='#070A0E', cursor='hand2', padx=15, pady=0, command=lambda: [login.pack_forget(), painel_controle.pack()])
continuar.place(x=997,y=552)
criarconta = Button(login, text='Sou novo, Criar Conta', font='Arial 12', foreground='black', bd=0, background='white', cursor='hand2', padx=15, pady=0, command=lambda: [login.pack_forget(), registro_novo_usuario.pack()])
criarconta.place(x=1049,y=665)
continuar = Button(login, text='Voltar', font='Arial 12', foreground='black', bd=0, background='white', cursor='hand2', padx=15, pady=0, command=lambda: [login.pack_forget(), inicio.pack()])
continuar.place(x=1112,y=710)
entry_cpf_login.bind("<KeyRelease>", format_cpf)
# Tela de registro
logar_conta = Button(registro_novo_usuario, text='Tenho conta, Fazer Login', font='Arial 12', foreground='black', bd=0, background='white', cursor='hand2', padx=15, pady=0, command=lambda: [registro_novo_usuario.pack_forget(), login.pack()])
logar_conta.place(x=737,y=660)

# Tela Painel Administrador
voltar_painel = Button(painel_controle, text='Voltar', font='Arial 11', foreground='black', bd=0, background='#FFB63A', cursor='hand2', padx=15, pady=0, command=lambda: [painel_controle.pack_forget(), registro_novo_usuario.pack()])
voltar_painel.place(x=460,y=630)
historicos_painel = Button(painel_controle, text='Historicos', font='Arial 11', foreground='black', bd=0, background='#FFB63A', cursor='hand2', padx=15, pady=0, command=lambda: [painel_controle.pack_forget(), historico.pack()])
historicos_painel.place(x=460,y=590)
alterar_painel = Button(painel_controle, text='Alterar Nome Produtos', font='Arial 11', foreground='black', bd=0, background='#FFB63A', cursor='hand2', padx=15, pady=0, command=lambda: [painel_controle.pack_forget(), alterar.pack()])
alterar_painel.place(x=460,y=550)
listar_painel = Button(painel_controle, text='Listar Produtos', font='Arial 11', foreground='black', bd=0, background='#FFB63A', cursor='hand2', padx=15, pady=0, command=lambda: [painel_controle.pack_forget(), listar.pack()])
listar_painel.place(x=460,y=510)

registar_painel = Button(painel_controle, text='REGISTRAR', font='Arial 19 bold', foreground='black', bd=0, background='white', cursor='hand2', padx=12, pady=55, command=lambda: [painel_controle.pack_forget(), cadastrar.pack()])
registar_painel.place(x=527,y=291)
compra_painel = Button(painel_controle, text='COMPRA & \nVENDA', font='Arial 18 bold', foreground='black', bd=0, background='white', cursor='hand2', padx=10, pady=49, command=lambda: [painel_controle.pack_forget(), venda.pack()])
compra_painel.place(x=808,y=286)

# Tela historico

def mostrar_historico_compra():
    banco = Banco()
    db = banco.listar_historico_compra()
    for y in range(len(banco.historicompra)):
        print(len(banco.historicompra))
        listagem_historico_compra.insert(END, banco.historicompra[y])
    else:
        pass

def mostrar_historico_venda():
    banco = Banco()
    db = banco.listar_historico_venda()
    for y in range(len(banco.historivenda)):
        print(len(banco.historivenda))
        listagem_historico_venda.insert(END, banco.historivenda[y])
    else:
        pass


voltar_painel = Button(historico, text='Voltar', font='Arial 15 bold', foreground='black', bd=0, background='white', cursor='hand2', padx=15, pady=0, command=lambda: [historico.pack_forget(), painel_controle.pack()])
voltar_painel.place(x=65,y=45)

listagem_historico_compra = Listbox(historico, font='Arial 11', foreground='black', bg='white', bd=0, selectbackground='#FFB63A',selectforeground='black',width=66, height=26)
listagem_historico_compra.place(x=150,y=334)
listagem_historico_venda = Listbox(historico, font='Arial 11', foreground='black', bg='white', bd=0, selectbackground='#FFB63A',selectforeground='black',width=66, height=26)
listagem_historico_venda.place(x=913,y=334)

def deleteh():
   listagem_historico_compra.delete(0,END)
   listagem_historico_venda.delete(0, END)

botao_historico = Button(historico, text='MOSTRAR', font='Arial 12', bg='#FFB63A', bd=0, command=lambda: [mostrar_historico_compra(), mostrar_historico_venda()])
botao_historico.place(x=755, y=550)
botao_historico_limp = Button(historico, text='LIMPAR', font='Arial 12', bg='#FFB63A', bd=0, command=lambda: [deleteh()])
botao_historico_limp.place(x=760, y=580)

# Tela alterar
atributo = 'nome_produto'
entry_cod_alterar = Entry(alterar, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=30, bd=0)
entry_cod_alterar.place(x=677, y=378)
entry_nome_alterar = Entry(alterar, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=30, bd=0)
entry_nome_alterar.place(x=675, y=468)
alterar_alterar = Button(alterar, text='ALTERAR', font='Arial 22 bold', foreground='white', bd=0, background='#070A0E', cursor='hand2', padx=38, pady=14, command=lambda: [banco_dados_mauro.alterar_dados(atributo, entry_nome_alterar.get(), entry_cod_alterar.get())])
alterar_alterar.place(x=700,y=536)
voltar_alterar = Button(alterar, text='Voltar', font='Arial 15', foreground='black', bd=0, background='white', cursor='hand2', padx=15, pady=0, command=lambda: [alterar.pack_forget(), painel_controle.pack()])
voltar_alterar.place(x=760,y=650)

# Tela listar


Listagem_produtos = Listbox(listar, font='Arial 13', foreground='black', bg='white', bd=0, selectbackground='#FFB63A',selectforeground='black',width=68, height=35)
Listagem_produtos.place(x=807, y=100)
entry_nome_listar = Entry(listar, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=35, bd=0)
entry_nome_listar.place(x=148, y=462)
def delete():
   Listagem_produtos.delete(0,END)

def search():
    banco = Banco()
    a = entry_nome_listar.get()
    db = banco.listar_produtos(a)
    if a != '':
        Listagem_produtos.insert(END, db)
    else:
        for y in range(len(banco.pls)):
            print(len(banco.pls))
            Listagem_produtos.insert(END, banco.pls[y])


voltar_listar = Button(listar, text='Voltar', font='Arial 15', foreground='black', bd=0, background='#FFB63A', cursor='hand2', padx=15, pady=0, command=lambda: [listar.pack_forget(), painel_controle.pack(), delete()])
voltar_listar.place(x=300,y=678)
listar_listar = Button(listar, text='LISTAR', font='Arial 22 bold', foreground='white', bd=0, background='#070A0E', cursor='hand2', padx=135, pady=12, command=lambda: [search()])
listar_listar.place(x=156,y=518)


# Tela registar ----------------------------------------------------------------------------------------------

cod_produto = None
quantidade = int(0)

entry_nome_produto_registrar = Entry(cadastrar, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=30, bd=0)
entry_nome_produto_registrar.place(x=372, y=506)
entry_nome_produto_fabricante_registrar = Entry(cadastrar, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=30, bd=0)
entry_nome_produto_fabricante_registrar.place(x=367, y=596)


cadas_fabricante_p = Button(cadastrar, text='CADASTRAR', font='Arial 19 bold', foreground='white', bd=0, background='#070A0E', cursor='hand2', padx=40, pady=14, command=lambda: [banco_dados_mauro.cadastrar_produto(cod_produto, entry_nome_produto_registrar.get(), entry_nome_produto_fabricante_registrar.get(), quantidade)])
cadas_fabricante_p.place(x=384,y=667)



cod = None
entry_nome_fabricante_registrar = Entry(cadastrar, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=30, bd=0)
entry_nome_fabricante_registrar.place(x=887, y=509)
cadas_fabricante = Button(cadastrar, text='CADASTRAR', font='Arial 19 bold', foreground='white', bd=0, background='#070A0E', cursor='hand2', padx=40, pady=14, command=lambda: [banco_dados_mauro.cadastrar_fabricante(cod, entry_nome_fabricante_registrar.get())])
cadas_fabricante.place(x=898,y=668)


voltar_listar = Button(cadastrar, text='Voltar', font='Arial 15 bold', foreground='black', bd=0, background='white', cursor='hand2', padx=15, pady=0, command=lambda: [cadastrar.pack_forget(), painel_controle.pack()])
voltar_listar.place(x=90,y=30)

# Tela venda

entry_nome_produto_venda = Entry(venda, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=35, bd=0)
entry_nome_produto_venda.place(x=251, y=279)
entry_quant_produto_venda = Entry(venda, font='Arial 13', foreground='#070A0E', background='white', cursor='hand2', width=35, bd=0)
entry_quant_produto_venda.place(x=242, y=380)
voltar_venda = Button(venda, text='Voltar', font='Arial 15 bold', foreground='black', bd=0, background='white', cursor='hand2', padx=15, pady=0, command=lambda: [venda.pack_forget(), painel_controle.pack()])
voltar_venda.place(x=90,y=30)

atributo_venda = 'quantidade_produto'
vender_venda = Button(venda, text='VENDER', font='Arial 19 bold', foreground='white', bd=0, background='#070A0E', cursor='hand2', padx=75, pady=12, command=lambda: [banco_dados_mauro.vender_produtos(atributo_venda, entry_nome_produto_venda.get(),  entry_quant_produto_venda.get())])
vender_venda.place(x=261,y=452)

compra_venda = Button(venda, text='COMPRAR', font='Arial 19 bold', foreground='white', bd=0, background='#070A0E', cursor='hand2', padx=68, pady=12, command=lambda: [banco_dados_mauro.comprar_produtos(atributo_compra, entry_nome_produto_venda.get(), entry_quant_produto_venda.get())])
compra_venda.place(x=259,y=577)
atributo_compra = 'quantidade_produto'


inicio.pack()
win.geometry('1600x900')
win.resizable(False, False)
win.mainloop()
