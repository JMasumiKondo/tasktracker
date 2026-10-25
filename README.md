# TaskTracker - Gestão Modular de Tarefas

> **Bootcamp II - Fase 3: Entrega Final (Conteinerização e Orquestração)**  
> **Curso:** Bacharelado em Ciência da Computação  
> **Autor:** Júlio Masumi Kondo  

---

## 📌 Descrição do Projeto
O **TaskTracker** é uma aplicação em linha de comando (CLI) desenvolvida em Python para centralizar e organizar tarefas diárias. O sistema permite o cadastro de pendências com validação estrita de dados, atualizar os dados ou o status de uma tarefa existente, remover permanentemente uma tarefa da lista com base no seu número, e a visualização clara de tarefas gravadas, garantindo o controlo de prioridades e datas limite. Nesta etapa final, a aplicação foi totalmente empacotada e isolada através de conteinerização[cite: 19, 21].

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x[cite: 24]
- **Conteinerização:** Docker[cite: 21]
- **Orquestração:** Docker Compose[cite: 25, 26]
- **Controlo de Versão:** Git / GitHub[cite: 7]

---

## 🐳 Como Executar via Docker

1. **Como construir a imagem:**
   ```bash
   docker build -t tasktracker .
   ```[cite: 27]

2. **Como rodar o container em modo isolado:**
   ```bash
   docker run -it tasktracker
   ```[cite: 27]

3. **Como rodar via orquestração (Recomendado):**
   ```bash
   docker compose run tasktracker
   ```[cite: 27]

---

## 📁 Estrutura do Repositório
```text
tasktracker/
├── README.md                   # Documentação e instruções do projeto[cite: 23]
├── .gitignore                  # Ficheiros ignorados pelo Git[cite: 23]
├── Dockerfile                  # Configuração para a imagem da aplicação[cite: 22, 23]
├── docker-compose.yml          # Orquestração para o terminal interativo (CLI)[cite: 22, 25, 23]
├── docs/
│   └── planejamento_logico.pdf # Planeamento lógico e arquitetural (Fase 1)[cite: 23]
└── src/
    └── main.py                 # Código-fonte principal da aplicação[cite: 23]