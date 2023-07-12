
import json
import shutil
import urllib.request
from pathlib import Path


def main():
    prepare_vscode_settings()
    prepare_gitignore()
    add_samples()
    

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
        }, indent=4) + "\n")

    if not vscode_settings_path.exists():
        vscode_settings_path.write_text(json.dumps({
        }, indent=4) + "\n")

    if not vscode_tasks_path.exists():
        vscode_tasks_path.write_text(json.dumps({
            "version": "2.0.0",
            "tasks": []
        }, indent=4) + "\n")

    if not workspace_path.exists():
        workspace_path.write_text(json.dumps({
        }, indent=4) + "\n")


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


def add_samples():
    samples_folder = Path("samples")
    archive_url = "https://github.com/multiversx/mx-contracts-rs/archive/refs/heads/main.zip"
    download_path = Path("/tmp/archive.zip")
    extract_path = Path("/tmp/extracted")
    contracts_in_extract_path = Path("mx-contracts-rs-main/contracts")

    if samples_folder.exists():
        return
    
    urllib.request.urlretrieve(archive_url, download_path)
    shutil.unpack_archive(download_path, extract_path)
    shutil.move(str(extract_path / contracts_in_extract_path), str(samples_folder))


if __name__ == "__main__":
    main()
