# 🛡️ DefendPS: Advanced PowerShell Threat Intelligence Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**DefendPS** is an enterprise-grade, Threat Intelligence and Defensive Security Library strictly focused on PowerShell. It is designed for SOC Analysts, Detection Engineers, Incident Responders (DFIR), and Threat Hunters.

Unlike standard cheatsheets, DefendPS dives into the absolute bleeding edge of PowerShell evasion, execution, and persistence techniques used by Tier-1 Nation-State actors, providing exact Splunk/Sigma detection rules, DFIR artifacts, and D3FEND mitigations.

## 👁️ Why DefendPS?
PowerShell is ubiquitous in enterprise environments, making it the weapon of choice for APTs (Advanced Persistent Threats) and ransomware operators. DefendPS maps these threats directly to the **MITRE ATT&CK** and **D3FEND** frameworks, providing actionable, zero-fluff intelligence.

##  Blind Spots Covered
DefendPS includes standard techniques (like AMSI bypasses and Download Cradles) but excels by exposing "Endgame" blind spots that bypass 99% of modern EDRs and SIEMs:
* **Fake 4104 (ScriptBlock Spoofing):** In-memory manipulation of ASTs to poison SIEM logs.
* **Pure In-Memory Eventing:** RAM-only persistence using .NET Timers (Zero WMI/Registry artifacts).
* **ETW Starvation:** Architecturally denying telemetry without triggering tampering alerts.
* **AD Attribute Staging:** Replicating fileless payloads across Domain Controllers via LDAP attributes.
* **TabExpansion Hijacking:** Keystroke execution before the user even presses 'Enter'.
* **Unicode & Homoglyph Evasion:** Bypassing ASCII-based YARA/Sigma rules via parser abuse.
* **EventLog Thread Suspension:** Phantom logging techniques to create silent time-gaps.
* **Compiled PS (PS2EXE) Reversing:** Analyzing C# wrapped payloads for Malware Analysts.

## 🛠️ How to Use
DefendPS is a fully self-contained, single-file application. No databases, no complex setups.
1. Download the `index.html` file.
2. Open it in any modern web browser.
3. Use the built-in search engine to instantly find techniques, evasion methods, or Splunk queries during an active incident.

### 🌐 Live Demo (GitHub Pages)
Access the live version of the platform here: https://defendps.github.io 

## 🤝 Contributing
Contributions from the Blue Team, Red Team, and DFIR communities are highly encouraged! If you have a newly discovered evasion technique or a solid detection rule, please open a Pull Request.

## ⚠️ Disclaimer
**For Educational and Defensive Purposes Only.** The techniques documented in this repository are intended to help security professionals build better detections, understand adversary tradecraft, and secure their environments. Do not use these techniques on systems you do not own or have explicit permission to test.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
