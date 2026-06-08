# AI-Powered Test Case Generator and Debugging Assistant

## Overview

AI-Powered Test Case Generator and Debugging Assistant is a Python-based tool that uses Large Language Models (Gemini or OpenAI) to assist software testing and debugging workflows.

The application analyzes Python functions or Java methods and automatically generates:

* Functional Test Cases
* Boundary Test Cases
* Edge Cases
* Invalid Input Test Cases
* Failure Point Analysis

It also analyzes error logs and stack traces to identify root causes, recommend fixes, and suggest validation tests.

The project was designed to demonstrate practical applications of LLMs in software testing and debugging rather than general-purpose chatbot functionality.

---

## Features

### Test Case Generation

Given a Python function or Java method, the application generates:

* Functional test cases
* Boundary test cases
* Edge cases
* Invalid input test cases
* Expected outputs

Example:

```python
def divide(a, b):
    return a / b
```

Generated output includes:

* Normal division scenarios
* Zero numerator cases
* Division by zero cases
* Invalid input scenarios

---

### Failure Point Analysis

The system identifies potential runtime risks such as:

* Division by zero
* Null or None references
* Empty collections
* Invalid indexes
* Type mismatches
* Overflow risks
* Infinite recursion risks

Example:

```python
def pop_item(stack):
    return stack.pop()
```

Potential failures:

* Empty list causing IndexError
* None input causing AttributeError
* Invalid object types

---

### Error Log Analysis

Given an error log, the application returns:

* Root Cause
* Technical Explanation
* Fix Recommendation
* Example Fix Code
* Validation Test Cases

Example:

```text
IndexError: pop from empty list
```

Output:

* Cause of failure
* Suggested fix
* Validation strategy

---

## Project Structure

```text
AI_Test_Assistant/

├── main.py
├── prompts.py
├── test_generator.py
├── debugger.py
├── requirements.txt
├── .env
└── README.md
```

---

## Tech Stack

* Python
* Gemini API
* OpenAI API
* python-dotenv
* json-repair

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI_Test_Assistant.git

cd AI_Test_Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

### Gemini

```env
LLM_PROVIDER=gemini

GEMINI_API_KEY=YOUR_API_KEY
```

### OpenAI

```env
LLM_PROVIDER=openai

OPENAI_API_KEY=YOUR_API_KEY
```

---

## Running the Application

```bash
python main.py
```

Menu:

```text
1. Generate Test Cases
2. Analyze Error Log
3. Exit
```

---

## Example Usage

### Generate Test Cases

Input:

```python
def divide(a, b):
    return a / b
```

Output:

```text
Functional Tests
Boundary Tests
Edge Cases
Invalid Input Tests
Failure Analysis
```

---

### Analyze Error Logs

Input:

```text
IndexError: pop from empty list
```

Output:

```text
Root Cause
Explanation
Fix Recommendation
Example Fix Code
Validation Tests
```

---

## Skills Demonstrated

* Prompt Engineering
* LLM Integration
* Software Testing Concepts
* Failure Analysis
* Debugging Workflows
* API Integration
* Python Development
* Structured JSON Processing

---

## Future Improvements

* Streamlit Web Interface
* Export Test Cases to JSON
* PyTest Test File Generation
* JUnit Test Generation
* Severity and Risk Scoring
* Multi-file Code Analysis

---

## Author

Harathi Chavala

Integrated M.Tech Computer Science and Engineering

AI/ML and Software Engineering Enthusiast
