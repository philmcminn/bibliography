from enum import Enum

Venue = Enum('Venue', ['BOOK_CHAPTER', 'CONFERENCE', 'JOURNAL', 'PHD_THESIS', 'TECH_REPORT', 'WORKSHOP'])

# Book chapters
esev = {'name': 'Empirical Software Engineering and Verification', 'type': Venue.BOOK_CHAPTER}
fmt = {'name': 'Formal Methods and Testing', 'type': Venue.BOOK_CHAPTER}

# Conferences
ase = {'name': 'International Conference on Automated Software Engineering', 'acronym': 'ASE', 'type': Venue.CONFERENCE}
ast_c = {'name': 'International Conference on Automation of Software Test', 'acronym': 'AST', 'type': Venue.CONFERENCE}
cec = {'name': 'Congress on Evolutionary Computation', 'acronym': 'CEC', 'type': Venue.CONFERENCE}
cseet = {'name': 'International Conference on Software Engineering Education and Training', 'acronym': 'CSEE&T', 'type': Venue.CONFERENCE}
gecco = {'name': 'Genetic and Evolutionary Computation Conference', 'acronym': 'GECCO', 'type': Venue.CONFERENCE}
hicss = {'name': 'Hawaii International Conference on System Sciences', 'acronym': 'HICSS', 'type': Venue.CONFERENCE}
icse = {'name': 'International Conference on Software Engineering', 'acronym': 'ICSE', 'type': Venue.CONFERENCE}
icse_seet = {'name': 'International Conference on Software Engineering — Software Engineering Education and Training track', 'acronym': 'ICSE-SEET', 'type': Venue.CONFERENCE}
icse_seip = {'name': 'International Conference on Software Engineering — Software Engineering In Practice track', 'acronym': 'ICSE-SEIP', 'type': Venue.CONFERENCE}
icse_jseet = {'name': 'International Conference on Software Engineering — Joint Track on Software Engineering Education and Training', 'acronym': 'ICSE-JSEET', 'type': Venue.CONFERENCE}
icsm = {'name': 'International Conference on Software Maintenance', 'acronym': 'ICSM', 'type': Venue.CONFERENCE}
icsme = {'name': 'International Conference on Software Maintenance and Evolution', 'acronym': 'ICSME', 'type': Venue.CONFERENCE}
icst = {'name': 'International Conference on Software Testing, Verification and Validation', 'acronym': 'ICST', 'type': Venue.CONFERENCE}
issta = {'name': 'International Symposium on Software Testing and Analysis', 'acronym': 'ISSTA', 'type': Venue.CONFERENCE}
seke = {'name': 'International Conference on Software Engineering and Knowledge Engineering', 'acronym': 'SEKE', 'type': Venue.CONFERENCE}
sigcse = {'name': 'ACM SIGCSE Technical Symposium on Computer Science Education', 'acronym': 'SIGCSE', 'type': Venue.CONFERENCE}
ssbse = {'name': 'International Symposium on Search-Based Software Engineering', 'acronym': 'SSBSE', 'type': Venue.CONFERENCE}
taicpart = {'name': 'Testing: Academic and Industrial Conference — Practice And Research Techniques', 'acronym': 'TAIC PART', 'type': Venue.CONFERENCE}

# Journals
bs = {'name': 'BioSystems', 'type': Venue.JOURNAL}
ec = {'name': 'Evolutionary Computation', 'type': Venue.JOURNAL}
emse = {'name': 'Empirical Software Engineering', 'acronym': 'EmSE', 'type': Venue.JOURNAL}
esecfse = {'name': 'Joint meeting of the European Software Engineering Conference and the ACM SIGSOFT Symposium on the Foundations of Software Engineering', 'acronym': 'ESEC/FSE', 'type': Venue.CONFERENCE}
ib = {'name': 'Integrative Biology', 'type': Venue.JOURNAL}
ist = {'name': 'Information and Software Technology', 'acronym': 'IST', 'type': Venue.JOURNAL}
jrsi = {'name': 'Journal of the Royal Society Interface', 'abbreviation': 'J. R. Soc. Interface', 'type': Venue.JOURNAL}
jss = {'name': 'Journal of Systems and Software', 'acronym': 'JSS', 'type': Venue.JOURNAL}
kcse = {'name': 'Korea Conference on Software Engineering', 'acronym': 'KCSE', 'type': Venue.CONFERENCE}
plosone = {'name': 'PLOS ONE', 'type': Venue.JOURNAL}
qsic = {'name': 'International Conference on Quality Software', 'acronym': 'QSIC', 'type': Venue.CONFERENCE}
scp = {'name': 'Science of Computer Programming', 'acronym': 'SCP', 'type': Venue.JOURNAL}
stvr = {'name': 'Software Testing, Verification and Reliability', 'acronym': 'STVR', 'type': Venue.JOURNAL}
tcs = {'name': 'Theoretical Computer Science', 'acronym': 'TCS', 'type': Venue.JOURNAL}
tosem = {'name': 'ACM Transactions on Software Engineering and Methodology', 'acronym': 'TOSEM', 'type': Venue.JOURNAL}
tse = {'name': 'IEEE Transactions on Software Engineering', 'acronym': 'TSE', 'type': Venue.JOURNAL}

# Workshops
apr = {'name': 'International Workshop on Automated Program Repair', 'acronym': 'APR', 'type': Venue.WORKSHOP}
ast_w = {'name': 'International Workshop on Automation of Software Test', 'acronym': 'AST', 'type': Venue.WORKSHOP}
mabs = {'name': 'Multi-Agent-Based Simulation XIII — International Workshop on Multi-Agent Simulation', 'acronym': 'MABS', 'type': Venue.WORKSHOP}
mutation = {'name': 'International Workshop on Mutation Analysis', 'acronym': 'Mutation', 'type': Venue.WORKSHOP}
ppig = {'name': 'Psychology of Programming Interest Group Annual Workshop', 'acronym': 'PPIG', 'type': Venue.WORKSHOP}
regression = {'name': 'International Workshop on Regression Testing', 'acronym': 'Regression', 'type': Venue.WORKSHOP}
sbst = {'name': 'International Workshop on Search-Based Software Testing', 'acronym': 'SBST', 'type': Venue.WORKSHOP}
scam = {'name': 'International Working Conference on Source Code Analysis & Manipulation', 'acronym': 'SCAM', 'type': Venue.CONFERENCE}
stov = {'name': 'International Workshop on Software Test Output Validation', 'acronym': 'STOV', 'type': Venue.WORKSHOP}
uktest = {'name': 'UK Software Testing Workshop', 'acronym': 'UKTest', 'type': Venue.WORKSHOP}
woda = {'name': 'International Workshop on Dynamic Analysis', 'acronym': 'WODA', 'type': Venue.WORKSHOP}

# Technical Reports
shefcs = {'name': 'Department of Computer Science, University of Sheffield', 'type': Venue.TECH_REPORT}

# PhD Thesis
shef = {'name': 'University of Sheffield', 'type': Venue.PHD_THESIS}