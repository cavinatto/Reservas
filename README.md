# 🏫 API de Reserva de Salas

Este repositório contém a **API de Reserva de Salas**, desenvolvida com **Flask**, **SQLAlchemy** e **SQLite**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Reserva de Salas é um **microsserviço** que integra o sistema principal de gerenciamento escolar, sendo responsável exclusivamente pelas **reservas de salas para turmas**.

⚠️ **Esta API depende da API principal de gerenciamento escolar**, que deve estar em execução localmente. A comunicação entre os serviços ocorre via **requisições REST HTTP**, especialmente para verificar:

- Se a **Turma** existe (`GET /api/turmas/<id>`)

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- Docker
- Requests (para requisições entre microsserviços)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone -b Reserva https://github.com/cavinatto/API-SchoolSystem.git 
cd API-SchoolSystem/API_reservas
```

### 2. Crie a pasta `instance/` na raiz do projeto (caso não exista)

```bash
mkdir instance
```

Ela armazenará o arquivo do banco `reservas.db`.

---

### 3. Executar com Docker

```bash
docker build -t api_reserva .
docker run -d -p 5001:5001 api-reserva
```

### 4. Executar localmente sem Docker

#### 4.1. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4.2. Execute a API

```bash
python app.py
```

📍 A aplicação estará disponível em: `http://127.0.0.1:5001` (ou em local host dependendo da sua execução)

---

## 📡 Endpoints da API

- `GET /reservas` – Lista todas as reservas
- `POST /reservas` – Cria uma nova reserva

### 📥 Exemplo de requisição POST:

```json
{
  "turma_id": 1,
  "sala": "Sala 101",
  "data": "2025-05-25",
  "hora_inicio": "08:00",
  "hora_fim": "10:00"
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API principal** esteja rodando em:

```
http://127.0.0.1:8000 (ou em localhost dependendo da sua execução)
```

E que o endpoint `GET /api/turmas/<id>` esteja funcionando corretamente.

---

## 📦 Estrutura do Projeto

```
reserva-salas/
│
├── app.py
├── reserva_model.py
├── reserva_route.py
├── database.py
├── Dockerfile
├── requirements.txt
├── config.py
├── instance/
│   └── reservas.db
└── README.md
```
