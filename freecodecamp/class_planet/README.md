# 🪐 Classe Planet

Exercício em Python focado em conceitos de **Programação Orientada a Objetos (POO)**, desenvolvido como parte da minha jornada de aprendizado em Python.

## 🎯 Objetivo

Criar uma classe `Planet` capaz de representar um planeta e sua relação com sua estrela.

A classe realiza validações dos dados recebidos durante a criação do objeto e possui métodos para exibir informações sobre o planeta e sua órbita.

## 🧠 Conceitos praticados

* Classes e objetos
* Construtor `__init__`
* Atributos de instância
* `self`
* Métodos personalizados
* Método especial `__str__`
* Validação de dados
* `TypeError` e `ValueError`
* F-strings
* Instanciação de objetos

## 🔧 Implementação

A classe `Planet` recebe três propriedades:

* `name` — nome do planeta
* `planet_type` — tipo do planeta
* `star` — estrela ao redor da qual o planeta orbita

O construtor valida se os três valores são strings e se não estão vazios.

A classe também possui:

* `orbit()` — retorna uma mensagem informando que o planeta está orbitando sua estrela.
* `__str__()` — retorna uma descrição formatada do planeta.

## ▶️ Exemplo

```python
planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Proxima Centauri b", "Super-Earth", "Proxima Centauri")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
```

### Output

```text
Planet: Earth | Type: Terrestrial | Star: Sun
Planet: Jupiter | Type: Gas Giant | Star: Sun
Planet: Proxima Centauri b | Type: Super-Earth | Star: Proxima Centauri

Earth is orbiting around Sun...
Jupiter is orbiting around Sun...
Proxima Centauri b is orbiting around Proxima Centauri...
```

## 📚 Contexto do aprendizado

Este exercício foi desenvolvido como parte dos meus estudos de Python, com o objetivo de reforçar conceitos fundamentais da linguagem e aprofundar meus conhecimentos em **Programação Orientada a Objetos**.
