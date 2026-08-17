# CrochêGest

Sistema web desenvolvido para gerenciamento de clientes e encomendas de uma artesã.

## Sobre o projeto

O CrochêGest foi desenvolvido com o objetivo de facilitar a organização de clientes e encomendas, centralizando as informações em um único sistema.

A aplicação permite cadastrar clientes e gerenciar encomendas, acompanhando informações importantes como produto, cor, datas, valor e status do pedido.

## Funcionalidades

- Cadastro de clientes
- Edição de clientes
- Exclusão de clientes
- Listagem de clientes
- Cadastro de encomendas
- Edição de encomendas
- Exclusão de encomendas
- Listagem de encomendas
- Controle de status das encomendas
- Registro de informações da encomenda

## Tecnologias

- Python
- Django
- HTML
- CSS
- SQLite

## strutura do projeto

```text
CrochêGest/
├── config/
├── encomendas/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
├── templates/
├── manage.py
├── db.sqlite3
└── README.md
```
## Como executar
1. Clone o repositório
```bash
git clone https://github.com/IsaClara/crochegest.git
```
3. Entre na pasta
```bash
cd crochegest
```
5. Crie um ambiente virtual
```bash
python -m venv venv
```
7. Ative o ambiente virtual
```bash
venv\Scripts\activate
```
9. Instale dependências
```bash
pip install -r requirements.txt
```
11. Execute as migrações
```bash
python manage.py migrate
```
13. Inicie o servidor
```bash
http://127.0.0.1:8000/
```
## Aprendizado
O desenvolvimento do CrochêGest permitiu praticar conceitos de desenvolvimento web utilizando Django, incluindo:
- Criação de modelos
- Operações CRUD
- Desenvolvimento de views
- Configuração de URLs
- Utilização de templates Django
- Organização de arquivos estáticos
- Persistência de dados com SQLite
- Estruturação de uma aplicação web
## Autora
Isa Clara Siqueira

Estudante de Análise e Desenvolvimento de Sistemas.

GitHub: [Isa Clara](https://github.com/IsaClara)

LinkedIn: [Isa Clara](www.linkedin.com/in/isaclarasiqueira)