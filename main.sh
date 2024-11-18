#!/usr/bin/bash

python3 /home/lera_proxy/workspace/github.com/codenodrama/static_site_generator/src/main.py 
cd public && python3 -m http.server 8888
