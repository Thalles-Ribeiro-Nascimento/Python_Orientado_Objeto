class Tv:
    def __init__(self, ligar, volume=0, canal=0):
        self.ligar = ligar
        self.volume = volume
        self.canal = canal

    def mudarCanal(self, novo_canal):
        if self.ligar == 'Ligar' or self.ligar == 'ligar':
            if 0 <= self.canal <= 50 and 0 <= novo_canal <= 50:
                self.canal = novo_canal
                print(f"Canal: {self.canal:.1f}")
            else:
                print(f'O canal {novo_canal:.1f} não existe!')
        else:
            print('Não é possível mudar de canal com a tv desligada')

    def aumentarDiminuir(self, volume):
        if self.ligar == 'Ligar' or self.ligar == 'ligar':
            if 0 <= self.volume <= 100 and 0 <= volume <= 100:
                self.volume = self.volume + volume
                print(f'Volume: {self.volume:.0f}')
            else:
                print('Não é possível aumentar ou diminuir!')
        else:
            print('Não é possível aumentar ou diminuir o volume com a tv desligada')


tv = Tv('Ligar')
tv.aumentarDiminuir(25)
tv.mudarCanal(64)
