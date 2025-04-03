FROM python:3.12-slim AS builder

WORKDIR /

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt install -y nano weasyprint && \
    apt install -y gcc g++ python3-dev python3-pip musl-dev libffi-dev

RUN python -m venv /opt/venv
ENV PATH "/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

FROM python:3.12-slim

COPY --from=builder /opt/venv /opt/venv

WORKDIR /
COPY . .
RUN mkdir /dbs

ENV PATH "/opt/venv/bin:$PATH"
ENV PYTHONPATH "/opt/venv/bin:$PYTHONPATH"
