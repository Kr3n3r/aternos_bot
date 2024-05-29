ARG BASE_IMAGE

FROM ${BASE_IMAGE}

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "pooling.py"]