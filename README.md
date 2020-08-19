# Exercício - Desenvolvimento de API 
 Criar uma API para um portal de notícias com cadastro, pesquisa e visualização de notícias utilizando mongodb.
 ## Consultar Notícias ☑
 ### Listar todas
 * **Método**
 `GET`
 * **URL**
  /noticias
 ### Mostrar única
 * **Método**
 `GET`
 * **URL**
 /noticia/id
## Cadastrar Notícias ☑
 ### Cadastro
 - Título (obrigatório) ☑
 - Texto (obrigatório) ☑
 - Autor (obrigatório com chave estrangeira para tabela Autor) | 
     pendente(dúvidas com relação ao uso de NoSQL e uso de chave estrangeira).
  * **Método**
 `POST`
 * **URL**
 /noticias
 ## Edição e Remoção ☑
 ### Edição
  * **Método**
 `PUT`
  * **URL**
 /noticia/id
 ### Remoção
 * **Método**
 `DELETE`
  * **URL**
 /noticia/id
