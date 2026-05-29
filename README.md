# Assistente Inteligente para Monitoramento de Pressão Arterial

Projeto desenvolvido na disciplina Projeto de Extensão de Aprendizado de Máquina do Centro Universitário Unicarioca.

O sistema auxilia no registro, acompanhamento e organização de medições de pressão arterial, com foco em simplicidade e facilidade de uso.

---

## Objetivo

Permitir que usuários realizem registros simples de pressão arterial, possibilitando acompanhamento contínuo das medições e identificação automática de categorias de risco.

---

## Funcionalidades

* Cadastro de medições de pressão arterial
* Histórico de registros
* Classificação automática da pressão arterial
* Identificação visual por cores e indicadores
* Registro automático de data e horário
* Conversão automática de valores simplificados

  * Exemplo:

    * 12 → 120
    * 8 → 80
* Interface simples

---

## Tecnologias Utilizadas

* Python
* Flask
* SQLite
* HTML
* CSS
* JavaScript

---

## Estrutura do Projeto

app_pressao/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── historico.html
│
├── static/
│   ├── style.css
│   └── script.js

---

## Como Executar

### 1. Instalar as dependências

pip install flask

---

### 2. Executar o sistema

python app.py

---

### 3. Abrir no navegador

http://127.0.0.1:5000

---

## Classificação Utilizada

| Categoria   | Indicador |
| ----------- | --------- |
| Normal      | 🟢        |
| Atenção     | 🟡        |
| Hipertensão | 🟠        |
| Risco Alto  | 🔴        |

---

## Observações

O projeto possui caráter acadêmico, educativo e informativo, não substituindo acompanhamento médico profissional.

A proposta prioriza simplicidade e organização das informações relacionadas ao monitoramento da pressão arterial.

---

## Integrantes

* Ana Guernelli
* Lucas Bentes
* Vannia Queiroz

Orientador:
Almir Fernandes
