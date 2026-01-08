# UNIVERSIDADE HIP HOP BRASIL / HORTO FLORESTAL QUILOBO CABULA SALVADOR-BA

Sistema de pesquisa e levantamento da cultura Hip-Hop nacional desenvolvido em Django com PostgreSQL e autenticação social Google.

## 🎤 Sobre o Projeto

A UNIVERSIDADE HIP HOP BRASIL / HORTO FLORESTAL QUILOBO CABULA SALVADOR-BA é uma plataforma para coletar e gerenciar informações sobre a cultura Hip-Hop brasileira, incluindo dados sobre MCs/Rappers, DJs, Grafiteiros, B-Boys/B-Girls, grupos, fãs e consumidores da cultura.

## 🚀 Tecnologias

- **Django 6.0** - Framework web Python
- **PostgreSQL** - Banco de dados
- **Django Allauth** - Autenticação social (Google OAuth)
- **Python 3.12**

## 📋 Campos da Pesquisa

O sistema coleta informações sobre:

1. **Atuação**: MC/Rapper, DJ, Grafite, Breaking, Grupo, Conhecimento, Fãs, Consumidores
2. **Dados Pessoais**: Nome, pseudônimo, idade
3. **Localização**: Estado e município
4. **Demografia**: Cor/raça e gênero
5. **Cultura Hip-Hop**: Tempo de atuação, nome do grupo, membros
6. **Formação**: Nível educacional e área de formação

## 🔧 Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/renanapcs/mhhbr.git
cd mhhbr

# Instale dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
cp .env.example .env
# Edite .env com suas configurações

# Execute migrações
python manage.py migrate

# Crie superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

📖 **Documentação completa**: Veja [SETUP.md](SETUP.md) para instruções detalhadas de configuração.

## 🔐 Autenticação

- Login via Google OAuth
- Interface administrativa Django
- Gerenciamento de usuários

## 💻 Uso

- **Admin**: http://localhost:8000/admin/
- **Login Google**: http://localhost:8000/accounts/google/login/

## 📊 Funcionalidades

- ✅ Cadastro de participantes da cultura Hip-Hop
- ✅ Autenticação social com Google
- ✅ Interface administrativa completa
- ✅ Filtros e buscas avançadas
- ✅ Exportação de dados
- ✅ Suporte a PostgreSQL

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [SETUP.md](SETUP.md) para instruções de desenvolvimento.

## 📝 Licença

Open Source

---

**UNIVERSIDADE HIP HOP BRASIL / HORTO FLORESTAL QUILOBO CABULA SALVADOR-BA** - Preservando e documentando a cultura Hip-Hop nacional 🎵

