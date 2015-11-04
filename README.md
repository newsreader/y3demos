# y3demos

This github contains the data used in the NewsReader timeline visualisation that can be found at [http://ic.vupr.nl/timeline](http://ic.vupr.nl/timeline). 

The data folder also contains a simplified version of the json that can be used in elasticsearch. The format currently contains the bulk loading format and can be loaded into an elasticsearch index using the command: 

curl -s -XPOST localhost:9200/_bulk --data-binary "@airbustimeline.json" 

(or appletimeline.json for apple, etc.)


