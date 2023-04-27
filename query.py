from llama_index import GPTSimpleVectorIndex
from dotenv import load_dotenv

load_dotenv()

# load from disk
index = GPTSimpleVectorIndex.load_from_disk("index.json")

statement = "start"

while statement != "exit":
    statement = input("What is your question? > ")
    print(" Your question is - " + statement)
    print("Answer: ")
    print(index.query(statement))
