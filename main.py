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