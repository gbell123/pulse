FROM thinkwhere/gdal-python

ADD requirements.txt /pulse/

WORKDIR /pulse

RUN pip install -r requirements.txt

COPY . /pulse/

CMD ["python", "./test.py"]
