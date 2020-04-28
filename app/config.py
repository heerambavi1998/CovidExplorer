
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
READMEPATH = "data/metadata.readme"
NERDATAPATH = "prge_from_abs_comb.csv"
CHEDDATAPATH = "ched_from_abs_comb.csv"
DASHURL = '/graphs/'
ENT_TYPES = ['ner_ched', 'ner_dna', 'ner_rna', 'ner_protein', 'ner_cell_type', 'ner_cell_line']
COLOR_MAP = {'ner_ched':'#F7BE81', 
                'ner_dna':'#819FF7', 
                'ner_rna':'#81F781',
                'ner_protein':'#F7819F', 
                'ner_cell_line':'#16a085', 
                'ner_cell_type':'#81DAF5'}