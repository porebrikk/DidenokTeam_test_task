FROM python:3.11-alpine as base

FROM base as builder

RUN apk update && apk upgrade
RUN apk add --no-cache git g++ musl-dev libffi-dev openssl-dev
RUN pip install --upgrade pip

WORKDIR /install
COPY ./requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
RUN apk --no-cache add libpq

WORKDIR /didenok_team
COPY ./app app

WORKDIR /didenok_team/app
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
