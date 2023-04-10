# SporeTec's custom ATEM Mini switcher
## Info
Grabs the image of your OBSbot Tiny 4k and pushes it into the obs virtual camera.  
"Should" work on Windows and Mac

[pyd/capALTERNATIVE.cpp](pyd/capALTERNATIVE.cpp) makes the capture use device paths instead of names.

Also includes:
* A Powershell script for a SRT Server [Docker/srtServer/srt.ps](Docker/srtServer/srt.ps)
* Dockerfile and starting script for a NOALBS container [Docker/NOALBS](Docker/NOALBS). See [https://github.com/715209/nginx-obs-automatic-low-bitrate-switching](https://github.com/715209/nginx-obs-automatic-low-bitrate-switching) for how to configure [Docker/NOALBS/config/config.json](Docker/NOALBS/config/config.json) and [Docker/NOALBS/config/.env](Docker/NOALBS/config/.env)


## Requirements
* obs installed and virtual cam not in use
* cd to the dir [pyd](pyd) and run `python setup.py build` -> put `pyd\build\lib.win-amd64-cpython-PYTHONVER` in your PYTHONPATH
* see [requirements.txt](requirements.txt)

## Howto
