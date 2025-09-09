## 👨‍💻 Author
**Raj Kapasi**  
- 🌐 GitHub: [rajkapasi](https://github.com/rajkapasi)  
- 💼 LnkedIn: [Raj Kapasi](https://www.linkedin.com/in/raj-kapasi-5828b3335)  
- 📧 Email: rajkapasi2005@gmail.com


# 🚀 API Fuzzer in Python

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-Library-green.svg)](https://docs.python-requests.org/)
[![Colorama](https://img.shields.io/badge/Colorama-Colored%20Output-yellow.svg)](https://pypi.org/project/colorama/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

A **multithreaded API Fuzzer** written in Python 🐍 for cybersecurity testing.  
It discovers hidden endpoints by replacing the keyword `FUZZ` in the target URL with words from a wordlist.  

This project was built as part of my **ethical hacking & cybersecurity learning journey**.  

---

## ✨ Features
- 🔹 **Path & Query Fuzzing** → replace `FUZZ` in URLs or request body  
- 🔹 **Custom Headers Support** → e.g., `-H "Auth:Bearer TOKEN,User-Agent:Test"`  
- 🔹 **Multiple HTTP Methods** → GET, POST, PUT, etc.  
- 🔹 **Multithreading** → faster fuzzing with `-t` option  
- 🔹 **Delay Support** → throttle requests with `--delay`  
- 🔹 **JSON Output** → save results using `-o results.json`  
- 🔹 **Colored Output** → easy-to-read results with status codes  

---

## ⚡ Installation

### Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/api-fuzzer.git
cd api-fuzzer
  

