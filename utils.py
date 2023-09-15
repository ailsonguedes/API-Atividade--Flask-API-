from models import Pessoas, db_session


def insere_pessoas():
    pessoa = Pessoas(nome='Felipe', idade=23)
    print(pessoa)
    pessoa.save()
     
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    print(pessoa.nome)
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.idade = 23
    pessoa.save()
    
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()
    
if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()