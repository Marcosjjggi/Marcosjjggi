import json
from datetime import datetime

ARQUIVO_DADOS = "estudos.json"

def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"tarefas": []}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def adicionar_tarefa():
    print("\n📝 Adicionar Nova Tarefa")
    materia = input("Matéria/Assunto: ")
    descricao = input("Descrição da tarefa: ")
    prazo = input("Prazo (formato: DD/MM/AAAA): ")
    prioridade = input("Prioridade (baixa/media/alta): ").lower()

    tarefa = {
        "id": len(dados["tarefas"]) + 1,
        "materia": materia,
        "descricao": descricao,
        "prazo": prazo,
        "prioridade": prioridade,
        "concluida": False,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    dados["tarefas"].append(tarefa)
    salvar_dados(dados)
    print("✅ Tarefa cadastrada com sucesso!")

def listar_tarefas(concluidas=False):
    filtro = [t for t in dados["tarefas"] if t["concluida"] == concluidas]
    
    if not filtro:
        print("\n🔍 Nenhuma tarefa encontrada!")
        return

    status = "✅ Concluídas" if concluidas else "⏳ Pendentes"
    print(f"\n=== {status} ===")
    for t in filtro:
        print(f"\nID: {t['id']}")
        print(f"Matéria: {t['materia']}")
        print(f"Descrição: {t['descricao']}")
        print(f"Prazo: {t['prazo']} | Prioridade: {t['prioridade'].upper()}")
        print("-" * 40)

def marcar_concluida():
    listar_tarefas()
    try:
        id_tarefa = int(input("\nDigite o ID da tarefa concluída: "))
        for t in dados["tarefas"]:
            if t["id"] == id_tarefa:
                t["concluida"] = True
                salvar_dados(dados)
                print("✅ Tarefa marcada como concluída!")
                return
        print("❌ ID não encontrado!")
    except ValueError:
        print("❌ Digite um número válido!")

def menu():
    while True:
        print("\n" + "="*30)
        print("📚 GERENCIADOR DE ESTUDOS")
        print("="*30)
        print("1. Adicionar tarefa")
        print("2. Ver tarefas pendentes")
        print("3. Ver tarefas concluídas")
        print("4. Marcar como concluída")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas(False)
        elif opcao == "3":
            listar_tarefas(True)
        elif opcao == "4":
            marcar_concluida()
        elif opcao == "5":
            print("👋 Até logo! Bons estudos!")
            break
        else:
            print("❌ Opção inválida, tente novamente!")

# Iniciar o programa
if __name__ == "__main__":
    dados = carregar_dados()
    menu()
