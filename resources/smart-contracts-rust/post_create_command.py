
import json
import subprocess
from glob import glob
from pathlib import Path


def main():
    prepare_vscode_settings()
    prepare_gitignore()
    add_examples_if_empty_workspace()


def prepare_vscode_settings():
    vscode_path = Path(".vscode")
    vscode_launch_path = vscode_path / "launch.json"
    vscode_settings_path = vscode_path / "settings.json"
    vscode_tasks_path = vscode_path / "tasks.json"
    workspace_path = Path("multiversx.workspace.json")

    vscode_path.mkdir(exist_ok=True)

    if not vscode_launch_path.exists():
        vscode_launch_path.write_text(json.dumps({
            "version": "0.2.0",
            "configurations": []
        }, indent=4))

    if not vscode_settings_path.exists():
        vscode_settings_path.write_text(json.dumps({
        }, indent=4))

    if not vscode_tasks_path.exists():
        vscode_tasks_path.write_text(json.dumps({
            "version": "2.0.0",
            "tasks": []
        }, indent=4))

    if not workspace_path.exists():
        workspace_path.write_text(json.dumps({
        }, indent=4))


def prepare_gitignore():
    gitignore_path = Path(".gitignore")

    if not gitignore_path.exists():
        gitignore_path.write_text("""
**/target/**
**/output/**
**/trace*.scen.json
Cargo.lock
!**/wasm*/Cargo.lock
""")


def add_examples_if_empty_workspace():
    subfolders = glob('*/')
    if len(subfolders) == 0:
        subprocess.check_output(["mxpy", "contract", "new", "--template", "adder", "adder"])


if __name__ == "__main__":
    main()
