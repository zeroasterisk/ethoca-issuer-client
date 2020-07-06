# An API client allowing an Issuer to use Ethoca

This is a quick-and-rough client for Ethoca's Digital Receipts API, which would be used by a credit card issuer, to lookup the receipt URL for a credit card transaction.

## Setup for Usage

Install python3 & pip3, then install all (framework) packages for this project.

```
$ pip install -r requirements.txt

$ pip install setup.py
```

Make a copy of the configuration file and edit to setup your API keys and details.

```
$ cp config/apiclient.yml.example ~/.apiclient.yml

$ vim config/apiclient.yml
```

WARNING be sure not to submit the API credentials to any version control system.

### Setup for Development

```
### create a virtualenv for development

Install `viralenv` if it's not already installed.
Then setup an environment for this project.

```
$ pip install virtualenv

$ make virtualenv

$ source env/bin/activate
```


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
