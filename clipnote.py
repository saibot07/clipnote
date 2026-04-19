import pyperclip
import os
import json
import datetime

def load_config():
    config_path = os.path.expanduser("~/.clipnote-config.json")
    if not os.path.exists(config_path):
        config = {"storage_dir": os.path.expanduser("~/clipnote/notes")}
        os.makedirs(config["storage_dir"], exist_ok=True)
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    else:
        with open(config_path, "r") as f:
            config = json.load(f)
    return config

def save_note():
    config = load_config()
    content = pyperclip.paste()
    if not content.strip():
        print("Clipboard is empty! Nothing to save.")
        return

    today = datetime.date.today().strftime("%Y-%m-%d")
    notes_path = os.path.join(config["storage_dir"], f"notes-{today}.txt")

    with open(notes_path, "a") as f:
        f.write(content + "\n")

    print(f"Saved clipboard content: \"{content}\"")

def list_notes():
    config = load_config()
    print("\nListing all notes:\n")
    for file in sorted(os.listdir(config["storage_dir"])):
        full_path = os.path.join(config["storage_dir"], file)
        with open(full_path, "r") as f:
            print(f"[{file}]")
            for line in f:
                print(line.strip())
            print()

def search_notes(query):
    if not query:
        print("Please provide a search query!")
        return
    config = load_config()
    print(f"Searching for \"{query}\":\n")
    for file in sorted(os.listdir(config["storage_dir"])):
        with open(os.path.join(config["storage_dir"], file), "r") as f:
            for line in f:
                if query.lower() in line.lower():
                    print(f"[{file}] {line.strip()}")

def clear_notes():
    config = load_config()
    for file in os.listdir(config["storage_dir"]):
        os.remove(os.path.join(config["storage_dir"], file))
    print("All notes have been cleared.")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="ClipNote: A Clipboard Note-Taking System")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("add", help="Save clipboard content as a note")
    subparsers.add_parser("list", help="Display all notes")
    subparsers.add_parser("clear", help="Remove all notes")

    search_parser = subparsers.add_parser("search", help="Search for notes by keyword")
    search_parser.add_argument("--query", required=True, help="Keyword to search within notes")

    args = parser.parse_args()

    if args.command == "add":
        save_note()
    elif args.command == "list":
        list_notes()
    elif args.command == "search":
        search_notes(args.query)
    elif args.command == "clear":
        clear_notes()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()