import os
import shutil

EXT_MAP = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv"],
    "archives": [".zip", ".tar", ".gz", ".rar"],
    "code": [".py", ".js", ".html", ".css", ".java"],
    "videos": [".mp4", ".mkv", ".avi"]
}

def get_category(fname):
    ext = os.path.splitext(fname)[1].lower()
    for cat, exts in EXT_MAP.items():
        if ext in exts:
            return cat
    return "others"

def organize(folder):
    if not os.path.isdir(folder):
        print("Folder not found:", folder); return
    for fname in os.listdir(folder):
        path = os.path.join(folder, fname)
        if os.path.isdir(path):
            continue
        cat = get_category(fname)
        target = os.path.join(folder, cat)
        os.makedirs(target, exist_ok=True)
        shutil.move(path, os.path.join(target, fname))
    print("Organized", folder)

if __name__ == "__main__":
    folder = input("Folder to organize (enter . for current): ").strip() or "."
    organize(folder)
