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
    return pubs
    # return sorted(pub.values(), key=lambda x: x['title'])
