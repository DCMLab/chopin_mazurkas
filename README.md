# annotation_workflow_template

This repo holds the current version of the DCML annotation workflow which is pulled by all subcorpus repos upon push to their main branch. 

Please note that the `meta_ corpora` branch should be used with collections of corpora.


# Overview
|  file_name  |measures|labels|standard|  annotators   |  reviewers  |
|-------------|-------:|-----:|--------|---------------|-------------|
|BI105-2op30-2|      64|   132|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI105-3op30-3|      95|   171|2.1.1   |Wendelin Bitzan|JH (1-72), AN|
|BI105-4op30-4|     139|   241|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI115-1op33-1|      48|    85|2.1.1   |Wendelin Bitzan|JH           |
|BI115-2op33-2|     135|   200|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI115-3op33-3|      48|   120|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI115-4op33-4|     224|   390|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI122op41-2  |      68|   143|2.1.1   |Wendelin Bitzan|JH           |
|BI126-1op41-4|      74|   152|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI126-3op41-1|     139|   252|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI126-4op41-3|      78|   132|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI134        |     112|   327|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI140        |     131|   239|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI145-1op50-1|     104|   225|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI145-2op50-2|     103|   162|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI145-3op50-3|     192|   379|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI153-1op56-1|     204|   477|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI153-2op56-2|      84|   174|2.1.1   |Wendelin Bitzan|JH           |
|BI153-3op56-3|     220|   532|2.1.1   |Wendelin Bitzan|AN           |
|BI157-1op59-1|     130|   279|2.1.1   |Wendelin Bitzan|AN           |
|BI157-2op59-2|     111|   236|2.1.1   |Wendelin Bitzan|AN           |
|BI157-3op59-3|     154|   374|2.1.1   |Wendelin Bitzan|AN           |
|BI16-1       |      32|    55|1.0.0   |Wendelin Bitzan|             |
|BI16-2       |      32|    51|2.3.0   |Wendelin Bitzan|             |
|BI162-1op63-1|     102|   205|2.1.1   |Wendelin Bitzan|AN           |
|BI162-2op63-2|      56|    91|2.1.1   |Wendelin Bitzan|AN           |
|BI162-3op63-3|      76|   169|2.1.1   |Wendelin Bitzan|AN           |
|BI163op67-4  |      80|   145|2.1.1   |Wendelin Bitzan|AN           |
|BI167op67-2  |      56|    80|2.1.1   |Wendelin Bitzan|AN           |
|BI168op68-4  |      40|    97|2.1.1   |Wendelin Bitzan|AN           |
|BI18op68-2   |      64|   114|2.1.1   |Wendelin Bitzan|JH           |
|BI34op68-3   |      60|    99|2.1.1   |Wendelin Bitzan|JH           |
|BI38op68-1   |      73|   140|2.1.1   |Wendelin Bitzan|JH           |
|BI60-1op06-1 |      72|   196|2.1.1   |Wendelin Bitzan|JH           |
|BI60-2op06-2 |      72|    85|2.1.1   |Wendelin Bitzan|JH           |
|BI60-3op06-3 |      90|   148|2.1.1   |Wendelin Bitzan|JH           |
|BI60-4op06-4 |      24|    58|2.1.1   |Wendelin Bitzan|JH           |
|BI61-1op07-1 |      64|    96|2.1.1   |Wendelin Bitzan|JH           |
|BI61-2op07-2 |      56|   115|2.1.1   |Wendelin Bitzan|JH           |
|BI61-3op07-3 |     105|   206|2.1.1   |Wendelin Bitzan|JH           |
|BI61-4op07-4 |      44|   103|2.1.1   |Wendelin Bitzan|JH           |
|BI61-5op07-5 |      20|    38|2.1.1   |Wendelin Bitzan|JH           |
|BI71         |      68|   170|        |               |             |
|BI73         |      32|    44|1.0.0   |Wendelin Bitzan|             |
|BI77-1op17-1 |      60|   119|2.1.1   |Wendelin Bitzan|JH           |
|BI77-2op17-2 |      68|   178|2.1.1   |Wendelin Bitzan|JH           |
|BI77-3op17-3 |      81|   214|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI77-4op17-4 |     132|   223|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI85         |      57|   103|        |               |             |
|BI89-1op24-1 |      64|   122|2.1.1   |Wendelin Bitzan|JH, AN       |
|BI89-2op24-2 |     120|   226|2.1.1   |Wendelin Bitzan|JH           |
|BI89-3op24-3 |      43|    63|2.1.1   |Wendelin Bitzan|JH           |
|BI89-4op24-4 |     146|   280|2.1.1   |Wendelin Bitzan|JH (1-34), AN|
|BI93-1op67-1 |      60|    93|2.1.1   |Wendelin Bitzan|JH           |
|BI93-2op67-3 |      56|    93|2.1.1   |Wendelin Bitzan|JH, AN       |
