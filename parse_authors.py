import bibtexparser
import bibtexparser.middlewares as m
import re
repeated_whitespace_pattern = re.compile(r'\s+')

def author_var_name(author):
  return author.split(',')[0].lower().replace('-', '').replace(' ', '').replace('{', '').replace('}', '').replace('\\\'', '')

def author_to_string(author):
  return author.replace('\\' , '\\\\')

# We want to add three new middleware layers to our parse stack:
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
  define_author = author_var_name(author) + ' = "' + author_to_string(author) + '"'
  print(define_author, file=f)

f.close()
