import time

class Agenda():
    
    def __init__(self):
        self.__contacts = []
        self.opc = 0
        self.data = time.localtime()
        self.day = (f'{self.data[2]}/{self.data[1]}/{self.data[0]}')
        
    @property
    def accessAgenda(self):
        return self.__contacts
    
    @accessAgenda.setter
    def addContact(self, x):
        self.__contacts.append(x)
    
    def viewAgenda(self):
        if len(agenda.accessAgenda) == 0:
            print('Você ainda não adicionou contatos a sua agenda')
            time.sleep(0.5)
            print('Retornando ao menu principal...')
            time.sleep(1)
                    
        else:                    
            cont = 1
            for i in agenda.accessAgenda:
                print(f'Contato {cont}')
                time.sleep(1)
                print(i)      
                cont += 1
                time.sleep(1)
                time.sleep(1)
    
    def add(self):
        a = str(input('Digite o nome: '))
        b = str(input('Digite o telefone: '))
        c = str(input('Digite o e-mail: '))
        for i in agenda.accessAgenda:
            if c in i['Nome'] or c in i['Telefone'] or c in i['Email']:
                print('E-mail conflita com o de outro contato salvo! Retornando ao menu...')
                time.sleep(1)
                return
        newContact = dict(Nome = a, Telefone = b, Email = c, Criado_dia = self.day)
        agenda.addContact = newContact        
        print('Contato adicionado!')
        time.sleep(0.5)
        
    def search(self):
        x = str(input('Digite algum dado do contato: '))
        for i in agenda.accessAgenda:
            if x in i['Nome'] or x in i['Telefone'] or x in i['Email']:
                print('Resultado encontrado!')
                time.sleep(1)
                print(i)
                time.sleep(2)
                return
        print('Não foi possível encontrar, confira seus contatos\nRetornando ao menu!')
        time.sleep(1)
    
    def updateContact(self):
        if len(agenda.accessAgenda) == 0:
            print('Não há contatos para alterar')
            time.sleep(1)
            return
        agenda.viewAgenda
        try:
            x = int(input('Digite o número do contato que deseja alterar: '))
            agenda.accessAgenda.pop((x-1))
            a = str(input('Digite o novo nome: '))
            b = str(input('Digite o novo telefone: '))
            c = str(input('Digite o novo e-mail: '))
            for i in agenda.accessAgenda:
                if c in i['Nome'] or c in i['Telefone'] or c in i['Email']:
                    print('E-mail conflita com o de outro contato salvo! Retornando ao menu...')
                    time.sleep(1)
                    return
            newContact = dict(Nome = a, Telefone = b, Email = c, Criado_dia = self.day)
            agenda.addContact = newContact
            print('Contato atualizado!')
            time.sleep(1)
        except Exception:
            print('Digite o número correspondente ao contato!Retornando ao menu...')
    
    def deleteContact(self):
        if len(agenda.accessAgenda) == 0:
            print('Não há contatos para deletar')
            time.sleep(1)
            return
        agenda.viewAgenda()
        try:
            x = int(input('Digite o número do contato que deseja excluir: '))
            agenda.accessAgenda.pop((x-1))
            print('Contato deletado!')
            time.sleep(1)
        except Exception:
            print('Digite o número correspondente ao contato!Retornando ao menu...')

    def menu(self):
        try:
            print('###Menu Principal###\n1 - Ver contatos\n2 - Consultar contato\n3 - Adicionar contato\n4 - Alterar contato\n5 - Excluir contato\n6 - Sair')
            self.opc = int(input('Digite uma opção: '))
            return self.opc
        except Exception:
            print('Erro! Digite a opção corretamente!')
            time.sleep(1)
            
    def main(self):
        print(f'Data de hoje: {self.day}')
        while self.opc != 6:
    
            self.opc = self.menu()
            
            if self.opc == 1:
                agenda.viewAgenda()
        
            elif self.opc == 2:
                agenda.search()
                
            elif self.opc == 3:
                agenda.add()
                
            elif self.opc == 4:
                agenda.updateContact()
            
            elif self.opc == 5:
                agenda.deleteContact()
                
            elif self.opc == 6:
                print('Fechando agenda!')
                time.sleep(0.5)
                print('Até mais!')
            else:
                print('Opção não encontrada!')
        
agenda = Agenda()
agenda.main()