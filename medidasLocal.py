from classRetangulo import *


def calculorodape(x, y):
    return x - y * 0.8 + (10 / 100)


# Variáveis recebendo os valores do usuário
comprimento = float(input('Insira o comprimento: '))
largura = float(input('Insira a largura: '))

# Instanciando um objeto
chao = Retangulo(comprimento, largura)

# Variáveis de calculo
area = chao.calculoArea()
qtd_piso = area * 4  # Levando em conta pisos de tamanho 50x50. 1m² equivale a 4 pisos de 50x50
qtd_rodape = calculorodape(area, 1)

print(f'Área = {chao.calculoArea()}m²\n'
      f'Serã necessários {qtd_piso} pisos e {qtd_rodape}m de material para o rodapé')

'''Na função calculorodape() utilizei 0,8m(80cm) para representar o tamanho vão de porta do ambiente e
o y returna a quantidade de vãos
presente no ambiente do usuário. Os 10% equivalem a cortes e rodapés extras.'''
