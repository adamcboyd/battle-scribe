import os
import subprocess
import sys

def run(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(1)

def main():
    if not os.path.isdir(".git"):
        print("This folder is not a Git repository.")
        print("Make sure you're in the root of your 'battle-scribe' project folder.")
        sys.exit(1)

    run("git add .")
    run("git commit -m \"Sync MVP code snapshot\"")
    run("git push origin main")

    print("\n✅ Sync complete! Your code is now safe on GitHub.")

if __name__ == "__main__":
    main()
