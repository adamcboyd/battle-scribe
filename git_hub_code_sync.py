# This script will act as the core sync and export handler
# for pushing all locally-generated Battle Scribe parsing code
# to your GitHub repo automatically.

# --- FILE: sync_to_github.py ---

import os
import subprocess
import shutil

def ensure_git_repo(path):
    if not os.path.isdir(os.path.join(path, ".git")):
        raise RuntimeError(f"Not a Git repository: {path}")

def stage_and_commit_all(path, message="Initial MVP code commit"):
    subprocess.run(["git", "add", "-A"], cwd=path, check=True)
    subprocess.run(["git", "commit", "-m", message], cwd=path, check=True)

def push_to_origin(path, branch="main"):
    subprocess.run(["git", "push", "origin", branch], cwd=path, check=True)

if __name__ == "__main__":
    PROJECT_DIR = r"C:\Users\adamc\Documents\PROJECTS\BATTLE SCRIBE\battle-scribe"  # <-- Adjust as needed

    try:
        print("🔍 Verifying repo...")
        ensure_git_repo(PROJECT_DIR)

        print("📦 Staging files...")
        stage_and_commit_all(PROJECT_DIR)

        print("🚀 Pushing to GitHub...")
        push_to_origin(PROJECT_DIR)

        print("✅ All files are now backed up on GitHub.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git command failed: {e}")
    except Exception as ex:
        print(f"❌ Error: {ex}")
