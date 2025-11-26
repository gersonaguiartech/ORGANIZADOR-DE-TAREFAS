def checar_tarefas(self):
    #CHECAGEM DAS TAREFAS JÁ LISTADAS
        if not self.tarefas:
            print('Não há tarefas listadas.')
        else:
            print('\n--- Lista de Tarefas ---')
            for index, tarefa in enumerate(self.tarefas, start=1):
                status = 'concluido' if tarefa['concluida'] else 'pendente'
                print(f'{index} - ({status}): {tarefa['nome']} ')
            print('-------------------------')

def concluir_tarefa(self):
        #CONCLUIR TAREFA
        self.checar_tarefas()
        if not self.tarefas:
            return
        try:
            escolha = int(input('\nDigite o número da tarefa a concluir: ')) - 1
            if 0 <= escolha < len (self.tarefas):
                if self.tarefas[escolha]['concluida']:
                    print(f'\nTarefa {self.tarefas[escolha]['nome']} já está concluida') 
                else :
                    self.tarefas[escolha]['concluida'] = True
                    print(f'\nTarefa "{self.tarefas[escolha]['nome']}" marcada como concluída.')
            else:
                print('\n O numero da tarefa está inválido')
        except ValueError:
            print('\nErro: número inválido!')
            
def editar_tarefas(self):
    #FUNCAO EDITAR TAREFAS
        self.checar_tarefas()
        if not self.tarefas:
            print('\nNão há tarefas listadas')
            return
        try:
            num_tarefa = int(input("Digite o numero da tarefa que deseja EDITAR: ")) -1
            if 0 <= num_tarefa <= len(self.tarefas):
                nova_tarefa = input(f'Nova descrição para "{self.tarefas[num_tarefa]['nome']}": ').strip()
                if nova_tarefa:
                    self.tarefas[num_tarefa]['nome'] = nova_tarefa
                    print('\nTarefa editada com sucesso.')
                else:
                    print('\nEdição cancelada (entrada vazia).')
            else:
                print('\n O numero da tarefa está inválide')
        except ValueError:
            print("entrada invalida. digite um numero")

def remover_tarefas(self):
        #REMOVENDO TAREFA UTILIZANDO O .POP
    self.checar_tarefas()
    if not self.checar_tarefas:
        return
    try:
        num_tarefa = int (input(f'Digite o numero da tarefa que deseja REMOVER: ')) -1
        if 0 <= num_tarefa <= len(self.tarefas):
            remover_tarefa = self.tarefas.pop(num_tarefa)
            print(f'Tarefa {remover_tarefa['nome']} foi removida com sucesso!!')
        else:
            print('\nNumero da tarefa incorreto.')
    except ValueError:
        print("entrada invalida. digite um numero")
