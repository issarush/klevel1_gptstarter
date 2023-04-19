# klevel1_gptstarter
1-Clone the repository to your local machine.
2-Change into the project directory.
3-Initialize a virtual environment.
4-Activate the virtual environment.
5-Install the project dependencies from the requirements.txt.
6-Run the Main python file.
7-You will be asked to provide the OPENAI KEY, followed by a prompt regarding the data in the Knowledge folder.
8-You will receive a response.

The model is using data from the text file(s) present in the Knowledge directory. So to add or modify the documents that the code uses, you can add or modify text files in the Knowledge directory. Each text file should contain one or more documents, separated by a blank line.


Note - the data from the txt file(s) inside that directory is being transformed into a json format via vectorIndex. 
This is then parsed into the answerMe function to generate the prompt.
