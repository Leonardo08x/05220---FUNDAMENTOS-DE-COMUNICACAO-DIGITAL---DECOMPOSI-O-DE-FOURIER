import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

# Importando sua classe modularizada
# Certifique-se de que o arquivo se chama fourier_logic.py ou ajuste o import
from classe_decompisão.decomposicao import decomposicao_fourier

class FourierGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de Decomposição de Fourier")
        self.setMinimumSize(900, 700)
        
        # Instanciando sua classe de lógica
        self.dec = decomposicao_fourier()
        
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # --- Cabeçalho e Explicação ---
        title = QLabel("Decomposição de Fourier: Análise da Onda Quadrada")
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        info_text = QLabel()
        info_text.setWordWrap(True)
        info_text.setTextFormat(Qt.TextFormat.RichText)
        info_text.setText("""
        <p style="font-size: 14px; line-height: 1.6;">
        <b>Introdução à Decomposição de Fourier</b><br>
        A análise de Fourier é uma ferramenta matemática fundamental que permite decompor qualquer sinal periódico em uma soma infinita de funções senoidais (senos e cossenos) de diferentes frequências. Essa decomposição revela a composição espectral do sinal, mostrando quais frequências estão presentes e com que amplitudes.
        </p>
        
        <p style="font-size: 14px; line-height: 1.6;">
        <b>O Caso da Onda Quadrada</b><br>
        A onda quadrada é um sinal periódico simples, alternando entre valores +1 e -1. Sua série de Fourier contém apenas harmônicos ímpares (frequências múltiplas ímpares da frequência fundamental), pois é uma função ímpar. A fórmula geral para a onda quadrada é:
        </p>
        
        <p style="font-size: 14px; line-height: 1.6; text-align: center; background-color: #f9f9f9; padding: 10px; border-radius: 5px;">
        <b>f(t) = (4/π) Σ<sub>k=1,3,5,...∞</sub> (1/k) · sin(k · ω₀ · t)</b>
        </p>
        
        <p style="font-size: 14px; line-height: 1.6;">
        Onde:<br>
        • k representa os harmônicos ímpares (1, 3, 5, 7, ...)<br>
        • ω₀ é a frequência angular fundamental (2π/T, onde T é o período)<br>
        • O coeficiente (4/π) normaliza a amplitude<br>
        • Cada termo (1/k) diminui a contribuição dos harmônicos mais altos
        </p>
        
        <p style="font-size: 14px; line-height: 1.6;">
        <b>Como a Soma se Constrói</b><br>
        Começamos com o primeiro harmônico (k=1): uma senoide pura que oscila lentamente. Adicionamos o terceiro harmônico (k=3), que vibra três vezes mais rápido e contribui menos (1/3 da amplitude). Continuamos somando termos ímpares sucessivos, cada um adicionando detalhes mais finos ao sinal. Matematicamente:
        </p>
        
        <p style="font-size: 14px; line-height: 1.6; text-align: center; background-color: #f0f8ff; padding: 10px; border-radius: 5px;">
        f(t) ≈ (4/π) [sin(t) + (1/3)sin(3t) + (1/5)sin(5t) + ... + (1/k)sin(kt)]
        </p>
        
        <p style="font-size: 14px; line-height: 1.6;">
        <b>Convergência e Fenômeno de Gibbs</b><br>
        À medida que aumentamos o número de termos na soma, a aproximação se torna cada vez mais precisa. No entanto, devido ao fenômeno de Gibbs, a soma nunca alcança exatamente o valor da onda quadrada nos pontos de descontinuidade, apresentando overshoot (sobressalto) de aproximadamente 18% do salto.
        </p>
        
        <p style="font-size: 14px; line-height: 1.6;">
        <b>Interatividade</b><br>
        Use o controle abaixo para variar o número de termos na soma e observe como o sinal se aproxima gradualmente da forma quadrada ideal. Cada termo adicional refina a representação, demonstrando o poder da síntese de Fourier.
        </p>
        """)
        layout.addWidget(info_text)

        formula = QLabel()
        formula.setTextFormat(Qt.TextFormat.RichText)
        formula.setText("""
        <p style="font-size: 14px; text-align: center; background-color: #e8f4f8; padding: 15px; border-radius: 8px; border: 1px solid #ccc;">
        <b>Fórmula Completa da Série de Fourier para Onda Quadrada:</b><br>
        f(t) = Σ<sub>n=1,3,5,...∞</sub> (4/(π·n)) · sin(n·t)
        </p>
        """)
        layout.addWidget(formula)

        # --- Área de Input ---
        input_layout = QHBoxLayout()
        self.label_input = QLabel("Número de termos (soma):")
        self.input_termos = QLineEdit()
        self.input_termos.setPlaceholderText("Ex: 10")
        self.btn_processar = QPushButton("Gerar Gráfico")
        self.btn_processar.clicked.connect(self.executar_pipeline)

        input_layout.addWidget(self.label_input)
        input_layout.addWidget(self.input_termos)
        input_layout.addWidget(self.btn_processar)
        layout.addLayout(input_layout)

        # --- Exibição do Resultado ---
        self.area_imagem = QLabel("O gráfico aparecerá aqui após o processamento.")
        self.area_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.area_imagem.setStyleSheet("border: 1px solid #ccc; background: white;")
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.area_imagem)
        layout.addWidget(scroll)

    def executar_pipeline(self):
        try:
            termos = int(self.input_termos.text())
            if termos <= 0: raise ValueError
            
            # Chama o método da sua classe
            # Dica: No seu código original, plt.show() trava a interface. 
            # O ideal seria sua classe apenas salvar o arquivo.
            self.dec.processo(termos)
            
            # Caminho onde o arquivo é gerado pela sua classe
            path_imagem = "output/decomposicao_fourier.png"
            
            if os.path.exists(path_imagem):
                pixmap = QPixmap(path_imagem)
                # Redimensiona para caber na tela mantendo o aspecto
                scaled_pixmap = pixmap.scaled(self.area_imagem.size(), 
                                              Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
                                              Qt.TransformationMode.SmoothTransformation)
                self.area_imagem.setPixmap(scaled_pixmap)
            else:
                self.area_imagem.setText("Erro: Imagem não encontrada no diretório output/.")
                
        except ValueError:
            self.area_imagem.setText("Por favor, insira um número inteiro positivo.")
#aspectRatioMode:
#keepAspectRatio
#keepAspectRatioByExpanding
#IgnoreAspectRatio
if __name__ == "__main__":
    # Garante que a pasta output exista para não dar erro na sua classe
    if not os.path.exists("output"):
        os.makedirs("output")
        
    app = QApplication(sys.argv)
    window = FourierGUI()
    window.show()
    sys.exit(app.exec())