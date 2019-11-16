FROM thinkwhere/gdal-python

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./test.py"]
