import os

FOLDER = "arts/0_NFT_EN"
EXPECTED_FILES = [f"{i:02d}.txt" for i in range(1, 11)]

def read_story(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"[ERROR: Cannot read {file_path}] {e}"

def main():
    print("Checking story files in:", FOLDER)
    all_ok = True

    for filename in EXPECTED_FILES:
        path = os.path.join(FOLDER, filename)

        if not os.path.exists(path):
            print(f"Missing: {filename}")
            all_ok = False
            continue

        content = read_story(path)

        if not content:
            print(f"Empty file: {filename}")
            all_ok = False
        elif "Dark Temptation" in content or "Karma Golf Club" in content:
            print(f"WARNING: {filename} may contain fallback text.")
            print(f"Starts with: {content[:60]}...")
            all_ok = False
        else:
            print(f"OK: {filename} — {len(content)} characters")

    if all_ok:
        print("\nALL FILES PASSED CHECK")
    else:
        print("\nSome issues found. Check above.")

if __name__ == "__main__":
    main()

