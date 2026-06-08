import json

from debugger import DebugAssistant
from test_generator import TestGenerator


def print_section(title):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_case_flow():

    print(
        "\nPaste Python/Java code."
    )

    print(
        "Type END on a separate line when done.\n"
    )

    lines = []

    while True:

        line = input()

        if line.strip() == "END":
            break

        lines.append(line)

    code = "\n".join(lines)

    generator = TestGenerator()

    try:

        tests = (
            generator.generate_tests(
                code
            )
        )

        failures = (
            generator.analyze_failures(
                code
            )
        )

        print_section(
            "TEST CASES"
        )

        print(
            json.dumps(
                tests,
                indent=4
            )
        )

        print_section(
            "FAILURE ANALYSIS"
        )

        print(
            json.dumps(
                failures,
                indent=4
            )
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )

def debug_flow():

    error_log = input(
        "\nPaste Error Log:\n"
    )

    debugger = DebugAssistant()

    try:

        result = debugger.analyze_error(
            error_log
        )

        print_section(
            "DEBUG ANALYSIS"
        )

        print(
            json.dumps(
                result,
                indent=4
            )
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )


def main():

    while True:

        print(
            """
AI Test Assistant

1. Generate Test Cases
2. Analyze Error Log
3. Exit
"""
        )

        choice = input(
            "Choose option: "
        )

        if choice == "1":

            test_case_flow()

        elif choice == "2":

            debug_flow()

        elif choice == "3":

            break

        else:

            print(
                "Invalid choice."
            )


if __name__ == "__main__":

    main()