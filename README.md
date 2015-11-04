# y3demos

This github contains the data used in the NewsReader timeline visualisation that can be found at [http://ic.vupr.nl/timeline](http://ic.vupr.nl/timeline). 

The data folder also contains a simplified version of the json that can be used in elasticsearch. The format currently contains the bulk loading format and can be loaded into an elasticsearch index using the command: 

curl -s -XPOST localhost:9200/_bulk --data-binary "@airbustimeline.json" 

(or appletimeline.json for apple, etc.)


# NWR Visualisations 

* on the KnowledgeStore (needs SPARQL queries or via SimpleAPI)
	* Currently the Wikinews KS is online: [https://knowledgestore.fbk.eu/](https://knowledgestore.fbk.eu/)
* Streaming architecture (no fixed API for that, a bunch of code is available or you can simulate it by taking a NAF file or a sequence of input files) (Filip knows more about this)
* You can also work in SEM TRiG files (RDF)
* There are also json versions of the data 

See [http://ic.vupr.nl/timeline](http://ic.vupr.nl/timeline)  for previous demo

Visualisations on top of Elasticsearch: [http://siren.solutions/kibi/](http://siren.solutions/kibi/)

To easily inspect your elasticsearch indices you can use: [https://github.com/mobz/elasticsearch-head](https://github.com/mobz/elasticsearch-head) It doesn't quite work for ES2.0 yet, so I use 1.7.3 

To get kibi to work with a standard installation of ES, you need to change the port number in kibi-0.1.1-demo-lite-darwin-x64/kibi/config/kibi.yml to 9200 

