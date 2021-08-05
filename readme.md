# Projeto e-diaristas

### Instalando o projeto

#### Clonar o Projeto
`git clone https://github.com/eduardobdamacena/multistack-ediaristas.git`

#### Instalar dependências
`pip install -r requirements.txt`

#### Alterar configurações do BD no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco_de_dados',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root'
    }
}
```

#### Migrar Banco de Dados
`python manage.py migrate`

#### Iniciar o servidor
`python manage.py runserver`
