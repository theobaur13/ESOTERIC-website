# ESOTERIC-website
A demo website for ESOTERIC. (Elasticsearch Semantic Optimized Text Extraction Retrieval from Information Corpus)

## Prerequisites
To run this system [Elasticsearch 8.12.2 x64](https://www.elastic.co/downloads/past-releases/elasticsearch-8-12-2) needs to be installed and an Elasticsearch database needs to be active. A detailed guide on how to set up Elasticsearch can be found [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html#_start_elasticsearch). 

To load embeddings  into the Elasticsearch database it is highly recommended that a [Google Colab](https://colab.research.google.com/) instance with a V100 GPU is used as this process is computationally expensive. Once the Elasticsearch database is loaded the retrieval process can be executed using only CPU power.

To run the web-application the Elasticsearch database must already be initialised, the full process can be found in the [ESOTERIC README](https://github.com/theobaur13/ESOTERIC/blob/master/README.md) in the Installation section.

## Installation

Clone repository.
```
git  clone  https://github.com/theobaur13/ESOTERIC-website
```
Set up virtual environment.
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Create a `.env` file inside the `ESOTERIC-website` root directory and fill with the following information:
```
ES_HOST_URL={ELASTICSEARCH DB URL}
ES_USER={ELASTICSEARCH DB USERNAME}
ES_PASS={ELASTICSEARCH DB PASSWORD}
ES_PORT={ELASTICSEARCH DB PORT}
ES_SCHEME={ELASTICSEARCH DB HTTP SCHEME}
```

### Passage Retrieval Model
Create the `models` directory inside the `app/ESOTERIC/` directory:
```
mkdir app\ESOTERIC\models
```
Create a `relevancy_classification` model inside the models directory.
```
mkdir app\ESOTERIC\models\relevancy_classification
```
Download the model [files](https://huggingface.co/theobaur/relevancy_classification_FEVER) and paste the model files into the `relevancy_classification` directory.
The directory structure should be as follows:
```
ESOTERIC-website
│
└───app
    │
    └───ESOTERIC
        │
        └───models
                └───relevancy_classification
                        │ config.json
                        │ model.safetensors
                        │ relevancy_classification_20000.json
                        │ special_tokens_map.json
                        │ tokenizer_config.json
                        │ tokenizer.json
                        │ vocab.txt
```
## Usage

Activate virtual environment.

```
venv\Scripts\activate
```
Run the `WSGI.py file`
```
py wsgi.py
```

## Contributing

  

Pull requests are welcome. For major changes, please open an issue first

to discuss what you would like to change.

  

Please make sure to update tests as appropriate.

  

## License

  

[MIT](https://choosealicense.com/licenses/mit/)
