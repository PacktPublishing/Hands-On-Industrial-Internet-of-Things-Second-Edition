FROM pytorch/pytorch:2.3.1-cuda11.8-cudnn8-devel

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY start-notebook.sh /
RUN chmod +x /start-notebook.sh

RUN mkdir /workspace/work

CMD [ "/start-notebook.sh" ]