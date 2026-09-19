Projeto Django com Docker, Nginx e PostgreSQL
Arquitetura multi-contentor containerizada composta por Django (executado via Gunicorn), Nginx atuando como proxy reverso e PostgreSQL como banco de dados relacional.

🛠️ Arquitetura do Sistema
db: Banco de dados PostgreSQL 15.

web: Aplicação Django executada através do servidor Gunicorn na porta interna 8000.

nginx: Proxy reverso escutando na porta 8888 e servindo arquivos estáticos e de mídia diretamente.

🚀 Como Executar
1. Iniciar os contentores
Bash
docker compose up -d --build
2. Executar as migrações do banco de dados
Bash
docker exec -it docker-django-web-1 python manage.py migrate
3. Coletar os arquivos estáticos (CSS/JS)
Bash
docker exec -it docker-django-web-1 python manage.py collectstatic --noinput
4. Criar um utilizador administrador
Bash
docker exec -it docker-django-web-1 python manage.py createsuperuser
🔗 Rotas e Acesso
Painel de Administração: http://localhost:8888/admin/

💾 Volumes e Persistência
postgres_data: Armazena os dados do banco PostgreSQL de forma persistente.

arquivos_volume: Armazena os ficheiros enviados por upload (/app/.arquivos).

static_volume: Compartilha os arquivos estáticos compilados entre o Django e o Nginx (/app/static).

🛑 Parar os Serviços
Bash
docker compose down