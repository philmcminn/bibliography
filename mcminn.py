from authors import *
from venues import *
from bibpy.bib import add_pub

bib = dict()

add_pub(
    bib,
    "Gruber2024",
    {
        "author": [gruber_m, roslan_m, parry_o, scharnbock_f, mcminn_p, fraser_g],
        "title": "Do Automatic Test Generation Tools Generate Flaky Tests?",
        "venue": icse,
        "year": 2024,
        "doi": "",
        "gsid": "",
        "authorship": "joint",
    },
)

add_pub(
    bib,
    "Parry2023",
    {
        "author": [parry_o, hilton_m, kapfhammer_g, mcminn_p],
        "title": "Empirically Evaluating Flaky Test Detection Techniques Combining Test Case Rerunning and Machine Learning Models",
        "venue": emse,
        "year": 2023,
        "issue": "3",
        "volume": "28",
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:uLbwQdceFCQC",
        "authorship": "joint",
        "previous_key": "j26",
    },
)

add_pub(
    bib,
    "Levai2023",
    {
        "author": [levai_z, mcminn_p],
        "title": "Batching Non-Conflicting Mutations for Efficient, Safe, Parallel Mutation Analysis in Rust",
        "venue": icst,
        "year": 2023,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:_Ybze24A_UAC",
        "authorship": "joint",
        "previous_key": "c75",
    },
)

add_pub(
    bib,
    "Roslan2022",
    {
        "author": [roslan_m, rojas_j, mcminn_p],
        "title": "An Empirical Comparison of EvoSuite and DSpot for Improving Developer-Written Test Suites With Respect to Mutation Score",
        "preserve_case": ["EvoSuite", "DSpot"],
        "venue": ssbse,
        "year": 2022,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:JQOojiI6XY0C",
        "authorship": "joint",
        "previous_key": "c74",
    },
)

add_pub(
    bib,
    "Parry2022",
    {
        "author": [parry_o, hilton_m, kapfhammer_g, mcminn_p],
        "title": "What Do Developer-Repaired Flaky Tests Tell Us About the Effectiveness of Automated Flaky Test Detection?",
        "venue": ast_c,
        "year": 2022,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:VL0QpB8kHFEC",
        "authorship": "joint",
        "previous_key": "c73",
    },
)

add_pub(
    bib,
    "Parry2022a",
    {
        "author": [parry_o, hilton_m, kapfhammer_g, mcminn_p],
        "title": "Surveying the Developer Experience of Flaky Tests",
        "venue": icse_seip,
        "year": 2022,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:WqliGbK-hY8C",
        "authorship": "joint",
        "previous_key": "c72",
    },
)

add_pub(
    bib,
    "Parry2022b",
    {
        "author": [parry_o, hilton_m, kapfhammer_g, mcminn_p],
        "title": "A Survey of Flaky Tests",
        "venue": tosem,
        "year": 2022,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:JoZmwDi-zQgC",
        "authorship": "joint",
        "previous_key": "j25",
    },
)

add_pub(
    bib,
    "Parry2022c",
    {
        "author": [parry_o, hilton_m, kapfhammer_g, mcminn_p],
        "title": "Evaluating Features for Machine Learning Detection of Order- And Non-Order-Dependent Flaky Tests",
        "venue": icst,
        "year": 2022,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:5awf1xo2G04C",
        "authorship": "joint",
        "previous_key": "c71",
    },
)

add_pub(
    bib,
    "Althomali2022",
    {
        "author": [althomali_i, kapfhammer_g, mcminn_p],
        "title": "Automated Repair of Responsive Web Page Layouts",
        "venue": icst,
        "year": 2022,
        "doi": "",
        "gsid": "l6Fc7gAAAAJ:ye4kPcJQO24C",
        "authorship": "joint",
        "previous_key": "c70",
    },
)

add_pub(
    bib,
    "Clegg2022",
    {
        "author": [clegg_b, mcminn_p, fraser_g],
        "title": "Diagnosability, Adequacy & Size: How Test Suites Impact Autograding",
        "venue": hicss,
        "year": 2022,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:eq2jaN3J8jMC",
        "authorship": "joint",
        "previous_key": "c69",
    },
)

add_pub(
    bib,
    "Clegg2021",
    {
        "author": [clegg_b, villauriol_m, mcminn_p, fraser_g],
        "title": "Gradeer: An Open-Source Modular Hybrid Grader",
        "venue": icse_jseet,
        "year": 2021,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:Mojj43d5GZwC",
        "authorship": "joint",
        "previous_key": "c68",
    },
)

add_pub(
    bib,
    "Althomali2021",
    {
        "author": [althomali_i, kapfhammer_g, mcminn_p],
        "title": "Automated Visual Classification of DOM-based Presentation Failure Reports for Responsive Web Pages",
        "venue": stvr,
        "year": 2021,
        "number": "4",
        "volume": "31",
        "doi": "10.1002/stvr.1756",
        "gsid": "ll6Fc7gAAAAJ:XiVPGOgt02cC",
        "authorship": "joint",
        "previous_key": "j24",
    },
)

add_pub(
    bib,
    "Mahajan2021",
    {
        "author": [mahajan_s, alameer_a, mcminn_p, halfond_w],
        "title": "Effective Automated Repair of Internationalization Presentation Failures in Web Applications Using Style Similarity Clustering and Search-Based Techniques",
        "venue": stvr,
        "year": 2021,
        "number": "1--2",  # TODO
        "volume": "31",
        "doi": "10.1002/stvr.1746",
        "gsid": "ll6Fc7gAAAAJ:wbdj-CoPYUoC",
        "authorship": "joint",
        "previous_key": "j22",
    },
)

add_pub(
    bib,
    "Clegg2021a",
    {
        "author": [clegg_b, mcminn_p, fraser_g],
        "title": "An Empirical Study to Determine if Mutants Can Effectively Simulate Students' Programming Mistakes to Increase Tutors' Confidence in Autograding",
        "venue": sigcse,
        "year": 2021,
        "pages": ["1055", "1061"],
        "doi": "10.1145/3408877.3432411",
        "gsid": "ll6Fc7gAAAAJ:AXPGKjj_ei8C",
        "authorship": "joint",
        "previous_key": "c67",
    },
)

add_pub(
    bib,
    "Binkley2020",
    {
        "author": [binkley_d, glenn_j, alsharif_a, mcminn_p],
        "title": "An Investigation Into the Effect of Control and Data Dependence Chain Length on Predicate Testability",
        "venue": scam,
        "year": 2020,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:olpn-zPbct0C",
        "authorship": "joint",
        "previous_key": "c66",
    },
)

add_pub(
    bib,
    "Walsh2020",
    {
        "author": [walsh_t, kapfhammer_g, mcminn_p],
        "title": "Automatically Identifying Potential Regressions in the Layout of Responsive Web Pages",
        "venue": stvr,
        "year": 2020,
        "number": "6",
        "volume": "30",
        "doi": "10.1002/stvr.1748",
        "gsid": "ll6Fc7gAAAAJ:J-pR_7NvFogC",
        "authorship": "joint",
        "previous_key": "j23",
    },
)

add_pub(
    bib,
    "Clegg2020",
    {
        "author": [clegg_b, mcminn_p, fraser_g],
        "title": "The Influence of Test Suite Properties on Automated Grading",
        "venue": cseet,
        "year": 2020,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:t6usbXjVLHcC",
        "authorship": "joint",
        "previous_key": "c65",
    },
)

add_pub(
    bib,
    "Alsharif2020",
    {
        "author": [alsharif_a, kapfhammer_g, mcminn_p],
        "title": "Hybrid Methods for Reducing Database Schema Test Suites: Experimental Insights From Computational and Human Studies",
        "venue": ast_c,
        "year": 2020,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:1qzjygNMrQYC",
        "authorship": "joint",
        "previous_key": "c64",
    },
)

add_pub(
    bib,
    "Parry2020",
    {
        "author": [parry_o, hilton_m, kapfhammer_g, mcminn_p],
        "title": "Flake It 'Till You Make It: Using Automated Repair to Induce and Fix Latent Test Flakiness",
        "venue": apr,
        "year": 2020,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:V3AGJWp-ZtQC",
        "authorship": "joint",
        "previous_key": "c63",
    },
)

add_pub(
    bib,
    "Alsharif2020a",
    {
        "author": [alsharif_a, kapfhammer_g, mcminn_p],
        "title": "STICCER: Fast and Effective Database Test Suite Reduction Through Merging of Similar Test Cases",
        "preserve_case": ["STICCER"],
        "venue": icst,
        "year": 2020,
        "publisher": "IEEE",
        "doi": "10.1109/ICST46399.2020.00031",
        "gsid": "ll6Fc7gAAAAJ:kRWSkSYxWN8C",
        "authorship": "joint",
        "previous_key": "c62",
    },
)

add_pub(
    bib,
    "Alsharif2019",
    {
        "author": [alsharif_a, kapfhammer_g, mcminn_p],
        "title": "What Factors Make SQL Test Cases Understandable for Testers? A Human Study of Automatic Test Data Generation Techniques",
        "preserve_case": ["SQL"],
        "venue": icsme,
        "year": 2019,
        "pages": ["437", "448"],
        "doi": "10.1109/ICSME.2019.00076",
        "gsid": "ll6Fc7gAAAAJ:eJXPG6dFmWUC",
        "authorship": "joint",
        "previous_key": "c61",
    },
)

add_pub(
    bib,
    "Paterson2019",
    {
        "author": [paterson_d, campos_j, abreu_r, kapfhammer_g, fraser_g, mcminn_p],
        "title": "An Empirical Study on the Use of Defect Prediction for Test Case Prioritization",
        "venue": icst,
        "year": 2019,
        "pages": ["346", "357"],
        "doi": "10.1109/ICST.2019.00041",
        "gsid": "ll6Fc7gAAAAJ:8AbLer7MMksC",
        "authorship": "joint",
        "previous_key": "c60",
    },
)

add_pub(
    bib,
    "Althomali2019",
    {
        "author": [althomali_i, kapfhammer_g, mcminn_p],
        "title": "Automatic Visual Verification of Layout Failures in Responsively Designed Web Pages",
        "venue": icst,
        "year": 2019,
        "pages": ["183", "193"],
        "doi": "10.1109/ICST.2019.00027",
        "gsid": "ll6Fc7gAAAAJ:4fKUyHm3Qg0C",
        "authorship": "joint",
        "previous_key": "c59",
        "comment": "Winner of an IEEE Distinguished Paper Award",
    },
)

add_pub(
    bib,
    "Clegg2019",
    {
        "author": [clegg_b, fraser_g, north_s, mcminn_p],
        "title": "Simulating Student Mistakes to Evaluate the Fairness of Automated Grading",
        "venue": icse_seet,
        "year": 2019,
        "pages": ["121", "125"],
        "doi": "10.1109/ICSE-SEET.2019.00021",
        "gsid": "ll6Fc7gAAAAJ:LPZeul_q3PIC",
        "authorship": "joint",
        "previous_key": "c58",
    },
)

add_pub(
    bib,
    "McMinn2019",
    {
        "author": [mcminn_p, wright_c, mccurdy_c, kapfhammer_g],
        "title": "Automatic Detection and Removal of Ineffective Mutants for the Mutation Analysis of Relational Database Schemas",
        "venue": tse,
        "year": 2019,
        "pages": ["427", "463"],
        "number": "5",
        "volume": "45",
        "doi": "10.1109/TSE.2017.2786286",
        "gsid": "ll6Fc7gAAAAJ:dshw04ExmUIC",
        "authorship": "principal",
        "previous_key": "j20",
    },
)

add_pub(
    bib,
    "Almasi2018",
    {
        "author": [almasi_m, hemmati_h, fraser_g, mcminn_p, benefelds_j],
        "title": "Search-Based Detection of Deviation Failures in the Migration of Legacy Spreadsheet Applications",
        "venue": issta,
        "year": 2018,
        "pages": ["266", "275"],
        "publisher": "ACM",
        "doi": "10.1145/3213846.3213861",
        "gsid": "ll6Fc7gAAAAJ:l7t_Zn2s7bgC",
        "authorship": "joint",
        "previous_key": "c57",
    },
)

add_pub(
    bib,
    "Paterson2018",
    {
        "author": [paterson_d, kapfhammer_g, fraser_g, mcminn_p],
        "title": "Using Controlled Numbers of Real Faults and Mutants to Empirically Evaluate Coverage-Based Test Case Prioritization",
        "venue": ast_c,
        "year": 2018,
        "pages": ["57", "63"],
        "publisher": "ACM",
        "doi": "10.1145/3194733.3194735",
        "gsid": "ll6Fc7gAAAAJ:u9iWguZQMMsC",
        "authorship": "joint",
        "previous_key": "c56",
    },
)

add_pub(
    bib,
    "You2018",
    {
        "author": [you_b, kim_j, kwon_m, mcminn_p, yoo_s],
        "title": "Evaluation of CAVM, Austin, and CodeScroll for Test Data Generation for C",
        "preserve_case": ["CAVM", "Austin", "CodeScroll", "C"],
        "venue": kcse,
        "year": 2018,
        "doi": "",
        "gsid": "",
        "authorship": "joint",
        "previous_key": "c55",
    },
)

add_pub(
    bib,
    "Alsharif2018",
    {
        "author": [alsharif_a, kapfhammer_g, mcminn_p],
        "title": "DOMINO: Fast and Effective Test Data Generation for Relational Database Schemas",
        "preserve_case": ["DOMINO"],
        "venue": icst,
        "year": 2018,
        "publisher": "IEEE",
        "doi": "10.1109/ICST.2018.00012",
        "gsid": "ll6Fc7gAAAAJ:OU6Ihb5iCvQC",
        "authorship": "principal",
        "previous_key": "c54",
    },
)

add_pub(
    bib,
    "Mahajan2018",
    {
        "author": [mahajan_s, alameer_a, mcminn_p, halfond_w],
        "title": "Automated Repair of Internationalization Failures Using Style Similarity Clustering and Search-Based Techniques",
        "venue": icst,
        "year": 2018,
        "publisher": "IEEE",
        "doi": "10.1109/ICST.2018.00030",
        "gsid": "ll6Fc7gAAAAJ:uWQEDVKXjbEC",
        "authorship": "joint",
        "previous_key": "c53",
        "comment": "Winner of an IEEE Distinguished Paper Award",
    },
)

add_pub(
    bib,
    "Shamshiri2018",
    {
        "author": [
            shamshiri_s,
            rojas_j,
            gazzola_l,
            fraser_g,
            mcminn_p,
            mariani_l,
            arcuri_a,
        ],
        "title": "Random or Evolutionary Search for Object-Oriented Test Suite Generation?",
        "venue": stvr,
        "year": 2018,
        "number": "4",
        "volume": "28",
        "doi": "10.1002/stvr.1660",
        "gsid": "ll6Fc7gAAAAJ:SP6oXDckpogC",
        "authorship": "joint",
        "sponsor": ["EPSRC-GREATEST"],
        "previous_key": "j21",
    },
)

add_pub(
    bib,
    "Mahajan2018a",
    {
        "author": [mahajan_s, abolhassani_n, mcminn_p, halfond_w],
        "title": "Automated Repair of Mobile Friendly Problems in Web Pages",
        "venue": icse,
        "year": 2018,
        "pages": ["140", "150"],
        "publisher": "ACM",
        "doi": "10.1145/3180155.3180262",
        "gsid": "ll6Fc7gAAAAJ:p2g8aNsByqUC",
        "authorship": "joint",
        "previous_key": "c52",
    },
)

add_pub(
    bib,
    "Hall2018",
    {
        "author": [hall_m, walkinshaw_n, mcminn_p],
        "title": "Effectively Incorporating Expert Knowledge in Automated Software Remodularisation",
        "venue": tse,
        "year": 2018,
        "pages": ["613", "630"],
        "number": "7",
        "volume": "44",
        "doi": "10.1109/TSE.2017.2786222",
        "gsid": "ll6Fc7gAAAAJ:UxriW0iASnsC",
        "authorship": "joint",
        "sponsor": ["EPSRC-REGI"],
        "previous_key": "j19",
    },
)

add_pub(
    bib,
    "Kim2017",
    {
        "author": [kim_j, you_b, kwon_m, mcminn_p, yoo_s],
        "title": "Evaluating CAVM: A New Search-Based Test Data Generation Tool for C",
        "preserve_case": ["CAVM", "C"],
        "venue": ssbse,
        "year": 2017,
        "pages": ["143", "149"],
        "doi": "10.1007/978-3-319-66299-2_12",
        "gsid": "ll6Fc7gAAAAJ:nb7KW1ujOQ8C",
        "authorship": "joint",
        "previous_key": "c51",
    },
)

add_pub(
    bib,
    "Walsh2017",
    {
        "author": [walsh_t, kapfhammer_g, mcminn_p],
        "title": "Automated Layout Failure Detection for Responsive Web Pages Without an Explicit Oracle",
        "venue": issta,
        "year": 2017,
        "pages": ["192", "202"],
        "doi": "10.1145/3092703.3092712",
        "gsid": "ll6Fc7gAAAAJ:1sJd4Hv_s6UC",
        "authorship": "principal",
        "previous_key": "c50",
    },
)

add_pub(
    bib,
    "Walsh2017a",
    {
        "author": [walsh_t, kapfhammer_g, mcminn_p],
        "title": "ReDeCheck: An Automatic Layout Failure Checking Tool for Responsively Designed Web Pages",
        "preserve_case": ["ReDeCheck"],
        "venue": issta,
        "year": 2017,
        "pages": ["360", "363"],
        "doi": "10.1145/3092703.3098221",
        "gsid": "ll6Fc7gAAAAJ:CHSYGLWDkRkC",
        "authorship": "joint",
        "previous_key": "c49",
    },
)

add_pub(
    bib,
    "Mahajan2017",
    {
        "author": [mahajan_s, alameer_a, mcminn_p, halfond_w],
        "title": "Automated Repair of Layout Cross Browser Issues Using Search-Based Techniques",
        "venue": issta,
        "year": 2017,
        "pages": ["249", "260"],
        "doi": "10.1145/3092703.3092726",
        "gsid": "ll6Fc7gAAAAJ:P5F9QuxV20EC",
        "authorship": "joint",
        "previous_key": "c48",
        "comment": "Winner of an ACM SIGSOFT Distinguished Paper Award",
    },
)

add_pub(
    bib,
    "Mahajan2017a",
    {
        "author": [mahajan_s, alameer_a, mcminn_p, halfond_w],
        "title": "XFix: Automated Tool for Repair of Layout Cross Browser Issues",
        "preserve_case": ["XFix"],
        "venue": issta,
        "year": 2017,
        "pages": ["368", "371"],
        "doi": "10.1145/3092703.3098223",
        "gsid": "ll6Fc7gAAAAJ:xtRiw3GOFMkC",
        "authorship": "joint",
        "previous_key": "c47",
    },
)

add_pub(
    bib,
    "Shamshiri2017",
    {
        "author": [shamshiri_s, campos_j, fraser_g, mcminn_p],
        "title": "Disposable Testing: Avoiding Maintenance of Generated Unit Tests by Throwing Them Away",
        "venue": icse,
        "year": 2017,
        "pages": ["207", "209"],
        "doi": "10.1109/ICSE-C.2017.100",
        "gsid": "ll6Fc7gAAAAJ:NhqRSupF_l8C",
        "authorship": "joint",
        "previous_key": "c46",
    },
)

add_pub(
    bib,
    "McMinn2016",
    {
        "author": [mcminn_p, wright_c, kinneer_c, mccurdy_c, camara_m, kapfhammer_g],
        "title": "SchemaAnalyst: Search-Based Test Data Generation for Relational Database Schemas",
        "preserve_case": ["SchemaAnalyst"],
        "venue": icsme,
        "year": 2016,
        "pages": ["586", "590"],
        "doi": "10.1109/ICSME.2016.93",
        "gsid": "ll6Fc7gAAAAJ:_xSYboBqXhAC",
        "authorship": "principal",
        "previous_key": "c45",
    },
)

add_pub(
    bib,
    "McCurdy2016",
    {
        "author": [mccurdy_c, mcminn_p, kapfhammer_g],
        "title": "mrstudyr: Retrospectively Studying the Effectiveness of Mutant Reduction Techniques",
        "preserve_case": ["mrstudyr"],
        "venue": icsme,
        "year": 2016,
        "pages": ["591", "595"],
        "doi": "10.1109/ICSME.2016.92",
        "gsid": "ll6Fc7gAAAAJ:EUQCXRtRnyEC",
        "authorship": "joint",
        "previous_key": "c44",
    },
)

add_pub(
    bib,
    "McMinn2016a",
    {
        "author": [mcminn_p, kapfhammer_g],
        "title": "AVMf: An Open-Source Framework and Implementation of the Alternating Variable Method",
        "preserve_case": ["AVMf"],
        "venue": ssbse,
        "year": 2016,
        "pages": ["259", "266"],
        "publisher": "Springer",
        "series": "Lecture Notes in Computer Science",
        "volume": "9962",
        "doi": "10.1007/978-3-319-47106-8_21",
        "gsid": "ll6Fc7gAAAAJ:f2IySw72cVMC",
        "authorship": "principal",
        "previous_key": "c43",
    },
)

add_pub(
    bib,
    "McMinn2016b",
    {
        "author": [mcminn_p, kapfhammer_g, wright_c],
        "title": "Virtual Mutation Analysis of Relational Database Schemas",
        "venue": ast_w,
        "year": 2016,
        "pages": ["36", "42"],
        "publisher": "ACM",
        "doi": "10.1145/2896921.2896933",
        "gsid": "ll6Fc7gAAAAJ:yD5IFk8b50cC",
        "authorship": "principal",
        "previous_key": "c42",
    },
)

add_pub(
    bib,
    "Kapfhammer2016",
    {
        "author": [kapfhammer_g, wright_c, mcminn_p],
        "title": "Hitchhikers Need Free Vehicles! Shared Repositories for Statistical Analysis in SBST",
        "preserve_case": ["SBST"],
        "venue": sbst,
        "year": 2016,
        "pages": ["55", "56"],
        "publisher": "ACM",
        "doi": "10.1145/2897010.2897017",
        "gsid": "ll6Fc7gAAAAJ:a0OBvERweLwC",
        "authorship": "joint",
        "previous_key": "c41",
    },
)

add_pub(
    bib,
    "McMinn2016c",
    {
        "author": [mcminn_p, harman_m, fraser_g, kapfhammer_g],
        "title": "Automated Search for Good Coverage Criteria: Moving From Code Coverage to Fault Coverage Through Search-Based Software Engineering",
        "venue": sbst,
        "year": 2016,
        "pages": ["43", "44"],
        "publisher": "ACM",
        "doi": "10.1145/2897010.2897013",
        "gsid": "ll6Fc7gAAAAJ:cFHS6HbyZ2cC",
        "authorship": "principal",
        "previous_key": "c40",
    },
)

add_pub(
    bib,
    "McMinn2015",
    {
        "author": [mcminn_p, wright_c, kapfhammer_g],
        "title": "The Effectiveness of Test Coverage Criteria for Relational Database Schema Integrity Constraints",
        "venue": tosem,
        "year": 2015,
        "pages": ["8:1", "8:49"],
        "number": "1",
        "volume": "25",
        "doi": "10.1145/2818639",
        "gsid": "ll6Fc7gAAAAJ:dfsIfKJdRG4C",
        "authorship": "principal",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "j18",
    },
)

add_pub(
    bib,
    "Walsh2015",
    {
        "author": [walsh_t, mcminn_p, kapfhammer_g],
        "title": "Automatic Detection of Potential Layout Faults Following Changes to Responsive Web Pages",
        "venue": ase,
        "year": 2015,
        "pages": ["709", "714"],
        "publisher": "ACM",
        "doi": "10.1109/ASE.2015.3",
        "gsid": "ll6Fc7gAAAAJ:4OULZ7Gr8RgC",
        "authorship": "joint",
        "previous_key": "c39",
    },
)

add_pub(
    bib,
    "Shamshiri2015",
    {
        "author": [shamshiri_s, just_r, rojas_j, fraser_g, mcminn_p, arcuri_a],
        "title": "Do Automatically Generated Unit Tests Find Real Faults? An Empirical Study of Effectiveness and Challenges",
        "venue": ase,
        "year": 2015,
        "pages": ["201", "211"],
        "publisher": "ACM",
        "doi": "10.1109/ASE.2015.86",
        "gsid": "ll6Fc7gAAAAJ:u_35RYKgDlwC",
        "authorship": "joint",
        "previous_key": "c38",
        "comment": "Winner of an ACM SIGSOFT Distinguished Paper Award",
    },
)

add_pub(
    bib,
    "McMinn2015a",
    {
        "author": [mcminn_p, wright_c, kapfhammer_g],
        "title": "An Analysis of the Effectiveness of Different Coverage Criteria for Testing Relational Database Schema Integrity Constraints",
        "venue": shefcs,
        "year": 2015,
        "number": "CS-15-01",
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:SeFeTyx0c_EC",
        "authorship": "principal",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "tr4",
        "jv": "j18",
    },
)

add_pub(
    bib,
    "Kinneer2015",
    {
        "author": [kinneer_c, kapfhammer_g, wright_c, mcminn_p],
        "title": "Automatically Evaluating the Efficiency of Search-Based Test Data Generation for Relational Database Schemas",
        "venue": seke,
        "year": 2015,
        "doi": "10.18293/SEKE2015-205",
        "gsid": "ll6Fc7gAAAAJ:ZHo1McVdvXMC",
        "authorship": "joint",
        "previous_key": "c37",
    },
)

add_pub(
    bib,
    "Kinneer2015a",
    {
        "author": [kinneer_c, kapfhammer_g, wright_c, mcminn_p],
        "title": "EXPOSE: Inferring Worst-Case Time Complexity by Automatic Empirical Study",
        "preserve_case": ["EXPOSE"],
        "venue": seke,
        "year": 2015,
        "doi": "10.18293/SEKE2015-254",
        "gsid": "ll6Fc7gAAAAJ:3s1wT3WcHBgC",
        "authorship": "joint",
        "previous_key": "c36",
    },
)

add_pub(
    bib,
    "Shamshiri2015a",
    {
        "author": [shamshiri_s, rojas_j, fraser_g, mcminn_p],
        "title": "Random or Genetic Algorithm Search for Object-Oriented Test Suite Generation?",
        "venue": gecco,
        "year": 2015,
        "pages": ["1367", "1374"],
        "publisher": "ACM",
        "doi": "10.1145/2739480.2754696",
        "gsid": "ll6Fc7gAAAAJ:zA6iFVUQeVQC",
        "authorship": "joint",
        "previous_key": "c35",
        "comment": "Winner of best paper award for the SBSE-SS track",
    },
)

add_pub(
    bib,
    "Kempka2015",
    {
        "author": [kempka_j, mcminn_p, sudholt_d],
        "title": "Design and Analysis of Different Alternating Variable Searches for Search-Based Software Testing",
        "venue": tcs,
        "year": 2015,
        "pages": ["1", "20"],
        "volume": "605",
        "doi": "10.1016/j.tcs.2014.12.009",
        "gsid": "ll6Fc7gAAAAJ:g5m5HwL7SMYC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "j17",
    },
)

add_pub(
    bib,
    "Barr2015",
    {
        "author": [barr_e, harman_m, mcminn_p, shahbaz_m, yoo_s],
        "title": "The Oracle Problem in Software Testing: A Survey",
        "venue": tse,
        "year": 2015,
        "pages": ["507", "525"],
        "number": "5",
        "volume": "41",
        "doi": "10.1109/TSE.2014.2372785",
        "gsid": "ll6Fc7gAAAAJ:M05iB0D1s5AC",
        "authorship": "joint",
        "previous_key": "j16",
    },
)

add_pub(
    bib,
    "Fraser2015",
    {
        "author": [fraser_g, staats_m, mcminn_p, arcuri_a, padberg_f],
        "title": "Does Automated Unit Test Generation Really Help Software Testers? A Controlled Empirical Study",
        "venue": tosem,
        "year": 2015,
        "editor": [harman_m, pezze_m],
        "number": "4",
        "volume": "24",
        "doi": "10.1145/2699688",
        "gsid": "ll6Fc7gAAAAJ:2P1L_qKh6hAC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "j15",
    },
)

add_pub(
    bib,
    "Fraser2015a",
    {
        "author": [fraser_g, arcuri_a, mcminn_p],
        "title": "A Memetic Algorithm for Whole Test Suite Generation",
        "venue": jss,
        "year": 2015,
        "pages": ["311", "327"],
        "volume": "103",
        "doi": "10.1016/j.jss.2014.05.032",
        "gsid": "ll6Fc7gAAAAJ:35N4QoGY0k4C",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "j14",
    },
)

add_pub(
    bib,
    "Shahbaz2015",
    {
        "author": [shahbaz_m, mcminn_p, stevenson_m],
        "title": "Automatic Generation of Valid and Invalid Test Data for String Validation Routines Using Web Searches and Regular Expressions",
        "venue": scp,
        "year": 2015,
        "pages": ["405", "425"],
        "number": "4",
        "volume": "97",
        "doi": "10.1016/j.scico.2014.04.008",
        "gsid": "ll6Fc7gAAAAJ:vV6vV6tmYwMC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "j13",
    },
)

add_pub(
    bib,
    "Wright2014",
    {
        "author": [wright_c, kapfhammer_g, mcminn_p],
        "title": "The Impact of Equivalent, Redundant and Quasi Mutants on Database Schema Mutation Analysis",
        "venue": qsic,
        "year": 2014,
        "pages": ["57", "66"],
        "publisher": "IEEE Computer Society",
        "doi": "10.1109/QSIC.2014.26",
        "gsid": "ll6Fc7gAAAAJ:70eg2SAEIzsC",
        "authorship": "joint",
        "previous_key": "c34",
    },
)

add_pub(
    bib,
    "Hall2014",
    {
        "author": [hall_m, khojaye_m, walkinshaw_n, mcminn_p],
        "title": "Establishing the Source Code Disruption Caused by Automated Remodularisation Tools",
        "venue": icsme,
        "year": 2014,
        "pages": ["466", "470"],
        "publisher": "IEEE Computer Society",
        "doi": "10.1109/ICSME.2014.75",
        "gsid": "ll6Fc7gAAAAJ:ldfaerwXgEUC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST, EPSRC-REGI"],
        "previous_key": "c33",
    },
)

add_pub(
    bib,
    "Harman2013",
    {
        "author": [harman_m, mcminn_p, shahbaz_m, yoo_s],
        "title": "A Comprehensive Survey of Trends in Oracles for Software Testing",
        "venue": shefcs,
        "year": 2013,
        "number": "CS-13-01",
        "gsid": "ll6Fc7gAAAAJ:lSLTfruPkqcC",
        "authorship": "joint",
        "previous_key": "tr3",
        "jv": "j16",
    },
)

add_pub(
    bib,
    "Fraser2013",
    {
        "author": [fraser_g, staats_m, mcminn_p, arcuri_a, padberg_f],
        "title": "Does Automated White-Box Test Generation Really Help Software Testers?",
        "venue": issta,
        "year": 2013,
        "pages": ["291", "301"],
        "publisher": "ACM",
        "doi": "10.1145/2483760.2483774",
        "gsid": "ll6Fc7gAAAAJ:RGFaLdJalmkC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "c32",
        "jv": "j15",
    },
)

add_pub(
    bib,
    "Kempka2013",
    {
        "author": [kempka_j, mcminn_p, sudholt_d],
        "title": "A Theoretical Runtime and Empirical Analysis of Different Alternating Variable Searches for Search-Based Testing",
        "venue": gecco,
        "year": 2013,
        "pages": ["1445", "1452"],
        "publisher": "ACM",
        "doi": "10.1145/2463372.2463549",
        "gsid": "ll6Fc7gAAAAJ:RYcK_YlVTxYC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "c31",
        "jv": "j17",
    },
)

add_pub(
    bib,
    "Fraser2013a",
    {
        "author": [fraser_g, arcuri_a, mcminn_p],
        "title": "Test Suite Generation With Memetic Algorithms",
        "venue": gecco,
        "year": 2013,
        "pages": ["1437", "1444"],
        "publisher": "ACM",
        "doi": "10.1145/2463372.2463548",
        "gsid": "ll6Fc7gAAAAJ:NaGl4SEjCO4C",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "c30",
        "jv": "j14",
    },
)

add_pub(
    bib,
    "Wright2013",
    {
        "author": [wright_c, mcminn_p, gallardo_j],
        "title": "Towards the Automatic Identification of Faulty Multi-Agent Based Simulation Runs Using MASTER",
        "preserve_case": ["MASTER"],
        "venue": mabs,
        "year": 2013,
        "pages": ["153", "172"],
        "publisher": "Springer",
        "series": "Lecture Notes in Artificial Intelligence",
        "volume": "7838",
        "doi": "10.1007/978-3-642-38859-0_11",
        "gsid": "ll6Fc7gAAAAJ:BqipwSGYUEgC",
        "authorship": "principal",
        "sponsor": ["EPSRC-MISBEHAVIOUR"],
        "previous_key": "c29",
    },
)

add_pub(
    bib,
    "Shamshiri2013",
    {
        "author": [shamshiri_s, fraser_g, mcminn_p, orso_a],
        "title": "Search-Based Propagation of Regression Faults in Automated Regression Testing",
        "venue": regression,
        "year": 2013,
        "pages": ["396", "399"],
        "publisher": "IEEE",
        "doi": "10.1109/ICSTW.2013.51",
        "gsid": "ll6Fc7gAAAAJ:ns9cj8rnVeAC",
        "authorship": "joint",
        "previous_key": "c28",
    },
)

add_pub(
    bib,
    "Anand2013",
    {
        "author": [
            anand_s,
            burke_e,
            chen_t,
            clark_j,
            cohen_m,
            grieskamp_w,
            harman_m,
            harrold_m,
            mcminn_p,
        ],
        "title": "An Orchestrated Survey on Automated Software Test Case Generation",
        "venue": jss,
        "year": 2013,
        "pages": ["1978", "2001"],
        "editor": [bertolino_a, foster_h, li_j, zhu_h],
        "number": "8",
        "volume": "86",
        "doi": "10.1016/j.jss.2013.02.061",
        "gsid": "ll6Fc7gAAAAJ:O3NaXMp0MMsC",
        "authorship": "joint",
        "previous_key": "j12",
    },
)

add_pub(
    bib,
    "Wright2013a",
    {
        "author": [wright_c, kapfhammer_g, mcminn_p],
        "title": "Efficient Mutation Analysis of Relational Database Structure Using Mutant Schemata and Parallelisation",
        "venue": mutation,
        "year": 2013,
        "pages": ["63", "72"],
        "publisher": "IEEE",
        "doi": "10.1109/ICSTW.2013.15",
        "gsid": "ll6Fc7gAAAAJ:GnPB-g6toBAC",
        "authorship": "joint",
        "previous_key": "c27",
    },
)

add_pub(
    bib,
    "Afshan2013",
    {
        "author": [afshan_s, mcminn_p, stevenson_m],
        "title": "Evolving Readable String Test Inputs Using a Natural Language Model to Reduce Human Oracle Cost",
        "venue": icst,
        "year": 2013,
        "pages": ["352", "361"],
        "publisher": "IEEE",
        "doi": "10.1109/ICST.2013.11",
        "gsid": "ll6Fc7gAAAAJ:NMxIlDl6LWMC",
        "authorship": "principal",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "c26",
    },
)

add_pub(
    bib,
    "Kapfhammer2013",
    {
        "author": [kapfhammer_g, mcminn_p, wright_c],
        "title": "Search-Based Testing of Relational Schema Integrity Constraints Across Multiple Database Management Systems",
        "venue": icst,
        "year": 2013,
        "pages": ["31", "40"],
        "publisher": "IEEE",
        "doi": "10.1109/ICST.2013.47",
        "gsid": "ll6Fc7gAAAAJ:YFjsv_pBGBYC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "c25",
    },
)

add_pub(
    bib,
    "McMinn2013",
    {
        "author": [mcminn_p],
        "title": "An Identification of Program Factors That Impact Crossover Performance in Evolutionary Test Input Generation for the Branch Coverage of C Programs",
        "preserve_case": ["C"],
        "venue": ist,
        "year": 2013,
        "pages": ["153", "172"],
        "number": "1",
        "volume": "55",
        "doi": "10.1016/j.infsof.2012.03.010",
        "gsid": "ll6Fc7gAAAAJ:bEWYMUwI8FkC",
        "authorship": "principal",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-RECOST"],
        "previous_key": "j11",
    },
)

add_pub(
    bib,
    "Hall2012",
    {
        "author": [hall_m, walkinshaw_n, mcminn_p],
        "title": "Supervised Software Modularisation",
        "venue": icsm,
        "year": 2012,
        "pages": ["472", "481"],
        "publisher": "IEEE",
        "doi": "10.1109/ICSM.2012.6405309",
        "gsid": "ll6Fc7gAAAAJ:JV2RwH3_ST0C",
        "authorship": "joint",
        "sponsor": ["EPSRC-REGI"],
        "previous_key": "c24",
    },
)

add_pub(
    bib,
    "Holcombe2012",
    {
        "author": [
            holcombe_m,
            adra_s,
            bicak_m,
            chin_s,
            coakley_s,
            graham_a,
            green_j,
            greenough_c,
            jackson_d,
            kiran_m,
            macneil_s,
            malekidizaji_a,
            mcminn_p,
            pogson_m,
            poole_r,
            qwarnstrom_e,
            ratnieks_f,
            rolfe_m,
            smallwood_r,
            sun_t,
            worth_d,
        ],
        "title": "Modelling Complex Biological Systems Using an Agent-Based Approach",
        "venue": ib,
        "year": 2012,
        "pages": ["53", "64"],
        "number": "1",
        "volume": "4",
        "doi": "10.1039/C1IB00042J",
        "gsid": "ll6Fc7gAAAAJ:M3ejUd6NZC8C",
        "authorship": "joint",
        "previous_key": "j10",
    },
)

add_pub(
    bib,
    "McMinn2012",
    {
        "author": [mcminn_p, harman_m, hassoun_y, lakhotia_k, wegener_j],
        "title": "Input Domain Reduction Through Irrelevant Variable Removal and Its Effect on Local, Global and Hybrid Search-Based Structural Test Data Generation",
        "venue": tse,
        "year": 2012,
        "pages": ["453", "477"],
        "number": "2",
        "volume": "38",
        "doi": "10.1109/TSE.2011.18",
        "gsid": "ll6Fc7gAAAAJ:4TOpqqG69KYC",
        "authorship": "principal",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-RECOST, EPSRC-REGI"],
        "previous_key": "j9",
    },
)

add_pub(
    bib,
    "McMinn2012a",
    {
        "author": [mcminn_p, shahbaz_m, stevenson_m],
        "title": "Search-Based Test Input Generation for String Data Types Using the Results of Web Queries",
        "venue": icst,
        "year": 2012,
        "pages": ["141", "150"],
        "publisher": "IEEE",
        "doi": "10.1109/ICST.2012.94",
        "gsid": "ll6Fc7gAAAAJ:qxL8FJ1GzNcC",
        "authorship": "principal",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-RECOST, EPSRC-REGI"],
        "previous_key": "c23",
    },
)

add_pub(
    bib,
    "Shahbaz2012",
    {
        "author": [shahbaz_m, mcminn_p, stevenson_m],
        "title": "Automated Discovery of Valid Test Strings From the Web Using Dynamic Regular Expressions Collation and Natural Language Processing",
        "venue": qsic,
        "year": 2012,
        "pages": ["79", "88"],
        "publisher": "IEEE",
        "doi": "10.1109/QSIC.2012.15",
        "gsid": "ll6Fc7gAAAAJ:hMod-77fHWUC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "c22",
        "jv": "j13",
    },
)

add_pub(
    bib,
    "Adra2011",
    {
        "author": [adra_s, kiran_m, mcminn_p, walkinshaw_n],
        "title": "A Multiobjective Optimisation Approach for Dynamic Inference and Refinement of Agent-Based Model Specifications",
        "venue": cec,
        "year": 2011,
        "pages": ["2237", "2244"],
        "publisher": "IEEE",
        "doi": "10.1109/CEC.2011.5949892",
        "gsid": "ll6Fc7gAAAAJ:7PzlFSSx8tAC",
        "authorship": "joint",
        "sponsor": ["EPSRC-MISBEHAVIOUR"],
        "previous_key": "c21",
    },
)

add_pub(
    bib,
    "Afshan2011",
    {
        "author": [afshan_s, mcminn_p],
        "title": "An Investigation Into Qualitative Human Oracle Costs",
        "venue": ppig,
        "year": 2011,
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:dhFuZR0502QC",
        "authorship": "joint",
        "sponsor": ["EPSRC-RECOST"],
        "previous_key": "c20",
    },
)

add_pub(
    bib,
    "Baars2011",
    {
        "author": [
            baars_a,
            harman_m,
            hassoun_y,
            lakhotia_k,
            mcminn_p,
            tonella_p,
            vos_t,
        ],
        "title": "Symbolic Search-Based Testing",
        "venue": ase,
        "year": 2011,
        "pages": ["53", "62"],
        "publisher": "IEEE",
        "doi": "10.1109/ASE.2011.6100119",
        "gsid": "ll6Fc7gAAAAJ:IWHjjKOFINEC",
        "authorship": "joint",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "c19",
    },
)

add_pub(
    bib,
    "Harman2011",
    {
        "author": [harman_m, mcminn_p, desouza_j, yoo_s],
        "title": "Search-Based Software Engineering: Techniques, Taxonomy, Tutorial",
        "venue": esev,
        "year": 2011,
        "pages": ["1", "59"],
        "editor": [meyer_b, nordio_m],
        "publisher": "Springer",
        "series": "Lecture Notes in Computer Science",
        "volume": "7007",
        "doi": "10.1007/978-3-642-25231-0_1",
        "gsid": "",
        "authorship": "joint",
        "previous_key": "ic2",
    },
)

add_pub(
    bib,
    "McMinn2011",
    {
        "author": [mcminn_p],
        "title": "Search-Based Software Testing: Past, Present and Future",
        "venue": sbst,
        "year": 2011,
        "pages": ["153", "163"],
        "publisher": "IEEE",
        "doi": "10.1109/ICSTW.2011.100",
        "gsid": "ll6Fc7gAAAAJ:aqlVkmm33-oC",
        "authorship": "principal",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "c18",
        "comment": "Keynote paper",
    },
)

add_pub(
    bib,
    "Adra2010",
    {
        "author": [adra_s, mcminn_p],
        "title": "Mutation Operators for Agent-Based Models",
        "venue": mutation,
        "year": 2010,
        "pages": ["151", "156"],
        "publisher": "IEEE",
        "doi": "10.1109/ICSTW.2010.9",
        "gsid": "ll6Fc7gAAAAJ:4DMP91E08xMC",
        "authorship": "joint",
        "sponsor": ["EPSRC-MISBEHAVIOUR"],
        "previous_key": "c17",
    },
)

add_pub(
    bib,
    "Afshan2010",
    {
        "author": [afshan_s, mcminn_p, walkinshaw_n],
        "title": "Using Dictionary Compression Algorithms to Identify Phases in Program Traces",
        "venue": shefcs,
        "year": 2010,
        "number": "CS-10-01",
        "doi": "",
        "gsid": "ll6Fc7gAAAAJ:ULOm3_A8WrAC",
        "authorship": "joint",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "tr2",
    },
)

add_pub(
    bib,
    "Hall2010",
    {
        "author": [hall_m, mcminn_p, walkinshaw_n],
        "title": "Superstate Identification for State Machines Using Search-Based Clustering",
        "venue": gecco,
        "year": 2010,
        "pages": ["1381", "1388"],
        "publisher": "ACM",
        "doi": "10.1145/1830483.1830736",
        "gsid": "ll6Fc7gAAAAJ:KlAtU1dfN6UC",
        "authorship": "joint",
        "sponsor": ["EPSRC-REGI"],
        "previous_key": "c16",
    },
)

add_pub(
    bib,
    "Harman2010",
    {
        "author": [harman_m, mcminn_p],
        "title": "A Theoretical and Empirical Study of Search Based Testing: Local, Global and Hybrid Search",
        "venue": tse,
        "year": 2010,
        "pages": ["226", "247"],
        "number": "2",
        "volume": "36",
        "doi": "10.1109/TSE.2009.71",
        "gsid": "ll6Fc7gAAAAJ:UeHWp8X0CEIC",
        "authorship": "principal",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "j8",
    },
)

add_pub(
    bib,
    "Harman2010a",
    {
        "author": [harman_m, kim_s, lakhotia_k, mcminn_p, yoo_s],
        "title": "Optimizing for the Number of Tests Generated in Search Based Test Data Generation With an Application to the Oracle Cost Problem",
        "venue": sbst,
        "year": 2010,
        "pages": ["182", "191"],
        "publisher": "IEEE",
        "doi": "10.1109/ICSTW.2010.31",
        "gsid": "ll6Fc7gAAAAJ:roLk4NBRz8UC",
        "authorship": "joint",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "c15",
    },
)

add_pub(
    bib,
    "Lakhotia2010",
    {
        "author": [lakhotia_k, mcminn_p, harman_m],
        "title": "An Empirical Investigation Into Branch Coverage for C Programs Using CUTE and AUSTIN",
        "preserve_case": ["C", "CUTE", "AUSTIN"],
        "venue": jss,
        "year": 2010,
        "pages": ["2379", "2391"],
        "number": "12",
        "volume": "83",
        "doi": "10.1016/j.jss.2010.07.026",
        "gsid": "ll6Fc7gAAAAJ:0EnyYjriUFMC",
        "authorship": "joint",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "j7",
    },
)

add_pub(
    bib,
    "McMinn2010",
    {
        "author": [mcminn_p],
        "title": "How Does Program Structure Impact the Effectiveness of the Crossover Operator in Evolutionary Testing?",
        "venue": ssbse,
        "year": 2010,
        "pages": ["9", "18"],
        "publisher": "IEEE",
        "doi": "10.1109/SSBSE.2010.11",
        "gsid": "ll6Fc7gAAAAJ:_kc_bZDykSQC",
        "authorship": "principal",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "c14",
        "jv": "j11",
        "comment": "Winner of SSBSE 2010 best paper award",
    },
)

add_pub(
    bib,
    "McMinn2010a",
    {
        "author": [mcminn_p, stevenson_m, harman_m],
        "title": "Reducing Qualitative Human Oracle Costs Associated With Automatically Generated Test Data",
        "venue": stov,
        "year": 2010,
        "pages": ["1", "4"],
        "publisher": "ACM",
        "doi": "10.1145/1868048.1868049",
        "gsid": "ll6Fc7gAAAAJ:MXK_kJrjxJIC",
        "authorship": "principal",
        "previous_key": "c13",
    },
)

add_pub(
    bib,
    "Walkinshaw2010",
    {
        "author": [walkinshaw_n, afshan_s, mcminn_p],
        "title": "Using Compression Algorithms to Support the Comprehension of Program Traces",
        "venue": woda,
        "year": 2010,
        "pages": ["8", "13"],
        "publisher": "ACM",
        "doi": "10.1145/1868321.1868323",
        "gsid": "ll6Fc7gAAAAJ:UebtZRa9Y70C",
        "authorship": "joint",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "c12",
    },
)

add_pub(
    bib,
    "Lakhotia2009",
    {
        "author": [lakhotia_k, mcminn_p, harman_m],
        "title": "Automated Test Data Generation for Coverage: Haven't We Solved This Problem Yet?",
        "venue": taicpart,
        "year": 2009,
        "pages": ["95", "104"],
        "publisher": "IEEE",
        "doi": "10.1109/TAICPART.2009.15",
        "gsid": "ll6Fc7gAAAAJ:ufrVoPGSRksC",
        "authorship": "joint",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "c11",
    },
)

add_pub(
    bib,
    "McMinn2009",
    {
        "author": [mcminn_p, binkley_d, harman_m],
        "title": "Empirical Evaluation of a Nesting Testability Transformation for Evolutionary Testing",
        "venue": tosem,
        "year": 2009,
        "pages": ["11:1", "11:27"],
        "number": "3",
        "volume": "18",
        "doi": "10.1145/1525880.1525884",
        "gsid": "ll6Fc7gAAAAJ:YsMSGLbcyi4C",
        "authorship": "principal",
        "previous_key": "j6",
    },
)

add_pub(
    bib,
    "McMinn2009a",
    {
        "author": [mcminn_p],
        "title": "Search-Based Failure Discovery Using Testability Transformations to Generate Pseudo-Oracles",
        "venue": gecco,
        "year": 2009,
        "pages": ["1689", "1696"],
        "publisher": "ACM Press",
        "doi": "10.1145/1569901.1570127",
        "gsid": "ll6Fc7gAAAAJ:hqOjcs7Dif8C",
        "authorship": "principal",
        "sponsor": ["EPSRC-MISBEHAVIOUR, EPSRC-REGI"],
        "previous_key": "c10",
    },
)

add_pub(
    bib,
    "Harman2008",
    {
        "author": [
            harman_m,
            baresel_a,
            binkley_d,
            hierons_r,
            hu_l,
            korel_b,
            mcminn_p,
            roper_m,
        ],
        "title": "Testability Transformation — Program Transformation to Improve Testability",
        "venue": fmt,
        "year": 2008,
        "pages": ["320", "344"],
        "editor": [hierons_r, bowen_j, harman_m],
        "publisher": "Springer",
        "series": "Lecture Notes in Computer Science",
        "volume": "4949",
        "doi": "10.1007/978-3-540-78917-8_11",
        "gsid": "",
        "authorship": "joint",
        "previous_key": "ic1",
    },
)

add_pub(
    bib,
    "Kiran2008",
    {
        "author": [kiran_m, coakley_s, walkinshaw_n, mcminn_p, holcombe_m],
        "title": "Validation and Discovery From Computational Biology Models",
        "venue": bs,
        "year": 2008,
        "pages": ["141", "150"],
        "number": "1--2",  # TODO
        "volume": "93",
        "doi": "10.1016/j.biosystems.2008.03.010",
        "gsid": "ll6Fc7gAAAAJ:5nxA0vEk-isC",
        "authorship": "joint",
        "previous_key": "j5",
    },
)

add_pub(
    bib,
    "Lakhotia2008",
    {
        "author": [lakhotia_k, harman_m, mcminn_p],
        "title": "Handling Dynamic Data Structures in Search-Based Testing",
        "venue": gecco,
        "year": 2008,
        "pages": ["1759", "1766"],
        "publisher": "ACM",
        "doi": "10.1145/1389095.1389435",
        "gsid": "",
        "authorship": "joint",
        "previous_key": "c9",
    },
)

add_pub(
    bib,
    "Sun2008",
    {
        "author": [sun_t, mcminn_p, holcombe_m, smallwood_r, macneil_s],
        "title": "Agent Based Modelling Helps in Understanding the Rules by Which Fibroblasts Support Keratinocyte Colony Formation",
        "venue": plosone,
        "year": 2008,
        "number": "5",
        "volume": "3",
        "doi": "10.1371/journal.pone.0002129",
        "gsid": "",
        "authorship": "joint",
        "previous_key": "j4",
    },
)

add_pub(
    bib,
    "Harman2007",
    {
        "author": [harman_m, hassoun_y, lakhotia_k, mcminn_p, wegener_j],
        "title": "The Impact of Input Domain Reduction on Search-Based Test Data Generation",
        "venue": esecfse,
        "year": 2007,
        "pages": ["155", "164"],
        "publisher": "ACM",
        "doi": "10.1145/1287624.1287647",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "c8",
        "jv": "j9",
    },
)

add_pub(
    bib,
    "Harman2007a",
    {
        "author": [harman_m, mcminn_p],
        "title": "A Theoretical and Empirical Analysis of Evolutionary Testing and Hill Climbing for Structural Test Data Generation",
        "venue": issta,
        "year": 2007,
        "pages": ["73", "83"],
        "publisher": "ACM",
        "doi": "10.1145/1273463.1273475",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "c7",
        "jv": "j8",
    },
)

add_pub(
    bib,
    "Harman2007b",
    {
        "author": [harman_m, lakhotia_k, mcminn_p],
        "title": "A Multi-Objective Approach to Search-Based Test Data Generation",
        "venue": gecco,
        "year": 2007,
        "pages": ["1098", "1105"],
        "publisher": "ACM",
        "doi": "10.1145/1276958.1277175",
        "gsid": "",
        "authorship": "joint",
        "previous_key": "c6",
    },
)

add_pub(
    bib,
    "McMinn2007",
    {
        "author": [mcminn_p],
        "title": "IGUANA: Input Generation Using Automated Novel Algorithms. A Plug and Play Research Tool",
        "preserve_case": ["IGUANA: Input Generation Using Automated Novel Algorithms"],
        "venue": shefcs,
        "year": 2007,
        "number": "CS-07-14",
        "doi": "",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "tr1",
    },
)

add_pub(
    bib,
    "Sun2007",
    {
        "author": [sun_t, mcminn_p, coakley_s, holcombe_m, smallwood_r, macneil_s],
        "title": "An Integrated Systems Biology Approach to Understanding the Rules of Keratinocyte Colony Formation",
        "venue": jrsi,
        "year": 2007,
        "pages": ["1077", "1092"],
        "number": "17",
        "volume": "4",
        "doi": "10.1098/rsif.2007.0227",
        "gsid": "",
        "authorship": "joint",
        "previous_key": "j3",
    },
)

add_pub(
    bib,
    "McMinn2006",
    {
        "author": [mcminn_p, holcombe_m],
        "title": "Evolutionary Testing Using an Extended Chaining Approach",
        "venue": ec,
        "year": 2006,
        "pages": ["41", "64"],
        "number": "1",
        "volume": "14",
        "doi": "10.1162/evco.2006.14.1.41",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "j2",
    },
)

add_pub(
    bib,
    "McMinn2006a",
    {
        "author": [mcminn_p, harman_m, binkley_d, tonella_p],
        "title": "The Species Per Path Approach to Search-Based Software Test Data Generation",
        "venue": issta,
        "year": 2006,
        "pages": ["13", "24"],
        "publisher": "ACM",
        "doi": "10.1145/1146238.1146241",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "c5",
    },
)

add_pub(
    bib,
    "McMinn2005",
    {
        "author": [mcminn_p, binkley_d, harman_m],
        "title": "Testability Transformation for Efficient Automated Test Data Search in the Presence of Nesting",
        "venue": uktest,
        "year": 2005,
        "pages": ["165", "182"],
        "doi": "",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "c4",
        "jv": "j6",
    },
)

add_pub(
    bib,
    "McMinn2005a",
    {
        "author": [mcminn_p, holcombe_m],
        "title": "Evolutionary Testing of State-Based Programs",
        "venue": gecco,
        "year": 2005,
        "pages": ["1013", "1020"],
        "publisher": "ACM",
        "doi": "10.1145/1068009.1068182",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "c3",
    },
)

add_pub(
    bib,
    "McMinn2005b",
    {
        "author": [mcminn_p],
        "title": "Evolutionary Search for Test Data in the Presence of State Behaviour",
        "venue": shef,
        "year": 2005,
        "doi": "",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "t1",
    },
)

add_pub(
    bib,
    "McMinn2004",
    {
        "author": [mcminn_p],
        "title": "Search-Based Software Test Data Generation: A Survey",
        "venue": stvr,
        "year": 2004,
        "pages": ["105", "156"],
        "number": "2",
        "volume": "14",
        "doi": "10.1002/stvr.294",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "j1",
    },
)

add_pub(
    bib,
    "McMinn2004a",
    {
        "author": [mcminn_p, holcombe_m],
        "title": "Hybridizing Evolutionary Testing With the Chaining Approach",
        "venue": gecco,
        "year": 2004,
        "pages": ["1363", "1374"],
        "publisher": "Springer",
        "series": "Lecture Notes in Computer Science",
        "volume": "3103",
        "doi": "10.1007/978-3-540-24855-2_157",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "c2",
        "jv": "j2",
        "comment": "Winner of best paper award for the SBSE track",
    },
)

add_pub(
    bib,
    "McMinn2003",
    {
        "author": [mcminn_p, holcombe_m],
        "title": "The State Problem for Evolutionary Testing",
        "venue": gecco,
        "year": 2003,
        "pages": ["2488", "2498"],
        "publisher": "Springer",
        "series": "Lecture Notes in Computer Science",
        "volume": "2724",
        "doi": "10.1007/3-540-45110-2_152",
        "gsid": "",
        "authorship": "principal",
        "previous_key": "c1",
    },
)
