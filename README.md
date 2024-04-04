<!-- Badge pills -->

![Python Version](https://img.shields.io/badge/Python-3.12.2-blue)

<!-- Demo -->
<div align=center>
  <h1>ENV VAR KEY GEN</h1>
  <p>Quick script to safely mutate a list of keys for an environment variable</p>
</div>

<!-- Main content -->

## Why ?

For those who in a very specific situation where they have no web server, no database, and need to manage an environment variable called 'API_KEY' containing a list of unqiue keys.

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

- Run _app.py_ to manage keys with following args:
  | Arg | Desc |
  |-----------------|-----------------|
  | `list` | Lists all relationships between api keys (masked) and their seed values |
  | `add [-v SEED_VALUE]` | Adds a new key and relationship row |
  | `revoke [-v SEED_VALUE]` | Revokes an existing key and relationship row |
  | `nuke` | Deletes all CSVs from the output dir |

- Sync your CSV API keys with your system's 'API_KEY' environment variable
  - Python scripts cannot modify env variables on a system-level (only within its own process)
  - To persist changes, run the shell script within current shell env
  - Set execute perms: `chmod u+x sync.sh`
  - Run: `source ./sync.sh`
  - Confirm: `echo $API_KEY`
  - ⚠️ Be careful running shell scripts!!! take a look at _sync.sh_ first
