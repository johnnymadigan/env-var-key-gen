<!-- Badge pills -->

![Python Version](https://img.shields.io/badge/Python-3.12.2-blue)

<!-- Demo -->
<div align=center>
  <h1>Game of Life v2</h1>
  <p>Quick script to safely mutate a list of keys for an environment variable</p>
  <img src="docs/images/gol-demo-all.gif">
</div>

<!-- Main content -->

## Why ?

For those who in a very specific situation where they have no web server, no database, and need to mutate an environment variable containing a list of keys.

## Setup

- Use Python version >=3.12.2
- Recommend using **pyenv** (like **nvm**): `pyenv install 3.12.2`, `pyenv global 3.12.2`
- Setup virtual environment `python -m venv venv`
- Activate in VSCode or `source ./venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- To run via CLI, main script needs execute perms: `chmod u+x app.py`
- Run `./app.py`

## Usage

```
 /)/)
( ..) so how do I use this ?
/づ🐍🔧
```

The following is a <span style="display: inline-block; padding: 0px 5px; border-radius: 5px; color: gold; background-color: blue;">Python</span> script of _Game of Life_ into an enhanced version - highly interactive and feature rich.

- Settings can be passed via CLI args, see `./game-of-life -h`
- Initial settings are applied from CLI
- You can modify/reset to defaults in the main menu
- <kbd>↑</kbd> <kbd>↓</kbd> to navigate through settings
- Start typing to set new input for selected setting
- <kbd>←</kbd> <kbd>→</kbd> to cycle through fixed setting options
- <kbd>delete</kbd> to clear the input
- <kbd>enter</kbd> to save the input
- <kbd>tab</kbd> <kbd>tab</kbd> to reset
- <kbd>space</kbd> <kbd>space</kbd> to start
- <kbd>Ctrl</kbd> <kbd>C</kbd> to exit
- GIFs are saved in _./gifs_

## Dev notes

### _How do I debug ?_

- Use VSCode:

  ![venv](docs/images/venv.png)

  ![debug](docs/images/debug.png)

### _How do I run unit tests ?_

- Use VSCode:

  ![product-screenshot](docs/images/tests.png)

### _How do I regen the dependency graph ?_

- Run `pipdeptree --graph-output png > dependencies.png`

## Dependency Graph

<img src="docs/images/dependencies.png">

- _curses_ for pretty screens + key events
- _numpy_ for merging multiple cell matrices (for ghost effect)
- _argparse_ for CLI args support
- _matplotlib_ + _pillow_ for creating GIF outputs
