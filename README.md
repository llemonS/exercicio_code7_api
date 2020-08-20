# Exercício - Desenvolvimento de API 
 Criar uma API para um portal de notícias com cadastro, pesquisa e visualização de notícias utilizando mongodb.
 ## Instalação:
 ### MongoDB
 - Instalar mongodb e mante-lo ativo
  `systemctl start mongodb`
 ### Python 3.8.3
 - Utilizar pip3 para instalação dos pacotes necessarios
  `pip3 install -r requirements.txt`
 ### Arquivo principal
 `python3 server_api.py`
 
 ## Consultar Notícias ☑
 ### - Listar todas
 * **Método**
 `GET`
 * **URL**
  /noticias
 ### - Mostrar única
 * **Método**
 `GET`
 * **URL**
 /noticia/id
## Cadastrar Notícias
 ### - Cadastro
 - Título (obrigatório)
 - Texto (obrigatório)
 - Autor (obrigatório com chave estrangeira para tabela Autor) | 
     pendente(dúvidas com relação ao uso de NoSQL e uso de chave estrangeira).
  * **Método**
 `POST`
 * **URL**
 /noticias
 ## Edição e Remoção ☑
 ### - Edição
  * **Método**
 `PUT`
  * **URL**
 /noticia/id
 ### - Remoção
 * **Método**
 `DELETE`
  * **URL**
 /noticia/id
