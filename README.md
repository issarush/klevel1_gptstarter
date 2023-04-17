# klevel1_gptstarter
After initializing a virtual environment, install the dependencies from the requirements.txt and run the main python file.
Upon execution, you are asked to provide a OPENAI Key, followed with a prompt regarding the data in the Knowledge folder.

Then, you receive a response.

The model is using data from the text file(s) present in the Knowledge directory.

Note - the data from the txt file(s) inside that directory is being transformed into a json format via vectorIndex. 
This is then parsed into the answerMe function to generate the prompt.
