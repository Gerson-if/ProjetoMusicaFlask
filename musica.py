from flask import Flask, render_template, request, redirect, session, flash, url_for
# da lib flask import a class Flask

#aqui criamos uma classe musica
class Musica(): 
    def __init__(self,nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero

#minha aplicação
app = Flask(__name__)
app.secret_key = 'apredendoiniciocomdaniel'#criamos uma chave secreta para aplicação

#instancias da classe musica
musica01 = Musica('Sem voce','Paula Fernandes', 'Sertanejo')
musica02 = Musica('Grandes Coisas', 'Fernandinho','Gospel')
musica03 = Musica('Teto de Vidro', 'Pit','Rock')

#criação de uma lista de musica 
lista = [musica01, musica02, musica03]


#criação de classe
class Usuario:
    # nao obrigatorio passar o self mas ela referencia a propia classe
    def __init__(self,nome,login,senha): 
        self.nome = nome
        self.login = login
        self.senha = senha


#declaração de estancias de clases
usuario01 = Usuario('Gerson Ferreira','admin','admin')
usuario02 = Usuario('luana Cardoso','luana','luana')
usuario03 = Usuario('Vilma Nunes', 'vilmanunes104','vilma')


#criamos um dicionario para trabalhar com chave valor
#aqui usamos chaves 
usuarios = {
     usuario01.login : usuario01, #aqui dezemos que o usuario01 vai ser buscado pelo login
     usuario02.login : usuario02,
     usuario03.login : usuario03
    }



#funcao de verificação de seção
def verifica_a_secao():
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        # se minha seção e igual a None, (nada)
        #ou nao temos seção  ativa para o usuario retorne para o login
        return redirect(url_for('login'))
    return None
    # se tiver tudo certo retorna nada ou seja nada precisa ser feito


#funcao de menssagem de erro de login
def menssagem_erro_de_login():
    flash("usuario ou senha invalidos")

#funcao de menssagem de sucesso com paramentros a receber
def menssagem_de_sucesso_login(nome_do_usuario):
    flash("Bem vindo " + nome_do_usuario)


#rota que retorna pagina inicial
@app.route('/') 
def lista_musicas():
    checagem = verifica_a_secao() # forma diferente de validar com uma função
    if checagem:
        return checagem
    return render_template('lista_musicas.html',
                           titulo = "Musicas Cadastradas",
                           musicas = lista)



#rota que retorna pagina de cadastro
@app.route('/cadastrar')
#declaração de função
def cadastrar_musica(): 
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))
    return render_template('cadastrar_musica.html',
                           titulo = "Cadastrar Musica") 
                            # ao chamar a função cadastrar_musica() ela retorna a pagina



# rota /adicionar, E informamos que sera recebido dados com metodo post
@app.route('/adicionar', methods=['POST',])
def adicionar_musica():
    nome = request.form['txtNome'] #resgate de informação da pagina com request
    cantorBanda = request.form['txtCantor']
    genero = request.form['txtGenero']
    novaMusica = Musica(nome, cantorBanda,genero)#aqui passamos os paramentros para clase
   
    lista.append(novaMusica) #adicionar ao fim da lista e passamos novaMusica como parametro
   
    return redirect(url_for('lista_musicas'))



#rota de retorna pagina login
@app.route('/login')
def login():
    return render_template('login.html',
                           titulo = "Entre com Suas Credencias")
#rota que trata autenticação
@app.route('/autenticar', methods=['POST',] )
def autenticar():
    if request.form['txtLogin'] in usuarios:# se oque eu digitei em login esta no dicionario usuarios
        usuarioEncontrado = usuarios[request.form['txtLogin']]
        #comparamos e acessamos o atributos do dicionario
        if request.form['txtSenha'] == usuarioEncontrado.senha:
            session['usuario_logado'] = request.form['txtLogin']#aqui criamos uma seção para o usuario
            menssagem_de_sucesso_login(usuarioEncontrado.login)
            nomelogin = usuarioEncontrado.login
            
            return redirect(url_for('lista_musicas')) 
            #aparentemente posso chamar qualquer função com
            # este url_for mesmo em rotas diferentes, mas devo evitar ter mesmo nome de funcao ja que sobrecarga nao é aceito.
        else:
            menssagem_erro_de_login()
            return redirect(url_for('login'))
            
    else:
        menssagem_erro_de_login()
        return redirect(url_for('login'))
        # aqui usamos o
        #url_for para deixar mais dinamico e dizemos
        #qual função vamos chamar ao envez de apontar para rota em si


#rota personalizada de perfil
#temos rotas diferentes uma redeirização e criamos outras para ação
#processamento de dados e exibição de dados
@app.route('/perfil')
def perfil_do_usuario():
    return render_template('perfil_usuario.html',
                           titulo = "Perfil")
@app.route('informacao', method="POST,")
def mostrar_informacao_usuario():
    pass


#aqui nesta rota destruimos a seção     
@app.route('/sair')
def sair():
    session['usuario_logado'] = None # encerramos a seção
    return redirect(url_for('login'))

app.run(debug=True) # inica aplicação em modo debug agente passando os parametros debug=true
