FROM jupyter/datascience-notebook:python-3.10.5

USER root
RUN apt-get update
RUN apt-get install -y gcc musl-dev python3-dev

RUN pip3 install -U pip setuptools wheel ruamel.yaml.clib fusepy

RUN pip3 install azureml-core azureml_widgets
RUN pip3 install azureml-sdk[notebooks]

#USER jovyan