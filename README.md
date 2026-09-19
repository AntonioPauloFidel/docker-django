# 🐳 Django Docker Multi-Container Stack

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

Arquitetura multi-container robusta e pronta para produção utilizando **Django (Gunicorn)**, **Nginx** como Proxy Reverso e **PostgreSQL** para persistência de dados.

---

## 🛠️ Arquitetura do Sistema

| Serviço | Tecnologia | Porta Host | Porta Container | Descrição |
| :--- | :--- | :---: | :---: | :--- |
| **`nginx`** | Nginx | `8888` | `80` | Proxy Reverso e servidor direto de arquivos estáticos/mídia |
| **`web`** | Django + Gunicorn | - | `8000` | Aplicação Backend WSGI |
| **`db`** | PostgreSQL 15 | `5432` | `5432` | Banco de Dados Relacional |

---

## 🚀 Como Executar o Projeto

### 1. Subir os Containers
Suba toda a pilha de serviços em segundo plano:
```bash
docker compose up -d --build
