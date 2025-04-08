# Função para ler dois valores inteiros
def ler_valores():
    while True:
            a = int(input("Digite o primeiro valor inteiro: "))
            b = int(input("Digite o segundo valor inteiro (maior que o primeiro): "))
            if b > a:
                return a, b
            else:
                print("O segundo valor deve ser maior que o primeiro. Tente novamente.")
    # seu código que pode gerar um ValueError
            exceptValueError:0
            
            print("Por favor, insira apenas números inteiros.")
# Função para calcular a soma dos inteiros entre os dois valores
def calcular_soma(a, b):
    return sum(range(a, b + 1))

# Programa principal
def main():
    a, b = ler_valores()
    soma = calcular_soma(a, b)
    print(f"A soma dos inteiros entre {a} e {b} (inclusive) é: {soma}")

# Executa o programa
if __name__ == "__main__":
    main()