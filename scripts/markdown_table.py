from pathlib import Path
import polars as pl

from scripts import CSV_FILE, README_FILE

EMOJIS = {
    "Easy": "🟢",
    "Medium": "🟠",
    "Hard": "🔴",
    "Python": "🐍",
    "C++": "💻",
    "Rust": "🦀",
}
TAGS_EMOJIS = {
    "Array": "🍡",
    "Hash Table": "🔑🗄️",
    "Sorting": "🔄📊",
    "String": "📜🔤",
}


def insert_md_table(content: str) -> None:
    with README_FILE.open("r") as f:
        lines = f.readlines()
    begin_idx, end_idx = -1, -1

    for i, line in enumerate(lines):
        if line.strip() == "## List of problems":
            begin_idx = i + 1
        if begin_idx != -1 and line.strip() == "<!-- END OF LIST -->":
            end_idx = i
            break
    if begin_idx == -1 or end_idx == -1:
        raise ValueError("Could not find the markdown table location in README.md")

    lines = lines[:begin_idx] + ["\n" + content] + lines[end_idx:]

    with README_FILE.open("w") as f:
        f.writelines(lines)


def generate_markdown_table(csv_path: Path = CSV_FILE) -> None:
    df = pl.read_csv(csv_path)
    table = ""
    head_names = ["ID", "Name", "Difficulty", "Tags", "Rust", "C++", "Python"]
    HEAD = "| " + " | ".join(head_names) + " |\n"
    head_lines = ["-" * len(name) for name in head_names]
    SEPARATOR = "|-" + "-|-".join(head_lines) + "-|\n"
    table += HEAD + SEPARATOR

    for row in df.rows(named=True):
        row_text = ""
        row_text += f"| {str(row['id'])} "
        name_link = f"[{row['name']}](problems/{row['id']:04d}-{row['slug']})"
        row_text += f"| {name_link} "

        diff = row["difficulty"]
        diff_emoji = EMOJIS.get(diff, diff)
        row_text += f"| {diff_emoji} {diff}"

        tag_text = []
        for tag in sorted(row["tags"].split(";")):
            tag_emoji = TAGS_EMOJIS.get(tag, "")
            if tag_emoji:
                tag_text.append(f"{tag_emoji} {tag}")
        row_text += f"| {', '.join(tag_text)} "

        row_text += "| "
        if row["rust"] == "y":
            row_text += "🦀 "
        row_text += "| "
        if row["cpp"] == "y":
            row_text += "💻 "
        row_text += "| "
        if row["python"] == "y":
            row_text += "🐍 "
        row_text += "|\n"
        table += row_text
    table += "\n"
    insert_md_table(table)


def update_md() -> None:
    generate_markdown_table()
