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


def pub_str(key, pub):
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


def format_pubs():
    count = 0
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
            count += 1
            print("* " + pub_str(key, pub))

    print("\n" + str(count) + " publications.")


format_pubs()
