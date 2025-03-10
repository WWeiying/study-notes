import os
import json

notes_dir = "notes"
output_file = "README.md"

# 读取自定义章节顺序
with open("chapter_order.json", "r", encoding="utf-8") as f:
    chapter_order = json.load(f)

# 按章节分组收集笔记文件
notes = {}
for filename in os.listdir(notes_dir):
    if filename.endswith(".md"):
        # 以第一个 '-' 为分隔符，确保文件名中后续 '-' 不影响分组
        chapter, rest = filename.split("-", 1)
        notes.setdefault(chapter, []).append(filename)

# 生成 README 文件内容
with open(output_file, "w", encoding="utf-8") as f:
    for chapter in chapter_order:
        if chapter in notes:
            f.write(f"## {chapter}\n\n")
            for file in sorted(notes[chapter]):  # 可根据需要排序文件名
                file_path = os.path.join(notes_dir, file)
                f.write(f"- [{file}]({file_path})\n")
            f.write("\n")
print("README.md 已更新。")