from bot import Bot

bot = Bot("alexa")

while True:
  frase = bot.escuta()
  resp = bot.pensa(frase)
  bot.fala(resp)
  
  if frase == "tchau":
    break

print("Até logo!")
