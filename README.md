# Exercício - Desenvolvimento de API 
 Criar uma API para um portal de notícias com cadastro, pesquisa e visualização de notícias utilizando mongodb.
 ## Consultar Notícias ☑
 - Listar todas
 * **URL**
  /noticias
 * **Método**
 `GET`
 - Mostrar única
 * **URL**
 /noticia/id
 * **Método**
 `GET`
## Cadastrar Notícias ☑
 - Cadastro
 - Título (obrigatório) ☑
 - Texto (obrigatório) ☑
 - Autor (obrigatório com chave estrangeira para tabela Autor) | 
     pendente(dúvidas com relação ao uso de NoSQL e uso de chave estrangeira).
 * **URL**
 /noticias
  * **Método**
 `POST`
 ## Edição e Remoção ☑
 - Edição
  * **URL**
 /noticia/id
  * **Método**
 `PUT`
 - Remoção
 * **Método**
 `DELETE`
