import os

OUTPUT_DIR: str = "out/"
"""The directory for outputting the site's content."""

def main() -> None:
    """Create the output directory."""
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == "__main__":
    main()
