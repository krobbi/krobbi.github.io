import os

OUTPUT_DIR: str = "out/"
"""The directory for outputting the site's content."""

def clean_dir(path: str) -> None:
    """Recursively clean a directory."""
    
    for entry in os.scandir(path):
        if entry.is_dir():
            clean_dir(entry.path)
            os.rmdir(entry)
        else:
            os.remove(entry)


def main() -> None:
    """Create and clean the output directory."""
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clean_dir(OUTPUT_DIR)


if __name__ == "__main__":
    main()
