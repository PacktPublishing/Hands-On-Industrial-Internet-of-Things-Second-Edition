FROM python:3.10-slim-bullseye

RUN apt update
RUN apt upgrade -y
RUN apt install -y git curl libffi-dev git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev

RUN curl https://pyenv.run | bash

RUN pip install psycopg2-binary boto3 virtualenv
RUN pip install --no-cache mlflow==2.15.1

RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $HOME/.bashrc
RUN echo '[[ -d $PYENV_ROOT/bin ]] &&  export PATH="$PYENV_ROOT/bin:$PATH"' >> $HOME/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> $HOME/.bashrc