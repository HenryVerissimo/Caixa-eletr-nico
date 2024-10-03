#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

def valorCentenas (centena):
    return f"✅ Notas de R$100: {centena}"

def valorDezenas (dezena):
    if dezena == "1":
        return "✅ Notas de R$10: 1 "
    elif dezena == "2":
        return "✅ Notas de R$20: 1 "
    elif dezena == "3":
        return "✅ Notas de R$20: 1\n✅ Notas de R$10: 1"
    elif dezena == "4":
        return "✅ Notas de R$20: 2"
    elif dezena == "5":
        return "✅ Notas de R$50: 1"
    elif dezena == "6":
        return "✅ Notas de $50: 1\n✅ Notas de R$10: 1"
    elif dezena == "7":
        return "✅ Notas de R$50: 1\n✅ Notas de R$20: 1"
    elif dezena == "8":
        return "✅ Notas de $50: 1\n✅ Notas de R$20: 1\n✅ Notas de R$10: 1"
    elif dezena == "9":
        return "✅ Notas de R$50: 1\n✅ Notas de R$20: 2"
    else:
        return "❌ Sem notas de R$10, R$20 ou R$50"
    
def valorUnidades (unidade):
    if unidade == "1":
        return "✅ Notas de R$01: 1"
    elif unidade == "2":
        return "✅ Notas de R$02: 1"
    elif unidade == "3":
        return "✅ Notas de R$02: 1\n✅ Notas de R$01: 1"
    elif unidade == "4":
        return "✅ Notas de R$02: 2"
    elif unidade == "5":
        return "✅ Notas de R$05: 1"
    elif unidade == "6":
        return "✅ Notas de R$05: 1\n✅ Notas de R$01: 1"
    elif unidade == "7":
        return "✅ Notas de R$05: 1\n✅ Notas de R$02: 1"
    elif unidade == "8":
        return "✅ Notas de R$05: 1\n✅ Notas de R$02: 1\n✅ Notas de R$01: 1"
    elif unidade == "9":
        return "✅ Notas de R$05: 1\n✅ Notas de R$02: 2"
    else:
        return "❌ Sem notas de R$01, R$02 ou R$05"
    
pergunta = input("Deseja sacar dinheiro no caixa eletrônico? (sim/não) ").strip().lower()

while (pergunta != "nao") and (pergunta != "não"):
    if pergunta == "sim":
        try:
            valor = int(input("Digite o valor inteiro entre 10 e 600 reais que deseja sacar: R$").strip())
        
            if (valor >= 10)  and (valor <= 600):
                if (valor >= 100):
                    valor= str(valor)
                    print(f"💰 Valor TOTAL sacado: R${valor}\n{valorCentenas(valor[0])}\n{valorDezenas(valor[1])}\n{valorUnidades(valor[2])}")

                else:
                    valor = str(valor)
                    print(f"💰 Valor TOTAL sacado: R${valor}\n{valorDezenas(valor[0])}\n{valorUnidades(valor[1])}")
            else:
                print("Você só pode sacar um valor entre 10 e 600 reais!")
        except ValueError:
            print("Algo deu errado, você precisa digitar um valor inteiro entre 10 e 600 reais para sacar!")
    else:
        print("Você precisa digitar sim ou não!")
    
    print(100*"-")
    pergunta = input("Deseja sacar dinheiro no caixa eletrônico? (sim/não) ").strip().lower()

print("Programa finalizado!")
