# 🎬 YouTube Video Analyzer — AI-Powered Content Intelligence
> **Instantly transform any YouTube video into a structured, timestamped analysis report using Groq's LLaMA-3.3-70B and the Agno agentic framework.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA--3.3--70B-orange?style=flat)](https://console.groq.com)
[![Agno](https://img.shields.io/badge/Agno-Agent%20Framework-blueviolet?style=flat)](https://github.com/agno-agi/agno)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Live Demo
🔗 **[Try it live →](https://youtube-video-analyzer-ai-ejo7czzqvevhwqmonzmctd.streamlit.app/)**  

## Overview
This project is an **AI-powered YouTube content analysis tool** that ingests any YouTube video URL and produces 
a comprehensive structured report — complete with auto-generated timestamps, content segmentation,
topic progression mapping, and key learning point extraction.It is built on an **agentic architecture** 
using the [Agno](https://github.com/agno-agi/agno) framework, powered by **Groq's ultra-fast LLaMA-3.3-70B-Versatile** model 
for real-time LLM inference, and served through an interactive **Streamlit** web interface.

## Features
|  Feature                  | Description |
|  **Agentic Pipeline**     | Tool-augmented AI agent with autonomous reasoning via Agno |
|  **Ultra-fast Inference** | Powered by Groq's hardware-accelerated LLaMA-3.3-70B |
|  **Auto Timestamping**    | Precise `[start, end, summary]` timestamp generation |
|  **Content Segmentation** | Groups related segments and tracks topic transitions |
|  **Responsive UI**        | Clean, interactive Streamlit web interface |
|  **Markdown Reports**     | Structured, formatted output with emoji-based content tagging |
|  **Secure Secrets**       | API keys managed via Streamlit secrets — never hardcoded |

## Architecture

```
User Input (YouTube URL)
        │
        ▼
  Streamlit UI (ui.py)
        │
        ▼
  Agno Agent (youtube_analyzer.py)
        │   ├── Model: Groq LLaMA-3.3-70B-Versatile
        │   └── Tool: YouTubeTools (transcript extraction)
        │
        ▼
  Structured Markdown Report
        │
        ▼
  Rendered in Browser
```

## Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Groq — LLaMA-3.3-70B-Versatile |
| **Agent Framework** | Agno |
| **YouTube Tool** | `youtube_transcript_api` via Agno's YouTubeTools |
| **Frontend** | Streamlit |
| **Secrets Management** | Streamlit Secrets / python-dotenv |
| **Deployment** | Streamlit Community Cloud |

## Local Setup
### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-video-analyzer-ai.git
cd youtube-video-analyzer-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at [console.groq.com](https://console.groq.com)

### 5. Run the app

```bash
streamlit run ui.py
```

Open your browser at `http://localhost:8501`

---

## Environment Variables
| Variable | Required | Description |
|---|---|---|
| `GROQ_API_KEY` | Yes | Groq API key for LLaMA-3.3-70B inference |

> **Never commit your `.env` file.** It is included in `.gitignore` by default.

## Project Structure

```
youtube-video-analyzer-ai/
├── ui.py                   # Streamlit frontend
├── youtube_analyzer.py     # Agno agent definition
├── requirements.txt        # Python dependencies
├── packages.txt            # System-level dependencies
├── .gitignore              # Git ignore rules
├── .streamlit/
│   └── secrets.toml        # Local secrets (not pushed to Git)
└── README.md               # This file
```
## Deployment (Streamlit Community Cloud)
This app is deployed via [Streamlit Community Cloud](https://share.streamlit.io) connected to this GitHub repository.
To redeploy after changes:
```bash
git add .
git commit -m "your update message"
git push origin main
```
Streamlit Cloud will automatically detect the push and redeploy.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
Built by **[Nitin Kumawat](www.linkedin.com/in/nitin-ku04)**
