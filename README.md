**Installation Guide**
1. Locate the directory where you want to install the project. Clone the repository by typing 'git clone https://github.com/JezzyOweTwo/project_chitchat_api.git'
3. Navigate into the project by typing cd ./project_chitchat_api
4. Ensure you have both Python [Installation](https://wiki.python.org/moin/BeginnersGuide/Download) and the poetry package manager [Installation](https://python-poetry.org/docs/#installing-with-pipx).
6. Type 'poetry install' to install all neccesary dependencies. 
7. Type 'poetry run python src/myApp/main.py'
Please note a .env file will need to be provided in order to get the project to work as intended.  

**Development Guide**
Yo, I have no clue why but poetry and Visual Studio Code DO NOT play nice on either of my computers by default. If you're having issues, try this.
1. 'poetry cache clear --all pypoetry'
2. 'poetry env use python3.13' -> will print a long path: smthin like .\pypoetry\Cache\virtualenvs\project-chitchat-api-oin7xhOD-py3.13
3. 'poetry install'
4. 'poetry env activate'
5. Ctrl + Shift + P -> 'Python:Select Interpreter' -> use the path from step 2
6. Close and reopen VS Code
