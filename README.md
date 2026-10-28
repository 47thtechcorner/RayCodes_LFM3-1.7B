<div align="center">
  <a href="https://youtu.be/9W65wLAiwEQ">
    <img src="https://img.youtube.com/vi/9W65wLAiwEQ/0.jpg" alt="Liquid AI Just Dropped LFM3: The 1GB Local AI Agent That Beats Qwen 9B!">
  </a>
  <h3>📺 <a href="https://youtu.be/9W65wLAiwEQ">Watch the full tutorial on YouTube</a></h3>
</div>

# LiquidAI/LFM3-1.7B: Local Tri-Hybrid Edge Agent

<div align="center">

| License | Model Size | WebArena Verified | Edge Memory |
| :---: | :---: | :---: | :---: |
| **LFM Open 1.0** | **1.73B Parameters** | **38.42 Score** | **~1.0 GB RAM (4-Bit)** |

</div>

> **LiquidAI/LFM3-1.7B** is a next-generation edge agent language model built on an automated hardware-in-the-loop tri-hybrid architecture. Combining 13 gated short convolutions, 5 sliding-window attention blocks, and 6 global attention layers, it achieves unprecedented long-prompt prefill throughput and supports a massive **256K context window** on consumer hardware.

---

## Benchmark & Workflow Summary

| Workflow | Capability Tested | Input Data | Generated Output |
| :--- | :--- | :--- | :--- |
| **Browser Action Sequencer** | Automated web shopping & checkout steps | E-commerce web store catalog HTML | Interactive browser action flow (HTML) |
| **256K Legal & Policy Auditor** | Spotting hidden contract risks in long files | Enterprise cloud master service agreement | Executive contract risk matrix (Markdown) |
| **Edge API Micro-Gateway** | Turning customer messages into API commands | Unstructured customer support ticket | Visual architecture dispatch graph (SVG) |

---

## Quick Start (Windows PowerShell)

### Step 1: Setup Environment, Download GGUF & Register in Ollama

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -U ollama huggingface_hub

hf download LiquidAI/LFM3-1.7B-GGUF LFM3-1.7B-QAD-Q4_0.gguf --local-dir models

ollama create lfm3-1.7b -f Modelfile
```

### Step 2: Run Production Pipeline

```powershell
python main.py
```

---

## Practical Use Cases

- 🛡️ **Offline Compliance & Contract Auditor:** Ingest massive 250K token enterprise NDAs, MSAs, and employment policies locally without transmitting proprietary legal clauses to third-party cloud APIs.
- ⚡ **Local E-Commerce & Web Workflow Bot:** Wire the 1.73B agent directly into headless browser controllers (Playwright / Puppeteer) to automate multi-step checkout and data harvesting with 38.42 WebArena reliability.
- 💳 **Edge Microservice API Router:** Deploy high-speed micro-gateways on base laptops and IoT edge boxes to convert unstructured user complaints into validated REST API dispatches with zero cloud latency.
- 📊 **Multi-Agent Workspace Matrix:** Run up to three distinct LFM3 agents concurrently (email triage, schedule optimization, and local SQL analysis) while keeping total combined system memory under 4 GB VRAM.

---

## Future Feature Roadmap

- 🌐 **Direct Playwright Browser Integration:** Real-time visual DOM tree observer and click-stream execution loop directly on desktop Chromium sessions.
- 🎙️ **Multi-Modal Cross-Attention Fusion:** Combine text agent planning with `LiquidAI/LFM3-Audio-2B` for real-time voice-driven tool dispatch.
- 🧠 **Local Vector RAG Accelerator:** Integrated FAISS / ChromaDB connector for hybrid sparse-dense retrieval over multimillion-word technical document bases.
- 🚀 **On-Device Continuous Fine-Tuning:** Single-GPU LoRA adapter training pipeline tailored for specialized enterprise ticket taxonomies.

---

## Search Tags

Liquid AI, LFM3 1.7B, Liquid AI LFM3, LFM3 GGUF, LFM3 local, LFM3 tutorial, LFM3 Ollama, LFM3 Hugging Face, local browser agent, LFM3 benchmark, LFM3 vs Qwen, WebArena agent, Liquid AI benchmark, LFM3 install, LiquidAI LFM3, LFM3 agent, Liquid LFM3, liquid ai, liquid ai model, Liquid AI model, LFM3 llama.cpp, liquid ai models, lfm2.5, lfm 2.5, liquidai, qwen 9b, liquid lfm, qwen 3.5 9b, lfm3 install, lfm3 benchmarks, liquid ai lfm3, liquid lfm2 1.2b, lfm3
