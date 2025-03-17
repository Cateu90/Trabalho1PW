while True:
    digitar_texto = input("Digite um texto com cinco palavras: ")
    palavras = digitar_texto.split()
    if len(palavras) == 5:
        print(f"{digitar_texto}")
        print("O Texto tem cinco palavras.")
        break
    else:
        print("Digite um texto com cinco frases.")
        