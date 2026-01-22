# SisEventos

Sistema web para gerenciamento de eventos, desenvolvido com **Django**, com foco em autenticação de usuários, controle de permissões e operações CRUD.

Projeto desenvolvido para fins **acadêmicos**, visando consolidar conhecimentos em backend, arquitetura MVC (MTV no Django) e boas práticas de desenvolvimento web.

---

## 📌 Descrição do Projeto

O **SisEventos** é um sistema que permite o gerenciamento de eventos por administradores e a inscrição de usuários nesses eventos.

O sistema diferencia **usuários comuns** e **administradores**, garantindo controle de acesso adequado às funcionalidades sensíveis, como criação e gerenciamento de eventos.

---

## ⚙️ Funcionalidades

### 👤 Usuário Comum
- Cadastro de usuário
- Login e logout
- Visualização de eventos disponíveis
- Inscrição em eventos
- Cancelamento de inscrição
- Visualização dos eventos em que está inscrito

### 👑 Administrador (Superuser)
- Cadastro de eventos
- Edição de eventos
- Exclusão de eventos
- Encerramento de eventos
- Visualização dos inscritos por evento
- Acesso ao painel administrativo do Django (`/admin`)

---

## 🔐 Controle de Usuários e Permissões

O sistema utiliza o **sistema de autenticação padrão do Django** (`django.contrib.auth`).

### Usuário comum
- Criado através da tela de cadastro do sistema
- Possui acesso apenas às funcionalidades básicas
- Não tem acesso ao painel administrativo

### Administrador (Superuser)
- Criado via terminal utilizando o comando:
```bash
python manage.py createsuperuser
```
Possui acesso total ao sistema

Pode acessar o painel administrativo do Django

Pode gerenciar eventos e visualizar inscritos

A distinção entre usuários é feita através das permissões is_staff e is_superuser.

---

### 🛠️ Tecnologias Utilizadas

- Python 3
- Django
- Bootstrap 5 (interface)
- HTML5
- SQLite (banco de dados em ambiente de desenvolvimento)

---

### ▶️ Como Executar o Projeto Localmente
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/siseventos.git
cd siseventos
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
```
3. Instale as dependências:
```bash
pip install django
```

4. Execute ass migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário (para controle admnistrativo do sistema de eventos):
```bash
python manage.py createsuperuser
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

7. Acesse o sistema no navegador:
- Aplicação:
http://127.0.0.1:8000/

- Painel administrativo:
http://127.0.0.1:8000/admin/

---

## DER do Sistema de Eventos
![teste](assets/DER_sistema_de_eventos.png)