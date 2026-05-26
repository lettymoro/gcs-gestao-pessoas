# Tutorial Técnico  
## Sistema de Gestão de Pessoas

**Repositório:** https://github.com/lettymoro/gcs-gestao-pessoas.git  
**Linguagem:** Python  
**Objetivo:** Demonstrar a reprodução, execução e evolução controlada do projeto utilizando Git e GitHub.

---

## 1. Preparação do ambiente

Para reproduzir o projeto, é necessário ter acesso a um computador com terminal e conexão com a internet.

O projeto não utiliza:

- banco de dados;
- frameworks web;
- interface gráfica;
- bibliotecas externas.

A aplicação é executada diretamente no terminal usando Python.

---

## 2. Instalação das ferramentas utilizadas

As ferramentas utilizadas foram:

- Python 3;
- Git;
- Visual Studio Code ou outro editor de código.

Verifique se o Python está instalado:

```bash
python --version
```

Ou:

```bash
python3 --version
```

Verifique se o Git está instalado:

```bash
git --version
```

## 3. Criação do repositório

O projeto foi versionado com Git e hospedado no GitHub.

Para reproduzir o projeto em outra máquina, clone o repositório:

```bash
git clone https://github.com/lettymoro/gcs-gestao-pessoas.git
```

Depois, acesse a pasta do projeto:

```bash
cd gcs-gestao-pessoas
```

Verifique o repositório remoto:

```bash
git remote -v
```
## 4. Estrutura inicial do projeto

A estrutura do projeto é:

```bash
gcs-gestao-pessoas/
│
├── .gitignore
├── README.md
└── main.py
```

Descrição dos arquivos:

| Arquivo      | Descrição                             |
| ------------ | ------------------------------------- |
| `.gitignore` | Define arquivos ignorados pelo Git.   |
| `README.md`  | Contém informações gerais do projeto. |
| `main.py`    | Arquivo principal da aplicação.       |

## 5. Criação de branches

O projeto foi organizado em branches para separar o desenvolvimento de cada funcionalidade.

Branches utilizadas:

```bash
main
feature-cadastro
feature-listagem
feature-busca
feature-atualizacao
feature-remocao
```

Para visualizar as branches:

```bash
git branch -a
```

Exemplo de criação de branch:

```bash
git checkout -b feature-cadastro
```

Após implementar uma funcionalidade, as alterações foram registradas com commit:

```bash
git add .
git commit -m "Adiciona funcionalidade de cadastro"
```

## 6. Processo de merge

Depois do desenvolvimento em cada branch, as funcionalidades foram integradas à branch principal main.

Exemplo de merge:

```bash
git checkout main
git merge feature-cadastro
```

O mesmo processo foi realizado para as demais branches:

```bash
git merge feature-listagem
git merge feature-busca
git merge feature-atualizacao
git merge feature-remocao
```

Para visualizar o histórico evolutivo do projeto:

```bash
git log --oneline --graph --decorate --all
```

Esse comando mostra commits, branches, merges e tags, permitindo acompanhar a evolução do sistema.

## 7. Definição das baselines

As baselines foram definidas usando tags do Git.

Tags utilizadas:

v1.0
v2.0

Para visualizar as baselines:

```bash
git tag
```

Para ver detalhes de uma baseline:

```bash
git show v1.0
git show v2.0
```

Descrição das baselines:

| Baseline | Descrição                                                  |
| -------- | ---------------------------------------------------------- |
| `v1.0`   | Versão intermediária do projeto.                           |
| `v2.0`   | Versão final com as funcionalidades principais integradas. |

## 8. Execução da aplicação

Após clonar o repositório, acesse a pasta do projeto:

```bash
cd gcs-gestao-pessoas
```

Execute a aplicação:

```bash
python main.py
```

Ou:

```bash
python3 main.py
```

Tela inicial esperada:

```bash
--- Sistema de Gestão de Pessoas ---
1. Cadastrar pessoa
2. Listar pessoas
3. Buscar pessoa
4. Atualizar pessoa
5. Remover pessoa
6. Sair
Escolha uma opção:
```

## 9. Explicação resumida das funcionalidades implementadas
Cadastro de pessoas

Permite cadastrar uma pessoa informando seu nome. Os dados são armazenados em uma lista em memória.

Listagem de pessoas

Exibe todas as pessoas cadastradas, mostrando o índice e o nome de cada uma.

Busca de pessoas

Permite buscar uma pessoa pelo nome ou parte do nome, sem diferenciar letras maiúsculas e minúsculas.

Atualização de pessoas

Permite alterar o nome de uma pessoa cadastrada a partir do índice exibido na listagem.

Remoção de pessoas

Permite remover uma pessoa cadastrada a partir do índice informado pelo usuário.

Menu principal

Permite navegar entre as funcionalidades do sistema até que o usuário escolha a opção de sair.
