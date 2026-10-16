# User Settings Manager

Laboratório em Python para construção de um **Gerenciador de Configurações de Usuário**, desenvolvido como parte dos estudos de Python.

O projeto implementa operações básicas para adicionar, atualizar, excluir e visualizar configurações armazenadas em um dicionário.

## 🎯 Objetivo

Praticar conceitos fundamentais de Python, especialmente:

- Dicionários (`dict`)
- Tuplas e desempacotamento
- Funções e parâmetros
- Condicionais (`if` / `else`)
- Métodos de dicionários (`items()`, `pop()`)
- Métodos de strings (`lower()`, `capitalize()`)
- F-strings
- Concatenação de strings
- Quebras de linha (`\n`)

## ⚙️ Funcionalidades

### `add_setting()`

Adiciona uma nova configuração ao dicionário.

- Converte chave e valor para letras minúsculas.
- Impede a criação de uma configuração com chave já existente.
- Retorna uma mensagem indicando sucesso ou erro.

### `update_setting()`

Atualiza uma configuração existente.

- Converte chave e valor para letras minúsculas.
- Atualiza somente configurações existentes.
- Retorna uma mensagem indicando sucesso ou erro.

### `delete_setting()`

Exclui uma configuração.

- Converte a chave para letras minúsculas.
- Remove a configuração utilizando `pop()`.
- Retorna uma mensagem indicando sucesso ou erro.

### `view_settings()`

Exibe as configurações cadastradas.

- Informa quando não existem configurações.
- Capitaliza a primeira letra das chaves.
- Exibe cada configuração em uma nova linha.
- Mantém uma quebra de linha ao final da saída.

## 🧪 Exemplo

Configurações iniciais:

```python
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}
```

Exemplo de visualização:

```text
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high
```

## ▶️ Como executar

Tenha o Python 3 instalado e execute:

```bash
python main.py
```

O arquivo contém as funções desenvolvidas no laboratório e o dicionário de teste utilizado durante os exercícios.

## 📚 Aprendizados

Este laboratório reforçou o uso de dicionários em Python e mostrou como pequenas funções podem ser combinadas para implementar operações de gerenciamento de dados.

O exercício também ajudou a praticar validações condicionais, manipulação de strings e formatação de mensagens com f-strings.

---

**Projeto desenvolvido durante os estudos de Python.**
