import json
import os
import re

from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai
from json_repair import repair_json

from prompts import (
    TEST_CASE_PROMPT,
    FAILURE_ANALYSIS_PROMPT
)

load_dotenv()


def extract_json(text):
    """
    Extract the first JSON object from an LLM response.
    """

    text = text.strip()

    # Remove markdown fences if present
    text = text.replace("```json", "")
    text = text.replace("```", "")

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if not match:
        raise ValueError(
            "No JSON object found in response."
        )

    return match.group(0)


class LLMClient:

    def __init__(self):

        self.provider = os.getenv(
            "LLM_PROVIDER",
            "gemini"
        ).lower()

        if self.provider == "openai":

            api_key = os.getenv(
                "OPENAI_API_KEY"
            )

            if not api_key:
                raise ValueError(
                    "OPENAI_API_KEY not found in .env"
                )

            self.client = OpenAI(
                api_key=api_key
            )

        elif self.provider == "gemini":

            api_key = os.getenv(
                "GEMINI_API_KEY"
            )

            if not api_key:
                raise ValueError(
                    "GEMINI_API_KEY not found in .env"
                )

            genai.configure(
                api_key=api_key
            )

            self.model = genai.GenerativeModel(
                "gemini-2.5-flash"
            )

        else:

            raise ValueError(
                "LLM_PROVIDER must be 'openai' or 'gemini'"
            )

    def generate(self, prompt):

        try:

            if self.provider == "openai":

                response = (
                    self.client.chat.completions.create(
                        model="gpt-4.1-mini",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        temperature=0.2
                    )
                )

                return (
                    response
                    .choices[0]
                    .message
                    .content
                )

            elif self.provider == "gemini":

                response = (
                    self.model.generate_content(
                        prompt
                    )
                )

                return response.text

        except Exception as e:

            raise RuntimeError(
                f"LLM API Error: {str(e)}"
            )


class TestGenerator:

    def __init__(self):

        self.llm = LLMClient()

    def parse_response(self, result):

        print("\n========== RAW RESPONSE ==========\n")
        print(result)
        print("\n==================================\n")

        try:

            json_text = extract_json(
                result
            )

            repaired_json = repair_json(
                json_text
            )

            return json.loads(
                repaired_json
            )

        except Exception as e:

            raise ValueError(
                f"JSON Parse Error: {str(e)}"
            )

    def generate_tests(self, code):

        prompt = TEST_CASE_PROMPT.format(
            code=code
        )

        result = self.llm.generate(
            prompt
        )

        return self.parse_response(
            result
        )

    def analyze_failures(self, code):

        prompt = FAILURE_ANALYSIS_PROMPT.format(
            code=code
        )

        result = self.llm.generate(
            prompt
        )

        return self.parse_response(
            result
        )