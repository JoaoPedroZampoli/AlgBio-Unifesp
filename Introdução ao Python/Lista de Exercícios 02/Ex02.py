#Em um script, o usuário deve responder à pergunta “Continuar (s/n)?”. 
#Se o usuário digitar ‘s’ ou ‘S’, o script deve retornar a mensagem “OK, continuando...”. 
#Se o usuário digitar ‘n’ ou ‘N’, o script deve retornar a mensagem “OK, parando...”. 
#Por fim, se o usuário digitar qualquer outra coisa, o script deve retornar uma mensagem de erro.

Continuar = input("Continuar? (s/n)? ")

if(Continuar == "S" or Continuar == "s"):
    print("OK, Continuando...")
elif(Continuar == "N" or Continuar == "n"):
    print("OK, Parando...")
else:
    print("Erro!")


