# Pin Extractor

## 📖 Sobre o laboratório

Neste laboratório do freeCodeCamp, o objetivo foi desenvolver uma função capaz de extrair códigos secretos escondidos em poemas.

Cada dígito do PIN é determinado pelo comprimento da n-ésima palavra da n-ésima linha de cada poema. A solução também trata casos em que uma linha possui menos palavras do que o esperado, adicionando o dígito `0` ao código para evitar erros.

---

## 🎯 Objetivos

- Trabalhar com funções em Python
- Manipular strings utilizando `split()`
- Percorrer listas com `for`
- Utilizar `enumerate()`
- Trabalhar com índices de listas
- Utilizar condicionais (`if/else`)
- Concatenar strings
- Armazenar resultados em listas com `append()`
- Retornar múltiplos resultados

---

## 🛠️ Conceitos praticados

- Strings
- Listas
- Loops
- Funções
- Validação de índices
- Tratamento de casos limite
- Organização de código

---

## 💡 Minha solução

A função percorre uma lista de poemas. Para cada poema:

1. Divide o poema em linhas.
2. Percorre cada linha utilizando `enumerate()`.
3. Divide cada linha em palavras.
4. Obtém o comprimento da palavra correspondente ao índice da linha.
5. Caso a palavra não exista, adiciona `0` ao código secreto.
6. Armazena o código gerado em uma lista.
7. Retorna todos os códigos extraídos.

---

## ▶️ Exemplo de uso

```python
print(pin_extractor([poem, poem2, poem3]))
```

Saída:

```python
['5202', '4246', '11110']
```

---

## 📚 Aprendizados

Durante este laboratório pratiquei:

- manipulação de strings;
- navegação entre listas e índices;
- utilização de `enumerate()`;
- validação para evitar `IndexError`;
- construção de algoritmos utilizando loops aninhados;
- organização de funções para resolver problemas de forma incremental.