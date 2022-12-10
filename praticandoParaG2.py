#TestG2 
import time

class Bank():
    
    def __init__(self):
        self.__currency = 250.0
        self.user = {
            'Fernandinho' : '7412-6'
            }
        self.transitions = []
        self.__drawLimit = 150.0
    
    def inputer(self):
        try:
            x = float(input('Digite o valor: '))
            return x
        except Exception:
            print('Erro! Tente novamente!')
            return self.inputer()
    
    def menu(self):
        try:
            print('###Menu Principal###\n1 - Ver perfil e histórico\n2 - Sacar\n3 - Depositar\n4 - Alterar Limite\n5 - Alterar perfil\n6 - Sair')
            opc = int(input('Digite uma opção: '))
            return opc
        except Exception:
            print('Erro! Digite a opção corretamente!')
    
    @property
    def money(self):
        return self.__currency
    
    @money.setter
    def draw(self, x):
        self.__currency -= x

    @money.setter
    def deposit(self, x):
        self.__currency += x
    
    @property
    def limit(self):
        return self.__drawLimit
    
    @limit.setter
    def setLimit(self, x):
        self.__drawLimit = x
        
main = Bank()
opc = 0

while opc != 6:
    
    opc = main.menu()
    
    if opc == 1:
        print(f'Usuário: {main.user.keys()}')
        print(f'Conta: {main.user.values()}')
        print(f'Saldo: R$ {main.money}')
        print(f'Limite de saque: R$ {main.limit}')
        y = len(main.transitions)
        if y != 0:
            time.sleep(1)
            print('Histórico:')
            for i in range(0,y):
                time.sleep(1)
                print(main.transitions[i])
            print('Fim!')
        time.sleep(1)
        
    elif opc == 2:
        value = main.inputer()
        if main.limit >= main.money and value <= main.money:
            main.draw = value
            main.transitions.append(f'Sacado: R$ {value}')
            print('Operação realizada com sucesso!')
            time.sleep(1)
        else:
            print('Saque cancelado! Confira seu saldo e limite.')
            time.sleep(1)
        
    elif opc == 3:
        value = main.inputer()
        main.deposit = value
        main.transitions.append(f'Depositado: R$ {value}')
        print('Operação realizada com sucesso!')
        time.sleep(1)
        
    elif opc == 4:
        value = main.inputer()
        main.setLimit = value
        print('Operação realizada com sucesso!')
        time.sleep(1)

    elif opc == 5:
        print('Inoperante!')
        
    elif opc == 6:
        print('Operações finalizadas\nAté mais!')