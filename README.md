# SporeTec's custom ATEM Mini switcher
## Info
Grabs the image of your OBSbot Tiny 4k and pushes it into the obs virtual camera.  
"Should" work on Windows and Mac

[pyd/capALTERNATIVE.cpp](pyd/capALTERNATIVE.cpp) makes the capture use device paths instead of names.

Also includes:
* A Powershell script for a SRT Server [Docker/srtServer/srt.ps](Docker/srtServer/srt.ps)
* Dockerfile and starting script for a NOALBS container [Docker/NOALBS](Docker/NOALBS)


## Requirements
* obs installed and virtual cam not in use
* cd to the dir [pyd](pyd) and run `python setup.py build` -> put `pyd\build\lib.win-amd64-cpython-PYTHONVER` in your PYTHONPATH
* see [requirements.txt](requirements.txt)

## Howto
