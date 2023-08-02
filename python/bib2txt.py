from authors import *
from venues import *
from bib import *
from mcminn import *


def author_str(author):
    formatted_name_parts = [name.strip().capitalize() for name in author[1:]]
    initials = "".join([name[0] for name in formatted_name_parts])
    return f"{initials} {author[0]}"


def authors_str(authors):
    authors_str = [author_str(author) for author in authors]
    if len(authors_str) == 0:
        return ""
    elif len(authors_str) == 1:
        return authors_str[0]
    else:
        return ", ".join(authors_str[:-1]) + " and " + authors_str[-1]


def venue_str(venue):
    if venue["type"] == Venue.BOOK_CHAPTER:
        return "In " + venue["name"]
    elif venue["type"] == Venue.CONFERENCE or venue["type"] == Venue.WORKSHOP:
        suffix = ""
        if venue["acronym"] != "":
            suffix = " (" + venue["acronym"] + ")"
        return venue["name"] + suffix
    elif venue["type"] == Venue.JOURNAL:
        return venue["name"]
    elif venue["type"] == Venue.PHD_THESIS:
        return "PhD Thesis, " + venue["name"]
    elif venue["type"] == Venue.TECH_REPORT:
        return "Technical Report, " + venue["name"]


def format_pub(key, pub):
    return (
        authors_str(pub["author"])
        + ". "
        + pub["title"]
        + ". "
        + venue_str(pub["venue"])
        + ", "
        + str(pub["year"])
        + "."
    )


def format_bib():
    years = get_years(bib)

    first = True
    for year in years:
        if first:
            first = False
        else:
            print()

        year_str = str(year)
        rule = "-" * len(year_str)
        print(year_str + "\n" + rule)

        pubs = get_pubs(bib, year)

        for key, pub in pubs.items():
            print("* " + format_pub(key, pub))


format_bib()

print("\n" + str(len(bib)) + " publications:")

types = {
    Venue.JOURNAL: "journal articles",
    Venue.CONFERENCE: "conference papers",
    Venue.WORKSHOP: "workshop papers",
    Venue.BOOK_CHAPTER: "book chapters",
    Venue.TECH_REPORT: "technical reports",
    Venue.PHD_THESIS: "phd theses",
}

for type, type_str in types.items():
    print("* " + str(count_venue_type(bib, type)) + " " + type_str)
