# 💰 Build a Budget App — Aplicativo de Orçamento

## 📝 Descrição

Este laboratório faz parte do currículo de Python do [freeCodeCamp](https://www.freecodecamp.org/) e consiste na criação de um aplicativo de orçamento para gerenciar transações financeiras organizadas por categorias.

O projeto permite registrar depósitos e retiradas, consultar saldos, transferir valores entre categorias e gerar um gráfico textual que representa a distribuição percentual dos gastos.

## 🎯 Objetivo

Desenvolver uma aplicação utilizando programação orientada a objetos em Python, praticando a criação de classes, métodos, manipulação de listas e dicionários, cálculos financeiros e formatação de strings.

## ⚙️ Funcionalidades

- **Criação de categorias:** permite criar categorias de orçamento, como alimentação, roupas e entretenimento.
- **Depósitos:** registra entradas de dinheiro com descrições opcionais.
- **Retiradas:** registra despesas somente quando há saldo suficiente.
- **Consulta de saldo:** calcula o saldo atual a partir das transações registradas.
- **Verificação de fundos:** verifica se uma categoria possui recursos suficientes para uma operação.
- **Transferências:** transfere valores entre categorias e registra as duas operações.
- **Extrato formatado:** exibe as transações com descrições e valores alinhados.
- **Gráfico de gastos:** apresenta a porcentagem dos gastos de cada categoria em um gráfico vertical, com valores arredondados para baixo em intervalos de dez pontos percentuais.

## 💻 Estrutura do projeto

```text
budget-app/
├── budget_app.py
└── README.md
```

## 🧪 Exemplo de utilização

```python
from budget_app import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "Initial deposit")
food.withdraw(150, "Groceries")

clothing = Category("Clothing")
clothing.deposit(500, "Initial deposit")
clothing.withdraw(100, "New clothes")

food.transfer(50, clothing)

print(food)
print(clothing)
print(create_spend_chart([food, clothing]))
```

O exemplo demonstra a criação de categorias, o registro de transações, uma transferência entre categorias e a geração do gráfico de gastos.

## 📚 Conceitos praticados

- Programação orientada a objetos (POO).
- Criação de classes, objetos e métodos.
- Inicialização de atributos com `__init__`.
- Manipulação de listas e dicionários.
- Laços de repetição (`for`).
- Estruturas condicionais (`if` e `else`).
- Métodos e atributos de instância.
- Formatação de strings com f-strings.
- Alinhamento de texto e formatação numérica.
- Cálculos de saldo e porcentagem.
- Uso de `sum()`, `abs()`, `range()` e `max()`.
- Construção de relatórios textuais a partir de dados estruturados.
- Tratamento de divisão por zero.

## 🛠️ Tecnologias

- **Python 3**
- **Git e GitHub** para versionamento e publicação do código.

## 🧠 Abordagem de aprendizado

O desenvolvimento foi realizado de forma incremental, implementando e validando cada parte da aplicação antes de avançar para a próxima etapa.

A solução foi construída a partir da análise dos requisitos, com atenção à lógica das transações, à validação de saldo e à formatação exata do gráfico exigido pelo laboratório.

## 🏁 Status

✅ **Laboratório concluído — todos os testes do freeCodeCamp passaram.**
