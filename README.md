# 📦 Sistema de Controle de Estoque

Este programa tem por objetivo ajudar colaboradores da área de almoxarifado no gerenciamento dos materiais.

Sistema desktop desenvolvido em **Python**, focado em lógica backend e persistência de dados com **MySQL**.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.14
- **Interface gráfica:** CustomTkinter (avisos com CTkMessagebox)
- **Banco de Dados:** MySQL (script de criação em `data/database_schema.sql`)
- **Arquitetura:** Separação de responsabilidades em camadas (veja abaixo)

---

## 🗂️ Estrutura do Projeto

```
controle-de-estoque/
├── main.py                  # ponto de entrada: abre a tela de login
├── requirements.txt         # dependências
├── .env.exemple             # modelo do arquivo de configuração do banco
├── data/
│   └── database_schema.sql  # criação do banco e das tabelas
└── src/
    ├── database/            # conexão com o MySQL
    ├── models/              # classes que representam os dados (Usuario, Material...)
    ├── repository/          # único lugar onde o SQL é escrito
    ├── security/            # hash e conferência de senhas (bcrypt)
    ├── controller/          # validações e regras de negócio
    └── view/                # telas (login, cadastro, dashboard)
```

O caminho dos dados é sempre o mesmo: **view → controller → repository → banco**. A tela só mostra e coleta informações, o controller valida e decide, e o repository conversa com o banco.

---

## ⚙️ Como executar

**Pré-requisitos:** Python 3.14 (versão usada no desenvolvimento) e um servidor MySQL instalado e em execução.

**1. Baixe o projeto**
```bash
git clone https://github.com/jkmacedo/controle-de-estoque.git
cd controle-de-estoque
```

**2. Crie o ambiente virtual e instale as dependências**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS
pip install -r requirements.txt
```

**3. Crie o banco de dados**

Execute o arquivo `data/database_schema.sql` no seu MySQL. Ele cria o banco `almoxarifado` e as tabelas. Pelo terminal:
```bash
mysql -u seu-usuario -p < data/database_schema.sql
```

**4. Configure o acesso ao banco**

Copie o arquivo `.env.exemple` para `.env` e preencha com os seus dados:
```
DB_HOST=localhost
DB_USER=seu-usuario
DB_PORT=3306
DB_PASSWORD=sua_senha
DB_NOME=almoxarifado
```
O arquivo `.env` guarda a senha do banco e **não é enviado ao GitHub** (já está no `.gitignore`).

> **Já tinha usuários cadastrados antes do hash de senhas?** As senhas deles estão em texto puro e não funcionam mais no login. Converta-as uma única vez com `python -m scripts.migrar_senhas` (faça um backup antes) ou cadastre os usuários de novo.

**5. Execute**
```bash
python main.py
```
Rode sempre a partir da pasta raiz do projeto.

---

## 🚀 Primeiros passos

1. Na tela de login, clique em **"Não tem cadastro? Cadastre-se aqui"**.
2. Preencha o cadastro seguindo as regras:
   - **Nome:** apenas letras
   - **E-mail:** apenas letras e números antes do domínio, que é escolhido na lista
   - **Matrícula:** exatamente 9 números
   - **Telefone:** 11 números (DDD + número), sem espaços ou traços
   - **Senha:** de 8 a 72 caracteres, sem espaços. O banco guarda apenas o hash da senha (bcrypt), nunca a senha digitada
3. Matrícula, e-mail e telefone não podem estar repetidos.

**Cadastrando materiais:** por enquanto ainda não existe tela para isso, então os materiais são inseridos direto no banco. Exemplo:
```sql
USE almoxarifado;

INSERT INTO categoria (nome_categoria) VALUES ('Ferramentas');

INSERT INTO material (nome_produto, quantidade, endereçamento, id_categoria)
VALUES ('Luva de segurança', 25, 'A-01', 1);
```

**Abrindo só o dashboard (para desenvolvimento):** como o login ainda não abre o dashboard, é possível vê-lo diretamente:
```bash
python -m src.view.dashboard_estoque
```

---

## ✨ Funcionalidades

**Já funcionam**
- Login por matrícula e senha
- Cadastro de usuários com validação dos dados
- Dashboard com total de itens cadastrados, retiradas do dia e alerta de estoque baixo (itens com menos de 10 unidades)
- Tabela de materiais com pesquisa por nome ou categoria
- Dar baixa e adicionar ao estoque (a baixa não deixa a quantidade ficar negativa e fica registrada na tabela de saídas)

**Em desenvolvimento**
- Abrir o dashboard após o login (hoje o login apenas valida os dados)
- Cadastrar novo item, editar e excluir (os botões já existem na tela, mas ainda não têm ação)

---

## 📌 Status do Projeto
🚧 **Em construção** 🚧
