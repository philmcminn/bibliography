import re
from bibpy.bib import Venue

def bibtex_str(str):
    str = (str.replace("é", "{\\'e}").
           replace("á", "{\\'a}").
           replace("è", "{\\`e}").
           replace("ö", "{\\\"o}").
           replace("&", "\\&").
           replace("—", "---").
           replace("–", "--"))
    
    return str


def preserve_case(str, words):
    for word in words:
        pattern = r'\b' + re.escape(word) + r'\b'
        str = re.sub(pattern, "{" + word + "}", str)
    return str


def author_str(author):
    surname = author[0]
    first_and_middle_names = " ".join(author[1:])
    formatted_author = f"{surname}, {first_and_middle_names}"
    return formatted_author


def authors_str(authors):
    authors_str = [author_str(author) for author in authors]
    return " and ".join(authors_str)


def pub_type(venue_type):
    if venue_type == Venue.BOOK_CHAPTER:
        return "incollection"
    elif venue_type == Venue.CONFERENCE or venue_type == Venue.WORKSHOP:
        return "inproceedings"
    elif venue_type == Venue.JOURNAL:
        return "article"
    elif venue_type == Venue.PHD_THESIS:
        return "phdthesis"
    elif venue_type == Venue.TECH_REPORT:
        return "techreport"

def pub_form(venue_type):
    if venue_type == Venue.BOOK_CHAPTER or venue_type == Venue.CONFERENCE or venue_type == Venue.WORKSHOP:
        return "booktitle"
    elif venue_type == Venue.JOURNAL:
        return "journal"
    elif venue_type == Venue.PHD_THESIS:
        return "school"
    elif venue_type == Venue.TECH_REPORT:
        return "institution"
    
def venue_str(venue):
    venue_str = venue["name"]
    if venue["type"] == Venue.CONFERENCE or venue["type"] == Venue.WORKSHOP:
        if venue["acronym"] != "":
            venue_str += " (" + venue["acronym"] + ")"
    return venue_str

def pages_str(pages):
    return "--".join(pages)

def format_pub(bib, pub_key): 
    pub = bib[pub_key]
    venue_type = pub["venue"]["type"]

    bibtex_entry_type = pub_type(venue_type)
    bibtex_entries = {}
    bibtex_entries["author"] = authors_str(pub["author"])
    bibtex_entries["title"] = preserve_case(pub["title"], pub.get("preserve_case", []))
    bibtex_entries[pub_form(venue_type)] = venue_str(pub["venue"])
    bibtex_entries["year"] = str(pub["year"])

    pages = pub.get("pages")
    if (pages is not None):
        bibtex_entries["pages"] = pages_str(pages)

    editor = pub.get("editor")
    if (editor is not None):
        bibtex_entries["editor"] = authors_str(pub["editor"])

    if venue_type == Venue.BOOK_CHAPTER:
        bibtex_entries["publisher"] = pub["publisher"]

    remaining_keys = ["issue", "number", "series", "volume"]
    for remaining_key in remaining_keys:
        remaining_value = pub.get(remaining_key)
        if (remaining_value is not None):
            bibtex_entries[remaining_key] = remaining_value

    # format the bib entry
    longest_key = max(len(key) for key in bibtex_entries.keys())    
    pub_str = "@" + bibtex_entry_type + "{" + pub_key + ",\n"
    first = True
    for bibtex_entry_key, bibtex_entry_value in bibtex_entries.items(): 
        if first:
            first = False
        else:
            pub_str += ",\n"   
        formatted_key = bibtex_entry_key.ljust(longest_key)
        formatted_value = bibtex_str(bibtex_entry_value)
        pub_str += "  " + formatted_key + " = \"" + formatted_value + "\""
    pub_str += "\n}\n\n"

    return pub_str

def format_bib(bib):
    bib_str = ''
    for key in bib.keys():
        bib_str += format_pub(bib, key)
    return bib_str


