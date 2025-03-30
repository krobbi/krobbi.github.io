import output
import style
import template

def generate_style(name: str):
    """Generate a style by its name and print its HTML code."""
    
    print(style.get_html(name).strip())


def main():
    """Generate the site's content."""
    
    output.reset()
    generate_style("main")
    generate_style("home")
    generate_style("page")


if __name__ == "__main__":
    #main()
    print(template.get_base()._source) # type: ignore
