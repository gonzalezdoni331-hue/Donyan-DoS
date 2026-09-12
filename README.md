# Donyan-DoS
Un mini programa de ataque de Denegacion de servicios, cualquier contribucion me ayudaria muchisimo

# 🐍 MEDUSA - Layer 7 DDoS Tool

> **High-Performance, Multi-Threaded HTTP Flood Tool for Penetration Testing**

<div align="center">
  <img src="https://img.shields.io/badge/Version-3.1.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/Language-Python%203-orange" alt="Language">
  <img src="https://img.shields.io/badge/Status-Stable-green" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</div>

<br>

**MEDUSA** is a robust, lightweight, and fast HTTP Flood tool designed for testing the resilience of web servers under load. Written in Python 3, it utilizes multi-threading to simulate thousands of concurrent connections with a minimalist, hacker-aesthetic terminal interface.

### ✨ Features

- 🚀 **High Performance:** Multi-threaded architecture for maximum throughput.
- 🎨 **Retro Terminal UI:** Clean, neon-colored logs with real-time status updates.
- 🛡️ **User-Agent Rotation:** Automatically rotates User-Agents to mimic diverse clients.
- ⏱️ **Configurable:** Set duration, thread count, and request rates easily.
- 📦 **Zero Dependencies:** Uses only standard libraries + `requests` and `colorama`.
- 💻 **Cross-Platform:** Works on Linux, macOS, and Windows.

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gonzalezdoni331-hue/MEDUSA.git
   cd MEDUSA
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 🚀 Usage

Basic usage with default settings (100s attack, 10 threads):
```bash
python3 medusa.py <target_url>
