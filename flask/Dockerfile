FROM python:3.9.9

WORKDIR /home/moljin/FDKproject0.1/

RUN git clone https://github.com/moljin/FDKproject0.1.git
WORKDIR /home/moljin/FDKproject0.1/flask/

RUN python -m pip install --upgrade pip

RUN pip install -r flask/requirements.txt

EXPOSE 5000

CMD ["run", "--host", "0.0.0.0"]