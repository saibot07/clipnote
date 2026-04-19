# ClipNote

ClipNote is a simple Python CLI tool that allows you to convert your clipboard content into a quick note-taking system with automatic file storage and organizational capabilities. Perfect for saving links, snippets, and thoughts on the go!

## Features
- Automatically capture clipboard content.
- Save notes into organized text files by date.
- Delete, list, or search notes via CLI commands.
- Portable and lightweight.

## Installation
```bash
pip install clipnote
```

## Usage
```bash
clipnote add   # Save your clipboard content as a note
clipnote list  # View all stored notes
clipnote search --query {query}  # Search notes by keyword
clipnote clear # Clear all notes
```

Example:
```bash
$ clipnote add
Saved clipboard content: "Don't forget the meeting at 3 PM!"

$ clipnote list
[2026-04-19]
1. Don't forget the meeting at 3 PM!

$ clipnote search --query meeting
Results:
1. Don't forget the meeting at 3 PM!
```

## Configuration
You can update the storage directory and preferred file format in the configuration file (`~/.clipnote-config.json`).

## License
This project is licensed under the MIT License. Feel free to use and contribute to ClipNote!
