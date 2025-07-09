import sys
import os
import json
from parser_core import parse_transcript

def main():
    if len(sys.argv) < 2:
        print("❌ Error: Please provide a transcript file as an argument.")
        print("Usage: python run_parser.py example_transcript.txt")
        return

    filepath = sys.argv[1]
    
    if not os.path.exists(filepath):
        print(f"❌ Error: File not found: {filepath}")
        return

    print(f"✅ Parsing transcript: {filepath}")
    parsed = parse_transcript(filepath)

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, "parsed_output.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2)

    print(f"✅ Done. Output written to {output_path}")

if __name__ == "__main__":
    main()
