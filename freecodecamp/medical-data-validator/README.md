# 🏥 Medical Records Validator

Projeto desenvolvido durante meus estudos de **Python**, com foco na validação e manipulação de estruturas de dados.

O exercício consiste em criar um validador para uma lista de registros médicos, verificando se os dados possuem a estrutura esperada e se seus valores atendem às regras definidas.

## 🎯 Objetivo

Praticar conceitos fundamentais de Python utilizando um cenário de validação de registros médicos.

O projeto trabalha principalmente com:

* Listas e dicionários
* Tuplas
* Estruturas condicionais
* Loops `for`
* Funções
* `isinstance()`
* `set()`
* List comprehensions
* Desempacotamento de dicionários com `**`
* Expressões regulares com `re`
* Validação de tipos e valores
* Controle de fluxo com `continue`
* Retorno de valores com `return`

## 🔎 Validações realizadas

O projeto verifica:

### Estrutura dos dados

* O objeto recebido é uma lista ou tupla.
* Cada elemento da sequência é um dicionário.
* Cada dicionário possui exatamente as chaves esperadas.

### Campos dos registros

**Patient ID**

* Deve ser uma string.
* Deve seguir o padrão `p` seguido por números.

**Age**

* Deve ser um número inteiro.
* O paciente deve possuir pelo menos 18 anos.

**Gender**

* Deve ser uma string.
* Os valores aceitos são `male` ou `female`.

**Diagnosis**

* Deve ser uma string ou `None`.

**Medications**

* Deve ser uma lista.
* Todos os elementos da lista devem ser strings.

**Last Visit ID**

* Deve ser uma string.
* Deve seguir o padrão `v` seguido por números.

## 🧠 Conceitos praticados

Durante o desenvolvimento, foram utilizados diferentes recursos da linguagem Python para construir uma validação em múltiplas etapas.

Um dos pontos principais do exercício foi utilizar o operador `**` para desempacotar um dicionário e passá-lo como argumentos nomeados para uma função.

Também foi utilizado `continue` para interromper a iteração atual quando um registro apresenta uma estrutura inválida, evitando que o restante da validação seja executado sobre dados que não possuem o formato esperado.

## ▶️ Execução

Para executar o projeto, tenha o Python instalado e execute:

```bash
python medical_records_validator.py
```

Com os dados fornecidos no exercício, a validação deverá indicar que os registros possuem formato válido.

## 📚 Contexto

Este projeto faz parte da minha jornada de estudos em **Python**, com o objetivo de fortalecer minha lógica de programação e minha capacidade de trabalhar com estruturas de dados, funções e validação de informações.

> Projeto desenvolvido para fins educacionais.
