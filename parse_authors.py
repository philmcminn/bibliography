import bibtexparser
import bibtexparser.middlewares as m
import re

def author_var_name(raw_author_string): 
  names = raw_author_string.split(',')
  surname = names[0].strip()
  first_names = names[1].strip()

  return (surname
            .lower()
            .replace('-', '')
            .replace(' ', '')
            .replace('{', '')
            .replace('}', '')
            .replace('\\\'', '') 
            + "_" + 
            first_names[0].lower())

def author_to_array(raw_author_string):
  author = (raw_author_string
            .replace("\\'{e}" , 'é')
            .replace("{\\'e}", 'é')
            .replace("\\'{a}", 'á'))
  
  names = author.split(',')
  surname = names[0].strip()
  first_names = names[1].split()

  processed_first_names = []
  for first_name in first_names:
    split = first_name.split('.')
    for element in split:
      if element.strip() != '':
        if len(element) == 1:
          element = element + "."
        processed_first_names.append(element)

  return [surname] + processed_first_names

def write_authors_file():
  repeated_whitespace_pattern = re.compile(r'\s+')

  layers = [
      m.SeparateCoAuthors(True), # Co-authors should be separated as list of strings
  ]

  file = "mcminn.bib"
  library = bibtexparser.parse_file("mcminn.bib", append_middleware=layers)

  authors = set()

  for entry in library.entries:
    entry_authors = entry.fields_dict['author'].value
    for author in entry_authors:
      author = re.sub(repeated_whitespace_pattern, ' ', author)
      authors.add(author)
        
  authors = sorted(authors)

  f = open('parsed_authors.py', 'w')

  for author in authors:
    code = author_var_name(author) + ' = ' # the assignment part

    names = author_to_array(author)
    first = True
    code = code + '['
    for name in names:
      if first:
        first = False
      else: 
        code = code + ', '
      code = code + '"' + name + '"'    
    code = code + ']'
    
    print(code, file=f)

  f.close()

write_authors_file()
