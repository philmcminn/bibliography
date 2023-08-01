import bibtexparser
import bibtexparser.middlewares as m
import re
from unidecode import unidecode
from titlecase import titlecase

from parse_authors import *
from parse_venues import *

layers = [
    m.SeparateCoAuthors(True), # Co-authors should be separated as list of strings
]

file = "mcminn.bib"
library = bibtexparser.parse_file("mcminn.bib", append_middleware=layers)
repeated_whitespace_pattern = re.compile(r'\s+')

print ('from authors import *')
print ('from venues import *')
print ('bib = dict()')
print ('')

for entry in library.entries:
  
  entry_authors = entry.fields_dict['author'].value

  # year
  year_value = re.sub(repeated_whitespace_pattern, ' ', entry.fields_dict['year'].value)

  # title
  title_value = titlecase(re.sub(repeated_whitespace_pattern, ' ', entry.fields_dict['title'].value).replace('{', '').replace('}', '').replace('---', '—')).replace("'", "\\'")
  first = True

  # author and key
  author_value = '[';
  for author in entry_authors:
    author = re.sub(repeated_whitespace_pattern, ' ', author)
    author_array = author_to_array(author)
    if first: 
      key_value = unidecode(author_array[0]) + year_value
      first = False
    else:
      author_value = author_value + ', '

    author_value += author_var_name(author)      
  author_value += ']'

  # venue
  if 'booktitle' in entry.fields_dict:
    raw_venue_string = entry.fields_dict['booktitle'].value
    venue_value = venue_var_name(venue_acronym(raw_venue_string))  
  elif 'journal' in entry.fields_dict:
    raw_venue_string = entry.fields_dict['journal'].value
    venue_value = venue_var_name(venue_acronym(raw_venue_string))  
  elif 'techreport' == entry['ENTRYTYPE']:
    venue_value = 'shefcs'
  elif 'phdthesis' == entry['ENTRYTYPE']:
    venue_value = 'shef'    
  else:
    print ("Unhandled entry type: " + entry['ENTRYTYPE'])
    quit()

  ignore_fields = ['author', 'title', 'booktitle', 'journal', 'year', 'abstract', 'editor', 'pages', 'doi', 'gsid', 'authorship', 'sponsor', 'comment', 'jv']

  # iterate through remaining fields
  remaining_fields = dict()
  for field in entry.fields_dict:
     if field not in ignore_fields and field not in ignore_fields:
        remaining_fields[field] = re.sub(repeated_whitespace_pattern, ' ', entry.fields_dict[field].value)

  entry_code  = "bib['" + key_value + "'] = {"
  entry_code += "\n  'author': " + author_value
  entry_code += ",\n  'title': '" + title_value + "'"
  entry_code += ",\n  'venue': " + venue_value
  entry_code += ",\n  'year': " + year_value

  # pages
  if 'pages' in entry.fields_dict:
    raw_pages = entry.fields_dict['pages'].value.split('--') 
    entry_code += ",\n  'pages': ['" + raw_pages[0] + "', '" + raw_pages[1] + "']"

  if 'editor' in entry.fields_dict:
    entry_code += ",\n  'editor': ['TO COMPLETE']"

  for key in sorted(remaining_fields.keys()):
    if key not in ignore_fields:
        entry_code += ", \n  '" + key + "': '" + remaining_fields[key] + "'"

  # pub id fields
  doi = ''
  if 'doi' in entry.fields_dict:
     doi = entry.fields_dict['doi'].value
  entry_code += ",\n\n  'doi': '" + doi + "'"
  
  # previous gsids are incorrect
  entry_code += ",\n  'gsid': ''"

  # custom fields
  authorship = 'joint'
  if 'authorship' in entry.fields_dict:
    authorship = entry.fields_dict['authorship'].value
  entry_code += ", \n\n  'authorship': '" + authorship + "'"
     
  if 'sponsor' in entry.fields_dict:
     sponsor = entry.fields_dict['sponsor'].value
     entry_code += ",\n  'sponsor': ['" + sponsor.upper() + "']"

  entry_code += ",\n  'previous_key': '" + entry.key + "'"

  if 'jv' in entry.fields_dict:
    comment = entry.fields_dict['jv'].value
    entry_code += ",\n  'jv': '" + comment + "'"

  if 'comment' in entry.fields_dict:
    comment = entry.fields_dict['comment'].value
    entry_code += ",\n  'comment': '" + comment + "'"

  entry_code += "\n}\n"

  print (entry_code)
