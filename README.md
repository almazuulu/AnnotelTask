1. How to start the REST API locally?
   - Clone this repository
   - Navigate to the folder of the project
   - From the Terminal run command: python3 app.py
  
  If you want to see all the converted OpenLabel data (which is converted from Annotel) just type the following in your browser:
  http://127.0.0.1:5000/openlabel
  
  If you want to see the specific objects's bbox Feature coordinate than just type the following in your browser:
  http://127.0.0.1:5000/openlabel/[id_object]
  example:
  http://127.0.0.1:5000/openlabel/2ef8a63f-37a9-488c-a7c7-b36d11eb19a7
  

2. How to install and use the python-library?
   - Open your project folder that was cloned with the terminal
   - Install Python Virtual Environment, You can follow this instruction to install:
      https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/
   OR if you have MAC OS:
      https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
      
   - After you activated venv update your pip:
      python -m pip install --upgrade pip
      (OR python3 -m pip install --upgrade pip)
      
   - Then run following command to install required python libraries:
      pip install -r requirements.txt --no-index
      
  
