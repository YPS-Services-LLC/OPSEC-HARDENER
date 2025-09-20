# OPSEC-HARDENER

[![Build Status](https://github.com/YPS-Services-LLC/OPSEC-HARDENER/actions/workflows/ci.yml/badge.svg)](https://github.com/YPS-Services-LLC/OPSEC-HARDENER/actions/workflows/ci.yml)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/YPS-Services-LLC/OPSEC-HARDENER)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

**OPSEC-HARDENER** is a modular Linux security toolkit.

## 🚀 Features
- Network Hardening (fake ethernet, kill switch, WiFi radio control)  
- Monitoring (libinput movements, network traffic, firewall rules)  
- Sys-Snapshots Integration (before/after audit trail with GPG signing)  
- Tamper-Proof Licensing (hashfile manifests, Cloudflare Zero Trust SaaS integration planned)

## 📦 Installation
Clone and install:

    git clone git@github.com:YPS-Services-LLC/OPSEC-HARDENER.git
    cd OPSEC-HARDENER
    pip install -e .

## 🖥️ Usage
Run GUI:

    opsec-gui

Run CLI:

    opsec --kill-switch wlan0

## 🧪 Testing

    pytest -v

## 📊 Workflow
- main → stable
- dev → active work

## 📜 License
MIT License.

## 🤝 Contributing
1. Fork repo  
2. Branch (`git checkout -b feature/foo`)  
3. Commit & push  
4. Open PR  

## 🛡️ Roadmap
- [x] Scaffold + CI  
- [x] Snapshots + GPG signing  
- [ ] Monitoring tab  
- [ ] Cloudflare Zero Trust licensing  
- [ ] v1.0.0 Stable Release

