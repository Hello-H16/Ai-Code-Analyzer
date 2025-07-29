from dotenv import load_dotenv
import os

from analyzer.parser import CodeParser
from analyzer.detector import DsaMistakeDetector
from analyzer.suggester import AICodeSuggester
from examples.test_cases import test_cases

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(" GROQ_API_KEY is not set. Check your .env file.")

suggester = AICodeSuggester(api_key)

# 🚀 Ask user how they want to input code
print(" AI Code Analyzer for DSA Mistakes")
print("1. Use a built-in test case")
print("2. Paste your own Python DSA code")

choice = input("Choose an option (1 or 2): ")

if choice == '1':
    print("\nAvailable Test Cases:")
    for i, key in enumerate(test_cases.keys(), start=1):
        print(f"{i}. {key}")
    test_choice = int(input("Enter test case number: "))
    key = list(test_cases.keys())[test_choice - 1]
    user_code = test_cases[key]
    print(f"\n Loaded test case: {key}\n")
else:
    print("\nPaste your Python DSA code below. Press Enter twice when done:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    user_code = "\n".join(lines)

#  Step 1: Parse the code
parser = CodeParser(user_code)
functions = parser.extract_functions()
recursions = parser.detect_recursion()

print(" Functions:", functions)
print(" Recursive functions:", recursions)

#  Step 2: Detect common mistakes
detector = DsaMistakeDetector(user_code)
mistakes = detector.check_missing_return_in_recursion()

#  Step 3: Ask Groq AI for suggestion (if mistakes found)
if mistakes:
    print("\nIssues Detected:")
    for m in mistakes:
        print("•", m)
    suggestion = suggester.suggest_fixes(user_code, mistakes[0])
    print("\n AI Suggestion:\n", suggestion)
else:
    print(" No common mistakes found.")
