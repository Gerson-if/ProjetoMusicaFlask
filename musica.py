from flask import Flask, render_template
# da lib flask import a class Flask

class Musica(): #aqui criamos uma classe musica
    def __init__(self,nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero

app = Flask(__name__)

musica01 = Musica('Sem voce','Paula Fernandes', 'Sertanejo')
musica02 = Musica('Grandes Coisas', 'Fernandinho','Gospel')
musica03 = Musica('Teto de Vidro', 'Pit','Rock')

lista = [musica01, musica02, musica03]

@app.route('/inicio')
def lista_musicas():
    return render_template('lista_musicas.html',
                           titulo = "Lista de Musicas - Aprendendo com Daniel",
                           musicas = lista)

app.run(debug=True) # inica aplicação em modo debug agente passando os parametros debug=true