# oPaladar

O **oPaladar** é uma aplicação web desenvolvida em **Django** com foco em avaliação e descoberta de restaurantes.  
O projeto foi criado como prática e consolidação dos conhecimentos aprendidos em curso, reunindo backend, frontend, autenticação de usuários e organização de arquivos estáticos.

## Sobre o projeto

A proposta do oPaladar é oferecer uma experiência visual agradável para que usuários possam acessar a plataforma, criar conta, fazer login e navegar por páginas como painel principal e seção “Sobre nós”.

Atualmente, o projeto possui:

- Página inicial
- Cadastro de usuários
- Login e logout
- Dashboard do usuário
- Página “Sobre nós”
- Estilização separada em arquivos CSS
- Estrutura organizada com Django

## Tecnologias utilizadas

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **SQLite3**

## Estrutura do projeto

```bash
oPaladar/
├── core/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── opaladar_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── dashboard.css
│   ├── home.css
│   ├── perfil.css
│   ├── sobre.css
│   ├── logo 2.png
│   └── logo.ico
├── templates/
│   ├── dashboard.html
│   ├── home.html
│   └── sobre.html
├── manage.py
└── .gitignore

## Como executar e testar o projeto

Siga este passo a passo para rodar o projeto localmente no seu computador.

### 1. Clonar o repositório

```bash
git clone https://github.com/iamkalashnikov/oPaladar.git

2. Entrar na pasta do projeto
cd oPaladar
3. Criar o ambiente virtual
Windows
python -m venv venv
Linux/macOS
python3 -m venv venv
4. Ativar o ambiente virtual
Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
5. Instalar o Django
pip install django
6. Criar as migrações do projeto
python manage.py makemigrations
7. Aplicar as migrações no banco de dados
python manage.py migrate
8. Criar um superusuário (opcional, para acessar o admin)
python manage.py createsuperuser
9. Iniciar o servidor
python manage.py runserver
10. Acessar o projeto no navegador

Abra o navegador e entre em:

http://127.0.0.1:8000/


