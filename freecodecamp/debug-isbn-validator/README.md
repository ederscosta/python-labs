# 🐛 Depurar um Validador de ISBN

## 📝 Descrição

Neste laboratório, o objetivo foi analisar e corrigir um validador de códigos ISBN que apresentava diferentes erros de sintaxe, lógica e tratamento de exceções.

O programa recebe um código ISBN e seu comprimento no formato:

```text
ISBN,length

Exemplos: 

1530051126,10
9781530051120,13
```

O programa deve validar códigos ISBN-10 e ISBN-13, identificar códigos inválidos e tratar entradas incorretas sem interromper a execução de forma inesperada.

## 🎯 Objetivo

Corrigir o código fornecido para que o programa seja capaz de:

○ Validar códigos ISBN-10 e ISBN-13.

○ Corrigir erros de indentação.

○ Corrigir erros de lógica relacionados aos índices do ISBN.

○ Tratar entradas sem valores separados por vírgula.

○ Tratar comprimentos não numéricos.

○ Identificar caracteres inválidos no código ISBN.

○ Exibir mensagens adequadas para cada tipo de entrada.

○ Fazer todos os testes automatizados do laboratório passarem.

## 🐛 Problemas identificados e correções

| Problema | Correção realizada |
| :--- | :--- |
| `IndentationError` no bloco `if/else` | Correção da indentação das instruções dentro dos blocos condicionais. |
| Uso incorreto da função `len()` | Alteração para verificar corretamente o tamanho da string `isbn`. |
| Erro de deslocamento (*off-by-one*) | Ajuste dos índices utilizados para separar os dígitos principais do dígito verificador. |
| `IndexError` em entradas sem vírgula | Tratamento da exceção com o bloco `try/except`. |
| `ValueError` para comprimento não numérico | Tratamento da conversão do comprimento para inteiro. |
| `ValueError` para caracteres inválidos | Tratamento da conversão dos dígitos do ISBN para valores inteiros. |
| Falta de encerramento após erros | Utilização de `return` para interromper a execução após entradas inválidas. |

## 💻 Código original

<details>
<summary>🔍 Clique para visualizar o código original com erros</summary>

```python
def validate_isbn(isbn, length):
    if len(isbn, length) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[0:length]
    given_check_digit = isbn[length]
    main_digits_list = [int(digit) for digit in main_digits]

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)

    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)

    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')
    isbn = values[0]
    length = int(values[1])

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

main()
```
</details>

## 🧪 Exemplos de testes

| Entrada | Resultado esperado |
| :--- | :--- |
| `1530051126,10` | `Valid ISBN Code.` |
| `9781530051120,13` | `Valid ISBN Code.` |
| `9971502100,10` | `Valid ISBN Code.` |
| `080442957X,10` | `Valid ISBN Code.` |
| `9781947172104,13` | `Valid ISBN Code.` |
| `1530051125,10` | `Invalid ISBN Code.` |
| `9781530051120,10` | `ISBN-10 code should be 10 digits long.` |
| `1530051126,13` | `ISBN-13 code should be 13 digits long.` |
| `15-0051126,10` | `Invalid character was found.` |
| `1530051126,9` | `Length should be 10 or 13.` |
| `1530051125,A` | `Length must be a number.` |
| `1530051125` | `Enter comma-separated values.` |

## 📚 Conceitos praticados

Durante este laboratório, foram praticados os seguintes conceitos:

○ Depuração de código Python.  
○ Identificação e correção de `IndentationError`.  
○ Uso da função `len()`.  
○ Índices e fatiamento de strings.  
○ Erros do tipo off-by-one.  
○ Tratamento de exceções com `try` e `except`.  
○ `IndexError`.  
○ `ValueError`.  
○ Conversão de strings para inteiros.  
○ List comprehensions.  
○ Funções e retorno antecipado com return.  
○ Estruturas condicionais if e else.  
○ Enumeração de elementos com enumerate().  

## 🏁 Status

### ✅ Laboratório concluído

Todos os testes automatizados foram concluídos com sucesso.



