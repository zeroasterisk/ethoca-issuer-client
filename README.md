# An API client allowing an Issuer to use Ethoca

This is a quick-and-rough client for Ethoca's Digital Receipts API, which would be used by a credit card issuer, to lookup the receipt URL for a credit card transaction.

## Setup

This requires settings to be configured in a `.env` file, which is not included in this repo.

```
KEYID="myaccountkeyid1234"
APIKEY="###myapikey###"
```

## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run apiclient cli application

$ apiclient --help


### run pytest / coverage

$ make test
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `Ethoca Issuer Client`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it apiclient --help
```
