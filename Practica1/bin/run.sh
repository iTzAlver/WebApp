#!/bin/bash
echo Abriendo Elasticsearch
~/elasticsearch-7.15.1/bin/elasticsearch -d -p 1300 # Puerto 9200
echo Abriendo Kibana
~/kibana-7.15.1/bin/kibana &                        # Puerto 5601
echo Abriendo Firefox
firefox localhost:5601