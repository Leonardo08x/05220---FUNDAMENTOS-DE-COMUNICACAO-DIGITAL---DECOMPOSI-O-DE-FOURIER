# Decomposição de Fourier - Simulador de Onda Quadrada

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Descrição

Este projeto é um simulador interativo para demonstrar a decomposição de Fourier de uma onda quadrada. Utilizando a série de Fourier, o aplicativo decompõe o sinal periódico em uma soma de funções senoidais (harmônicos ímpares), permitindo visualizar como a adição progressiva de termos aproxima a forma de onda original.

A interface gráfica, desenvolvida com PyQt6, oferece uma experiência intuitiva para explorar conceitos fundamentais de processamento de sinais, incluindo o fenômeno de Gibbs e a convergência da série.

### 🎯 Objetivos Educacionais
- Compreender a teoria da análise de Fourier para sinais periódicos.
- Visualizar a síntese de sinais através da soma de harmônicos.
- Explorar o impacto do número de termos na precisão da reconstrução.
- Demonstrar limitações como o overshoot de Gibbs em descontinuidades.

## 🚀 Funcionalidades

- **Decomposição Interativa**: Insira o número de termos da série de Fourier e visualize a reconstrução em tempo real.
- **Gráficos Detalhados**: Comparação entre a onda quadrada ideal e a soma aproximada.
- **Interface Amigável**: GUI responsiva com explicações teóricas integradas.
- **Exportação de Gráficos**: Geração automática de imagens PNG para análise posterior.
- **Suporte a Ambientes Virtuais**: Compatível com uv e pip para gerenciamento de dependências.

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Sistema operacional: Linux, macOS ou Windows

### Opção 1: Usando uv (Recomendado - Mais Rápido)
1. Instale o uv:
   ```bash
   # Linux/macOS
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   winget install astral-sh.uv
   ```

2. Clone ou navegue até o diretório do projeto.

3. Sincronize as dependências:
   ```bash
   uv sync
   ```

### Opção 2: Usando pip e requirements.txt
1. Certifique-se de ter o pip instalado (vem com Python).

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # ou .venv\Scripts\activate no Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Uso

### Executando o Aplicativo
- **Com uv**:
  ```bash
  uv run python main.py
  ```

- **Com pip** (após ativar o ambiente virtual):
  ```bash
  python main.py
  ```

### Como Usar a Interface
1. Abra o aplicativo.
2. Leia a explicação teórica na tela principal.
3. Insira o número de termos da série de Fourier (ex: 10).
4. Clique em "Gerar Gráfico".
5. Visualize o gráfico gerado na área de rolagem.
6. Ajuste o número de termos para observar a convergência.

### Exemplo de Uso Programático
```python
from classe_decompisão.decomposicao import decomposicao_fourier

dec = decomposicao_fourier()
dec.processo(5)  # Gera gráfico com 5 termos
```

## 🏗️ Estrutura do Projeto

```
decomposicao-fourier/
├── main.py                    # Interface gráfica principal (PyQt6)
├── classe_decompisão/
│   └── decomposicao.py        # Lógica de cálculo da decomposição de Fourier
├── output/                    # Diretório para gráficos gerados
├── pyproject.toml             # Configuração do projeto (uv)
├── requirements.txt           # Lista de dependências (pip)
└── README.md                  # Este arquivo
```

## 🧮 Fórmula Matemática

A série de Fourier para uma onda quadrada é dada por:

\[ f(t) = \frac{4}{\pi} \sum_{k=1,3,5,\dots}^{\infty} \frac{1}{k} \sin(k \cdot \omega_0 \cdot t) \]

Onde:
- \( k \): Harmônicos ímpares
- \( \omega_0 \): Frequência angular fundamental
- A soma converge para a onda quadrada, mas apresenta overshoot de Gibbs.

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

### Diretrizes
- Siga o estilo PEP 8 para código Python.
- Adicione testes para novas funcionalidades.
- Atualize a documentação conforme necessário.

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

