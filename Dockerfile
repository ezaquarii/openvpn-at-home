FROM node AS frontend
COPY . /src
WORKDIR /src/frontend
RUN make build-prod

FROM python:3-alpine3.7 AS builder
RUN apk add -U gcc musl-dev libffi-dev
RUN apk add -U openssl-dev
COPY . /src
WORKDIR /src/backend
RUN mkdir /wheel && pip wheel --no-cache-dir -r requirements.txt -w /wheel


FROM python:3-alpine3.7
COPY . /src
WORKDIR /src/backend
RUN apk add -U openssl libcrypto1.0 openvpn
COPY --from=frontend /src/backend/openvpnathome/apps/frontend/static /src/backend/openvpnathome/apps/frontend/static
COPY --from=builder /wheel /wheel
RUN pip install --no-cache-dir /wheel/*
RUN rm -f openvpnathome/config.py && \
    ./manage.py configure && \
    mkdir /data && \
    sed -i "s,get_backend_path('db.sqlite3'),'/data/openvpnathome.db'," openvpnathome/config.py
VOLUME /data
EXPOSE 80
CMD ./manage.py runserver --insecure 0.0.0.0:80
