# Change this:
# from langchain_ollama.llms import OllamaLLM 

# To this:
from langchain_ollama.llms import OllamaLLM  #importing ollama models
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
        You are an expert in answering about products
        Here are some relavent details: {details}
        Here is the question to answer: {question}
    """

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

# result = chain.invoke({"details":[], "question":"What is the price of the skin care product Eco Radio?"})
# print(result)

# while loop to ask question repeatedly
while True:
    print("\n\n-----------------------------------")
    question = input("Ask your question (q to quit):")
    print("\n\n")
    if question == "q":
        break
    details = retriever.invoke(question)
    #result = chain.invoke({"details":[], "question":question})
    result = chain.invoke({"details":details, "question":question}) #similarity search algorithm
    print(result)






