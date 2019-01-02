# Showcase
A web development learning/prototyping workspace.
Could also be used to give an interface for some useful functions, which explain the name of the project.


## Requirements
* [Python 3.7](https://www.python.org/)
* [Node.js](https://nodejs.org/en/)
* [pre-commit](https://pre-commit.com/)

## Backend
A Python/Flask backend.

Note: we recommend using Python Virtual Environments that you can setup using [this guide](https://docs.python-guide.org/dev/virtualenvs/). Then simply use the following commands:

**Installation**
```bash
pip install -r ./backend/requirements.txt
```

**Execution**
```bash
python ./backend/main.py
```

**Note**

The backend currently serves the built frontend (`./frontend/build/`).


## Frontend
For details about the frontend, refer to the frontend [README.md](frontend/README.md)

**Installation** (from within the `frontend` directory)
```bash
npm install
```

**Execution** (from within the `frontend` directory)
```bash
npm start
```

## pre-commit
*pre-commit* is used to ensure some rules (e.g. see [Formatters](#formatters)) are respected before you commit/push any change. The *pre-commit* package itself has been installed during the backend installation step. In order to set the hooks defined in the [.pre-commit-config.yaml], simply run:
```bash
pre-commit install
```

## Formatters
[Black](https://black.readthedocs.io/en/stable/) is use to format Python files and [Prettier](https://prettier.io/) is used to format Web files as well as some text files (JSON, YAML). You can run those tools manually:
```bash
black ./backend/
node ./frontend/node_modules/.bin/prettier --config=./.prettierrc --write "frontend/**/*.{html,css,js,jsx,json,yaml,md}"
```
 
 It is also generally possible to set those tools with your IDE (e.g. to be triggered when you save a file). Please refer to the tools and/or IDE documentation.
