frase = str(input('Digite uma frase qualquer: ').upper().strip()) #Frase
palavras = frase.split()
junto = ''.join(palavras)
inverso =''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto[letra], end='')
