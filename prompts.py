TEST_CASE_PROMPT = """
You are a Senior Software Test Engineer.

Analyze the following code:

{code}

Your task is to generate practical software testing scenarios.

IMPORTANT RULES:

1. Focus on realistic QA testing.
2. Do NOT generate excessive theoretical cases.
3. Avoid Infinity, NaN, float('inf'), float('nan').
4. Avoid obscure language-specific corner cases.
5. Prioritize cases a software tester would actually write.
6. Return EXACTLY:
   - 5 functional tests
   - 3 boundary tests
   - 3 edge cases
   - 3 invalid input cases

Return ONLY valid JSON.

{{
    "functional_tests": [
        {{
            "input": "",
            "expected_output": "",
            "reason": ""
        }}
    ],
    "boundary_tests": [
        {{
            "input": "",
            "expected_output": "",
            "reason": ""
        }}
    ],
    "edge_cases": [
        {{
            "input": "",
            "expected_output": "",
            "reason": ""
        }}
    ],
    "invalid_cases": [
        {{
            "input": "",
            "expected_output": "",
            "reason": ""
        }}
    ]
}}
"""


FAILURE_ANALYSIS_PROMPT = """
You are a Software QA Engineer.

Analyze the following code:

{code}

Identify practical software failure points.

Focus on:

- Null/None values
- Empty collections
- Invalid indexes
- Division by zero
- Type mismatch
- Invalid parameters
- Overflow risks
- Runtime exceptions

Return ONLY valid JSON.

{{
    "failure_points": [
        {{
            "failure_type": "",
            "description": "",
            "likelihood": "",
            "recommended_test": ""
        }}
    ]
}}
"""


DEBUG_PROMPT = """
You are a Senior Debugging Engineer.

Analyze this error log:

{error_log}

Keep responses concise.

Return ONLY valid JSON.

{{
    "root_cause": "",
    "explanation": "",
    "fix_recommendation": "",
    "example_fix_code": "",
    "validation_tests": [
        ""
    ]
}}

Rules:

- root_cause: maximum 1 sentence
- explanation: maximum 3 sentences
- fix_recommendation: maximum 2 sentences
- example_fix_code: maximum 10 lines
- validation_tests: maximum 4 items

Do not include markdown.
Do not include ```json.
Do not include text outside the JSON object.
"""