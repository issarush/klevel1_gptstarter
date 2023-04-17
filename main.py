from gpt_index import SimpleDirectoryReader,GPTListIndex,GPTSimpleVectorIndex,LLMPredictor,PromptHelper, ServiceContext
from langchain import OpenAI
import sys
import os

os.environ['OPENAI_API_KEY'] = ''

def createVectorIndex(path):
  max_input = 4096
  tokens = 200
  chunk_size = 600 #for LLM, we need to define chunk size
  max_chunk_overlap = 20
  
  #define prompt
  promptHelper = PromptHelper(max_input,tokens,max_chunk_overlap,chunk_size_limit=chunk_size)
  
  #define LLM — there could be many models we can use, but in this example, let’s go with OpenAI model
  llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001",max_tokens=tokens))
  
  #load data — it will take all the .txt files, if there are more than 1
  docs = SimpleDirectoryReader(path).load_data()

  service_context = ServiceContext.from_defaults(llm_predictor=llmPredictor,prompt_helper=promptHelper)
  vectorIndex = GPTSimpleVectorIndex.from_documents(documents=docs,service_context=service_context)

  #create vector index
  vectorIndex.save_to_disk('vectorIndex.json')
  return vectorIndex

# create vector index/json file from the txt data to be consumed by the answerMe function
vectorIndex = createVectorIndex('Knowledge')

def answerMe(vectorIndex):
  vIndex = GPTSimpleVectorIndex.load_from_disk(vectorIndex)
  while True:
    prompt = input('Please ask: ')
    response = vIndex.query(prompt,response_mode='compact')
    print(f'Response: {response} \n')

answerMe('vectorIndex.json')