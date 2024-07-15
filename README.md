# Interact with your complex PDF that includes images, tables, and graphs using Raptor RAG.


## Table of Contents

- [Introduction](#introduction)
- [RAPTOR](#Recursive-Abstractive-Processing-for-Tree-Organized-Retrieval)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)


## Introduction

The RAG-RAPTOR-DEMO project simplifies the process of extracting and querying information from Complex PDF documents, including complex content such as tables, graphs, and images. Leveraging state-of-the-art natural language processing models and Unstructured.io for document parsing, as well as integrating RAPTOR, which introduces a novel approach to retrieval-augmented language models by constructing a recursive tree structure from documents for more efficient and context-aware information retrieval across large texts, and Raptor Rag for retrieve semantic chunk, the chatbot provides a user-friendly interface to interact with and retrieve detailed information from these documents.


## RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="data/raptor_dark.png">
  <img alt="Shows an illustrated sun in light color mode and a moon with stars in dark color mode." src="data/raptor.jpg">
</picture>

**RAPTOR** introduces a novel approach to retrieval-augmented language models by constructing a recursive tree structure from documents. This allows for more efficient and context-aware information retrieval across large texts, addressing common limitations in traditional language models. 


For detailed methodologies and implementations, refer to the original paper:

- [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://arxiv.org/abs/2401.18059)

[![Paper page](https://huggingface.co/datasets/huggingface/badges/resolve/main/paper-page-sm.svg)](https://huggingface.co/papers/2401.18059)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/raptor-recursive-abstractive-processing-for/question-answering-on-quality)](https://paperswithcode.com/sota/question-answering-on-quality?p=raptor-recursive-abstractive-processing-for)

- [Github Repo](https://github.com/parthsarthi03/raptor)
- [Youtube link](https://youtu.be/jbGchdTL7d0?si=Pfc_3vpXw8QdJP5T)

## Features

- **Table Extraction**: Identify and parse tables to retrieve structured data, making it easier to answer data-specific questions.
- **Text Extraction**: Efficiently extract and process text from PDFs, enabling accurate and comprehensive information retrieval.
- **Image Analysis**: Extract and interpret images within the PDFs to provide contextually relevant information.



## Technologies Used

- **LangChain**: Framework for building applications with language models.
- **RAG (Retrieval-Augmented Generation)**: Combines retrieval and generation for more accurate answers.
- **RAPTOR**: Constructs a recursive tree structure from documents for efficient, context-aware information retrieval.
- **Streamlit**: Framework for creating interactive web applications with Python.
- **Unstructured.io**: Tool for parsing and extracting complex content from PDFs, such as tables, graphs, and images.
- **Poetry**: Dependency management and packaging tool for Python.



## Setup Instructions

Follow these steps to set up the project on your local machine:

**1. Clone the Repository:**
- Begin by cloning the repository to your local machine:
```
https://github.com/langchain-tech/Rag-raptor-demo.git
cd Rag-raptor-demo
```

**2. Install project dependencies:**
- Use Poetry to install the dependencies defined in your pyproject.toml file. This command will also respect the versions pinned in your poetry.lock file:
```
poetry install
```
This will create a virtual environment (if one does not already exist) and install the dependencies into it.


**3. Activate the virtual environment (optional):**
- If you want to manually activate the virtual environment created by Poetry, you can do so with:
```
poetry shell
```
This step is optional because Poetry automatically manages the virtual environment for you when you run commands through it.


**4. Set Up Environment Variables:**
Create a .env file in the root directory of your project and add the required environment variables. For example:
```
OPENAI_API_KEY=Your_OPENAI_API_KEY
POSTGRES_URL_EMBEDDINDS=YOUR_POSTGRES_URL  like:-postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}
POSTGRES_URL=YOUR_POSTGRES_URL   like:- postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}
```

**5. Run Data ingestion file**
-Install the necessary packages listed in the requirements.txt file:
```
python3 ingest/app.py
```


**6. Start the Application:**

Run the application using Streamlit:
```
streamlit run app.py
```

## Examples
![My test image](data/raptor1.png)
![My test image](data/raptor2.png)