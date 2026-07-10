# 💼 AI Resume Analyzer & ATS Optimization Engine

An enterprise-grade, high-performance resume analysis application built using Python, Streamlit, and the Google Gemini-2.5-Flash LLM. This application tokenizes, parses, and contrasts a candidate’s PDF resume profile directly against target corporate job mandates to provide real-time ATS compatibility scoring, gap isolation, and granular bullet-point improvement plans.

## 🖥️ System Preview
<img src="Screenshots/Ai resume analyzer.png" alt="AI Resume Analyzer Dashboard" width="100%">

---

## 🚀 Core Features

* **PDF Ingestion & Structural Parsing:** Uses native byte-stream extractions to cleanly pull layout text parameters from raw `.pdf` documents.
* **ATS Compatibility Evaluation:** Instantly calculates alignment score indices using structured prompt isolation heuristics via advanced LLMs.
* **Gap Isolation Matrix:** Flags structural skill omissions and missing tech stacks (e.g., Vector Databases, Large Language Models) at a glance.
* **Granular Action Plans:** Generates clear, high-impact, actionable bullet points to optimize and tailor resume syntax.
* **On-the-Fly PDF Report Exporting:** Generates optimized compilation summary reports using an in-memory `fpdf2` binary buffer.

---

## 🛠️ Tech Stack Architecture

* **Frontend User Interface:** Streamlit (Layout engine, state persistence, handling responsive column layouts)
* **LLM Core Engine:** Google Gemini-2.5-Flash API (REST parsing architecture)
* **PDF Extraction:** PyPDF
* **Export Subsystem:** FPDF2 (Lightweight, pure Python in-memory document building)

---

## ⚡ Local Setup & Installation

Follow these steps to run the enterprise validation runtime environment locally:

### 1. Clone the Architecture Repository
```bash
git clone [https://github.com/vivek65666/ai-resume-analyzer.git](https://github.com/vivek65666/ai-resume-analyzer.git)
cd ai-resume-analyzer
