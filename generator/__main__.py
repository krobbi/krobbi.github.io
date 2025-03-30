from . import output
from . import pages

def main():
    """Generate the site's content."""
    
    output.reset()
    pages.generate_pages()


if __name__ == "__main__":
    main()
