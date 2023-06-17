# APIWORDS

Projeto feito para teste de admissão,onde: Neste projeto contém dois endpoints desenvolvidos usando o framework FastAPI. Abaixo está uma descrição de cada um deles.

___

### Executando o Projeto com Docker
  * Certifique-se de ter o Docker instalado na sua máquina.
  * Crie uma imagem Docker a partir do Dockerfile incluído no projeto:
  ```shell
    $ docker build -t app .
  ```
  * Execute o projeto usando o Docker Compose:
  ```shell
    $ docker-compose up
  ```
  * Para iniciar o servidor local do app ``` uvicorn app.main:app --reload```

### Executando o Projeto sem Docker
  * Instale as dependências:
  ```shell
  $ poetry install
  ```
  * Inicie o servidor de desenvolvimento:
  ```shell
  $ poetry run uvicorn app.main:app --reload
  ```

---
##Swagger
[Swagger](http://127.0.0.1:8000/docs)

---

#Endpoints

* URL:```http://127.0.0.1:8000/api```

### `/vowel_count`
Este endpoint recebe uma lista de palavras e retorna a contagem de vogais em cada palavra. As palavras são enviadas no corpo da requisição em formato JSON.

### Requisição

- Método: POST
- URL: `/vowel_count`
- Corpo da Requisição (JSON):
```json
  {
    "words": ["palavra1", "palavra2", "palavra3"]
  } 
```
### Resposta

A resposta é um objeto JSON contendo a contagem de vogais para cada palavra enviada.

Exemplo de resposta bem-sucedida:
```json
{
  "palavra1": 3,
  "palavra2": 2,
  "palavra3": 1
}
```


### `/sort`
Este endpoint recebe uma lista de palavras e um parâmetro opcional reverse para especificar se a ordem deve ser invertida. As palavras são enviadas no corpo da requisição em formato JSON.

### Requisição

- Método: POST
- URL: `/sort`
- Corpo da Requisição (JSON):
```json
  {
    "words": ["palavra1", "palavra2", "palavra3"]
  }
```

### Resposta
A resposta é um objeto JSON contendo a lista de palavras ordenada de acordo com a configuração de inversão.

Exemplo de resposta bem-sucedida com `reverse = True`:

```json
{
  "words": ["palavra3", "palavra2", "palavra1"],
  "order": "desc"
}
```
Exemplo de resposta bem-sucedida com `reverse = False`:


```json
{
  "words": ["palavra1", "palavra2", "palavra3"],
  "order": "asc"
}
```