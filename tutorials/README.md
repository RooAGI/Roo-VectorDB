# Roo-VectorDB Tutorials

We will show our tutorials in Jupyter notebooks. Please follow the preparing steps below before running notebooks.


### Create a python virtual environment

The tutorial code is written in python, we need to prepare a standalone virtual environemnt for tutorial only.
Say this virtual environment name is `roovenv`, then you can created it by run:

```bash
cd tutorials
python3 -m venv roovenv
```
(If you have virtualenv installed, an alternative approach for creating `roovenv` could be `virtualenv -p python3 roovenv`.)

### Install requirement packages

Activate the environment by run:
```bash
source roovenv/bin/activate
```
and install all requirement packages that are needed in the following tutorials by run:
```bash
pip install -r requirements.txt
```
(Some package may require `python-dev` package. In Ubuntu you can just run `sudo apt-get install python-dev`)



### Pointing Jupyter kernal to the new created virtual environment

Then register `roovenv` as a candidate kernel:
```bash
python3 -m ipykernel install --user --name=roovenv --display-name "RooVenv"
```
Now start Jupyter server
```bash
jupyter notebook
```
In any notebook page, under the menu "*Kernel*" -> "*Change Kernel*", you should be able to see `RooVenv` as one of candidate kernels to select.
Select `RooVenv` kernel to run any tutorial notebooks.


<br>

<!-- Text Search -->
## Full Text Search

In this tutorial, we show how to perform a full text search with Roo-VectorDB.

### Download data and embedding model

In this tutorial, we use the [Amazon-QA](https://www.kaggle.com/datasets/praneshmukhopadhyay/amazon-questionanswer-dataset) dataset. Each entry in the dataset consists of a question followed by one or more corresponding answers (user reviews). We process the data by enumerating each answer and pairing it with its associated question to form distinct question-answer pairs.
We then create a table with three metadata columns: `question`, `answer`, and a concatenated `question+answer` field. Embeddings are computed from this combined text, allowing vector search to capture semantic similarity across both the question and its answer.

The embedding vectors are generated on-the-fly using a[Sentence Transformer](https://sbert.net/) model. To enable this, the model file will be downloaded beforehand.

1. Amazon-QA text data jsonl file: [amazon-qa.jsonl](https://rooagi8-my.sharepoint.com/:u:/g/personal/chaoma_rooagi_com/ETPyi_peQj9Kg_v5RkQF7OwBvS6a2Q1on0gAJV48uPh9Rg?e=QdGapa) (678MB)
<!-- 1. Sentence Transformer model file: [sent_embed_all-mpnet-base-v2.pickle](https://rooagi8-my.sharepoint.com/:u:/g/personal/chaoma_rooagi_com/EV1p4jOKJ8lEmBv-zhogEosB3XgCAql8WNIGdAZ5JwxlWQ?e=WvjiTb) (418MB) -->

Please verify the file size after downloading to ensure the download completed successfully and the file is not corrupted.

### Start and follow steps of tutorial

First, start the PostgreSQL server with the Roo-VectorDB extension enabled. Then launch the Jupyter server and open the [tutorial_text_search.ipynb](tutorial_text_search.ipynb) notebook. Follow the instructions step by step. In the first few steps (steps 1–2), you’ll need to provide some basic configuration information before proceeding.


<br>

<!-- Image Search -->
## Image Search

In this tutorial, we show how to perform image search with Roo-VectorDB.

### Download image data and image embedding files

We use [Imagenet Train Subset 100k](https://www.kaggle.com/datasets/tusonggao/imagenet-train-subset-100k) dataset, a subset of full ImageNet data in this tutorial. Two files need to be downloaded first.

1. The original image dataset zip file: [archive.zip](https://www.kaggle.com/datasets/tusonggao/imagenet-train-subset-100k?resource=download) (Login Kaggle and click Download) (10.6GB)
1. The precomputed image embedding file: [imgnet100k_dim128.txt](https://rooagi8-my.sharepoint.com/:t:/g/personal/chaoma_rooagi_com/ERJz6FZqNrtFutH3X9B8ad8B-w912c0xYrEo3smyBCEcwg?e=PRhMMF) (248.3MB)

Please verify the file size after downloading to ensure the download completed successfully and the file is not corrupted.

For (2), there are two alternative choices:

* 128-dimension embedding file: [imgnet100k_dim128.txt](https://rooagi8-my.sharepoint.com/:t:/g/personal/chaoma_rooagi_com/ERJz6FZqNrtFutH3X9B8ad8B-w912c0xYrEo3smyBCEcwg?e=PRhMMF) (248.3MB)
* 2048-dimension embedding file: [imgnet100k_dim2048.txt](https://rooagi8-my.sharepoint.com/:t:/g/personal/chaoma_rooagi_com/ERGUdXFOKs5GnXuYAva2o50BopRWHbFxknJqk9yHkHuXLw?e=SYOdgz) (3.36GB)

You are free to choose any of the available embedding files to experiment with. However, make sure to set the `embedding_file_info` tuple in the notebook with values that match your selection. For example, if you choose "imgnet100k_dim2048.txt", be sure to set the embedding dimension to 2048 accordingly.

### Start and follow steps of tutorial

First, start the PostgreSQL server with the Roo-VectorDB extension enabled. Then launch the Jupyter server and open the [tutorial_image_search.ipynb](tutorial_image_search.ipynb) notebook. Follow the instructions step by step. In the first few steps (steps 1–2), you’ll need to provide some basic configuration information before proceeding.

<br>

<!-- Long Document Search -->
## Long Document Search

In this tutorial, we demonstrate how to perform long-document search using Roo-VectorDB. As an example, we treat books as long documents, and show how to run searches at different levels of granularity—such as chapters, sections, paragraphs, or the entire book.

### Download segmented book data

We use the [Pile](https://huggingface.co/datasets/EleutherAI/pile) dataset (specifically the *Books1* subset) as the source of data. This subset contains approximately 18,000 books, each ranging from 100,000 to 1,000,000 words. For this tutorial, we randomly sample 1,000 books from the dataset.
Because a single book is too large to store as one record—making both storage and search inefficient—we preprocess the books using [LangChain TextSplitter](https://python.langchain.com/docs/concepts/text_splitters/). Each book is split into 1024‑token chunks with a 30% overlap between adjacent chunks. Each chunk is stored as an individual row in the database table. The preprocessed dataset can be downloaded here:

1. Preprocessed Pile Books1 data file: [pile_book1.jsonl](https://rooagi8-my.sharepoint.com/:u:/g/personal/chaoma_rooagi_com/EUNiTYeTIPNKrr-NI4t-BOcB9mlh_15NIVNSIF7D75RztA?e=AecDqa) (506.5MB)

Please verify the file size after downloading to ensure the download completed successfully and the file is not corrupted.

### Start and follow steps of tutorial

First, start the PostgreSQL server with the Roo-VectorDB extension enabled. Then launch the Jupyter server and open the [tutorial_long_document_search.ipynb](tutorial_long_document_search.ipynb) notebook. Follow the instructions step by step. In the first few steps (steps 1–2), you’ll need to provide some basic configuration information before proceeding.
