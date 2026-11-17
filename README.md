# Gerador de Senhas em Python

Um gerador de senhas aleatórias desenvolvido em **Python**, com opções de personalização e validação de entradas. O projeto permite criar senhas de acordo com as preferências do usuário, escolhendo quais tipos de caracteres deseja incluir.

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da linguagem Python por meio de uma aplicação interativa executada no terminal.

O programa permite configurar o tamanho da senha, selecionar os tipos de caracteres utilizados e gerar novas senhas sem precisar reiniciar a aplicação.

## Funcionalidades

- **Tamanho personalizado:** geração de senhas com comprimento entre 6 e 50 caracteres.
- **Seleção de caracteres:** escolha entre letras minúsculas, números e caracteres especiais.
- **Geração aleatória:** utilização do módulo `random` para selecionar os caracteres.
- **Validação de entradas:** tratamento de valores inválidos e opções fora dos limites permitidos.
- **Geração contínua:** possibilidade de criar várias senhas durante a mesma execução.
- **Alteração de preferências:** permite modificar as configurações antes de gerar uma nova senha.

## Tecnologias utilizadas

- **Python 3**
- **Módulo random** — geração de caracteres aleatórios.
- **Terminal** — interface de interação com o usuário.

## Como executar

### Pré-requisitos

- Python 3 instalado em sua máquina.
- Git (opcional, para clonar o repositório).

### Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/DanielFerreira76/gerador-de-senha.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd gerador-de-senha
   ```

3. Execute o programa:

   ```bash
   python gerador.py
   ```

   Caso necessário, utilize:

   ```bash
   python3 gerador.py
   ```

## Exemplo de utilização

Ao executar o programa, o usuário poderá configurar as características da senha:

```text
======================
  Gerador de Senhas
======================
Incluir letras? [0 = não / 1 = sim] 1
Incluir números? [0 = não / 1 = sim] 1
Incluir caracteres especiais? [0 = não / 1 = sim] 1
Tamanho da senha: [entre 6 e 50] 12

A senha gerada foi: a8@k2#m9p$x1

Quer gerar outra senha? [0 = não / 1 = sim]
```

*Exemplo ilustrativo de execução.*

## Conceitos praticados

Durante o desenvolvimento, foram aplicados conceitos importantes de programação:

- Definição e utilização de funções.
- Variáveis e manipulação de strings.
- Estruturas condicionais (`if`, `elif` e `else`).
- Estruturas de repetição (`while` e `for`).
- Tratamento de exceções com `try` e `except`.
- Utilização de módulos e funções da biblioteca padrão.
- Validação de dados fornecidos pelo usuário.

## Objetivo de aprendizado

Este projeto faz parte da minha jornada de aprendizado em programação e desenvolvimento de software. Seu desenvolvimento contribuiu para consolidar conhecimentos fundamentais de Python e exercitar a construção de aplicações interativas.

---

**Desenvolvido por [Daniel Ferreira Vieira](https://github.com/DanielFerreira76)**

*Estudante de Engenharia de Software | Desenvolvedor em formação*
