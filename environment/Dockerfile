
FROM python@sha256:8762744791535492d53589886a0b2d308365611394c869f37c37617c05001229

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
