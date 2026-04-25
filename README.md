# Sleep Detector (Anti-Sono) 👁️💤

Um sistema de segurança baseado em **Visão Computacional** projetado para prevenir acidentes ou monitorar a produtividade, detectando sinais de fadiga através do fechamento dos olhos.

## 📋 Funcionalidades
* **Monitoramento via WebCam:** Rastreia os marcos faciais (*facial landmarks*) do usuário em tempo real.
* **Cálculo de EAR (Eye Aspect Ratio):** Algoritmo matemático que determina se o olho está aberto ou fechado.
* **Alerta de Segurança:** Se os olhos permanecerem fechados por mais de **3 segundos**, um alarme sonoro de alta intensidade é disparado.

## 🛠️ Tecnologias
* **Python**
* **OpenCV:** Para processamento de imagem e acesso à câmera.
* **Dlib / MediaPipe:** Para detecção precisa dos pontos dos olhos.
* **Pygame Mixer:** Para a execução do alarme sonoro.

## ⚙️ Lógica do Sistema
O script analisa a relação de aspecto do olho (EAR). A fórmula utilizada para calcular a abertura é:

$$EAR = \frac{||p_2 - p_6|| + ||p_3 - p_5||}{2||p_1 - p_4||}$$

Quando essa distância cai abaixo de um limiar por um tempo $t > 3s$, o evento de **"Sono Detectado"** é acionado.

## 🚀 Como Iniciar

Certifique-se de ter as dependências instaladas e execute:

```bash
python main.py
