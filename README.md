# EdgeFix AI: On-Device Multimodal Maintenance Copilot

[![Snapdragon AI Lab Challenge 2026](https://img.shields.io/badge/Snapdragon-AI%20Lab%202026-0075FF)](https://unstop.com)
[![Platform](https://img.shields.io/badge/Platform-Windows%2011%20ARM64-blue)](https://microsoft.com)
[![Acceleration](https://img.shields.io/badge/NPU-Qualcomm%20Hexagon-brightgreen)](https://qualcomm.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**EdgeFix AI** is a private, zero-cloud, multimodal field-troubleshooting copilot built for Snapdragon-powered HP PCs. It accepts camera feeds, spoken voice input, and local PDF service manuals to produce real-time, evidence-ranked diagnostic steps—completely offline.

---

## Key Features

- **On-Device Vision:** Real-time component, display, and indicator LED identification via INT8 quantized visual models running on the Qualcomm Hexagon NPU.
- **Local Speech-to-Text:** Hands-free symptom description transcribes voice locally using Whisper-Tiny from Qualcomm AI Hub.
- **Offline Retrieval Augmented Generation (RAG):** Fast vector search across large service manuals stored locally in your knowledge base.
- **Privacy & Power Efficient:** Zero telemetry, 100% offline execution, preserving laptop battery life during extended field operations.

---

## System Architecture & Snapdragon Optimization

EdgeFix AI routes perception and vector search workloads to the Hexagon NPU via ONNX Runtime with the Qualcomm QNN Execution Provider (`QNNHtp.dll`), while falling back gracefully to the CPU when required.

