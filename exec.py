
def retornar_numero_primo_divisivel(numero_a_ser_fatorado):
    numeros_primos = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
        67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137
        ] 
    resultado_fatorados_e_primos = {}
    n = 0

    while True:
        '''
            Sequencia:
            1º- testa se o 'numero_a_ser_fatorado' pode ser dividido por um numero primo
            2º- atribui o resultado da divisão pelo primo na variavel 'numero_dividido_por_primo' 
            3º- adiciona o numero dividido e o primo em um dicionario 
            4º- atribui o resultado da divisão na variavel 'numero_a_ser_fatorado'
            5º- caso o numero_a_ser_fatorado seja 1 quer dizer que não tem mais como dividir, então ele finaliza
        '''

        if numero_a_ser_fatorado % numeros_primos[n] == 0: #1º
            
            numero_dividido_por_primo = numero_a_ser_fatorado // numeros_primos[n] #2º
            resultado_fatorados_e_primos[numero_a_ser_fatorado] = numeros_primos[n] #3º
            numero_a_ser_fatorado = numero_dividido_por_primo #4º

        elif numero_a_ser_fatorado == 1: #5º
            break

        else:
            n += 1

    return resultado_fatorados_e_primos

def print_cmd(result):
    for fatorados, primos in result.items():
        print(str(fatorados) + ' | ' + str(primos))

    print(
        '''
        ---------------
        1# fatorar outro numero
        2# mostrar apenas os primos
        3# exit
        '''
        )
    
    escolha = int(input('Escolha: '))
    
    if escolha == 1:
        init()
    
    elif escolha == 2:
        apenas_primos = []
        
        for primos in result.values():
            apenas_primos.append(primos)

        print(apenas_primos)
        init()

def init():
    numero_a_ser_fatorado = int(input('Digite o numero a ser fatorado: '))
    result = retornar_numero_primo_divisivel(numero_a_ser_fatorado)
    print_cmd(result)

init()