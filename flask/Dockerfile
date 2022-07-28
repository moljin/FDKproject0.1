FROM python:3.9.9

# github에서 내려받는 작업: 내려받으면 FDKproject0.1폴더가 만들어진다.
WORKDIR /home/moljin/
RUN git clone https://github.com/moljin/FDKproject0.1.git

# 만들어진 FDKproject0.1 폴더에서 작업
WORKDIR /home/moljin/FDKproject0.1/
RUN python -m pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r flask/requirements.txt

# flask 폴더 안에 있는 app.py실행
EXPOSE 5000
#CMD ["python3", "flask/app.py", "--host=0.0.0.0"]
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0", "app:app"]
