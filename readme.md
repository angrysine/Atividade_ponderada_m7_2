# Atividade ponderada de programação 2

## Arquitetura

Nosso repositório contem 2 pastas a pasta backend_docker que contem um backend que usa FastAPI e o banco de dados Postgres, e a pasta frontend_docker que contem um frontend que usa ReactJS e NextJs.

## Como rodar

Para rodar o projeto é necessário ter o docker e o docker-compose instalados na sua maquina, após isso basta rodar o comando `docker compose up` na raiz do projeto.Nosso frontend estará disponível em `localhost:3000` e o backend em `localhost:5000` e  o banco de dados está em `localhost:5432`, é importante ressaltar que wait-for-db.sh permite que o banco de dados começe antes da api(porém pelo que eu vi no git da imagem isso é um erro em aberto e tende ter comportamento errrático. De o primeiro docker compose não iniciar o backend rodar a segunda vez resolve o problema).

## Vídeo

