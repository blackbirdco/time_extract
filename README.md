# Time Extract
A python lib to extract time entities from text

## Metadat extraction

### Usage

Le script utilise une fonction avec 2 paramètres :
- text to analyse
- a metadata

```sh
python SEM.py message metadata
```

Example:

```sh
python SEM.py 'je voudrais partir lundi' 'date'
```

## Installation

Since it's complex to have a valid environment to run treetagger + python. 
We provide a valid Dockerfile and some scripts to ease the tool usage.

1. Install docker https://docs.docker.com/engine/installation/
2. run bin/build_dev.sh

## Launch nlp env

```sh
bin/dev.sh
```

## Run webserver

```sh
bin/dev_server.sh
```

It listen on port 8080. Wait for POST calls on `/api/v1/metadata` and wait for 2 args:

* 'message' : the text to analyse
* 'name' : the name of the metadata (either date or duration)

There's an authentication mechanism that is reading the 'Http-Auth' header en check that it contains the same thing as in https://github.com/blackbirdco/time_extract/blob/master/secrets/config.yml

## Testing

```sh
bin/test.sh
```
