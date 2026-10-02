# Email Simulator

Um simulador de e-mail desenvolvido em Python como parte dos laboratórios de Python do freeCodeCamp.

O projeto simula o envio, recebimento, leitura e exclusão de e-mails entre usuários, utilizando classes, objetos e métodos para representar as diferentes partes do sistema.

## Objetivo

Praticar conceitos fundamentais de Programação Orientada a Objetos (POO) em Python por meio da construção de um sistema simples de e-mail.

O laboratório permite trabalhar com usuários, mensagens e caixas de entrada, conectando diferentes classes para representar o funcionamento básico de um serviço de e-mail.

## Funcionalidades

* Criação de usuários.
* Criação de caixas de entrada individuais.
* Envio de e-mails entre usuários.
* Registro de remetente e destinatário.
* Registro de assunto e corpo da mensagem.
* Registro automático de data e hora do recebimento.
* Listagem dos e-mails recebidos.
* Identificação de e-mails como lidos ou não lidos.
* Leitura completa de e-mails.
* Exclusão de e-mails.
* Validação de índices de e-mails.
* Mensagens de confirmação e feedback para o usuário.

## Conceitos praticados

* Classes e objetos.
* Construtores com `__init__`.
* Atributo `self`.
* Métodos de instância.
* Encapsulamento de comportamentos.
* Composição entre classes.
* Listas.
* Índices e conversão de índices.
* Estruturas condicionais (`if`).
* `return`.
* Laços `for`.
* `enumerate()`.
* F-strings.
* Formatação de data e hora com `datetime`.
* Método especial `__str__`.
* Expressão condicional.
* Argumentos posicionais.
* Parâmetros de métodos.
* `if __name__ == '__main__':`.
* Organização de um programa em funções e classes.

## Estrutura

O simulador é dividido em três classes principais:

### `Email`

Representa uma mensagem de e-mail.

Armazena:

* Remetente.
* Destinatário.
* Assunto.
* Corpo.
* Data e hora.
* Status de leitura.

Também possui métodos para marcar a mensagem como lida, exibir seu conteúdo completo e representar o e-mail como texto.

### `User`

Representa um usuário do sistema.

Cada usuário possui:

* Nome.
* Caixa de entrada própria.

A classe permite enviar e-mails, verificar a caixa de entrada, ler mensagens e excluí-las.

### `Inbox`

Representa a caixa de entrada de um usuário.

É responsável por:

* Armazenar os e-mails recebidos.
* Receber novas mensagens.
* Listar os e-mails.
* Localizar e ler mensagens.
* Excluir mensagens.
* Validar índices informados pelo usuário.

## Exemplo de fluxo

O programa cria dois usuários:

```text
Tory
Ramy
```

Tory envia um e-mail para Ramy:

```text
Subject: Hello
Body: Hi Ramy, just saying hello!
```

Ramy responde:

```text
Subject: Re: Hello
Body: Hi Tory, hope you are fine.
```

Em seguida, Ramy:

1. Verifica sua caixa de entrada.
2. Lê o primeiro e-mail.
3. Exclui o primeiro e-mail.
4. Verifica novamente sua caixa de entrada.

## Exemplo de saída

```text
Email sent from Tory to Ramy!

Email sent from Ramy to Tory!

Ramy's Inbox:

Your Emails:
1. [Unread] From: Tory | Subject: Hello | Time: 2026-...

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2026-...
Body: Hi Ramy, just saying hello!
------------

Email deleted.

Ramy's Inbox:
Your inbox is empty.
```

## Como executar

Com o Python instalado, execute o arquivo principal pelo terminal:

```bash
python main.py
```

O programa executará automaticamente a função `main()` quando o arquivo for executado diretamente.

## Aprendizado

Este laboratório reforça a ideia de que classes podem trabalhar em conjunto para representar diferentes entidades de um sistema.

O projeto também demonstra como um objeto pode possuir outro objeto como atributo. Neste caso, cada `User` possui uma `Inbox`, enquanto cada `Inbox` armazena objetos `Email`.

A construção foi realizada passo a passo, permitindo praticar a decomposição de um problema maior em classes, atributos e métodos menores e reutilizáveis.
