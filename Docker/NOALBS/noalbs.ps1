docker rm -f noalbs | out-null
docker run -it --name=noalbs --restart=unless-stopped --mount src=$PWD/config,target=/home/noalbs_files,type=bind local/noalbs