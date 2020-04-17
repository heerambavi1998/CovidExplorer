
ES_PORT = 9210
#place all pdf_json files above pmc_json files since entity csv is constructed with preference to pdf sha over pmc id
DATAPATHS = ["data/comm_use_subset/comm_use_subset/pdf_json/*.json",
            "data/noncomm_use_subset/noncomm_use_subset/pdf_json/*.json",
            "data/biorxiv_medrxiv/biorxiv_medrxiv/pdf_json/*.json",
            "data/custom_license/custom_license/pdf_json/*.json",
            "data/custom_license/custom_license/pmc_json/*.json",            
            "data/noncomm_use_subset/noncomm_use_subset/pmc_json/*.json",
            "data/comm_use_subset/comm_use_subset/pmc_json/*.json",
            ]
METADATAPATH = "data/metadata.csv"
NERDATAPATH = "prge_from_abs_comb.csv"
CHEDDATAPATH = "ched_from_abs_comb.csv"
DASHURL = '/graphs/'