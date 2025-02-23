**Installation Guide**
1. In Command Prompt or Windows Powershell, naviagate to the location where you want this project to be saved using the 'cd' command.
2. Once you have found the location, clone the repository by using 'git clone https://github.com/JezzyOweTwo/project_chitchat_api.git'
3. Navigate into the project by typing cd ./project_chitchat_api
4. Type 'set PYTHONPATH=src' into the terminal
5. Ensure you have the poetry package manager installed. If not, visit https://python-poetry.org/docs/#installing-with-pipx
6. Once inside the project, type 'poetry install' to install all neccesary dependencies. 
7. type 'poetry run ./src/init.py' to run the project.

Please note a .env file will need to be provided in order to get the project to work as intended.  

**Development Guide**
Yo, I have no clue why but poetry and Visual Studio Code DO NOT play nice on either of my computers by default. If you're having issues, try this.
1. 'poetry cache clear --all pypoetry'
2. 'poetry env use python3.13' -> will print a long path: smthin like .\pypoetry\Cache\virtualenvs\project-chitchat-api-oin7xhOD-py3.13
3. 'poetry install'
4. 'poetry env activate'
5. Ctrl + Shift + P -> 'Python:Select Interpreter' -> use the path from step 2
6. Close and reopen Vscode
