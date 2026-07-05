# Financial Knowledge Assistant

## Project Overview
This is a simple Python-based Financial Knowledge Assistant. It searches local banking policy documents and returns the most relevant policy answer based on the user's question.

## Business Problem
Banking teams such as fraud analysts, customer support, compliance, and operations often need to search through policies, SOPs, fraud manuals, and support documents. Manual searching takes time and can lead to inconsistent answers. This project demonstrates a simple document retrieval assistant that helps users find relevant policy information quickly.

## Technologies Used
- Python
- File Handling
- Text Processing
- Keyword Matching
- Basic RAG Concept
- Policy Document Search

## Project Features
- Loads banking policy documents from local text files
- Accepts user questions from the command line
- Searches across fraud, customer support, and compliance policies
- Finds the most relevant document
- Returns matching policy sentences as the answer
- Shows the source document used for the answer

## Project Structure

financial-knowledge-assistant/
│
├── documents/
│   ├── fraud_policy.txt
│   ├── customer_support_policy.txt
│   └── compliance_policy.txt
│
├── src/
│   └── financial_assistant.py
│
├── README.md
└── .gitignore

## How to Run

Run this command:

python src/financial_assistant.py

## Sample Questions
- What should we do for international wire transfers?
- Can customer data be shared without authentication?
- What happens if suspicious activity is found?
- Who handles policy violations?
- How should high-risk transactions be reviewed?

## Interview Explanation
I created a simple Financial Knowledge Assistant using Python. This project is inspired by my recent Generative AI and RAG work in the banking domain. The program searches local policy documents, compares the user question with available policy content, identifies the most relevant document, and returns grounded policy sentences as the answer. I built this lightweight version without heavy external packages to demonstrate the core concepts of document retrieval, RAG, policy search, and Python-based text processing.