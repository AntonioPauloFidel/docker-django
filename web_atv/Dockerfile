FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema para o Postgres
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala requisitos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . /app/

EXPOSE 8000

# Executa o Gunicorn apontando para a sua pasta real 'aula_19_09'
CMD ["gunicorn", "aula_19_09.wsgi:application", "--bind", "0.0.0.0:8000"]