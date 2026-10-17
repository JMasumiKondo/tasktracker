def cadastrar_tarefa(tarefas):
    print("\n--- Cadastro de Nova Tarefa ---")
    
    while True:
        titulo = input("Digite o titulo da tarefa (obrigatorio): ").strip()
        if titulo:
            break
        print("Erro: O titulo da tarefa nao pode estar vazio. Tente novamente.")
        
    descricao = input("Digite a descricao detalhada da tarefa: ").strip()
    
    while True:
        prioridade = input("Digite a prioridade (Alta, Media ou Baixa): ").strip().capitalize()
        if prioridade in ["Alta", "Media", "Baixa"]:
            break
        print("Erro: Prioridade invalida! Escolha estritamente entre 'Alta', 'Media' ou 'Baixa'.")
        
    data_limite = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()
    
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    tarefas.append(tarefa)
    print("Tarefa salva com sucesso!")

def visualizar_tarefas(tarefas):
    print("\n--- Lista de Tarefas ---")
    
    if not tarefas:
        print("Aviso: Nao existem tarefas cadastradas no momento.")
        return
    
    total_pendentes = sum(1 for t in tarefas if t["status"] == "Pendente")
    
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {i}:")
        print(f"  - Titulo: {tarefa['titulo']}")
        print(f"  - Descricao: {tarefa['descricao'] if tarefa['descricao'] else 'Nenhuma descricao informada'}")
        print(f"  - Prioridade: {tarefa['prioridade']}")
        print(f"  - Data Limite: {tarefa['data_limite'] if tarefa['data_limite'] else 'Nao informada'}")
        print(f"  - Status: {tarefa['status']}")
        
    print(f"\nTotal de tarefas cadastradas: {len(tarefas)}")
    print(f"Tarefas Pendentes: {total_pendentes}")

def editar_tarefa(tarefas):
    print("\n--- Editar Tarefa ---")
    if not tarefas:
        print("Aviso: Nao existem tarefas para editar.")
        return
    
    visualizar_tarefas(tarefas)
    
    try:
        indice = int(input("\nDigite o numero da tarefa que deseja editar: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa = tarefas[indice]
            print(f"Editando a tarefa: {tarefa['titulo']}")
            
            novo_titulo = input(f"Novo titulo [{tarefa['titulo']}]: ").strip()
            if novo_titulo:
                tarefa['titulo'] = novo_titulo
                
            nova_desc = input(f"Nova descricao [{tarefa['descricao']}]: ").strip()
            if nova_desc:
                tarefa['descricao'] = nova_desc
                
            while True:
                nova_prio = input(f"Nova prioridade (Alta, Media, Baixa) [{tarefa['prioridade']}]: ").strip().capitalize()
                if not nova_prio:
                    break
                if nova_prio in ["Alta", "Media", "Baixa"]:
                    tarefa['prioridade'] = nova_prio
                    break
                print("Erro: Prioridade invalida!")
                
            nova_data = input(f"Nova data limite [{tarefa['data_limite']}]: ").strip()
            if nova_data:
                tarefa['data_limite'] = nova_data
                
            novo_status = input(f"Novo status (Pendente / Concluida) [{tarefa['status']}]: ").strip().capitalize()
            if novo_status in ["Pendente", "Concluida"]:
                tarefa['status'] = novo_status
                
            print("Tarefa atualizada com sucesso!")
        else:
            print("Erro: Numero de tarefa invalido.")
    except ValueError:
        print("Erro: Por favor, digite um numero valido.")

def apagar_tarefa(tarefas):
    print("\n--- Apagar Tarefa ---")
    if not tarefas:
        print("Aviso: Nao existem tarefas para apagar.")
        return
    
    visualizar_tarefas(tarefas)
    
    try:
        indice = int(input("\nDigite o numero da tarefa que deseja apagar: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida['titulo']}' apagada com sucesso!")
        else:
            print("Erro: Numero de tarefa invalido.")
    except ValueError:
        print("Erro: Por favor, digite um numero valido.")

def main():
    tarefas = []
    while True:
        print("\n==============================")
        print("     TASKTRACKER - MENU")
        print("==============================")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Editar tarefa")
        print("4. Apagar tarefa")
        print("5. Sair da aplicacao")
        
        opcao = input("Escolha uma opcao (1-5): ").strip()
        
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            editar_tarefa(tarefas)
        elif opcao == "4":
            apagar_tarefa(tarefas)
        elif opcao == "5":
            print("A sair da aplicacao. Ate breve!")
            break
        else:
            print("Erro: Opcao invalida! Escolha entre 1 e 5.")

if __name__ == "__main__":
    main()