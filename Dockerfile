FROM python:3.8

WORKDIR /usr/src/adv_scum

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/adv_scum/requirements.txt

RUN pip install -U pip --no-cache-dir && \
    pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /usr/src/adv_scum/entrypoint.sh

COPY ./src /usr/src/adv_scum/src

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]