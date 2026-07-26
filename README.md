# Projeto Django com frontend de chat para um MCP

Este repositório contém dois projetos Django independentes:

- `frontend`: interface de chat estilizada com Bootstrap que consome a API do backend.

## Estrutura

- `frontend/`
    - `chat/`
    - `config/`

## Como executar

1. Crie os ambientes virtuais:

```powershell
python -m venv frontend/.venv
```

2. Instale as dependências de cada projeto:

```powershell
frontend/.venv/Scripts/python -m pip install -r frontend/requirements.txt
```

3. Configure as variáveis de ambiente a partir dos arquivos `.env.example`.

4. Inicie o frontend na porta `8001`.

## Observações

- O frontend chama o endpoint `/api/chat/` do backend.

