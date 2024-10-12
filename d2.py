import os
import click
import re


def process_svg_file(path: str):
    """
    Remove "UNLICENSED COPY" text from SVG file using tag filtering.
    """
    with open(path, "r") as file:
        content = file.read()

    # Use regex to find and remove the unwanted text element
    pattern = r"<text[^>]*>UNLICENSED COPY</text>"
    content = re.sub(pattern, "", content)

    # Write the modified content back to the file
    with open(path, "w") as file:
        file.write(content)

    print(f"Processed {path}: Removed 'UNLICENSED COPY' text.")


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("-w", "--watch", is_flag=True, help="Watch on browser")
def build_d2(path: str, watch: bool):
    """
    This script builds the D2 project and removes the 'UNLICENSED COPY' text from the output SVG.
    """
    path_output = path.replace(".d2", ".svg")
    if watch:
        command = f'd2 -w "{path}" "{path_output}" --theme 1 --layout tala --scale 1'
    else:
        command = f'd2 "{path}" "{path_output}" --theme 1 --layout tala --scale 1'

    try:
        os.system(command)
        click.echo("D2 project built successfully.")

        # Process the output SVG to remove the unwanted text
        if not watch:
            process_svg_file(path_output)
            click.echo("SVG processed: 'UNLICENSED COPY' text removed.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")


if __name__ == "__main__":
    build_d2()
