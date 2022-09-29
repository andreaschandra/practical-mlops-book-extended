FROM python:3.7

ARG VERSION

LABEL org.label-schema.version=$VERSION

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY webapp/* /webapp/

ENTRYPOINT ["python"]

CMD ["app.py"]