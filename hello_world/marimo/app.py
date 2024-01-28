import marimo

__generated_with = "0.1.73"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("hello world")
    return


@app.cell
def __():
    import marimo as mo


if __name__ == "__main__":
    app.run()
