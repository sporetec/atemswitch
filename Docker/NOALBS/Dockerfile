FROM alpine

RUN apk update && apk add curl
RUN mkdir -p /opt/noalbs && cd /opt/noalbs
RUN curl -sL https://github.com/715209/nginx-obs-automatic-low-bitrate-switching/releases/download/v2.7.3/noalbs-v2.7.3-x86_64-unknown-linux-musl.tar.gz -o noalbs.tar.gz
RUN tar -xvf noalbs.tar.gz --strip 1
RUN rm config.json
RUN rm .env

ENTRYPOINT [ "noalbs" ]

