# API Python

---

Esta é uma API simples criada com Flask que retorna uma mensagem JSON de boas-vindas.

## Endpoint

- `GET /`

Resposta:

```json
{
  "message": "hello python"
}
```

---

## Site

A API está disponível na Vercel: [API Python](https://api-python-murex.vercel.app/)

---

## Como rodar localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/danielvor/api-python.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd api-python
   ```

3. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Execute o servidor:

   ```bash
   python app.py
   ```

6. Acesse a API em:

   ```
   http://localhost:5000/
   ```

---

### Dependências

- Flask
- Flask-CORS
```
