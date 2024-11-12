# Jogo da Vida de Conway

Este é uma implementação do clássico **Jogo da Vida de Conway** utilizando a biblioteca `pygame` para renderização e `numpy` para manipulação de dados da grid. O jogo simula a evolução de células em um grid bidimensional com base em regras simples de vizinhança.

## Requisitos

Antes de rodar o projeto, você precisará instalar as dependências:

- Python 3.x
- Pygame
- Numpy

Você pode instalar as dependências com o seguinte comando:

```bash
pip install pygame numpy
```

## Como Rodar

1. Clone o repositório para o seu computador:

```bash
git clone https://github.com/Zer0G0ld/ConWay.git
cd ConWay
```

2. Execute o arquivo principal (`app.py` ou `main.py`) para iniciar a simulação.

### Para `app.py`:

```bash
python app.py
```

### Para `main.py`:

```bash
python main.py
```

## Como Jogar

- **Interação com o Mouse**: Clique nas células para alternar entre vivos e mortos.
- **Teclas de Controle**:
  - **Espaço (Space)**: Pausar e retomar o jogo.
  - **C**: Limpar todas as células e reiniciar o jogo.
  - **G**: Gerar células aleatórias para iniciar uma nova simulação.

## Regras do Jogo

O Jogo da Vida de Conway segue as seguintes regras:

1. **Células Vivas**: Uma célula viva com menos de 2 vizinhos morre de solidão. Com 2 ou 3 vizinhos vivos, sobrevive. Com mais de 3 vizinhos vivos, morre de superpopulação.
2. **Células Mortas**: Uma célula morta com exatamente 3 vizinhos vivos se torna uma célula viva (nascimento).

## Como Funciona

O grid é representado por uma matriz de células, onde cada célula pode estar em um dos dois estados: viva (1) ou morta (0). A cada iteração, o estado das células é atualizado com base nas regras descritas acima.

O jogo pode ser pausado a qualquer momento, e você pode interagir diretamente com o grid clicando para alterar o estado das células.

## Diferença entre `app.py` e `main.py`

Existem duas implementações diferentes do Jogo da Vida de Conway no projeto, cada uma com abordagens distintas para a renderização e atualização das células.

### `app.py`
- **Bibliotecas**: Usa apenas a biblioteca `pygame`.
- **Representação das Células**: Utiliza um conjunto de posições (`set`) para armazenar as células vivas, onde cada célula é representada por uma tupla de coordenadas `(coluna, linha)`.
- **Lógica de Atualização**: A atualização das células é feita manualmente através da função `adjust_grid`, que verifica os vizinhos de cada célula e aplica as regras do jogo.
- **Interatividade**: O jogo pode ser controlado com o teclado e o mouse. As células podem ser alternadas entre vivas e mortas ao clicar, e o jogo pode ser pausado ou reiniciado usando as teclas de controle.

### `main.py`
- **Bibliotecas**: Usa as bibliotecas `pygame` e `numpy`.
- **Representação das Células**: Utiliza uma matriz 2D (`numpy.ndarray`) para representar o grid, onde cada célula é um valor binário (0 para morta, 1 para viva).
- **Lógica de Atualização**: A atualização das células é feita de forma vetorizada utilizando `numpy`, o que torna o código mais eficiente ao calcular os vizinhos e atualizar o estado das células.
- **Interatividade**: A interação com o jogo é semelhante à de `app.py`, mas a simulação ocorre de forma contínua, sendo controlada principalmente pela tecla **Espaço** para pausar e retomar a execução.

| Aspecto               | `app.py`                                          | `main.py`                                     |
|-----------------------|---------------------------------------------------|-----------------------------------------------|
| **Bibliotecas**        | Usa apenas `pygame`.                             | Usa `pygame` e `numpy`.                       |
| **Representação das Células** | Conjunto de posições (set).                  | Matriz 2D (numpy.ndarray).                    |
| **Lógica de Atualização**  | Função `adjust_grid` com vizinhos manuais.     | Função `update` com operações vetorizadas.    |
| **Interatividade**     | Controle com teclado e mouse.                    | Controle com teclado e mouse, mas com foco em simulação contínua. |
| **Performance**        | Mais simples, usa o controle manual de vizinhos.  | Mais eficiente, usa `numpy` para operações vetorizadas. |


## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou encontrar problemas, por favor, abra uma issue ou faça um pull request.

## Licença

Este projeto está licenciado sob a licença APACHE 2.0 - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
