FROM thinkwhere/gdal-python

ADD requirements.txt /pulse/

WORKDIR /pulse

RUN pip install -r requirements.txt

COPY . /pulse/

RUN mkdir /tmp/maps
RUN mkdir /tmp/gifs

CMD ["python", "./test.py"]
