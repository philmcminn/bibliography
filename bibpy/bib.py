from enum import Enum

Venue = Enum(
    "Venue",
    ["BOOK_CHAPTER", "CONFERENCE", "JOURNAL", "PHD_THESIS", "TECH_REPORT", "WORKSHOP"],
)

def add_pub(bib, key, pub):
    if key in bib:
        print('"' + key + '" already in bib')
        quit()
    bib[key] = pub


def get_years(bib):
    years = {inner_dict["year"] for inner_dict in bib.values() if "year" in inner_dict}
    return sorted(years, reverse=True)


def get_pubs(bib, year):
    pubs = {
        key: inner_dict
        for key, inner_dict in bib.items()
        if "year" in inner_dict and inner_dict["year"] == year
    }
    return dict(sorted(pubs.items(), key=lambda item: item[1]["author"]))


def count_venue_type(bib, venue_type):
    filtered_entries = filter(
        lambda pub: isinstance(pub, dict)
        and "venue" in pub
        and "type" in pub["venue"]
        and pub["venue"]["type"] == venue_type,
        bib.values(),
    )
    count = len(list(filtered_entries))
    return count
