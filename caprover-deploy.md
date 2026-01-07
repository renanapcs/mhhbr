# Guia de Deploy no CapRover

## Pré-requisitos

1. **CapRover instalado** em um servidor
2. **Conta GitHub** com push access
3. **Domínio configurado** apontando para seu servidor CapRover

## Configuração Inicial

### 1. Preparar o Projeto

O projeto já possui:
- `Dockerfile` - Imagem Docker otimizada
- `captain-definition` - Configuração do CapRover
- `.dockerignore` - Arquivos a ignorar no build
- `.env.example` - Variáveis de ambiente

### 2. Configurar Variáveis de Ambiente

No dashboard do CapRover:

1. Acesse a aplicação "mhhbr"
2. Vá para "App Configs" → "Environment Variables"
3. Configure as seguintes variáveis:

```
DEBUG=False
SECRET_KEY=<gere-uma-chave-segura>
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DATABASE_URL=postgresql://user:password@postgres-host:5432/mhhbr_db
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=seu-app-password
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### 3. Configurar Banco de Dados PostgreSQL

#### Opção A: PostgreSQL em Contêiner CapRover
1. Crie uma nova aplicação "One-click Apps" → PostgreSQL
2. Configure o banco:
   - Nome: `mhhbr_db`
   - Usuário: `mhhbr_user`
   - Senha: <gere-uma-senha-segura>

#### Opção B: Banco de Dados Externo
Use um serviço como AWS RDS, Heroku Postgres ou similar

### 4. Deploy via GitHub

#### Método 1: Push to Deploy (Recomendado)

1. No CapRover Dashboard:
   - Acesse "Deployment" → "Deploy from GitHub"
   - Conecte sua conta GitHub
   - Selecione o repositório `renanapcs/mhhbr`
   - Branch: `main`
   - Ative "Automatic Deploy on Push"

2. Sempre que fazer push para `main`, o deploy ocorrerá automaticamente

#### Método 2: Push via Capfile

1. Instale CapRover CLI:
```bash
npm install -g caprover
```

2. Configure a conexão:
```bash
caprover login
```

3. Deploy:
```bash
caprover deploy
```

### 5. Executar Migrações

Após o primeiro deploy:

1. No dashboard do CapRover, acesse a aplicação "mhhbr"
2. Vá para "App Configs" → "Run Command"
3. Execute:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

### 6. Configurar SSL/HTTPS

1. No dashboard, vá para "HTTP Settings"
2. Ative "HTTPS"
3. O CapRover usa Let's Encrypt automaticamente

### 7. Configurar Google OAuth

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto
3. Ative a API "Google+ API"
4. Crie credenciais OAuth 2.0 (Aplicação Web)
5. URLs de redirecionamento autorizadas:
   ```
   https://seu-dominio.com/accounts/google/login/callback/
   ```
6. Copie Client ID e Client Secret
7. Configure no Django Admin:
   - Acesse `https://seu-dominio.com/admin/`
   - Vá para "Social Applications"
   - Crie uma nova aplicação Google com as credenciais

### 8. Configurar Email (Gmail)

1. Ative "Less secure app access" na conta Google (ou use App Password)
2. Configure as variáveis:
   - `EMAIL_HOST_USER`: seu-email@gmail.com
   - `EMAIL_HOST_PASSWORD`: seu-app-password

## Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'django'"

Verifique se a imagem Docker foi construída corretamente:
- Verifique `captain-definition`
- Reconstrua manualmente no CapRover Dashboard

### Erro de Banco de Dados

1. Verifique a variável `DATABASE_URL`
2. Teste a conexão:
```bash
psql $DATABASE_URL
```

### Erro de Static Files

Execute no CapRover:
```bash
python manage.py collectstatic --noinput --clear
```

### Logs

Acesse "App Configs" → "Logs" para ver logs em tempo real

## Monitoramento

1. **Health Checks**: CapRover monitora automaticamente
2. **Alertas**: Configure em "Monitoring"
3. **Backup de Banco**: Configure em "Databases"

## Atualizar Aplicação

Após fazer commits no branch `main`:

```bash
git add .
git commit -m "sua mensagem"
git push origin main
```

O deploy ocorrerá automaticamente se configurado "Push to Deploy"

## Segurança

- Senhas e chaves nunca devem estar no repositório
- Use variáveis de ambiente no CapRover
- Mantenha Django em DEBUG=False em produção
- Configure ALLOWED_HOSTS corretamente
- Use HTTPS obrigatoriamente
