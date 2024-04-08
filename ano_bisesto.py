#######
# - Vai solicidar para o usuario informar o ano
# - retorna se o ano é bissexto ou não
# - para ser bissexto precisa:
# - ser multiplo por 400
# - não pode ser divisivel por 100 a nao ser que seja por 400
ano = int(input("Digite o ano que você quer saber se é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")
