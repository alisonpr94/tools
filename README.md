# API de Ferramentas

Esta é uma API simples para gerenciar ferramentas, desenvolvida usando Django REST Framework.

## Funcionalidades

- Listar todas as ferramentas
- Criar uma nova ferramenta
- Obter detalhes de uma ferramenta por ID
- Excluir uma ferramenta por ID
- Filtrar ferramentas por tag
- Atualizar as tags de uma ferramenta

## Configuração do Ambiente

1. Clone este repositório:

git clone https://github.com/alisonpr94/tools.git
cd tools

3. Clone este repositório:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

4. Instale as dependências:

pip install -r requirements.txt

5. Execute as migrações:

python manage.py migrate

6. Inicie o servidor:

python manage.py runserver

## Endpoints

- Listar todas as ferramentas: GET /api/tools/
- Criar uma nova ferramenta: POST /api/tools/
- Obter detalhes de uma ferramenta por ID: GET /api/tools/{id}/
- Excluir uma ferramenta por ID: DELETE /api/tools/{id}/
- Filtrar ferramentas por tag: GET /api/tools/by-tag/{tag}/
- Atualizar as tags de uma ferramenta: PUT /api/tools/{id}/update/