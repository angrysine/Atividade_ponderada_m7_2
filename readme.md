# Atividade ponderada de programação 2

## Arquitetura

Nosso repositório contem 2 pastas a pasta backend_docker que contem um backend que usa FastAPI e o banco de dados Postgres, e a pasta frontend_docker que contem um frontend que usa ReactJS e NextJs.

## Como rodar

Para rodar o projeto é necessário ter o docker e o docker-compose instalados na sua maquina, após isso basta rodar o comando `docker compose up` na raiz do projeto.Nosso frontend estará disponível em `localhost:3000` e o backend em `localhost:5000` e o banco de dados está em `localhost:5432`, é importante ressaltar que wait-for-db.sh permite que o banco de dados começe antes da api(porém pelo que eu vi no git da imagem isso é um erro em aberto e tende ter comportamento errrático. Se o primeiro docker compose não iniciar o backend rodar a segunda vez resolve o problema).

## arquitetura

![arquitetura](https://github.com/angrysine/Atividade_ponderada_m7_2/blob/master/arquitetura.png)

## estrutura de pastas

├── nextjs-docker
│   ├── app.json
│   ├── next.config.js
│   ├── README.md
│   ├── public
│   ├── postcss.config.js
│   ├── styles
│   │   └── globals.css
│   ├── tailwind.config.js
│   ├── pages
│   │   ├── api
│   │   │   └── hello.js
│   │   ├── _app.js
│   │   ├── login.jsx
│   │   ├── index.jsx
│   │   └── main.js
│   ├── package.json
│   ├── components
│   │   ├── sidebar
│   │   │   ├── side_bar.jsx
│   │   │   ├── side_bar_list.jsx
│   │   │   └── side_bar_list_component.jsx
│   │   └── main_page
│   │       ├── input.jsx
│   │       ├── card_top.jsx
│   │       ├── body_card_introduction.jsx
│   │       ├── card_top_title.jsx
│   │       ├── body_card_add.jsx
│   │       └── body_card_task.jsx
│   ├── package-lock.json
│   └── Dockerfile
├── backend_docker
│   ├── requirements.txt
│   ├── app.py
│   └── Dockerfile
├── wait-for-db.sh
├── readme.md
├── compose.yml
└── arquitetura.png

## Vídeo

Vídeo da solução <https://drive.google.com/drive/folders/1pMR2M2NiF-xmajJvHBjWp3Jn0IRZROZP?usp=sharing>
