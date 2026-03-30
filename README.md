# PsiBot

Chatbot de apoyo psicológico basado en inteligencia artificial, diseñado para brindar soporte emocional mediante técnicas de terapia cognitivo-conductual (TCC). Utiliza el modelo **Llama 2 7B** ajustado con LoRA y cuenta con detección de mensajes de alto riesgo con alertas automáticas por correo.

## Características

- Respuestas empáticas generadas con un LLM (Llama 2 7B Chat) fine-tuneado
- Detección de mensajes de riesgo (ideación suicida, autolesiones, desesperanza)
- Alertas por correo electrónico cuando se detecta un mensaje de alto riesgo
- Contexto conversacional: mantiene las últimas 4 interacciones para coherencia
- Interfaz web de chat (Flask + HTML/CSS/JS)
- Exposición pública automática mediante túnel Ngrok

## Estructura del proyecto

```
PsiBotRepo/
├── app.py              # Aplicación Flask principal y configuración de Ngrok
├── modelo.py           # Carga e inicialización del modelo LLM
├── evaluador.py        # Módulo de detección de riesgo por palabras clave
├── respuesta.py        # Generación de respuestas con contexto conversacional
├── correo.py           # Envío asíncrono de alertas por correo
├── requirements.txt    # Dependencias Python
├── static/
│   ├── css/style.css   # Estilos de la interfaz de chat
│   └── js/chat.js      # Lógica del frontend
└── templates/
    ├── base.html        # Plantilla base HTML
    └── index.html       # Página principal del chat
```

## Requisitos

- Python 3.9+
- GPU con soporte CUDA (recomendado para inferencia con Llama 2)
- Cuenta de Ngrok (para exposición pública)
- Cuenta de Gmail con contraseña de aplicación (para alertas por correo)

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/lolociv/psibotrepo.git
cd psibotrepo
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno (ver sección siguiente).

## Configuración

Antes de ejecutar, define las siguientes variables de entorno para evitar exponer credenciales:

```bash
export NGROK_AUTH_TOKEN="tu_token_de_ngrok"
export GMAIL_USER="tu_correo@gmail.com"
export GMAIL_PASSWORD="tu_contraseña_de_aplicacion"
export ALERT_EMAIL="correo_destino_alertas@ejemplo.com"
```

> **Importante:** No incluyas credenciales directamente en el código. Usa variables de entorno o un archivo `.env` (agregado a `.gitignore`).

## Uso

Ejecuta la aplicación:

```bash
python app.py
```

Al iniciar, se mostrará en consola la URL pública generada por Ngrok. Abre esa URL en tu navegador para acceder al chat.

## Funcionamiento interno

1. **Evaluación de riesgo** (`evaluador.py`): Analiza cada mensaje del usuario buscando palabras y frases asociadas a ideación suicida, autolesiones y desesperanza (en español e inglés).
2. **Generación de respuesta** (`respuesta.py`): Construye el prompt adecuado según el nivel de riesgo y genera una respuesta empática con el modelo LLM, manteniendo el contexto de la conversación.
3. **Alerta por correo** (`correo.py`): Si se detecta riesgo alto, se envía un correo de alerta de forma asíncrona para no interrumpir la experiencia del usuario.
4. **Modelo** (`modelo.py`): Carga Llama 2 7B Chat con cuantización de 8 bits (bitsandbytes) y adapters LoRA (PEFT) para reducir el consumo de memoria.

## Dependencias principales

| Paquete | Uso |
|---|---|
| `torch` / `transformers` | Inferencia con Llama 2 |
| `peft` | Fine-tuning con LoRA |
| `bitsandbytes` | Cuantización 8-bit |
| `flask` | Servidor web |
| `pyngrok` | Túnel público |
| `sentence-transformers` | Herramientas de similitud semántica |

## Consideraciones de seguridad

- Nunca expongas tokens de Ngrok ni credenciales de correo en el código fuente.
- Agrega un archivo `.env` para manejar secretos y asegúrate de incluirlo en `.gitignore`.
- Este proyecto está orientado a soporte emocional complementario y **no reemplaza la atención profesional de salud mental**.

## Licencia

Este proyecto es de uso educativo y experimental. Consulta con el equipo antes de desplegarlo en entornos de producción.
