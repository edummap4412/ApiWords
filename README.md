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
  * Para iniciar o servidor local do app ```http://localhost:8000```

---
## Swagger
[Swagger](http://127.0.0.1:8000/docs)

---

# Endpoints

* URL:```http://127.0.0.1:8000/api```

### `/vowel_count`
Este endpoint recebe uma lista de palavras e retorna a contagem de vogais em cada palavra. As palavras são enviadas no corpo da requisição em formato JSON.

### Requisição

- Método: POST
- URL: `/vowel_count`
- Corpo da Requisição (JSON):
```json
  {
  "words": ["hello", "world", "example"]
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
	"words": ["hello", "world", "example"],
	"order": "asc"
}
```

### Resposta
A resposta é um objeto JSON contendo a lista de palavras ordenada de acordo com a configuração de inversão.

Exemplo de resposta bem-sucedida com `order = asc`:

```json
{
	"words": ["hello", "world", "example"]
}
```
Exemplo de resposta bem-sucedida com `order = desc`:


```json
{
	"words": ["example", "world", "hello"]
}
```