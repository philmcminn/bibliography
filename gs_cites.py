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

# Open the TSV file and read its contents
with open(citations_file, 'r') as tsvfile:
    # Create a CSV reader object with tab as the delimiter
    reader = csv.reader(tsvfile, delimiter='\t')
    # Skip the header row if needed
    header = next(reader)
    # Read each row in the TSV file and append it to the data list
    for row in reader:
        data.append(row)

for pub_info in data:
    gsid = pub_info[0]
    cites = int(pub_info[1])
    pub = get_pub_by_gsid(bib, gsid)
    
    if pub is None:
        pass
        #print("Warning could not find https://scholar.google.com/citations?view_op=view_citation&hl=en&user=ll6Fc7gAAAAJ&pagesize=80&citation_for_view=" + gsid)
    else: 
        year = pub["year"]
        cites_per_year = cites / (2023 - year + 1)
        print(pub["title"] + " " + str(cites) + " " + str(cites_per_year))
    
