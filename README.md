<div align="center">

  <h1>Urban CLI</h1>

   <a href="_blank">
     <img
          width="64px"
          alt="book icon"
          src="https://github.com/GH-Syn/urban-cli/blob/feat/docs/readme/.github/images/book.png"/></a>
    <br>
  <code>A command line interface for the infamous <a href="https://www.urbandictionary.com/">Urban Dictionary</a></code>
</div>



## Installation

__All platforms__

All platforms must install requirements before running.
 > This won't be needed in the next planned release for Linux and WSL.

```sh
python -m pip install --user -r requirements.txt
```

__Linux__

On Linux platforms, run `sh install.sh`.
> This assumes that ~/.local/bin is present

__Windows__

For Windows, you'll have to manually modify your path environment variables to add:
`%USERPROFILE%/Downloads/urban-cli/src/urban.py`

From there you'll have to type `urban.py` instead of `urban`.
The exception of course is you've installed WSL through which you can run `install.sh`.

## Usage

![demo](https://gifcord.gg/direct/output-2023-05-23160638-456595.gif)

## License

This project is licensed under the common MIT license, the details of which you'll find in `LICENSE` in the repository files.
