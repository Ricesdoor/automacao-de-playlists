﻿# automacao-de-playlists
Esse programa utiliza as APIs spotipy e ytmusicapi para automatizar o processo da transfência de playlists do Spotify para o Youtube Music.

## Dependências:
Utilize o gerenciador de pacotes pip para instalar o spotipy e ytmusicapi:
```
  pip install spotipy
  pip install ytmusicapi
```
## Funcionamento:
Para o funcionamento do código, ele precisa ter acesso a suas contas do Spotify e Youtube Music, isso é feito da seguinte maneira:
### Acessando sua conta no Youtube Music:
1. Acesse o [YouTube Music](https://music.youtube.com/) no Firefox e entre em sua conta
2. Acesse as Ferramentas de Desenvolvedor (F12) e vá para 'Rede'
3. Procure pela requisição POST autenticada, e se certifique que ela aparece dessa maneira: Status 200, Method POST, Domain music.youtube.com, File browse?...
4. Caso essa requisição não apareça inicialmente, entre na sua biblioteca e depois retorne para a página inicial, assim a requisição deve aparecer
5. Clique com o botão direito -> Copiar Valores -> Copiar Cabeçalhos de Requisição
6. Agora, no terminal, digite:
```
  ytmusicapi browser
```
7. Aperte Enter, Ctrl+Z, Enter
8. Isso deve criar um arquivo chamado browser.json
9. Por último, cole o caminho para esse arquivo em 'caminho-para-seu-arquivo-browser.json', em main.py
10. Caso você tenha mais dificuldades nesse processo, você pode saber mais [aqui.](https://ytmusicapi.readthedocs.io/en/stable/setup/browser.html)
### Acessando sua conta no Spotify:
1. Acesse o [Spotify para Desenvolvedores](https://developer.spotify.com), clique nas 3 barras no canto superior direito e faça login com sua conta
2. Vá para Dashboard e clique em "Criar um App"
3. Coloque o nome, descrição e URI de sua preferência. Um exemplo de URI seria http://localhost:8888/callback
4. Após criar o app, 2 informações aparecerão:
     - Client ID
     - Client Secret
5. Coloque essas 2 informações e o URI em suas respectivas áreas em main.py
## Rodando o Código
Agora basta rodar o código main.py e ele irá adicionar todas as playlists da sua biblioteca do Spotify para o Youtube Music, bem como adicionar as musicas faltantes em playlists já existentes.
Esse processo pode demorar um pouco, visto que o ytmusicapi não é uma API oficial, e simula o acesso ao YouTube Music através de um navegador.
## Cuidados
Rodando o código, podem acontecer alguns erros antes da finalização da transferência de todas as playlists. Com sorte, todos podem ser contornados facilmente. Os 3 principais problemas que causam esses erros são:
### 1. Cookies do YouTube Music Expirados:
   Caso os cookies armazenados no arquivo browser.json se expirem, o programa perderá acesso ao YouTube Music e retornará um erro. Para resolver esse problema, basta refazer a etapa de acesso ao Youtube Music, criando um novo browser.json, assim o código funcionará a funcionar corretamente.
### 2. Problema na Requisição com o Youtube Music:
   Em alguns momentos pode ocorrer uma falha na comunicação do ytmusicapi com o YouTube Music, que impede que uma música seja adicionada e retorna um erro. Sinceramente não sei por que isso acontece mas o programa volta a funcionar se você rodar ele novamente.
### 3. Limite Diário de Criação de Playlists:
   O YouTube Music limita a criação de playlist para cerca de 10 playlists diárias. Caso você tenha uma quantidade grande de playlists na sua biblioteca do Spotify, o programa retornará um erro após a criação da 10ª playlist. Tente rodar o código novamente no dia seguinte e as playlists restantes serão adicionadas.
   
