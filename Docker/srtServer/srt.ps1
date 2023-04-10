docker rm -f srt-server | out-null
docker run -d -p 30000:30000/udp -p 8181:8181/tcp --name=srt-server --restart=unless-stopped --pull=always -v sls-b3ck-edit_data:/data b3ckontwitch/sls-b3ck-edit