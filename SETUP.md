# UNIVERSIDADE HIP HOP BRASIL / HORTO FLORESTAL QUILOBO CABULA SALVADOR-BA - Sistema de Pesquisa

Sistema Django para levantamento e pesquisa da cultura Hip-Hop nacional.

## Recursos

- **Django 6.0** - Framework web Python
- **PostgreSQL** - Banco de dados relacional
- **Django Allauth** - Autenticação social com Google OAuth
- **Pesquisa Hip-Hop** - Formulário de coleta de dados sobre a cultura Hip-Hop

## Estrutura do Projeto

```
mhhbr/
├── config/              # Configurações do Django
│   ├── settings.py     # Configurações principais
│   ├── urls.py         # URLs do projeto
│   └── wsgi.py         # WSGI application
├── survey/             # App de pesquisa
│   ├── models.py       # Modelo HipHopSurvey
│   ├── admin.py        # Interface administrativa
│   └── migrations/     # Migrações do banco de dados
├── manage.py           # Gerenciador Django
├── requirements.txt    # Dependências Python
└── .env.example        # Exemplo de variáveis de ambiente
```

## Pré-requisitos

- Python 3.8+
- PostgreSQL 12+
- pip (gerenciador de pacotes Python)

## Configuração Inicial

### 1. Clone o repositório

```bash
git clone https://github.com/renanapcs/mhhbr.git
cd mhhbr
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados PostgreSQL

Crie um banco de dados PostgreSQL:

```sql
CREATE DATABASE mhhbr_db;
CREATE USER mhhbr_user WITH PASSWORD 'sua_senha';
ALTER ROLE mhhbr_user SET client_encoding TO 'utf8';
ALTER ROLE mhhbr_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE mhhbr_user SET timezone TO 'America/Sao_Paulo';
GRANT ALL PRIVILEGES ON DATABASE mhhbr_db TO mhhbr_user;
```

### 5. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e configure:

```bash
cp .env.example .env
```

Edite o arquivo `.env`:

```env
SECRET_KEY=sua-chave-secreta-aqui-gere-uma-nova
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=mhhbr_db
DB_USER=mhhbr_user
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

# Google OAuth Configuration
GOOGLE_CLIENT_ID=seu-google-client-id
GOOGLE_CLIENT_SECRET=seu-google-client-secret
```

### 6. Configure o Google OAuth

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative a Google+ API
4. Crie credenciais OAuth 2.0:
   - Tipo: Aplicação Web
   - Origens JavaScript autorizadas: `http://localhost:8000`
   - URIs de redirecionamento: `http://localhost:8000/accounts/google/login/callback/`
5. Copie o Client ID e Client Secret para o arquivo `.env`

### 7. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 9. Configure o Google Social App no Django Admin

1. Inicie o servidor: `python manage.py runserver`
2. Acesse: `http://localhost:8000/admin/`
3. Login com o superusuário
4. Vá para **Sites** e edite o site example.com:
   - Domain name: `localhost:8000`
   - Display name: `UNIVERSIDADE HIP HOP BRASIL`
5. Vá para **Social applications** > Add
   - Provider: Google
   - Name: Google OAuth
   - Client id: (seu Google Client ID)
   - Secret key: (seu Google Client Secret)
   - Sites: Adicione `localhost:8000` aos sites escolhidos

### 10. Execute o servidor

```bash
python manage.py runserver
```

Acesse:
- Admin: http://localhost:8000/admin/
- Login Google: http://localhost:8000/accounts/google/login/

## Modelo de Dados - Pesquisa Hip-Hop

O modelo `HipHopSurvey` coleta as seguintes informações:

### Informações Pessoais
- **Nome**: Nome completo
- **Pseudônimo**: Nome artístico (opcional)

### Localização
- **Estado**: Estado brasileiro
- **Município**: Cidade

### Demografia
- **Idade**: Idade do participante
- **Cor/Raça**: Preta, Parda, Branca, Indígena, Amarela
- **Gênero**: Masculino, Feminino, Não-binário, Outro

### Atuação no Hip-Hop
- **Atuação**: MC/Rapper/Cantor, DJ, Grafite, Breaking, Grupo, Conhecimento, Fãs, Consumidor
- **Tempo na cultura**: Quanto tempo participa da cultura Hip-Hop
- **Nome do Grupo**: Se faz parte de um grupo (opcional)
- **Membros**: Quantidade de membros masculinos e femininos (opcional)

### Formação
- **É formado?**: Sim/Não
- **Qual formação?**: Área de formação (se aplicável)

### Adicionais
- **Observações**: Informações adicionais
- **Metadados**: Data de criação e atualização

## Uso do Sistema

### Admin Interface

Acesse `http://localhost:8000/admin/` para:
- Visualizar e gerenciar pesquisas
- Filtrar por atuação, estado, gênero, cor
- Buscar por nome, pseudônimo, município
- Exportar dados

### Login Social

Os usuários podem fazer login via Google OAuth em:
`http://localhost:8000/accounts/google/login/`

## Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor
python manage.py runserver

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell Django
python manage.py shell
```

## Estrutura do Banco de Dados

A tabela principal `survey_hiphopsurvey` contém todos os campos da pesquisa com índices para otimizar consultas por:
- Estado
- Atuação
- Gênero
- Cor/Raça
- Data de criação

## Segurança

- Use HTTPS em produção
- Mantenha `DEBUG=False` em produção
- Use variáveis de ambiente para credenciais sensíveis
- Configure `ALLOWED_HOSTS` apropriadamente
- Use senhas fortes para o banco de dados
- Mantenha as dependências atualizadas

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto é open source.

## Contato

Projeto: [https://github.com/renanapcs/mhhbr](https://github.com/renanapcs/mhhbr)
