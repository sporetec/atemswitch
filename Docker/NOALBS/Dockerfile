FROM alpine

RUN apk update && apk add curl
RUN mkdir -p /opt/noalbs
WORKDIR  /opt/noalbs
RUN curl -sL https://github.com/715209/nginx-obs-automatic-low-bitrate-switching/releases/download/v2.7.3/noalbs-v2.7.3-x86_64-unknown-linux-musl.tar.gz -o noalbs.tar.gz
RUN tar -xvf noalbs.tar.gz --strip 1
RUN rm noalbs.tar.gz
RUN rm .env
RUN rm config.json
WORKDIR /home
ADD entrypoint.sh .

ENTRYPOINT [ "~/entrypoint.sh" ]

