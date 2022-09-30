FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /code

COPY . /code

RUN make install

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
