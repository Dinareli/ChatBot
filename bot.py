import json

class Bot:
  def __init__(self, nome):
    try:
      memoria = open(nome+'.json', 'r')
    except FileNotFoundError:
      memoria = open(nome+'.json', 'w')
      memoria.write('["Gleidson"]')
      memoria.close()
      memoria = open(nome+ '.json', 'r')
    self.nome = nome
    self.conhecidos = json.load(memoria)
    memoria.close()
    self.historico = [""]
    self.pergutaNome =["Olá, qual é o seu nome?", "Olá, eu estou bem! Qual é o seu nome?"]
    self.frases = {'oi': "Olá, qual é o seu nome?", "tchau":"tchau", "bom dia": "Bom dia!", "ola": "Olá, qual é o seu nome?", "oi, tudo bem?": "Olá, eu estou bem! Qual é o seu nome?"}
    

  def escuta(self):
    frase = input('>: ')
    frase = frase.lower()
    frase = frase.replace('é', 'eh')
    frase = frase.replace('á', 'a')
    return frase

  def pensa(self, frase):
    if frase in self.frases:
      return self.frases[frase]

    if frase == "aprende":
      chave = input("Digite uma frase: ")
      chave = chave.lower()
      chave = chave.replace("é", "eh")
      resp = input("Digite a resposta: ")
      self.frases[chave] = resp
      return "Aprendido"
      
    if self.historico[-1] in self.pergutaNome:
      nome = self.pegaNome(frase)
      resp = self.respondeNome(nome)
      return resp
  
    try:
      resp = eval(frase)
      return resp
    except:
      pass
    return "Não entendi"

  def pegaNome(self, nome):
    if 'o meu nome eh ' in nome:
      nome = nome[14:]

    if 'eu sou o ' in nome:
      nome = nome[9:]

    if 'eu sou a ' in nome:
      nome = nome[9:]

    if 'me chamo ' in nome:
      nome = nome[9:]
      
    nome = nome.title()
    return nome

  def respondeNome(self, nome):

    if nome in self.conhecidos:
      frase = "Eaew "
    else:
      frase = "Muito prazer, "
      self.conhecidos.append(nome)
      memoria = open(self.nome+'.json', 'w')
      json.dump(self.conhecidos, memoria)
      memoria.close()
  
    return frase + nome

  def fala(self, frase):
    print(frase)
    self.historico.append(frase)