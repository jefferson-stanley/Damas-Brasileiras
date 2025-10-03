# Jogo de Damas em Python

Este projeto implementa o clássico jogo de Damas (**Checkers**) em Python, seguindo as regras oficiais, incluindo movimentação de peões e damas, promoção, **capturas obrigatórias**, e a regra de **capturas em série**.

---

## ♟️ Regras Implementadas

O jogo adere estritamente às seguintes regras:

* **Peões:** Movimentam-se apenas uma casa na diagonal **para frente**, com a exceção do movimento de captura, que pode ser realizado na diagonal para trás.
* **Damas:** Podem movimentar-se várias casas na diagonal, tanto para frente quanto para trás, desde que o caminho esteja livre.
* **Promoção:** Um peão é promovido a dama ao atingir a última linha do tabuleiro adversário.
* **Captura Obrigatória:** Se houver qualquer captura possível no tabuleiro, o jogador é forçado a realizá-la.
* **Capturas em Série:** Após realizar uma captura, se a mesma peça puder capturar novamente (conforme a regra), o jogador deve continuar a sequência de capturas até que não haja mais movimentos de captura disponíveis para aquela peça.

---

## 📁 Estrutura do Projeto

O código está organizado em dois arquivos principais:

* **todas\_funcoes.py:** Contém a lógica central do jogo. Inclui todas as funções necessárias para:
    * Geração de movimentos possíveis.
    * Verificação de capturas e capturas em série.
    * Aplicação das regras de promoção.
    * Contagem de peças e estado do jogo.

* **main.py:** É o ponto de entrada do programa. É responsável por:
    * Inicializar o tabuleiro 8x8.
    * Gerenciar o *loop* principal da partida entre os dois jogadores.
    * Tratar a interação com o usuário.

---

## 🎮 Como Jogar

O jogo é executado diretamente no **terminal** e o tabuleiro é exibido como uma matriz 8x8.

### Passos:

1.  Execute o arquivo `main.py`.
2.  Na sua vez, o sistema solicitará duas entradas:
    * **Coordenadas da peça** a ser movida (ex: `3A`).
    * **Coordenadas do destino** (casa de pouso) (ex: `4B`).
3.  O sistema validará o movimento conforme as regras implementadas (incluindo a obrigação de capturar).

---

## 🏁 Encerramento da Partida

A partida é finalizada quando:

* Um dos jogadores não possui mais peças no tabuleiro.
* Um dos jogadores não pode realizar mais nenhum movimento válido (está "**bloqueado**").

---

## 🚀 Instalação e Execução

Para rodar o projeto localmente, siga os passos:

1.  Clone o repositório:

    ```bash
    git clone [Link do seu Repositório]
    ```

2.  Entre no diretório do projeto:

    ```bash
    cd [Nome do seu Repositório]
    ```

3.  Execute o arquivo principal:

    ```bash
    python main.py
    ```

---

*Este é um projeto desenvolvido para fins de aprendizado/prática e está aberto a contribuições.*
