# 🚗 AI-Powered Car Diagnostic Agent (WIP)

An intelligent vehicle health assistant that bridges the gap between raw OBD-II data and human-understandable mechanical advice. This project uses **Groq Llama 3** to analyze fault codes and live sensor data in real-time.

> **⚠️ WORK IN PROGRESS**: This project is currently in active development. The Core AI engine and API backend are functional, while the mobile frontend is currently being architected.

## 🌟 Key Features
- **Real-time OBD-II Integration**: Connects to vehicles via ELM327 adapters (USB/Bluetooth).
- **Groq AI Analysis**: Processes DTC (Diagnostic Trouble Codes) using Llama 3 for professional-grade mechanical insights.
- **Simulator Mode**: A robust testing framework to simulate engine failures (misfires, overheating, etc.) without a physical car.
- **FastAPI Backend**: A decoupled professional architecture ready for mobile app integration.

## 🏗️ The Architecture
The project follows a modern **Client-Server** model:
1. **The Brain (Backend)**: Python FastAPI server handling AI logic and data processing.
2. **The Interface (Frontend)**: [In Progress] A mobile application to interface with the car's Bluetooth hardware.



## 🚀 Current Progress (Roadmap)
- [x] Create Mock OBD library for rapid testing.
- [x] Integrate Groq Cloud API for high-speed LLM inference.
- [x] Build FastAPI backend for remote diagnostics.
- [ ] Implement SQLite/PostgreSQL database for vehicle history.
- [ ] Develop Flutter mobile application.
- [ ] Deploy backend to cloud (Render/Railway).

## 🛠️ Tech Stack
- **Language**: Python 3.11+
- **AI Model**: Llama 3 (via Groq Cloud)
- **Frameworks**: FastAPI, Uvicorn
- **Hardware Protocol**: OBD-II (ELM327)
- **Environment**: Dotenv for secure API management

## 🔧 Installation & Testing
To test the AI logic using the simulator:

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/yourusername/car_diagnostic_agent.git](https://github.com/yourusername/car_diagnostic_agent.git)