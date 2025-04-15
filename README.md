# 👁️‍🗨️ Projeto de Visão Computacional para Detecção de Quedas em Plataformas de Petróleo

> *"Porque o mar não perdoa, mas a tecnologia pode ajudar a salvar."*

## 🎯 Objetivo

Este projeto tem como finalidade o desenvolvimento de um sistema inteligente baseado em **visão computacional** para a **detecção de quedas de seres humanos em plataformas de petróleo**. O foco é garantir a segurança de trabalhadores em ambientes hostis e de difícil acesso, promovendo uma resposta rápida em situações críticas.

Ao identificar a queda, o sistema aciona automaticamente um **robô submarino autônomo** que será responsável por executar a missão de resgate, localizando a vítima e fornecendo auxílio emergencial até a chegada da equipe especializada.

> Embora pensado inicialmente para plataformas de petróleo, este sistema pode ser adaptado para diversos outros contextos — desde portos, navios, até áreas de lazer com acesso ao mar.

## 🧠 Tecnologias Utilizadas

- 🐍 **Python**
- 🎯 **YOLO (You Only Look Once)**
- 🎥 **OpenCV**
- 🤖 **Arduino**
- 🔌 **PyFirmata / Firmata**

## 🔧 Funcionamento

1. A câmera captura o ambiente em tempo real.
2. O modelo YOLO identifica pessoas na cena.
3. Caso uma queda seja detectada, o sistema envia um sinal via Arduino.
4. O Arduino aciona o **robô subaquático autônomo**.

## 🛠️ Como Rodar o Projeto

### Pré-requisitos

- Python 3.8+
- Arduino Uno
- Webcam
- YOLOv5
- PyFirmata
- OpenCV
