#!/usr/bin/env python3

import os
import subprocess
import datetime
import argparse

def get_daily_note_path(base_path):
    today = datetime.date.today()
    filename = f"{today.strftime('%Y-%m-%d')}.md"
    return os.path.join(base_path, filename)

def add_note(file_path):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    
    temp_file = "/tmp/obsidian_note_temp.md"
    with open(temp_file, "w") as f:
        f.write(f"\n---\n`{timestamp}`\n\n")
    
    editor = os.environ.get('EDITOR', 'vim')
    if editor == 'vim':
        subprocess.run(["vim", "+$", "-c", "startinsert", "-c", "autocmd VimLeave * :wq", temp_file])
    else:
        subprocess.run([editor, temp_file])
    
    with open(temp_file, "r") as temp, open(file_path, "a") as daily_note:
        content = temp.read().strip()
        if content:
            daily_note.write("\n\n" + content + "\n")
    
    os.remove(temp_file)

def main():
    parser = argparse.ArgumentParser(description="Add a note to today's Obsidian daily note.")
    parser.add_argument("--path", default="~/Documents/Vault", help="Path to Obsidian daily notes folder")
    args = parser.parse_args()
    
    base_path = os.path.expanduser(args.path)
    daily_note_path = get_daily_note_path(base_path)
    
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    add_note(daily_note_path)
    print(f"Note added to {daily_note_path}")

if __name__ == "__main__":
    main()
