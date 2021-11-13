# Chatbot-API



#### Introduction
Chatbot-API is a tool that is designed to run on a Raspberry Pi 3 or greater device. 
This repository is an experimental repository and later on, it will be merged into 
the AIRO-Chatbot Repository. 

#### Requirements

- [ ] pydantic
- [ ] streamlit
- [ ] fastapi
- [ ] nltk
- [ ] numpy
- [ ] pickle5
- [ ] fastapi


#### Installation
The installation is easy as 123. All you have to do is to run the commands listed below:


Create a new virtual environment

`python3 -m venv <NAME OF FILE>`

Make sure you are using BASH. If you are in a different shell, please type this command:


`bash`


Activate the virtual environment 

`source <NAME OF FILE>/bin/activate`


Installing the dependencies 

`pip3 install -r requirements.txt`

Note: Normally you be given a caution warning that says like in this example: 

`WARNING: You are using pip version 21.2.4; however, version 21.3.1 is available.
You should consider upgrading via the '/Users/<NAME OF USER>/UNF-AIRO/Chatbot-API/chatbot_api_virtual_environment/bin/python3.9 -m pip install --upgrade pip' command.`


All you have to do is to use this command 

`python3.9 -m pip install --upgrade pip`



This is the output of what it does in this example: 

`Requirement already satisfied: pip in ./chatbot_api_virtual_environment/lib/python3.9/site-packages (21.2.4)
Collecting pip
  Using cached pip-21.3.1-py3-none-any.whl (1.7 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-21.3.1`