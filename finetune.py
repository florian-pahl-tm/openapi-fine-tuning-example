from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, download_loader

load_dotenv()

UnstructuredURLLoader = download_loader("UnstructuredURLLoader")

urls = [
    "https://www.techminers.com/",
    "https://careers.techminers.org/",
    "https://careers.techminers.org/jobs/1355045-senior-technology-analyst-f-m-x",
    "https://careers.techminers.org/jobs/1381749-technology-expert-f-m-x-freelance",
]

loader = UnstructuredURLLoader(
    urls=urls,
    continue_on_failure=False,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    },
)
documents = loader.load()

index = GPTSimpleVectorIndex.from_documents(documents)
index.save_to_disk("index.json")
