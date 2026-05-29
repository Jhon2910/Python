# comentario por linha
"""
comentario multilinhas

"""

print("Hello World") # print


primeiroNumero = 10
segundoNumero = 5
multiplicar = primeiroNumero * segundoNumero

print("Resultado: ", multiplicar)
#----------------------------------------------
media = 0

primeiraNota = float(input("Digite a primeira nota: ")) # primeira nota vira float
media += primeiraNota
segundoNota = float(input("Digite a segunda nota: "))
media += segundoNota
terceiraNota = float(input("Digite a terceira nota: "))
media += terceiraNota

media /= 3.0

print ("media = ", media)
#--------------------------------

frase = "sistemas de informação"

upperfrase = frase.upper()# aumentar todas as letras
lowerfrase = frase.lower()# diminuir
dividido = frase.split()#espacos em branco

print(upperfrase)
print(lowerfrase)
print(dividido)

#----------------------------
# condicional

tempo = int(input("Quantos anos o computador tem? : "))

if tempo <= 3:
    print("Computador novo")

else:
    print("Computador velho")

print("Fim")

#elif // in

time = input("Qual seu time?")
if time == "Atletico":
    print("Boa escolha")

elif time == "Flamengo" or time == "Palmeiras" or time == "corinthians":
    print("Seu time e popular")

elif time in "Gremio internacional Juventude": # in = algum dentro da string
    print("Seu time e do RS")

else:
    print("Okay")

#----------------------

#repeticao


#for

for contador in range(0, 50):
    print("oi")

for contador in range(0, 50, 2): # 2 em 2
    print(contador)

for contador in range(50, 0, -1): # regressivo
    print(contador)

#while

r = "s"
while r == "s":
    n = int(input("Digite o valor"))
    r = str(input("Quer continuar? [s/n] "))
    r = r.upper()
print("Fim")

#-------------------------

#lista

lista = [1,"a" , ["ab, cd"]]


