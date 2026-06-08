import json
import re

from json_repair import repair_json

from prompts import DEBUG_PROMPT
from test_generator import LLMClient


def extract_json(text):

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if not match:
        raise ValueError(
            "No JSON found."
        )

    return match.group(0)


class DebugAssistant:

    def __init__(self):

        self.llm = LLMClient()

    def analyze_error(self, error_log):

        prompt = DEBUG_PROMPT.format(
            error_log=error_log
        )

        result = self.llm.generate(
            prompt
        )

        try:

            json_text = extract_json(
                result
            )

            repaired = repair_json(
                json_text
            )

            return json.loads(
                repaired
            )

        except Exception:

            print("\nRAW RESPONSE:\n")
            print(result)

            raise ValueError(
                "Failed to parse debug response."
            )