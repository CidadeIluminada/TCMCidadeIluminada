# TCMCidadeIluminada

## Instalação do ambiente de desenvolvimento no Ubuntu
1. Baixe o arquivo `install.sh` da raíz do repositório.
1. Abra um terminal.
    1. Aperte a tecla do Windows
    1. Digite `terminal`
    1. Aperte `[ENTER]`
    1. Trave o terminal na barra do Ubuntu, para isso, clique com o botão direito no ícone e clique em travar na barra.
1. Recomendo colocar o script em uma pasta separada:
    1. `mkdir code`
    1. `cd code`
    1. `mv ../install.sh ./`
1. Digite `sh install.sh`. Se ele pedir uma senha, digite a senha que você usa para entrar no Ubuntu.  **Note que** a senha não vai aparecer na tela, mas ela vai funcionar normalmente.

**Dica:** Você pode copiar e colar os comandos no terminal usando `[CTRL+SHIFT+V]`

Neste ponto o python, o Java, o virtualenvwrapper, o banco de dados e o git estão instalados.

Agora, no canto esquerdo do terminal deve estar escrito `(cidadeiluminada)`, isso quer dizer que o ambiente de desenvolvimento de python está ativo. Quando você fechar o terminal e voltar, o ambiente vai voltar ao normal. Para ativar de novo, digite `workon cidadeiluminada`. **Dica:** Use o `[TAB]`

Entretanto, o git e o banco estão desconfigurados. Vamos começar com o git, que é mais fácil.

### Configurando o git e o GitHub
[Guia oficial](https://help.github.com/articles/set-up-git/)

Para configurar o git é simples. No terminal, digite:

1. `git config --global user.name "YOUR NAME"`
1. `git config --global user.email "YOUR EMAIL ADDRESS"`
1. `git config --global core.editor vim`

O SSH é mais chato:

1. Digite no terminal `ssh-keygen -t rsa -C "your_email@example.com"`
1. Nesse ponto, o ssh-keygen vai pedir uma senha. Deixe em branco
1. Digite no terminal `eval "$(ssh-agent -s)"`
1. Digite no terminal `ssh-add ~/.ssh/id_rsa`
1. Digite no terminal `gedit ~/.ssh/id_rsa.pub`. Um editor de texto deve abrir. Copie tudo.
1. [Siga os passos para adicionar a senha na conta do GitHub](https://help.github.com/articles/generating-ssh-keys/#step-3-add-your-ssh-key-to-your-account)
1. A partir daqui o ssh deve estar funcionando.[ Teste seguindo o **Step 4** do guia do GitHub](https://help.github.com/articles/generating-ssh-keys/#step-4-test-everything-out)


### Banco de dados (PostgreSQL)

Agora não é bom copiar os comandos. Digite do jeito que estão aparecendo aqui:

1. `sudo -u postgres psql postgres`
1. `\password postgres`
1. `root` (Não vai aparecer na tela, igual o da instalação)
1. `root`
1. `CREATE EXTENSION adminpack;`
1. `\q`
1. `sudo -u postgres createuser --superuser $USER`
1. `sudo -u postgres psql`
1. `\password $USER`
1. `\q`
1. `sudo -u postgres createdb $USER`

Ufa. Por fim, digite `sudo gedit /etc/postgresql/9.3/main/pg_hba.conf` e no editor que abrir, substitua as linhas

```
# Database administrative login by Unix domain socket
local   all             postgres                                peer
```
por
```
# Database administrative login by Unix domain socket
local   all             postgres                                md5
```

Recarregue o postgres usando `sudo service postgres reload`.

Finalmente, rode o pgAdmin3 usando `pgadmin3` e configure uma nova conexão usando o nome e senha de seu usuario. Aproveite e crie um banco de dados chamado `cidadeiluminada`


### Baixando e Instalando a aplicação web

Depois de uma excitante viagem, finalmente podemos instalar a aplicação:

Em uma pasta, digite `git clone git@github.com:HardDiskD/TCMCidadeIluminada.git`. Isso irá criar uma pasta chamada `TCMCidadeIluminada`, com uma pasta `webservice` e outra `android` dentro.

Vamos agora instalar a aplicação em python:

1. `cd TCMCidadeIluminada` (se você ainda não entrou nessa pasta)
1. `sh install-cidadeiluminada.sh`


Se deu tudo certo, o seu terminal vai ter algo do tipo

`Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

aparecendo.

Por fim, crie o usuário padrão: `python manage.py criar_usuario admin admin`


### Instalando o PyCharm
[Baixe aqui](https://download.jetbrains.com/python/pycharm-community-4.0.4.tar.gz) e descompacte para qualquer lugar.

Para rodar, entre na pasta que extraiu e digite:

1. `cd bin`
1. `sh pycharm.sh`

## Instalação do ambiente de desenvolvimento no Windows
lol

##Configurações de ambiente

O arquivo `settings.py` guarda várias várias variáveis de configuração de ambiente. Neste arquivo estão guardado todos os valores padrões e de exemplo.

Para configurar o seu ambiente local, crie uma pasta chamada `instance` na pasta onde está o `manage.py`, e dentro dela crie um arquivo chamado `settings_local.py`. A connection string do Postgres deve ser configurada no `settings_local.py`.

**Somente o arquivo `settings_local.py` deve ser alterado, e no arquivo `settings.py` ficam somente os exemplos de chave/valor.**

O `settings_local.py` será lido depois do settings de fora, então para configurar localmente, somente substitua as variáveis em **maiúsculo** para os valores desejados.

**Sobre a conexão do Postgres:** Do modo que foi configurado nesse arquivo, o campo `username` deve ficar vazio. Isso pode ou não dar problemas. Vou perguntar para quem sabe e atualizar isso aqui. Eu *acho* que não tem problema porque essas instruções são só para máquinas de desenvolvimento.
