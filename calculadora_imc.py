# inputs definidos pelo usario, com correcao automatica em caso de usar virgulas ao inves de ponto
height = input("Qual sua altura em m: ").replace(',','.')
weight = input("Qual o seu peso em kg: ").replace(',','.')
        # LISTA IMC (referencia):
        # Abaixo de 17	Muito abaixo do peso
        # Entre 17 e 18,49	Abaixo do peso
        # Entre 18,50 e 24,99	Peso normal
        # Entre 25 e 29,99	Acima do peso
        # Entre 30 e 34,99	Obesidade I
        # Entre 35 e 39,99	Obesidade II (severa)
        # Acima de 40	Obesidade III (mórbida)
# Converte os inputs para numeros e calcula o IMC
w=float(weight)
h=float(height)
bmi = round(w / (h**2),1)

# Printa o resultado do IMC e qual categoria se encontra em relacao a tabela de referencia
print(f'Seu IMC é {bmi}')
if bmi < 17:
    print ("Sua categoria de IMC é Muito Abaixo do Peso")
elif 17 <= bmi < 18.5: 
    print ("Sua categoria de IMC é Abaixo do Peso")
elif 18.5 <= bmi < 25: 
    print ("Sua categoria de IMC é Peso Ideal")
elif 25 <= bmi < 30: 
    print ("Sua categoria de IMC é Acima do Peso")
elif 30 <= bmi < 35: 
    print ("Sua categoria de IMC é Obesidade I")
elif 35 <= bmi < 40: 
    print ("Sua categoria de IMC é Obesidade II (Severa)")
elif bmi >= 40:
    print ("Sua categoria de IMC é Obseidade III (Mórbida)")