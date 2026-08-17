import typer

from text_toolkit.core import count_words
from text_toolkit.models import ChunkConfig

app = typer.Typer()


@app.command()
def stats(file: str):
    """Show word count statistics for a text file."""
    with open(file) as f:
        text = f.read()
    counts = count_words(text)
    typer.echo(f"Total unique words: {len(counts)}")


@app.command()
def chunk(file: str, size: int = 100, overlap: int = 0):
    """Split a text file into overlapping chunks."""
    config = ChunkConfig(size=size, overlap=overlap)
    with open(file) as f:
        text = f.read()
    chunks = [
        text[i : i + config.size]
        for i in range(0, len(text), config.size - config.overlap)
    ]
    typer.echo(f"Created {len(chunks)} chunks")


@app.command()
def clean(file: str):
    """Normalize whitespace in a text file."""
    with open(file) as f:
        text = f.read()
    cleaned = " ".join(text.split())
    typer.echo(cleaned)


if __name__ == "__main__":
    app()
