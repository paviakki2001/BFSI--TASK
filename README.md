🏦 BFSI Call Center AI Assistant
Internship Technical Submission

Submitted by: Pavithra Veerapathiran

📌 Project Overview

The BFSI Call Center AI Assistant is a compliance-focused, lightweight AI solution designed specifically for Banking, Financial Services, and Insurance (BFSI) environments.

This system is engineered to deliver accurate, policy-grounded, and regulation-compliant responses to customer queries while minimizing hallucination risks and operational overhead.

The architecture follows a structured hybrid approach combining:

Dataset-first similarity matching

Fine-tuned Small Language Model (SLM)

Retrieval-Augmented Generation (RAG) principles

Safety guardrails for financial compliance

🚀 Key Features
🔹 1. Domain-Specific Training Dataset

150+ Alpaca-formatted BFSI conversational samples

Covers loan eligibility, EMI calculations, policy clarifications, and financial FAQs

Structured instruction-input-output format for model alignment

🔹 2. Similarity-Based Response Prioritization

Dataset-first architecture

Ensures curated, pre-approved responses are prioritized

Reduces unnecessary model generation

Enhances reliability and compliance

🔹 3. Lightweight & Efficient Architecture

Designed for cost-efficient local execution

Modular component structure

Scalable for enterprise-grade deployment

Optimized for call center use cases

🧠 System Architecture Highlights
Component	Purpose
Similarity Engine	Returns safe, curated dataset responses
Fine-Tuned Local SLM	Generates fallback conversational outputs
RAG Retrieval Layer	Grounds responses in financial policy context
Guardrails Layer	Prevents unsafe financial advice & hallucinations

💻 Running the Project in Google Colab

Step 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

Step 2: Navigate to Project Directory
%cd /content/drive/MyDrive/bfsi-callcenter-ai-assistant-top1

Step 3: Install Required Dependencies
!pip install -r requirements.txt

Step 4: Import and Run Response Router
from src.response_router import get_response

query = "Check personal loan eligibility for salary ₹50000 and CIBIL 700"
response = get_response(query)

print(response)

📦 Project Repository

🔗 Project ZIP:
bfsi-callcenter-ai-assistant-top1.zip

🎯 Why This Solution Stands Out

BFSI compliance-aware architecture

Controlled AI generation with guardrails

Dataset-first reliability

Cost-efficient model strategy

Enterprise-ready modular design

Designed with scalability in mind

👩‍💻 Submitted By

Pavithra Veerapathiran
B.Tech Information Technology (2024)
Executive PG in Data Science & AI (2025)
