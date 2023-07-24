# SIDE-001 

***To run a demo use rundown.ipynb or Chatbot.py***

***type 'end' or '\n' to exit***

***Run eval.py for Accuracy using LLM***

***Accuracy: 0.9117647058823529***


## Steps to build Model

### Loading Data 
- Load data using loader
- Use text loader for txt file
- (Optional) Load CSV by preprocessing txt file

### Splitting Data
- Splitting the Data into chunks for better sectioning
- Use Char splitting for Equal sized splits
- Use Markdown for extracting metadata and splitting based on that

### Embedding
- Converting strings to vector using embeddings
- Can use OpenAI embeddings, BERT embeddings, GloVe embeddings

### Vectorspace
- For storing the embedded data in vectorspaces for retriving later

### Retrival
- Comparing similarity scores for document retrival
- MMR for diversity in retrival
- metadata fields for additional data during retrival

### Coversation chains
- Using Langchain chat models for queries
- Using chat history for incoparating past data and forming a coversation than a single quention and done

## Additional Features

### Evaulation
- Run all the questions in SampleQuestions.xlsx and store results
- Generate examples using LLMs from stored docs
- Evaluate results and examples by using llm and eval chain

### Multilingual 
- Create vector store using Cohere Embeddings instead of OpenAI for multilingual chatbot


