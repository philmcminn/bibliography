from datetime import date
import os
from scholarly import scholarly
import csv
from mcminn import bib
from bibpy.bib import get_pub_by_gsid

today = str(date.today())
citations_file = "gs_citations/" + today + ".tsv"

if not os.path.exists(citations_file):

    search_query = scholarly.search_author('Phil McMinn')
    first_author_result = next(search_query)
    author = scholarly.fill(first_author_result)

    tsv_data = ""
    for pub in author['publications']:
        tsv_data += pub['author_pub_id'] + "\t" + str(pub['num_citations']) + "\n"
                                                      
    with open(citations_file, 'w') as file:
        file.write(tsv_data)

data = []

with open(citations_file, 'r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        data.append(row)

for pub_info in data:
    gsid = pub_info[0]
    cites = int(pub_info[1])
    pub = get_pub_by_gsid(bib, gsid)
    
    if pub is not None:
        year = pub["year"]
        cites_per_year = cites / (2023 - year + 1)
        print(pub["title"] + "\t" + str(pub["year"]) + "\t" + str(cites) + "\t" + str(cites_per_year))
    
