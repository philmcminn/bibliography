import bibtexparser
import re

def venue_acronym(raw_venue_string):
  repeated_whitespace_pattern = re.compile(r'\s+')
  venue = re.sub(repeated_whitespace_pattern, ' ', raw_venue_string)
  
  bracket = venue.rfind('(')
  if bracket != -1:
    orig_acronym = venue[bracket + 1:]
    
    digit_match = re.search(r'^\D+', orig_acronym)

    if digit_match:
      acronym = digit_match.group()

    if acronym == orig_acronym:
        closing_bracket_index = acronym.find(')')
        if closing_bracket_index != -1:
            acronym = acronym[:closing_bracket_index]
  else:
    acronym = ''.join([char for char in venue if char.isupper()])
    acronym = acronym.replace('IEEE', '').replace('ACM', '')

  # some preprogrammed acronyms for venues where the rules don't apply...
  if venue.startswith("ACM Transactions on Software"):
    acronym = 'TOSEM'

  return acronym.strip()

def venue_name(raw_venue_string):
  repeated_whitespace_pattern = re.compile(r'\s+')
  venue = re.sub(repeated_whitespace_pattern, ' ', raw_venue_string)  
  name = venue.replace('---', '—').replace('\\&', '&')

  if name.rfind('(') != -1:
    name = name[:name.rfind('(')]

  return name.strip()

def venue_var_name(acronym):
  var_name = (acronym.lower()
              .replace('\&', '')
              .replace('-', '_')
              .replace('/', '')
              .replace(' ', ''))
  return var_name

def booktitle_type(venue_name):
  type = 'BOOK_CHAPTER'
  if 'workshop' in venue_name.lower():
    type = 'WORKSHOP'
  elif 'conference' in venue_name.lower():
    type = 'CONFERENCE'
  elif 'symposium' in venue_name.lower():
    type = 'CONFERENCE'
  return type

def write_venues_file():
  file = "mcminn.bib"
  library = bibtexparser.parse_file("mcminn.bib")

  venues = dict()

  # conferences
  for entry in library.entries:
    if 'booktitle' in entry.fields_dict:
      raw_venue_string = entry.fields_dict['booktitle'].value
      name = venue_name(raw_venue_string)
      acronym = venue_acronym(raw_venue_string)    
      type = booktitle_type(name)
      venues[name] = [acronym, type]
    elif 'journal' in entry.fields_dict:
      raw_venue_string = entry.fields_dict['journal'].value
      name = venue_name(raw_venue_string)
      acronym = venue_acronym(raw_venue_string)    
      type = 'JOURNAL'
      venues[name] = [acronym, type]

  sorted_items = sorted(venues.items(), key=lambda item: item[1][0])

  f = open('parsed_venues.py', 'w')

  for name, details in sorted_items:
    acronym = details[0]
    type = details[1]  
    var_name = venue_var_name(acronym)
    
    define_venue = var_name + " = {'name': '" + name + "', 'acronym': '" + acronym + "', 'type': " + type + "}"
    print(define_venue, file=f)

  f.close()

write_venues_file()      
