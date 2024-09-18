context = """
{
  "data": {
    "formfields": {
      "deal": {
        "locations": {
          "label": "Locations",
          "class": "JSONSchemaFormField",
          "required": false
        },
        "country": {
          "label": "Target country",
          "class": "CountryForeignKey",
          "required": false,
          "related_model": "Country"
        },
        "intended_size": {
          "label": "Intended size (in ha)",
          "class": "DecimalField",
          "required": false,
          "unit": "ha"
        },
        "contract_size": {
          "label": "Size under contract (leased or purchased area, in ha)",
          "class": "JSONDateAreaField",
          "required": false
        },
        "production_size": {
          "label": "Size in operation (production, in ha)",
          "class": "JSONDateAreaField",
          "required": false
        },
        "land_area_comment": {
          "label": "Comment on land area",
          "class": "TextField",
          "required": false
        },
        "intention_of_investment": {
          "label": "Intention of investment",
          "class": "JSONDateAreaChoicesField",
          "required": false,
          "choices": [
            {
              "value": "BIOFUELS",
              "label": "Biomass for biofuels",
              "group": "Agriculture"
            },
            {
              "value": "BIOMASS_ENERGY_GENERATION",
              "label": "Biomass for energy generation (agriculture)",
              "group": "Agriculture"
            },
            {
              "value": "FODDER",
              "label": "Fodder",
              "group": "Agriculture"
            },
            {
              "value": "FOOD_CROPS",
              "label": "Food crops",
              "group": "Agriculture"
            },
            {
              "value": "LIVESTOCK",
              "label": "Livestock",
              "group": "Agriculture"
            },
            {
              "value": "NON_FOOD_AGRICULTURE",
              "label": "Non-food agricultural commodities",
              "group": "Agriculture"
            },
            {
              "value": "AGRICULTURE_UNSPECIFIED",
              "label": "Agriculture unspecified",
              "group": "Agriculture"
            },
            {
              "value": "BIOMASS_ENERGY_PRODUCTION",
              "label": "Biomass for energy generation (forestry)",
              "group": "Forestry"
            },
            {
              "value": "CARBON",
              "label": "For carbon sequestration/REDD",
              "group": "Forestry"
            },
            {
              "value": "FOREST_LOGGING",
              "label": "Forest logging / management for wood and fiber",
              "group": "Forestry"
            },
            {
              "value": "TIMBER_PLANTATION",
              "label": "Timber plantation for wood and fiber",
              "group": "Forestry"
            },
            {
              "value": "FORESTRY_UNSPECIFIED",
              "label": "Forestry unspecified",
              "group": "Forestry"
            },
            {
              "value": "SOLAR_PARK",
              "label": "Solar park",
              "group": "Renewable energy power plants"
            },
            {
              "value": "WIND_FARM",
              "label": "Wind farm",
              "group": "Renewable energy power plants"
            },
            {
              "value": "RENEWABLE_ENERGY",
              "label": "Renewable energy unspecified",
              "group": "Renewable energy power plants"
            },
            {
              "value": "CONVERSATION",
              "label": "Conservation",
              "group": "Other"
            },
            {
              "value": "INDUSTRY",
              "label": "Industry",
              "group": "Other"
            },
            {
              "value": "LAND_SPECULATION",
              "label": "Land speculation",
              "group": "Other"
            },
            {
              "value": "MINING",
              "label": "Mining",
              "group": "Other"
            },
            {
              "value": "OIL_GAS_EXTRACTION",
              "label": "Oil / Gas extraction",
              "group": "Other"
            },
            {
              "value": "TOURISM",
              "label": "Tourism",
              "group": "Other"
            },
            {
              "value": "OTHER",
              "label": "Other",
              "group": "Other"
            }
          ]
        },
        "intention_of_investment_comment": {
          "label": "Comment on intention of investment",
          "class": "TextField",
          "required": false
        },
        "carbon_offset_project": {
          "label": "Carbon offset project",
          "class": "NullBooleanField",
          "required": false
        },
        "carbon_offset_project_comment": {
          "label": "Carbon offset project comment",
          "class": "TextField",
          "required": false
        },
        "nature_of_deal": {
          "label": "Nature of the deal",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "OUTRIGHT_PURCHASE",
              "label": "Outright purchase"
            },
            {
              "value": "LEASE",
              "label": "Lease"
            },
            {
              "value": "CONCESSION",
              "label": "Concession"
            },
            {
              "value": "EXPLOITATION_PERMIT",
              "label": "Exploitation permit / license / concession (for mineral resources)"
            },
            {
              "value": "PURE_CONTRACT_FARMING",
              "label": "Pure contract farming"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        "nature_of_deal_comment": {
          "label": "Comment on nature of the deal",
          "class": "TextField",
          "required": false
        },
        "negotiation_status": {
          "label": "Negotiation status",
          "class": "JSONDateChoiceField",
          "required": false,
          "choices": [
            {
              "value": "EXPRESSION_OF_INTEREST",
              "label": "Intended (Expression of interest)"
            },
            {
              "value": "UNDER_NEGOTIATION",
              "label": "Intended (Under negotiation)"
            },
            {
              "value": "MEMORANDUM_OF_UNDERSTANDING",
              "label": "Intended (Memorandum of understanding)"
            },
            {
              "value": "ORAL_AGREEMENT",
              "label": "Concluded (Oral Agreement)"
            },
            {
              "value": "CONTRACT_SIGNED",
              "label": "Concluded (Contract signed)"
            },
            {
              "value": "CHANGE_OF_OWNERSHIP",
              "label": "Concluded (Change of ownership)"
            },
            {
              "value": "NEGOTIATIONS_FAILED",
              "label": "Failed (Negotiations failed)"
            },
            {
              "value": "CONTRACT_CANCELED",
              "label": "Failed (Contract cancelled)"
            },
            {
              "value": "CONTRACT_EXPIRED",
              "label": "Contract expired"
            }
          ]
        },
        "negotiation_status_comment": {
          "label": "Comment on negotiation status",
          "class": "TextField",
          "required": false
        },
        "implementation_status": {
          "label": "Implementation status",
          "class": "JSONDateChoiceField",
          "required": false,
          "choices": [
            {
              "value": "PROJECT_NOT_STARTED",
              "label": "Project not started"
            },
            {
              "value": "STARTUP_PHASE",
              "label": "Startup phase (no production)"
            },
            {
              "value": "IN_OPERATION",
              "label": "In operation (production)"
            },
            {
              "value": "PROJECT_ABANDONED",
              "label": "Project abandoned"
            }
          ]
        },
        "implementation_status_comment": {
          "label": "Comment on implementation status",
          "class": "TextField",
          "required": false
        },
        "purchase_price": {
          "label": "Purchase price",
          "class": "DecimalField",
          "required": false
        },
        "purchase_price_currency": {
          "label": "Purchase price currency",
          "class": "CurrencyForeignKey",
          "required": false,
          "related_model": "Currency"
        },
        "purchase_price_type": {
          "label": "Purchase price area type",
          "class": "TypedChoiceField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "PER_HA",
              "label": "per ha"
            },
            {
              "value": "PER_AREA",
              "label": "for specified area"
            }
          ]
        },
        "purchase_price_area": {
          "label": "Purchase price area",
          "class": "DecimalField",
          "required": false
        },
        "purchase_price_comment": {
          "label": "Comment on purchase price",
          "class": "TextField",
          "required": false
        },
        "annual_leasing_fee": {
          "label": "Annual leasing fee",
          "class": "DecimalField",
          "required": false
        },
        "annual_leasing_fee_currency": {
          "label": "Annual leasing fee currency",
          "class": "CurrencyForeignKey",
          "required": false,
          "related_model": "Currency"
        },
        "annual_leasing_fee_type": {
          "label": "Annual leasing fee area type",
          "class": "TypedChoiceField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "PER_HA",
              "label": "per ha"
            },
            {
              "value": "PER_AREA",
              "label": "for specified area"
            }
          ]
        },
        "annual_leasing_fee_area": {
          "label": "Annual leasing fee area",
          "class": "DecimalField",
          "required": false
        },
        "contract_farming": {
          "label": "Contract farming",
          "class": "NullBooleanField",
          "required": false
        },
        "on_the_lease_state": {
          "label": "On leased / purchased",
          "class": "NullBooleanField",
          "required": false
        },
        "on_the_lease": {
          "label": "On leased area/farmers/households",
          "class": "JSONLeaseField",
          "required": false
        },
        "off_the_lease_state": {
          "label": "Not on leased / purchased (out-grower)",
          "class": "NullBooleanField",
          "required": false
        },
        "off_the_lease": {
          "label": "Not on leased area/farmers/households (out-grower)",
          "class": "JSONLeaseField",
          "required": false
        },
       
        "contracts": {
          "label": "Contracts",
          "class": "JSONSchemaFormField",
          "required": false
        },
        "total_jobs_created": {
          "label": "Jobs created (total)",
          "class": "NullBooleanField",
          "required": false
        },
        "total_jobs_planned": {
          "label": "Planned number of jobs (total)",
          "class": "IntegerField",
          "required": false,
          "unit": "jobs"
        },
        "total_jobs_planned_employees": {
          "label": "Planned employees (total)",
          "class": "IntegerField",
          "required": false,
          "unit": "employees"
        },
        "total_jobs_planned_daily_workers": {
          "label": "Planned daily/seasonal workers (total)",
          "class": "IntegerField",
          "required": false,
          "unit": "workers"
        },
        "total_jobs_current": {
          "label": "Current total number of jobs/employees/ daily/seasonal workers",
          "class": "JSONJobsField",
          "required": false
        },
       
        "foreign_jobs_created": {
          "label": "Jobs created (foreign)",
          "class": "NullBooleanField",
          "required": false
        },
        "foreign_jobs_planned": {
          "label": "Planned number of jobs (foreign)",
          "class": "IntegerField",
          "required": false,
          "unit": "jobs"
        },
        "foreign_jobs_planned_employees": {
          "label": "Planned employees (foreign)",
          "class": "IntegerField",
          "required": false,
          "unit": "employees"
        },
        "foreign_jobs_planned_daily_workers": {
          "label": "Planned daily/seasonal workers (foreign)",
          "class": "IntegerField",
          "required": false,
          "unit": "workers"
        },
        "foreign_jobs_current": {
          "label": "Current foreign number of jobs/employees/ daily/seasonal workers",
          "class": "JSONJobsField",
          "required": false
        },
        
        "domestic_jobs_created": {
          "label": "Jobs created (domestic)",
          "class": "NullBooleanField",
          "required": false
        },
        "domestic_jobs_planned": {
          "label": "Planned number of jobs (domestic)",
          "class": "IntegerField",
          "required": false,
          "unit": "jobs"
        },
        "domestic_jobs_planned_employees": {
          "label": "Planned employees (domestic)",
          "class": "IntegerField",
          "required": false,
          "unit": "employees"
        },
        "domestic_jobs_planned_daily_workers": {
          "label": "Planned daily/seasonal workers (domestic)",
          "class": "IntegerField",
          "required": false,
          "unit": "workers"
        },
        "domestic_jobs_current": {
          "label": "Current domestic number of jobs/employees/ daily/seasonal workers",
          "class": "JSONJobsField",
          "required": false
        },
        
        "operating_company": {
          "label": "Operating company",
          "class": "InvestorForeignKey",
          "required": false,
          "related_model": "Investor"
        },
        "involved_actors": {
          "label": "Actors involved in the negotiation / admission process",
          "class": "JSONActorsField",
          "required": false,
          "choices": [
            {
              "value": "GOVERNMENT_OR_STATE_INSTITUTIONS",
              "label": "Government / state institutions (government, ministries, departments, agencies etc.)"
            },
            {
              "value": "TRADITIONAL_LAND_OWNERS_OR_COMMUNITIES",
              "label": "Traditional land-owners / communities"
            },
            {
              "value": "TRADITIONAL_LOCAL_AUTHORITY",
              "label": "Traditional local authority (e.g. Chiefdom council / Chiefs)"
            },
            {
              "value": "BROKER",
              "label": "Broker"
            },
            {
              "value": "INTERMEDIARY",
              "label": "Intermediary"
            },
            {
              "value": "OTHER",
              "label": "Other (please specify)"
            }
          ]
        },
        "project_name": {
          "label": "Name of investment project",
          "class": "CharField",
          "required": false
        },
        "investment_chain_comment": {
          "label": "Comment on investment chain",
          "class": "TextField",
          "required": false
        },
        "datasources": {
          "label": "Data sources",
          "class": "JSONSchemaFormField",
          "required": false
        },
        "name_of_community": {
          "label": "Name of community",
          "class": "SimpleArrayField",
          "required": false
        },
        "name_of_indigenous_people": {
          "label": "Name of indigenous people",
          "class": "SimpleArrayField",
          "required": false
        },
        "people_affected_comment": {
          "label": "Comment on communities / indigenous peoples affected",
          "class": "TextField",
          "required": false
        },
        "recognition_status": {
          "label": "Recognition status of community land tenure",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "INDIGENOUS_RIGHTS_RECOGNIZED",
              "label": "Indigenous Peoples traditional or customary rights recognized by government"
            },
            {
              "value": "INDIGENOUS_RIGHTS_NOT_RECOGNIZED",
              "label": "Indigenous Peoples traditional or customary rights not recognized by government"
            },
            {
              "value": "COMMUNITY_RIGHTS_RECOGNIZED",
              "label": "Community traditional or customary rights recognized by government"
            },
            {
              "value": "COMMUNITY_RIGHTS_NOT_RECOGNIZED",
              "label": "Community traditional or customary rights not recognized by government"
            }
          ]
        },
        "recognition_status_comment": {
          "label": "Comment on recognition status of community land tenure",
          "class": "TextField",
          "required": false
        },
        "community_consultation": {
          "label": "Community consultation",
          "class": "TypedChoiceField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "NOT_CONSULTED",
              "label": "Not consulted"
            },
            {
              "value": "LIMITED_CONSULTATION",
              "label": "Limited consultation"
            },
            {
              "value": "FPIC",
              "label": "Free, Prior and Informed Consent (FPIC)"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        "community_consultation_comment": {
          "label": "Comment on consultation of local community",
          "class": "TextField",
          "required": false
        },
        "community_reaction": {
          "label": "Community reaction",
          "class": "TypedChoiceField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "CONSENT",
              "label": "Consent"
            },
            {
              "value": "MIXED_REACTION",
              "label": "Mixed reaction"
            },
            {
              "value": "REJECTION",
              "label": "Rejection"
            }
          ]
        },
        "community_reaction_comment": {
          "label": "Comment on community reaction",
          "class": "TextField",
          "required": false
        },
        "land_conflicts": {
          "label": "Presence of land conflicts",
          "class": "NullBooleanField",
          "required": false
        },
        "land_conflicts_comment": {
          "label": "Comment on presence of land conflicts",
          "class": "TextField",
          "required": false
        },
        "displacement_of_people": {
          "label": "Displacement of people",
          "class": "NullBooleanField",
          "required": false
        },
        "displaced_people": {
          "label": "Number of people actually displaced",
          "class": "IntegerField",
          "required": false
        },
        "displaced_households": {
          "label": "Number of households actually displaced",
          "class": "IntegerField",
          "required": false
        },
        "displaced_people_from_community_land": {
          "label": "Number of people displaced out of their community land",
          "class": "IntegerField",
          "required": false
        },
        "displaced_people_within_community_land": {
          "label": "Number of people displaced staying on community land",
          "class": "IntegerField",
          "required": false
        },
        "displaced_households_from_fields": {
          "label": "Number of households displaced",
          "class": "IntegerField",
          "required": false
        },
        "displaced_people_on_completion": {
          "label": "Number of people facing displacement once project is fully implemented",
          "class": "IntegerField",
          "required": false
        },
        
        "negative_impacts": {
          "label": "Negative impacts for local communities",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "ENVIRONMENTAL_DEGRADATION",
              "label": "Environmental degradation"
            },
            {
              "value": "SOCIO_ECONOMIC",
              "label": "Socio-economic"
            },
            {
              "value": "CULTURAL_LOSS",
              "label": "Cultural loss"
            },
            {
              "value": "EVICTION",
              "label": "Eviction"
            },
            {
              "value": "DISPLACEMENT",
              "label": "Displacement"
            },
            {
              "value": "VIOLENCE",
              "label": "Violence"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
       
        "promised_compensation": {
          "label": "Promised compensation (e.g. for damages or resettlements)",
          "class": "TextField",
          "required": false
        },
        "received_compensation": {
          "label": "Received compensation (e.g. for damages or resettlements)",
          "class": "TextField",
          "required": false
        },
        "promised_benefits": {
          "label": "Promised benefits for local communities",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "HEALTH",
              "label": "Health"
            },
            {
              "value": "EDUCATION",
              "label": "Education"
            },
            {
              "value": "PRODUCTIVE_INFRASTRUCTURE",
              "label": "Productive infrastructure (e.g. irrigation, tractors, machinery...)"
            },
            {
              "value": "ROADS",
              "label": "Roads"
            },
            {
              "value": "CAPACITY_BUILDING",
              "label": "Capacity building"
            },
            {
              "value": "FINANCIAL_SUPPORT",
              "label": "Financial support"
            },
            {
              "value": "COMMUNITY_SHARES",
              "label": "Community shares in the investment project"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        
        "materialized_benefits": {
          "label": "Materialized benefits for local communities",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "HEALTH",
              "label": "Health"
            },
            {
              "value": "EDUCATION",
              "label": "Education"
            },
            {
              "value": "PRODUCTIVE_INFRASTRUCTURE",
              "label": "Productive infrastructure (e.g. irrigation, tractors, machinery...)"
            },
            {
              "value": "ROADS",
              "label": "Roads"
            },
            {
              "value": "CAPACITY_BUILDING",
              "label": "Capacity building"
            },
            {
              "value": "FINANCIAL_SUPPORT",
              "label": "Financial support"
            },
            {
              "value": "COMMUNITY_SHARES",
              "label": "Community shares in the investment project"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        
        "presence_of_organizations": {
          "label": "Presence of organizations and actions taken (e.g. farmer organizations, NGOs, etc.)",
          "class": "TextField",
          "required": false
        },
        "former_land_owner": {
          "label": "Former land owner",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "STATE",
              "label": "State"
            },
            {
              "value": "PRIVATE_SMALLHOLDERS",
              "label": "Private (smallholders)"
            },
            {
              "value": "PRIVATE_LARGE_SCALE",
              "label": "Private (large-scale farm)"
            },
            {
              "value": "COMMUNITY",
              "label": "Community"
            },
            {
              "value": "INDIGENOUS_PEOPLE",
              "label": "Indigenous people"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        
        "former_land_use": {
          "label": "Former land use",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "COMMERCIAL_AGRICULTURE",
              "label": "Commercial (large-scale) agriculture"
            },
            {
              "value": "SMALLHOLDER_AGRICULTURE",
              "label": "Smallholder agriculture"
            },
            {
              "value": "SHIFTING_CULTIVATION",
              "label": "Shifting cultivation"
            },
            {
              "value": "PASTORALISM",
              "label": "Pastoralism"
            },
            {
              "value": "HUNTING_GATHERING",
              "label": "Hunting/Gathering"
            },
            {
              "value": "FORESTRY",
              "label": "Forestry"
            },
            {
              "value": "CONSERVATION",
              "label": "Conservation"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        
        "former_land_cover": {
          "label": "Former land cover",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "CROPLAND",
              "label": "Cropland"
            },
            {
              "value": "FOREST_LAND",
              "label": "Forest land"
            },
            {
              "value": "PASTURE",
              "label": "Pasture"
            },
            {
              "value": "RANGELAND",
              "label": "Shrub land/Grassland (Rangeland)"
            },
            {
              "value": "MARGINAL_LAND",
              "label": "Marginal land"
            },
            {
              "value": "WETLAND",
              "label": "Wetland"
            },
            {
              "value": "OTHER_LAND",
              "label": "Other land (e.g. developed land – specify in comment field)"
            }
          ]
        },
        "crops": {
          "label": "Crops area/yield/export",
          "class": "JSONExportsField",
          "required": false,
          "choices": [
            {
              "value": "ACC",
              "label": "Accacia"
            },
            {
              "value": "ALF",
              "label": "Alfalfa"
            },
            {
              "value": "ALG",
              "label": "Seaweed / Macroalgae(unspecified)"
            },
            {
              "value": "ALM",
              "label": "Almond"
            },
            {
              "value": "ALV",
              "label": "Aloe Vera"
            },
            {
              "value": "APL",
              "label": "Apple"
            },
            {
              "value": "AQU",
              "label": "Aquaculture (unspecified crops)"
            },
            {
              "value": "BAM",
              "label": "Bamboo"
            },
            {
              "value": "BAN",
              "label": "Banana"
            },
            {
              "value": "BEA",
              "label": "Bean"
            },
            {
              "value": "BOT",
              "label": "Bottle Gourd"
            },
            {
              "value": "BRL",
              "label": "Barley"
            },
            {
              "value": "BWT",
              "label": "Buckwheat"
            },
            {
              "value": "CAC",
              "label": "Cacao"
            },
            {
              "value": "CAS",
              "label": "Cassava (Maniok)"
            },
            {
              "value": "CAW",
              "label": "Cashew"
            },
            {
              "value": "CHA",
              "label": "Chat"
            },
            {
              "value": "CHE",
              "label": "Cherries"
            },
            {
              "value": "CNL",
              "label": "Canola"
            },
            {
              "value": "COC",
              "label": "Coconut"
            },
            {
              "value": "COF",
              "label": "Coffee Plant"
            },
            {
              "value": "COT",
              "label": "Cotton"
            },
            {
              "value": "CRL",
              "label": "Cereals (unspecified)"
            },
            {
              "value": "CRN",
              "label": "Corn (Maize)"
            },
            {
              "value": "CRO",
              "label": "Croton"
            },
            {
              "value": "CST",
              "label": "Castor Oil Plant"
            },
            {
              "value": "CTR",
              "label": "Citrus Fruits (unspecified)"
            },
            {
              "value": "DIL",
              "label": "Dill"
            },
            {
              "value": "EUC",
              "label": "Eucalyptus"
            },
            {
              "value": "FLW",
              "label": "Flowers (unspecified)"
            },
            {
              "value": "FNT",
              "label": "Fig-Nut"
            },
            {
              "value": "FOD",
              "label": "Fodder Plants (unspecified)"
            },
            {
              "value": "FOO",
              "label": "Food crops (unspecified)"
            },
            {
              "value": "FRT",
              "label": "Fruit (unspecified)"
            },
            {
              "value": "GRA",
              "label": "Grapes"
            },
            {
              "value": "GRN",
              "label": "Grains (unspecified)"
            },
            {
              "value": "HRB",
              "label": "Herbs (unspecified)"
            },
            {
              "value": "JTR",
              "label": "Jatropha"
            },
            {
              "value": "LNT",
              "label": "Lentils"
            },
            {
              "value": "MAN",
              "label": "Mango"
            },
            {
              "value": "MUS",
              "label": "Mustard"
            },
            {
              "value": "OAT",
              "label": "Oats"
            },
            {
              "value": "OIL",
              "label": "Oil Seeds (unspecified)"
            },
            {
              "value": "OLE",
              "label": "Oleagionous plant"
            },
            {
              "value": "OLV",
              "label": "Olives"
            },
            {
              "value": "ONI",
              "label": "Onion"
            },
            {
              "value": "OPL",
              "label": "Oil Palm"
            },
            {
              "value": "OTH",
              "label": "Other crops (please specify)"
            },
            {
              "value": "PAL",
              "label": "Palms"
            },
            {
              "value": "PAP",
              "label": "Papaya"
            },
            {
              "value": "PAS",
              "label": "Passion fruit"
            },
            {
              "value": "PEA",
              "label": "Peanut (groundnut)"
            },
            {
              "value": "PEP",
              "label": "Pepper"
            },
            {
              "value": "PES",
              "label": "Peas"
            },
            {
              "value": "PIE",
              "label": "Pine"
            },
            {
              "value": "PIN",
              "label": "Pineapple"
            },
            {
              "value": "PLS",
              "label": "Pulses (unspecified)"
            },
            {
              "value": "POM",
              "label": "Pomegranate"
            },
            {
              "value": "PON",
              "label": "Pongamia Pinnata"
            },
            {
              "value": "PTT",
              "label": "Potatoes"
            },
            {
              "value": "RAP",
              "label": "Rapeseed"
            },
            {
              "value": "RCH",
              "label": "Rice (hybrid)"
            },
            {
              "value": "RIC",
              "label": "Rice"
            },
            {
              "value": "ROS",
              "label": "Roses"
            },
            {
              "value": "RUB",
              "label": "Rubber tree"
            },
            {
              "value": "RYE",
              "label": "Rye"
            },
            {
              "value": "SEE",
              "label": "Seeds Production (unspecified)"
            },
            {
              "value": "SES",
              "label": "Sesame"
            },
            {
              "value": "SOR",
              "label": "Sorghum"
            },
            {
              "value": "SOY",
              "label": "Soya Beans"
            },
            {
              "value": "SPI",
              "label": "Spices (unspecified)"
            },
            {
              "value": "SSL",
              "label": "Sisal"
            },
            {
              "value": "SUB",
              "label": "Sugar beet"
            },
            {
              "value": "SUC",
              "label": "Sugar Cane"
            },
            {
              "value": "SUG",
              "label": "Sugar (unspecified)"
            },
            {
              "value": "SUN",
              "label": "Sun Flower"
            },
            {
              "value": "SWP",
              "label": "Sweet Potatoes"
            },
            {
              "value": "TBC",
              "label": "Tobacco"
            },
            {
              "value": "TEA",
              "label": "Tea"
            },
            {
              "value": "TEF",
              "label": "Teff"
            },
            {
              "value": "TEK",
              "label": "Teak"
            },
            {
              "value": "TOM",
              "label": "Tomatoes"
            },
            {
              "value": "TRE",
              "label": "Trees (unspecified)"
            },
            {
              "value": "VGT",
              "label": "Vegetables (unspecified)"
            },
            {
              "value": "VIN",
              "label": "Vineyard"
            },
            {
              "value": "WHT",
              "label": "Wheat"
            },
            {
              "value": "YAM",
              "label": "Yam"
            }
          ]
        },
        "animals": {
          "label": "Livestock area/yield/export",
          "class": "JSONExportsField",
          "required": false,
          "choices": [
            {
              "value": "AQU",
              "label": "Aquaculture (animals)"
            },
            {
              "value": "BEE",
              "label": "Beef Cattle"
            },
            {
              "value": "CTL",
              "label": "Cattle"
            },
            {
              "value": "DCT",
              "label": "Dairy Cattle"
            },
            {
              "value": "FSH",
              "label": "Fish"
            },
            {
              "value": "GOT",
              "label": "Goats"
            },
            {
              "value": "OTH",
              "label": "Other livestock (please specify)"
            },
            {
              "value": "PIG",
              "label": "Pork"
            },
            {
              "value": "POU",
              "label": "Poultry"
            },
            {
              "value": "SHP",
              "label": "Sheep"
            },
            {
              "value": "SHR",
              "label": "Shrimp"
            }
          ]
        },
        "mineral_resources": {
          "label": "Mineral resources area/yield/export",
          "class": "JSONExportsField",
          "required": false,
          "choices": [
            {
              "value": "ALU",
              "label": "Aluminum"
            },
            {
              "value": "ASP",
              "label": "Asphaltite"
            },
            {
              "value": "ATC",
              "label": "Anthracite"
            },
            {
              "value": "BAR",
              "label": "Barite"
            },
            {
              "value": "BAS",
              "label": "Basalt"
            },
            {
              "value": "BAX",
              "label": "Bauxite"
            },
            {
              "value": "BEN",
              "label": "Bentonite"
            },
            {
              "value": "BUM",
              "label": "Building materials"
            },
            {
              "value": "CAR",
              "label": "Carbon"
            },
            {
              "value": "CHR",
              "label": "Chromite"
            },
            {
              "value": "CLA",
              "label": "Clay"
            },
            {
              "value": "COA",
              "label": "Coal"
            },
            {
              "value": "COB",
              "label": "Cobalt"
            },
            {
              "value": "COP",
              "label": "Copper"
            },
            {
              "value": "DIA",
              "label": "Diamonds"
            },
            {
              "value": "EME",
              "label": "Emerald"
            },
            {
              "value": "FLD",
              "label": "Feldspar"
            },
            {
              "value": "FLO",
              "label": "Fluoride"
            },
            {
              "value": "GAS",
              "label": "Gas"
            },
            {
              "value": "GLD",
              "label": "Gold"
            },
            {
              "value": "GRT",
              "label": "Granite"
            },
            {
              "value": "GRV",
              "label": "Gravel"
            },
            {
              "value": "HEA",
              "label": "Heavy Mineral Sands"
            },
            {
              "value": "ILM",
              "label": "Ilmenite"
            },
            {
              "value": "IRO",
              "label": "Iron"
            },
            {
              "value": "JAD",
              "label": "Jade"
            },
            {
              "value": "LED",
              "label": "Lead"
            },
            {
              "value": "LIM",
              "label": "Limestone"
            },
            {
              "value": "LIT",
              "label": "Lithium"
            },
            {
              "value": "MAG",
              "label": "Magnetite"
            },
            {
              "value": "MBD",
              "label": "Molybdenum"
            },
            {
              "value": "MGN",
              "label": "Manganese"
            },
            {
              "value": "MRB",
              "label": "Marble"
            },
            {
              "value": "NIK",
              "label": "Nickel"
            },
            {
              "value": "OTH",
              "label": "Other minerals (please specify)"
            },
            {
              "value": "PET",
              "label": "Petroleum"
            },
            {
              "value": "PHP",
              "label": "Phosphorous"
            },
            {
              "value": "PLT",
              "label": "Platinum"
            },
            {
              "value": "PUM",
              "label": "Hydrocarbons (e.g. crude oil)"
            },
            {
              "value": "PYR",
              "label": "Pyrolisis Plant"
            },
            {
              "value": "RUT",
              "label": "Rutile"
            },
            {
              "value": "SAN",
              "label": "Sand"
            },
            {
              "value": "SIC",
              "label": "Silica"
            },
            {
              "value": "SIL",
              "label": "Silver"
            },
            {
              "value": "SLT",
              "label": "Salt"
            },
            {
              "value": "STO",
              "label": "Stone"
            },
            {
              "value": "TIN",
              "label": "Tin"
            },
            {
              "value": "TTM",
              "label": "Titanium"
            },
            {
              "value": "URM",
              "label": "Uranium"
            },
            {
              "value": "ZNC",
              "label": "Zinc"
            }
          ]
        },
        "mineral_resources_comment": {
          "label": "Comment on mineral resources",
          "class": "TextField",
          "required": false
        },
        "contract_farming_crops": {
          "label": "Contract farming crops",
          "class": "JSONDateAreaChoicesField",
          "required": false,
          "help_text": "ha",
          "choices": [
            {
              "value": "ACC",
              "label": "Accacia"
            },
            {
              "value": "ALF",
              "label": "Alfalfa"
            },
            {
              "value": "ALG",
              "label": "Seaweed / Macroalgae(unspecified)"
            },
            {
              "value": "ALM",
              "label": "Almond"
            },
            {
              "value": "ALV",
              "label": "Aloe Vera"
            },
            {
              "value": "APL",
              "label": "Apple"
            },
            {
              "value": "AQU",
              "label": "Aquaculture (unspecified crops)"
            },
            {
              "value": "BAM",
              "label": "Bamboo"
            },
            {
              "value": "BAN",
              "label": "Banana"
            },
            {
              "value": "BEA",
              "label": "Bean"
            },
            {
              "value": "BOT",
              "label": "Bottle Gourd"
            },
            {
              "value": "BRL",
              "label": "Barley"
            },
            {
              "value": "BWT",
              "label": "Buckwheat"
            },
            {
              "value": "CAC",
              "label": "Cacao"
            },
            {
              "value": "CAS",
              "label": "Cassava (Maniok)"
            },
            {
              "value": "CAW",
              "label": "Cashew"
            },
            {
              "value": "CHA",
              "label": "Chat"
            },
            {
              "value": "CHE",
              "label": "Cherries"
            },
            {
              "value": "CNL",
              "label": "Canola"
            },
            {
              "value": "COC",
              "label": "Coconut"
            },
            {
              "value": "COF",
              "label": "Coffee Plant"
            },
            {
              "value": "COT",
              "label": "Cotton"
            },
            {
              "value": "CRL",
              "label": "Cereals (unspecified)"
            },
            {
              "value": "CRN",
              "label": "Corn (Maize)"
            },
            {
              "value": "CRO",
              "label": "Croton"
            },
            {
              "value": "CST",
              "label": "Castor Oil Plant"
            },
            {
              "value": "CTR",
              "label": "Citrus Fruits (unspecified)"
            },
            {
              "value": "DIL",
              "label": "Dill"
            },
            {
              "value": "EUC",
              "label": "Eucalyptus"
            },
            {
              "value": "FLW",
              "label": "Flowers (unspecified)"
            },
            {
              "value": "FNT",
              "label": "Fig-Nut"
            },
            {
              "value": "FOD",
              "label": "Fodder Plants (unspecified)"
            },
            {
              "value": "FOO",
              "label": "Food crops (unspecified)"
            },
            {
              "value": "FRT",
              "label": "Fruit (unspecified)"
            },
            {
              "value": "GRA",
              "label": "Grapes"
            },
            {
              "value": "GRN",
              "label": "Grains (unspecified)"
            },
            {
              "value": "HRB",
              "label": "Herbs (unspecified)"
            },
            {
              "value": "JTR",
              "label": "Jatropha"
            },
            {
              "value": "LNT",
              "label": "Lentils"
            },
            {
              "value": "MAN",
              "label": "Mango"
            },
            {
              "value": "MUS",
              "label": "Mustard"
            },
            {
              "value": "OAT",
              "label": "Oats"
            },
            {
              "value": "OIL",
              "label": "Oil Seeds (unspecified)"
            },
            {
              "value": "OLE",
              "label": "Oleagionous plant"
            },
            {
              "value": "OLV",
              "label": "Olives"
            },
            {
              "value": "ONI",
              "label": "Onion"
            },
            {
              "value": "OPL",
              "label": "Oil Palm"
            },
            {
              "value": "OTH",
              "label": "Other crops (please specify)"
            },
            {
              "value": "PAL",
              "label": "Palms"
            },
            {
              "value": "PAP",
              "label": "Papaya"
            },
            {
              "value": "PAS",
              "label": "Passion fruit"
            },
            {
              "value": "PEA",
              "label": "Peanut (groundnut)"
            },
            {
              "value": "PEP",
              "label": "Pepper"
            },
            {
              "value": "PES",
              "label": "Peas"
            },
            {
              "value": "PIE",
              "label": "Pine"
            },
            {
              "value": "PIN",
              "label": "Pineapple"
            },
            {
              "value": "PLS",
              "label": "Pulses (unspecified)"
            },
            {
              "value": "POM",
              "label": "Pomegranate"
            },
            {
              "value": "PON",
              "label": "Pongamia Pinnata"
            },
            {
              "value": "PTT",
              "label": "Potatoes"
            },
            {
              "value": "RAP",
              "label": "Rapeseed"
            },
            {
              "value": "RCH",
              "label": "Rice (hybrid)"
            },
            {
              "value": "RIC",
              "label": "Rice"
            },
            {
              "value": "ROS",
              "label": "Roses"
            },
            {
              "value": "RUB",
              "label": "Rubber tree"
            },
            {
              "value": "RYE",
              "label": "Rye"
            },
            {
              "value": "SEE",
              "label": "Seeds Production (unspecified)"
            },
            {
              "value": "SES",
              "label": "Sesame"
            },
            {
              "value": "SOR",
              "label": "Sorghum"
            },
            {
              "value": "SOY",
              "label": "Soya Beans"
            },
            {
              "value": "SPI",
              "label": "Spices (unspecified)"
            },
            {
              "value": "SSL",
              "label": "Sisal"
            },
            {
              "value": "SUB",
              "label": "Sugar beet"
            },
            {
              "value": "SUC",
              "label": "Sugar Cane"
            },
            {
              "value": "SUG",
              "label": "Sugar (unspecified)"
            },
            {
              "value": "SUN",
              "label": "Sun Flower"
            },
            {
              "value": "SWP",
              "label": "Sweet Potatoes"
            },
            {
              "value": "TBC",
              "label": "Tobacco"
            },
            {
              "value": "TEA",
              "label": "Tea"
            },
            {
              "value": "TEF",
              "label": "Teff"
            },
            {
              "value": "TEK",
              "label": "Teak"
            },
            {
              "value": "TOM",
              "label": "Tomatoes"
            },
            {
              "value": "TRE",
              "label": "Trees (unspecified)"
            },
            {
              "value": "VGT",
              "label": "Vegetables (unspecified)"
            },
            {
              "value": "VIN",
              "label": "Vineyard"
            },
            {
              "value": "WHT",
              "label": "Wheat"
            },
            {
              "value": "YAM",
              "label": "Yam"
            }
          ]
        },
        "contract_farming_crops_comment": {
          "label": "Comment on contract farming crops",
          "class": "TextField",
          "required": false
        },
        "contract_farming_animals": {
          "label": "Contract farming livestock",
          "class": "JSONDateAreaChoicesField",
          "required": false,
          "help_text": "ha",
          "choices": [
            {
              "value": "AQU",
              "label": "Aquaculture (animals)"
            },
            {
              "value": "BEE",
              "label": "Beef Cattle"
            },
            {
              "value": "CTL",
              "label": "Cattle"
            },
            {
              "value": "DCT",
              "label": "Dairy Cattle"
            },
            {
              "value": "FSH",
              "label": "Fish"
            },
            {
              "value": "GOT",
              "label": "Goats"
            },
            {
              "value": "OTH",
              "label": "Other livestock (please specify)"
            },
            {
              "value": "PIG",
              "label": "Pork"
            },
            {
              "value": "POU",
              "label": "Poultry"
            },
            {
              "value": "SHP",
              "label": "Sheep"
            },
            {
              "value": "SHR",
              "label": "Shrimp"
            }
          ]
        },
       
        "electricity_generation": {
          "label": "Electricity generation",
          "class": "JSONElectricityGenerationField",
          "required": false,
          "choices": [
            {
              "value": "WIND",
              "label": "On-shore wind turbines"
            },
            {
              "value": "PHOTOVOLTAIC",
              "label": "Solar (Photovoltaic)"
            },
            {
              "value": "SOLAR_HEAT",
              "label": "Solar (Thermal system)"
            }
          ]
        },
       
        "carbon_sequestration": {
          "label": "Carbon sequestration/offsetting",
          "class": "JSONCarbonSequestrationField",
          "required": false,
          "choices": [
            {
              "value": "REFORESTATION",
              "label": "Reforestation & afforestation"
            },
            {
              "value": "AVOIDED_FOREST_CONVERSION",
              "label": "Avoided forest conversion"
            },
            {
              "value": "AVOIDED_GRASSLAND_CONVERSION",
              "label": "Avoided grassland conversion"
            },
            {
              "value": "PEATLAND_RESTORATION",
              "label": "Peatland restoration"
            },
            {
              "value": "IMPROVED_FOREST_MANAGEMENT",
              "label": "Improved forest management"
            },
            {
              "value": "SUSTAINABLE_AGRICULTURE",
              "label": "Sustainable agriculture"
            },
            {
              "value": "SUSTAINABLE_GRASSLAND_MANAGEMENT",
              "label": "Sustainable grassland management"
            },
            {
              "value": "RICE_EMISSION_REDUCTIONS",
              "label": "Rice emission reductions"
            },
            {
              "value": "SOLAR_PARK",
              "label": "Solar park"
            },
            {
              "value": "WIND_FARM",
              "label": "Wind farm"
            },
            {
              "value": "OTHER",
              "label": "Other (please specify in a comment)"
            }
          ]
        },
        
        "has_domestic_use": {
          "label": "Has domestic use",
          "class": "NullBooleanField",
          "required": false
        },
        "domestic_use": {
          "label": "Domestic use",
          "class": "FloatField",
          "required": false,
          "unit": "%",
          "min_value": 0,
          "max_value": 100
        },
        "has_export": {
          "label": "Has export",
          "class": "NullBooleanField",
          "required": false
        },
        "export": {
          "label": "Export",
          "class": "FloatField",
          "required": false,
          "unit": "%",
          "min_value": 0,
          "max_value": 100
        },
        "export_country1": {
          "label": "Country 1",
          "class": "CountryForeignKey",
          "required": false,
          "related_model": "Country"
        },
        "export_country1_ratio": {
          "label": "Country 1 ratio",
          "class": "FloatField",
          "required": false,
          "unit": "%",
          "min_value": 0,
          "max_value": 100
        },
        "export_country2": {
          "label": "Country 2",
          "class": "CountryForeignKey",
          "required": false,
          "related_model": "Country"
        },
        "export_country2_ratio": {
          "label": "Country 2 ratio",
          "class": "FloatField",
          "required": false,
          "unit": "%",
          "min_value": 0,
          "max_value": 100
        },
        "export_country3": {
          "label": "Country 3",
          "class": "CountryForeignKey",
          "required": false,
          "related_model": "Country"
        },
        "export_country3_ratio": {
          "label": "Country 3 ratio",
          "class": "FloatField",
          "required": false,
          "unit": "%",
          "min_value": 0,
          "max_value": 100
        },
        "use_of_produce_comment": {
          "label": "Comment on use of produce",
          "class": "TextField",
          "required": false
        },
        "in_country_processing": {
          "label": "In country processing of produce",
          "class": "NullBooleanField",
          "required": false
        },
        "in_country_processing_comment": {
          "label": "Comment on in country processing of produce",
          "class": "TextField",
          "required": false
        },
        "in_country_processing_facilities": {
          "label": "Processing facilities / production infrastructure of the project (e.g. oil mill, ethanol distillery, biomass power plant etc.)",
          "class": "TextField",
          "required": false
        },
        "in_country_end_products": {
          "label": "In-country end products of the project",
          "class": "TextField",
          "required": false
        },
        "water_extraction_envisaged": {
          "label": "Water extraction envisaged",
          "class": "NullBooleanField",
          "required": false
        },
        "water_extraction_envisaged_comment": {
          "label": "Comment on water extraction envisaged",
          "class": "TextField",
          "required": false
        },
        "source_of_water_extraction": {
          "label": "Source of water extraction",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "GROUNDWATER",
              "label": "Groundwater"
            },
            {
              "value": "SURFACE_WATER",
              "label": "Surface water"
            },
            {
              "value": "RIVER",
              "label": "River"
            },
            {
              "value": "LAKE",
              "label": "Lake"
            }
          ]
        },
        
        "water_extraction_amount": {
          "label": "Water extraction amount",
          "class": "IntegerField",
          "required": false,
          "unit": "m3/year"
        },
       
        "use_of_irrigation_infrastructure": {
          "label": "Use of irrigation infrastructure",
          "class": "NullBooleanField",
          "required": false
        },
       
        "water_footprint": {
          "label": "Water footprint of the investment project",
          "class": "TextField",
          "required": false
        },
        "gender_related_information": {
          "label": "Comment on gender-related info",
          "class": "TextField",
          "required": false
        },
       
        "fully_updated": {
          "label": "Fully updated",
          "class": "BooleanField",
          "required": false
        },
        "confidential": {
          "label": "Confidential",
          "class": "BooleanField",
          "required": false
        },
       
        "current_contract_size": {
          "label": "Current contract size",
          "class": "DecimalField",
          "required": false,
          "unit": "ha"
        },
        "current_production_size": {
          "label": "Current production size",
          "class": "DecimalField",
          "required": false
        },
        "current_intention_of_investment": {
          "label": "Current intention of investment",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "BIOFUELS",
              "label": "Biomass for biofuels"
            },
            {
              "value": "BIOMASS_ENERGY_GENERATION",
              "label": "Biomass for energy generation (agriculture)"
            },
            {
              "value": "FODDER",
              "label": "Fodder"
            },
            {
              "value": "FOOD_CROPS",
              "label": "Food crops"
            },
            {
              "value": "LIVESTOCK",
              "label": "Livestock"
            },
            {
              "value": "NON_FOOD_AGRICULTURE",
              "label": "Non-food agricultural commodities"
            },
            {
              "value": "AGRICULTURE_UNSPECIFIED",
              "label": "Agriculture unspecified"
            },
            {
              "value": "BIOMASS_ENERGY_PRODUCTION",
              "label": "Biomass for energy generation (forestry)"
            },
            {
              "value": "CARBON",
              "label": "For carbon sequestration/REDD"
            },
            {
              "value": "FOREST_LOGGING",
              "label": "Forest logging / management for wood and fiber"
            },
            {
              "value": "TIMBER_PLANTATION",
              "label": "Timber plantation for wood and fiber"
            },
            {
              "value": "FORESTRY_UNSPECIFIED",
              "label": "Forestry unspecified"
            },
            {
              "value": "SOLAR_PARK",
              "label": "Solar park"
            },
            {
              "value": "WIND_FARM",
              "label": "Wind farm"
            },
            {
              "value": "RENEWABLE_ENERGY",
              "label": "Renewable energy unspecified"
            },
            {
              "value": "CONVERSATION",
              "label": "Conservation"
            },
            {
              "value": "INDUSTRY",
              "label": "Industry"
            },
            {
              "value": "LAND_SPECULATION",
              "label": "Land speculation"
            },
            {
              "value": "MINING",
              "label": "Mining"
            },
            {
              "value": "OIL_GAS_EXTRACTION",
              "label": "Oil / Gas extraction"
            },
            {
              "value": "TOURISM",
              "label": "Tourism"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        "current_negotiation_status": {
          "label": "Current negotiation status",
          "class": "TypedChoiceField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "EXPRESSION_OF_INTEREST",
              "label": "Intended (Expression of interest)"
            },
            {
              "value": "UNDER_NEGOTIATION",
              "label": "Intended (Under negotiation)"
            },
            {
              "value": "MEMORANDUM_OF_UNDERSTANDING",
              "label": "Intended (Memorandum of understanding)"
            },
            {
              "value": "ORAL_AGREEMENT",
              "label": "Concluded (Oral Agreement)"
            },
            {
              "value": "CONTRACT_SIGNED",
              "label": "Concluded (Contract signed)"
            },
            {
              "value": "CHANGE_OF_OWNERSHIP",
              "label": "Concluded (Change of ownership)"
            },
            {
              "value": "NEGOTIATIONS_FAILED",
              "label": "Failed (Negotiations failed)"
            },
            {
              "value": "CONTRACT_CANCELED",
              "label": "Failed (Contract cancelled)"
            },
            {
              "value": "CONTRACT_EXPIRED",
              "label": "Contract expired"
            }
          ]
        },
        "current_implementation_status": {
          "label": "Current implementation status",
          "class": "TypedChoiceField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "PROJECT_NOT_STARTED",
              "label": "Project not started"
            },
            {
              "value": "STARTUP_PHASE",
              "label": "Startup phase (no production)"
            },
            {
              "value": "IN_OPERATION",
              "label": "In operation (production)"
            },
            {
              "value": "PROJECT_ABANDONED",
              "label": "Project abandoned"
            }
          ]
        },
        "current_crops": {
          "label": "Current crops",
          "class": "SimpleArrayField",
          "required": false
        },
        "current_animals": {
          "label": "Current animals",
          "class": "SimpleArrayField",
          "required": false
        },
        "current_mineral_resources": {
          "label": "Current mineral resources",
          "class": "SimpleArrayField",
          "required": false
        },
        "current_electricity_generation": {
          "label": "Current electricity generation",
          "class": "SimpleArrayField",
          "required": false
        },
        "current_carbon_sequestration": {
          "label": "Current carbon sequestration",
          "class": "SimpleArrayField",
          "required": false
        },
        "deal_size": {
          "label": "Deal size",
          "class": "DecimalField",
          "required": false,
          "unit": "ha"
        },
        "created_at": {
          "label": "Created",
          "class": "DateTimeField",
          "required": false
        },
        "created_by": {
          "label": "Created by",
          "class": "ModelChoiceField",
          "required": false,
          "related_model": "User"
        },
        "modified_at": {
          "label": "Last update",
          "class": "DateTimeField",
          "required": false
        },
        "modified_by": {
          "label": "Modified by",
          "class": "ModelChoiceField",
          "required": false,
          "related_model": "User"
        },
        "fully_updated_at": {
          "label": "Last full update",
          "class": "DateTimeField",
          "required": false
        },
        "id": {
          "label": "ID",
          "class": "AutoField"
        },
        "workflowinfos": {
          "class": "WorkflowInfosField",
          "label": "Comments / History"
        },
        "combined_status": {
          "class": "StatusField"
        }
      }
    }
  }
}
"""



context_REST_RAG = """

That is the countries and their ids, so if you want to know the id of each countrie, use this, and don't use an other source :
{
  "data": {
    "countries": [
      {
        "id": 4,
        "name": "Afghanistan"
      },
      {
        "id": 8,
        "name": "Albania"
      },
      {
        "id": 12,
        "name": "Algeria"
      },
      {
        "id": 16,
        "name": "American Samoa"
      },
      {
        "id": 20,
        "name": "Andorra"
      },
      {
        "id": 24,
        "name": "Angola"
      },
      {
        "id": 28,
        "name": "Antigua and Barbuda"
      },
      {
        "id": 31,
        "name": "Azerbaijan"
      },
      {
        "id": 32,
        "name": "Argentina"
      },
      {
        "id": 36,
        "name": "Australia"
      },
      {
        "id": 40,
        "name": "Austria"
      },
      {
        "id": 44,
        "name": "Bahamas"
      },
      {
        "id": 48,
        "name": "Bahrain"
      },
      {
        "id": 50,
        "name": "Bangladesh"
      },
      {
        "id": 51,
        "name": "Armenia"
      },
      {
        "id": 52,
        "name": "Barbados"
      },
      {
        "id": 56,
        "name": "Belgium"
      },
      {
        "id": 60,
        "name": "Bermuda"
      },
      {
        "id": 64,
        "name": "Bhutan"
      },
      {
        "id": 68,
        "name": "Bolivia"
      },
      {
        "id": 70,
        "name": "Bosnia and Herzegovina"
      },
      {
        "id": 72,
        "name": "Botswana"
      },
      {
        "id": 76,
        "name": "Brazil"
      },
      {
        "id": 84,
        "name": "Belize"
      },
      {
        "id": 90,
        "name": "Solomon Islands"
      },
      {
        "id": 92,
        "name": "British Virgin Islands"
      },
      {
        "id": 96,
        "name": "Brunei Darussalam"
      },
      {
        "id": 100,
        "name": "Bulgaria"
      },
      {
        "id": 104,
        "name": "Myanmar"
      },
      {
        "id": 108,
        "name": "Burundi"
      },
      {
        "id": 112,
        "name": "Belarus"
      },
      {
        "id": 116,
        "name": "Cambodia"
      },
      {
        "id": 120,
        "name": "Cameroon"
      },
      {
        "id": 124,
        "name": "Canada"
      },
      {
        "id": 132,
        "name": "Cape Verde"
      },
      {
        "id": 136,
        "name": "Cayman Islands"
      },
      {
        "id": 140,
        "name": "Central African Republic"
      },
      {
        "id": 144,
        "name": "Sri Lanka"
      },
      {
        "id": 148,
        "name": "Chad"
      },
      {
        "id": 152,
        "name": "Chile"
      },
      {
        "id": 156,
        "name": "China"
      },
      {
        "id": 170,
        "name": "Colombia"
      },
      {
        "id": 174,
        "name": "Comoros"
      },
      {
        "id": 175,
        "name": "Mayotte"
      },
      {
        "id": 178,
        "name": "Congo, Rep."
      },
      {
        "id": 180,
        "name": "Congo, Dem. Rep."
      },
       {
        "id": 184,
        "name": "Cook Islands"
      },
      {
        "id": 188,
        "name": "Costa Rica"
      },
      {
        "id": 191,
        "name": "Croatia"
      },
      {
        "id": 192,
        "name": "Cuba"
      },
      {
        "id": 196,
        "name": "Cyprus"
      },
      {
        "id": 203,
        "name": "Czech Republic"
      },
      {
        "id": 204,
        "name": "Benin"
      },
      {
        "id": 208,
        "name": "Denmark"
      },
      {
        "id": 212,
        "name": "Dominica"
      },
      {
        "id": 214,
        "name": "Dominican Republic"
      },
      {
        "id": 218,
        "name": "Ecuador"
      },
      {
        "id": 222,
        "name": "El Salvador"
      },
      {
        "id": 226,
        "name": "Equatorial Guinea"
      },
      {
        "id": 231,
        "name": "Ethiopia"
      },
      {
        "id": 232,
        "name": "Eritrea"
      },
      {
        "id": 233,
        "name": "Estonia"
      },
      {
        "id": 234,
        "name": "Faeroe Islands"
      },
      {
        "id": 238,
        "name": "Falkland Islands (Malvinas)"
      },
      
{
        "id": 242,
        "name": "Fiji"
      },
      {
        "id": 246,
        "name": "Finland"
      },
      {
        "id": 248,
        "name": "Åland Islands"
      },
      {
        "id": 250,
        "name": "France"
      },
      {
        "id": 254,
        "name": "French Guiana"
      },
      {
        "id": 258,
        "name": "French Polynesia"
      },
      {
        "id": 262,
        "name": "Djibouti"
      },
      {
        "id": 266,
        "name": "Gabon"
      },
      {
        "id": 268,
        "name": "Georgia"
      },
      {
        "id": 270,
        "name": "Gambia, The"
      },
      {
        "id": 275,
        "name": "West Bank and Gaza"
      },
      {
        "id": 276,
        "name": "Germany"
      },
      {
        "id": 288,
        "name": "Ghana"
      },
      {
        "id": 292,
        "name": "Gibraltar"
      },
      {
        "id": 296,
        "name": "Kiribati"
      },
      {
        "id": 300,
        "name": "Greece"
      },
      {
        "id": 304,
        "name": "Greenland"
      },
      {
        "id": 308,
        "name": "Grenada"
      },
      {
        "id": 312,
        "name": "Guadeloupe"
      },
      {
        "id": 316,
        "name": "Guam"
      },
      {
        "id": 320,
        "name": "Guatemala"
      },
      {
        "id": 324,
        "name": "Guinea"
      },
      {
        "id": 328,
        "name": "Guyana"
      },
      {
        "id": 332,
        "name": "Haiti"
      },
      {
        "id": 336,
        "name": "Holy See"
      },
      {
        "id": 340,
        "name": "Honduras"
      },
      {
        "id": 344,
        "name": "China, Hong Kong Special Administrative Region"
      },
      {
        "id": 348,
        "name": "Hungary"
      },
      {
        "id": 352,
        "name": "Iceland"
      },
      {
        "id": 356,
        "name": "India"
      },
      {
        "id": 360,
        "name": "Indonesia"
      },
      {
        "id": 364,
        "name": "Iran, Islamic Rep."
      },
      {
        "id": 368,
        "name": "Iraq"
      },
      {
        "id": 372,
        "name": "Ireland"
      },
      {
        "id": 376,
        "name": "Israel"
      },
      {
        "id": 380,
        "name": "Italy"
      },
      {
        "id": 384,
        "name": "Côte d'Ivoire"
      },
      {
        "id": 388,
        "name": "Jamaica"
      },
      {
        "id": 392,
        "name": "Japan"
      },
      {
        "id": 398,
        "name": "Kazakhstan"
      },
      {
        "id": 400,
        "name": "Jordan"
      },
      {
        "id": 404,
        "name": "Kenya"
      },
      {
        "id": 408,
        "name": "Korea, Dem. People's Rep."
      },
      {
        "id": 410,
        "name": "Republic of Korea"
      },
      {
        "id": 414,
        "name": "Kuwait"
      },
      {
        "id": 417,
        "name": "Kyrgyz Republic"
      },
      {
        "id": 418,
        "name": "Lao PDR"
      },
      {
        "id": 422,
        "name": "Lebanon"
      },
      {
        "id": 426,
        "name": "Lesotho"
      },
      {
        "id": 428,
        "name": "Latvia"
      },
      {
        "id": 430,
        "name": "Liberia"
      },
      {
        "id": 434,
        "name": "Libya"
      },
      {
        "id": 438,
        "name": "Liechtenstein"
      },
      {
        "id": 440,
        "name": "Lithuania"
      },
      {
        "id": 442,
        "name": "Luxembourg"
      },
      {
        "id": 446,
        "name": "China, Macao Special Administrative Region"
      },
      {
        "id": 450,
        "name": "Madagascar"
      },
      {
        "id": 454,
        "name": "Malawi"
      },
      {
        "id": 458,
        "name": "Malaysia"
      },
      {
        "id": 462,
        "name": "Maldives"
      },
      {
        "id": 466,
        "name": "Mali"
      },
      {
        "id": 470,
        "name": "Malta"
      },
      {
        "id": 474,
        "name": "Martinique"
      },
      {
        "id": 478,
        "name": "Mauritania"
      },
      {
        "id": 480,
        "name": "Mauritius"
      },
      {
        "id": 484,
        "name": "Mexico"
      },
      {
        "id": 492,
        "name": "Monaco"
      },
      {
        "id": 496,
        "name": "Mongolia"
      },
      {
        "id": 498,
        "name": "Moldova"
      },
      {
        "id": 499,
        "name": "Montenegro"
      },
      {
        "id": 500,
        "name": "Montserrat"
      },
      {
        "id": 504,
        "name": "Morocco"
      },
      {
        "id": 508,
        "name": "Mozambique"
      },
      {
        "id": 512,
        "name": "Oman"
      },
      {
        "id": 516,
        "name": "Namibia"
      },
      {
        "id": 520,
        "name": "Nauru"
      },
      {
        "id": 524,
        "name": "Nepal"
      },
      {
        "id": 528,
        "name": "Netherlands"
      },
      {
        "id": 531,
        "name": "Curaçao"
      },
      {
        "id": 533,
        "name": "Aruba"
      },
      {
        "id": 534,
        "name": "Sint Maarten (Dutch part)"
      },
      {
        "id": 535,
        "name": "Bonaire, Saint Eustatius and Saba"
      },
      {
        "id": 540,
        "name": "New Caledonia"
      },
      {
        "id": 548,
        "name": "Vanuatu"
      },
      {
        "id": 554,
        "name": "New Zealand"
      },
      {
        "id": 558,
        "name": "Nicaragua"
      },
      {
        "id": 562,
        "name": "Niger"
      },
      {
        "id": 566,
        "name": "Nigeria"
      },
      {
        "id": 570,
        "name": "Niue"
      },
      {
        "id": 574,
        "name": "Norfolk Island"
      },
      {
        "id": 578,
        "name": "Norway"
      },
      {
        "id": 580,
        "name": "Northern Mariana Islands"
      },
      {
        "id": 583,
        "name": "Micronesia, Fed. Sts."
      },
      {
        "id": 584,
        "name": "Marshall Islands"
      },
      {
        "id": 585,
        "name": "Palau"
      },
      {
        "id": 586,
        "name": "Pakistan"
      },
      {
        "id": 591,
        "name": "Panama"
      },
      {
        "id": 598,
        "name": "Papua New Guinea"
      },
      {
        "id": 600,
        "name": "Paraguay"
      },
      {
        "id": 604,
        "name": "Peru"
      },
      {
        "id": 608,
        "name": "Philippines"
      },
      {
        "id": 612,
        "name": "Pitcairn"
      },
      {
        "id": 616,
        "name": "Poland"
      },
      {
        "id": 620,
        "name": "Portugal"
      },
      {
        "id": 624,
        "name": "Guinea-Bissau"
      },
      {
        "id": 626,
        "name": "Timor-Leste"
      },
      {
        "id": 630,
        "name": "Puerto Rico"
      },
      {
        "id": 634,
        "name": "Qatar"
      },
      {
        "id": 638,
        "name": "Réunion"
      },
      {
        "id": 642,
        "name": "Romania"
      },
      {
        "id": 643,
        "name": "Russian Federation"
      },
      {
        "id": 646,
        "name": "Rwanda"
      },
      {
        "id": 652,
        "name": "Saint-Barthélemy"
      },
      {
        "id": 654,
        "name": "Saint Helena"
      },
      {
        "id": 659,
        "name": "St. Kitts and Nevis"
      },
      {
        "id": 660,
        "name": "Anguilla"
      },
      {
        "id": 662,
        "name": "St. Lucia"
      },
      {
        "id": 663,
        "name": "Saint-Martin (French part)"
      },
      {
        "id": 666,
        "name": "Saint Pierre and Miquelon"
      },
      {
        "id": 670,
        "name": "St. Vincent and the Grenadines"
      },
      {
        "id": 674,
        "name": "San Marino"
      },
      {
        "id": 678,
        "name": "São Tomé and Principe"
      },
      {
        "id": 680,
        "name": "Sark"
      },
      {
        "id": 682,
        "name": "Saudi Arabia"
      },
      {
        "id": 686,
        "name": "Senegal"
      },
      {
        "id": 688,
        "name": "Serbia"
      },
      {
        "id": 690,
        "name": "Seychelles"
      },
      {
        "id": 694,
        "name": "Sierra Leone"
      },
      
      {
        "id": 702,
        "name": "Singapore"
      },
      {
        "id": 703,
        "name": "Slovakia"
      },
      {
        "id": 704,
        "name": "Vietnam"
      },
      {
        "id": 705,
        "name": "Slovenia"
      },
      {
        "id": 706,
        "name": "Somalia"
      },
      {
        "id": 710,
        "name": "South Africa"
      },
      {
        "id": 716,
        "name": "Zimbabwe"
      },
      {
        "id": 724,
        "name": "Spain"
      },
      {
        "id": 728,
        "name": "South Sudan"
      },
      {
        "id": 729,
        "name": "Sudan"
      },
      {
        "id": 732,
        "name": "Western Sahara"
      },
      {
        "id": 740,
        "name": "Suriname"
      },
      {
        "id": 744,
        "name": "Svalbard and Jan Mayen Islands"
      },
      {
        "id": 748,
        "name": "Swaziland"
      },
      {
        "id": 752,
        "name": "Sweden"
      },
      {
        "id": 756,
        "name": "Switzerland"
      },
      {
        "id": 760,
        "name": "Syrian Arab Republic"
      },
      {
        "id": 762,
        "name": "Tajikistan"
      },
      {
        "id": 764,
        "name": "Thailand"
      },
      {
        "id": 768,
        "name": "Togo"
      },
      {
        "id": 772,
        "name": "Tokelau"
      },
      {
        "id": 776,
        "name": "Tonga"
      },
      {
        "id": 780,
        "name": "Trinidad and Tobago"
      },
      {
        "id": 784,
        "name": "United Arab Emirates"
      },
      {
        "id": 788,
        "name": "Tunisia"
      },
      {
        "id": 792,
        "name": "Türkiye"
      },
      {
        "id": 795,
        "name": "Turkmenistan"
      },
      {
        "id": 796,
        "name": "Turks and Caicos Islands"
      },
      {
        "id": 798,
        "name": "Tuvalu"
      },
      {
        "id": 800,
        "name": "Uganda"
      },
      {
        "id": 804,
        "name": "Ukraine"
      },
      
       {
        "id": 807,
        "name": "North Macedonia"
      },
      {
        "id": 818,
        "name": "Egypt, Arab Rep."
      },
      {
        "id": 826,
        "name": "United Kingdom of Great Britain and Northern Ireland"
      },
      {
        "id": 831,
        "name": "Guernsey"
      },
      {
        "id": 832,
        "name": "Jersey"
      },
      {
        "id": 833,
        "name": "Isle of Man"
      },
      {
        "id": 834,
        "name": "Tanzania"
      },
      {
        "id": 840,
        "name": "United States of America"
      },
      {
        "id": 850,
        "name": "United States Virgin Islands"
      },
      {
        "id": 854,
        "name": "Burkina Faso"
      },
      {
        "id": 858,
        "name": "Uruguay"
      },
      {
        "id": 860,
        "name": "Uzbekistan"
      },
      {
        "id": 862,
        "name": "Venezuela, RB"
      },
      {
        "id": 876,
        "name": "Wallis and Futuna Islands"
      },
      {
        "id": 882,
        "name": "Samoa"
      },
      {
        "id": 887,
        "name": "Yemen, Rep."
      },
      {
        "id": 894,
        "name": "Zambia"
      }
    ]
  }
}
#######################################################################################################################################################

That is the regions and their ids, so if you want to know the id of each region, use this, and don't use an other source :

{
  "data": {
    "regions": [
      {
        "id": 2,
        "name": "Africa"
      },
      {
        "id": 9,
        "name": "Oceania"
      },
      {
        "id": 21,
        "name": "Northern America"
      },
      {
        "id": 142,
        "name": "Asia"
      },
      {
        "id": 150,
        "name": "Eastern Europe"
      },
      {
        "id": 419,
        "name": "Latin America and the Caribbean"
      }
    ]
  }
}

################################################################################################################################################"


values that can take the attributes:

{
  "data": {
    "formfields": {
      "deal": {
        "locations": {
          "label": "Locations",
          "class": "JSONSchemaFormField",
          "required": false
        },
        "country": {
          "label": "Target country",
          "class": "CountryForeignKey",
          "required": false,
          "related_model": "Country"
        },
        "contract_size": {
          "label": "Size under contract (leased or purchased area, in ha)",
          "class": "JSONDateAreaField",
          "required": false
        },
        "intention_of_investment": {
          "label": "Intention of investment",
          "class": "JSONDateAreaChoicesField",
          "required": false,
          "choices": [
            {
              "value": "BIOFUELS",
              "label": "Biomass for biofuels",
              "group": "Agriculture"
            },
            {
              "value": "BIOMASS_ENERGY_GENERATION",
              "label": "Biomass for energy generation (agriculture)",
              "group": "Agriculture"
            },
            {
              "value": "FODDER",
              "label": "Fodder",
              "group": "Agriculture"
            },
            {
              "value": "FOOD_CROPS",
              "label": "Food crops",
              "group": "Agriculture"
            },
            {
              "value": "LIVESTOCK",
              "label": "Livestock",
              "group": "Agriculture"
            },
            {
              "value": "NON_FOOD_AGRICULTURE",
              "label": "Non-food agricultural commodities",
              "group": "Agriculture"
            },
            {
              "value": "AGRICULTURE_UNSPECIFIED",
              "label": "Agriculture unspecified",
              "group": "Agriculture"
            },
            {
              "value": "BIOMASS_ENERGY_PRODUCTION",
              "label": "Biomass for energy generation (forestry)",
              "group": "Forestry"
            },
            {
              "value": "CARBON",
              "label": "For carbon sequestration/REDD",
              "group": "Forestry"
            },
            {
              "value": "FOREST_LOGGING",
              "label": "Forest logging / management for wood and fiber",
              "group": "Forestry"
            },
            {
              "value": "TIMBER_PLANTATION",
              "label": "Timber plantation for wood and fiber",
              "group": "Forestry"
            },
            {
              "value": "FORESTRY_UNSPECIFIED",
              "label": "Forestry unspecified",
              "group": "Forestry"
            },
            {
              "value": "SOLAR_PARK",
              "label": "Solar park",
              "group": "Renewable energy power plants"
            },
            {
              "value": "WIND_FARM",
              "label": "Wind farm",
              "group": "Renewable energy power plants"
            },
            {
              "value": "RENEWABLE_ENERGY",
              "label": "Renewable energy unspecified",
              "group": "Renewable energy power plants"
            },
            {
              "value": "CONVERSATION",
              "label": "Conservation",
              "group": "Other"
            },
            {
              "value": "INDUSTRY",
              "label": "Industry",
              "group": "Other"
            },
            {
              "value": "LAND_SPECULATION",
              "label": "Land speculation",
              "group": "Other"
            },
            {
              "value": "MINING",
              "label": "Mining",
              "group": "Other"
            },
            {
              "value": "OIL_GAS_EXTRACTION",
              "label": "Oil / Gas extraction",
              "group": "Other"
            },
            {
              "value": "TOURISM",
              "label": "Tourism",
              "group": "Other"
            },
            {
              "value": "OTHER",
              "label": "Other",
              "group": "Other"
            }
          ]
        },
       
        "nature_of_deal": {
          "label": "Nature of the deal",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "OUTRIGHT_PURCHASE",
              "label": "Outright purchase"
            },
            {
              "value": "LEASE",
              "label": "Lease"
            },
            {
              "value": "CONCESSION",
              "label": "Concession"
            },
            {
              "value": "EXPLOITATION_PERMIT",
              "label": "Exploitation permit / license / concession (for mineral resources)"
            },
            {
              "value": "PURE_CONTRACT_FARMING",
              "label": "Pure contract farming"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
       
        "negotiation_status": {
          "label": "Negotiation status",
          "class": "JSONDateChoiceField",
          "required": false,
          "choices": [
            {
              "value": "EXPRESSION_OF_INTEREST",
              "label": "Intended (Expression of interest)"
            },
            {
              "value": "UNDER_NEGOTIATION",
              "label": "Intended (Under negotiation)"
            },
            {
              "value": "MEMORANDUM_OF_UNDERSTANDING",
              "label": "Intended (Memorandum of understanding)"
            },
            {
              "value": "ORAL_AGREEMENT",
              "label": "Concluded (Oral Agreement)"
            },
            {
              "value": "CONTRACT_SIGNED",
              "label": "Concluded (Contract signed)"
            },
            {
              "value": "CHANGE_OF_OWNERSHIP",
              "label": "Concluded (Change of ownership)"
            },
            {
              "value": "NEGOTIATIONS_FAILED",
              "label": "Failed (Negotiations failed)"
            },
            {
              "value": "CONTRACT_CANCELED",
              "label": "Failed (Contract cancelled)"
            },
            {
              "value": "CONTRACT_EXPIRED",
              "label": "Contract expired"
            }
          ]
        },
        "implementation_status": {
          "label": "Implementation status",
          "class": "JSONDateChoiceField",
          "required": false,
          "choices": [
            {
              "value": "PROJECT_NOT_STARTED",
              "label": "Project not started"
            },
            {
              "value": "STARTUP_PHASE",
              "label": "Startup phase (no production)"
            },
            {
              "value": "IN_OPERATION",
              "label": "In operation (production)"
            },
            {
              "value": "PROJECT_ABANDONED",
              "label": "Project abandoned"
            }
          ]
        },
        "recognition_status": {
          "label": "Recognition status of community land tenure",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "INDIGENOUS_RIGHTS_RECOGNIZED",
              "label": "Indigenous Peoples traditional or customary rights recognized by government"
            },
            {
              "value": "INDIGENOUS_RIGHTS_NOT_RECOGNIZED",
              "label": "Indigenous Peoples traditional or customary rights not recognized by government"
            },
            {
              "value": "COMMUNITY_RIGHTS_RECOGNIZED",
              "label": "Community traditional or customary rights recognized by government"
            },
            {
              "value": "COMMUNITY_RIGHTS_NOT_RECOGNIZED",
              "label": "Community traditional or customary rights not recognized by government"
            }
          ]
        },
        "negative_impacts": {
          "label": "Negative impacts for local communities",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "ENVIRONMENTAL_DEGRADATION",
              "label": "Environmental degradation"
            },
            {
              "value": "SOCIO_ECONOMIC",
              "label": "Socio-economic"
            },
            {
              "value": "CULTURAL_LOSS",
              "label": "Cultural loss"
            },
            {
              "value": "EVICTION",
              "label": "Eviction"
            },
            {
              "value": "DISPLACEMENT",
              "label": "Displacement"
            },
            {
              "value": "VIOLENCE",
              "label": "Violence"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        "crops": {
          "label": "Crops area/yield/export",
          "class": "JSONExportsField",
          "required": false,
          "choices": [
            {
              "value": "ACC",
              "label": "Accacia"
            },
            {
              "value": "ALF",
              "label": "Alfalfa"
            },
            {
              "value": "ALG",
              "label": "Seaweed / Macroalgae(unspecified)"
            },
            {
              "value": "ALM",
              "label": "Almond"
            },
            {
              "value": "ALV",
              "label": "Aloe Vera"
            },
            {
              "value": "APL",
              "label": "Apple"
            },
            {
              "value": "AQU",
              "label": "Aquaculture (unspecified crops)"
            },
            {
              "value": "BAM",
              "label": "Bamboo"
            },
            {
              "value": "BAN",
              "label": "Banana"
            },
            {
              "value": "BEA",
              "label": "Bean"
            },
            {
              "value": "BOT",
              "label": "Bottle Gourd"
            },
            {
              "value": "BRL",
              "label": "Barley"
            },
            {
              "value": "BWT",
              "label": "Buckwheat"
            },
            {
              "value": "CAC",
              "label": "Cacao"
            },
            {
              "value": "CAS",
              "label": "Cassava (Maniok)"
            },
            {
              "value": "CAW",
              "label": "Cashew"
            },
            {
              "value": "CHA",
              "label": "Chat"
            },
            {
              "value": "CHE",
              "label": "Cherries"
            },
            {
              "value": "CNL",
              "label": "Canola"
            },
            {
              "value": "COC",
              "label": "Coconut"
            },
            {
              "value": "COF",
              "label": "Coffee Plant"
            },
            {
              "value": "COT",
              "label": "Cotton"
            },
            {
              "value": "CRL",
              "label": "Cereals (unspecified)"
            },
            {
              "value": "CRN",
              "label": "Corn (Maize)"
            },
            {
              "value": "CRO",
              "label": "Croton"
            },
            {
              "value": "CST",
              "label": "Castor Oil Plant"
            },
            {
              "value": "CTR",
              "label": "Citrus Fruits (unspecified)"
            },
            {
              "value": "DIL",
              "label": "Dill"
            },
            {
              "value": "EUC",
              "label": "Eucalyptus"
            },
            {
              "value": "FLW",
              "label": "Flowers (unspecified)"
            },
            {
              "value": "FNT",
              "label": "Fig-Nut"
            },
            {
              "value": "FOD",
              "label": "Fodder Plants (unspecified)"
            },
            {
              "value": "FOO",
              "label": "Food crops (unspecified)"
            },
            {
              "value": "FRT",
              "label": "Fruit (unspecified)"
            },
            {
              "value": "GRA",
              "label": "Grapes"
            },
            {
              "value": "GRN",
              "label": "Grains (unspecified)"
            },
            {
              "value": "HRB",
              "label": "Herbs (unspecified)"
            },
            {
              "value": "JTR",
              "label": "Jatropha"
            },
            {
              "value": "LNT",
              "label": "Lentils"
            },
            {
              "value": "MAN",
              "label": "Mango"
            },
            {
              "value": "MUS",
              "label": "Mustard"
            },
            {
              "value": "OAT",
              "label": "Oats"
            },
            {
              "value": "OIL",
              "label": "Oil Seeds (unspecified)"
            },
            {
              "value": "OLE",
              "label": "Oleagionous plant"
            },
            {
              "value": "OLV",
              "label": "Olives"
            },
            {
              "value": "ONI",
              "label": "Onion"
            },
            {
              "value": "OPL",
              "label": "Oil Palm"
            },
            {
              "value": "OTH",
              "label": "Other crops (please specify)"
            },
            {
              "value": "PAL",
              "label": "Palms"
            },
            {
              "value": "PAP",
              "label": "Papaya"
            },
            {
              "value": "PAS",
              "label": "Passion fruit"
            },
            {
              "value": "PEA",
              "label": "Peanut (groundnut)"
            },
            {
              "value": "PEP",
              "label": "Pepper"
            },
            {
              "value": "PES",
              "label": "Peas"
            },
            {
              "value": "PIE",
              "label": "Pine"
            },
            {
              "value": "PIN",
              "label": "Pineapple"
            },
            {
              "value": "PLS",
              "label": "Pulses (unspecified)"
            },
            {
              "value": "POM",
              "label": "Pomegranate"
            },
            {
              "value": "PON",
              "label": "Pongamia Pinnata"
            },
            {
              "value": "PTT",
              "label": "Potatoes"
            },
            {
              "value": "RAP",
              "label": "Rapeseed"
            },
            {
              "value": "RCH",
              "label": "Rice (hybrid)"
            },
            {
              "value": "RIC",
              "label": "Rice"
            },
            {
              "value": "ROS",
              "label": "Roses"
            },
            {
              "value": "RUB",
              "label": "Rubber tree"
            },
            {
              "value": "RYE",
              "label": "Rye"
            },
            {
              "value": "SEE",
              "label": "Seeds Production (unspecified)"
            },
            {
              "value": "SES",
              "label": "Sesame"
            },
            {
              "value": "SOR",
              "label": "Sorghum"
            },
            {
              "value": "SOY",
              "label": "Soya Beans"
            },
            {
              "value": "SPI",
              "label": "Spices (unspecified)"
            },
            {
              "value": "SSL",
              "label": "Sisal"
            },
            {
              "value": "SUB",
              "label": "Sugar beet"
            },
            {
              "value": "SUC",
              "label": "Sugar Cane"
            },
            {
              "value": "SUG",
              "label": "Sugar (unspecified)"
            },
            {
              "value": "SUN",
              "label": "Sun Flower"
            },
            {
              "value": "SWP",
              "label": "Sweet Potatoes"
            },
            {
              "value": "TBC",
              "label": "Tobacco"
            },
            {
              "value": "TEA",
              "label": "Tea"
            },
            {
              "value": "TEF",
              "label": "Teff"
            },
            {
              "value": "TEK",
              "label": "Teak"
            },
            {
              "value": "TOM",
              "label": "Tomatoes"
            },
            {
              "value": "TRE",
              "label": "Trees (unspecified)"
            },
            {
              "value": "VGT",
              "label": "Vegetables (unspecified)"
            },
            {
              "value": "VIN",
              "label": "Vineyard"
            },
            {
              "value": "WHT",
              "label": "Wheat"
            },
            {
              "value": "YAM",
              "label": "Yam"
            }
          ]
        },
        "animals": {
          "label": "Livestock area/yield/export",
          "class": "JSONExportsField",
          "required": false,
          "choices": [
            {
              "value": "AQU",
              "label": "Aquaculture (animals)"
            },
            {
              "value": "BEE",
              "label": "Beef Cattle"
            },
            {
              "value": "CTL",
              "label": "Cattle"
            },
            {
              "value": "DCT",
              "label": "Dairy Cattle"
            },
            {
              "value": "FSH",
              "label": "Fish"
            },
            {
              "value": "GOT",
              "label": "Goats"
            },
            {
              "value": "OTH",
              "label": "Other livestock (please specify)"
            },
            {
              "value": "PIG",
              "label": "Pork"
            },
            {
              "value": "POU",
              "label": "Poultry"
            },
            {
              "value": "SHP",
              "label": "Sheep"
            },
            {
              "value": "SHR",
              "label": "Shrimp"
            }
          ]
        },
        "mineral_resources": {
          "label": "Mineral resources area/yield/export",
          "class": "JSONExportsField",
          "required": false,
          "choices": [
            {
              "value": "ALU",
              "label": "Aluminum"
            },
            {
              "value": "ASP",
              "label": "Asphaltite"
            },
            {
              "value": "ATC",
              "label": "Anthracite"
            },
            {
              "value": "BAR",
              "label": "Barite"
            },
            {
              "value": "BAS",
              "label": "Basalt"
            },
            {
              "value": "BAX",
              "label": "Bauxite"
            },
            {
              "value": "BEN",
              "label": "Bentonite"
            },
            {
              "value": "BUM",
              "label": "Building materials"
            },
            {
              "value": "CAR",
              "label": "Carbon"
            },
            {
              "value": "CHR",
              "label": "Chromite"
            },
            {
              "value": "CLA",
              "label": "Clay"
            },
            {
              "value": "COA",
              "label": "Coal"
            },
            {
              "value": "COB",
              "label": "Cobalt"
            },
            {
              "value": "COP",
              "label": "Copper"
            },
            {
              "value": "DIA",
              "label": "Diamonds"
            },
            {
              "value": "EME",
              "label": "Emerald"
            },
            {
              "value": "FLD",
              "label": "Feldspar"
            },
            {
              "value": "FLO",
              "label": "Fluoride"
            },
            {
              "value": "GAS",
              "label": "Gas"
            },
            {
              "value": "GLD",
              "label": "Gold"
            },
            {
              "value": "GRT",
              "label": "Granite"
            },
            {
              "value": "GRV",
              "label": "Gravel"
            },
            {
              "value": "HEA",
              "label": "Heavy Mineral Sands"
            },
            {
              "value": "ILM",
              "label": "Ilmenite"
            },
            {
              "value": "IRO",
              "label": "Iron"
            },
            {
              "value": "JAD",
              "label": "Jade"
            },
            {
              "value": "LED",
              "label": "Lead"
            },
            {
              "value": "LIM",
              "label": "Limestone"
            },
            {
              "value": "LIT",
              "label": "Lithium"
            },
            {
              "value": "MAG",
              "label": "Magnetite"
            },
            {
              "value": "MBD",
              "label": "Molybdenum"
            },
            {
              "value": "MGN",
              "label": "Manganese"
            },
            {
              "value": "MRB",
              "label": "Marble"
            },
            {
              "value": "NIK",
              "label": "Nickel"
            },
            {
              "value": "OTH",
              "label": "Other minerals (please specify)"
            },
            {
              "value": "PET",
              "label": "Petroleum"
            },
            {
              "value": "PHP",
              "label": "Phosphorous"
            },
            {
              "value": "PLT",
              "label": "Platinum"
            },
            {
              "value": "PUM",
              "label": "Hydrocarbons (e.g. crude oil)"
            },
            {
              "value": "PYR",
              "label": "Pyrolisis Plant"
            },
            {
              "value": "RUT",
              "label": "Rutile"
            },
            {
              "value": "SAN",
              "label": "Sand"
            },
            {
              "value": "SIC",
              "label": "Silica"
            },
            {
              "value": "SIL",
              "label": "Silver"
            },
            {
              "value": "SLT",
              "label": "Salt"
            },
            {
              "value": "STO",
              "label": "Stone"
            },
            {
              "value": "TIN",
              "label": "Tin"
            },
            {
              "value": "TTM",
              "label": "Titanium"
            },
            {
              "value": "URM",
              "label": "Uranium"
            },
            {
              "value": "ZNC",
              "label": "Zinc"
            }
          ]
        },
        "current_contract_size": {
          "label": "Current contract size",
          "class": "DecimalField",
          "required": false,
          "unit": "ha"
        },
        "current_production_size": {
          "label": "Current production size",
          "class": "DecimalField",
          "required": false
        },
        "intention_of_investment": {
          "label": "intention of investment",
          "class": "SimpleArrayField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "BIOFUELS",
              "label": "Biomass for biofuels"
            },
            {
              "value": "BIOMASS_ENERGY_GENERATION",
              "label": "Biomass for energy generation (agriculture)"
            },
            {
              "value": "FODDER",
              "label": "Fodder"
            },
            {
              "value": "FOOD_CROPS",
              "label": "Food crops"
            },
            {
              "value": "LIVESTOCK",
              "label": "Livestock"
            },
            {
              "value": "NON_FOOD_AGRICULTURE",
              "label": "Non-food agricultural commodities"
            },
            {
              "value": "AGRICULTURE_UNSPECIFIED",
              "label": "Agriculture unspecified"
            },
            {
              "value": "BIOMASS_ENERGY_PRODUCTION",
              "label": "Biomass for energy generation (forestry)"
            },
            {
              "value": "CARBON",
              "label": "For carbon sequestration/REDD"
            },
            {
              "value": "FOREST_LOGGING",
              "label": "Forest logging / management for wood and fiber"
            },
            {
              "value": "TIMBER_PLANTATION",
              "label": "Timber plantation for wood and fiber"
            },
            {
              "value": "FORESTRY_UNSPECIFIED",
              "label": "Forestry unspecified"
            },
            {
              "value": "SOLAR_PARK",
              "label": "Solar park"
            },
            {
              "value": "WIND_FARM",
              "label": "Wind farm"
            },
            {
              "value": "RENEWABLE_ENERGY",
              "label": "Renewable energy unspecified"
            },
            {
              "value": "CONVERSATION",
              "label": "Conservation"
            },
            {
              "value": "INDUSTRY",
              "label": "Industry"
            },
            {
              "value": "LAND_SPECULATION",
              "label": "Land speculation"
            },
            {
              "value": "MINING",
              "label": "Mining"
            },
            {
              "value": "OIL_GAS_EXTRACTION",
              "label": "Oil / Gas extraction"
            },
            {
              "value": "TOURISM",
              "label": "Tourism"
            },
            {
              "value": "OTHER",
              "label": "Other"
            }
          ]
        },
        "negotiation_status": {
          "label": "negotiation status",
          "class": "TypedChoiceField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "EXPRESSION_OF_INTEREST",
              "label": "Intended (Expression of interest)"
            },
            {
              "value": "UNDER_NEGOTIATION",
              "label": "Intended (Under negotiation)"
            },
            {
              "value": "MEMORANDUM_OF_UNDERSTANDING",
              "label": "Intended (Memorandum of understanding)"
            },
            {
              "value": "ORAL_AGREEMENT",
              "label": "Concluded (Oral Agreement)"
            },
            {
              "value": "CONTRACT_SIGNED",
              "label": "Concluded (Contract signed)"
            },
            {
              "value": "CHANGE_OF_OWNERSHIP",
              "label": "Concluded (Change of ownership)"
            },
            {
              "value": "NEGOTIATIONS_FAILED",
              "label": "Failed (Negotiations failed)"
            },
            {
              "value": "CONTRACT_CANCELED",
              "label": "Failed (Contract cancelled)"
            },
            {
              "value": "CONTRACT_EXPIRED",
              "label": "Contract expired"
            }
          ]
        },
        "implementation_status": {
          "label": "implementation status",
          "class": "TypedChoiceField",
          "required": false,
          "choices": [
            {
              "value": "",
              "label": "---------"
            },
            {
              "value": "PROJECT_NOT_STARTED",
              "label": "Project not started"
            },
            {
              "value": "STARTUP_PHASE",
              "label": "Startup phase (no production)"
            },
            {
              "value": "IN_OPERATION",
              "label": "In operation (production)"
            },
            {
              "value": "PROJECT_ABANDONED",
              "label": "Project abandoned"
            }
          ]
        },
        "area_max": {
          "label": "area_max",
          "class": "DecimalField",
          "required": false,
          "unit": "ha"
        },
        "area_min": {
          "label": "area_min",
          "class": "DecimalField",
          "required": false,
          "unit": "ha"
        },
        "created_at": {
          "label": "Created",
          "class": "DateTimeField",
          "required": false
        }
      }
    }
  }
}

#############################################################################################################################################

for the questions about, deal size, surface, or ha use just the attribut area_max or area_min, not use something different like deal_size.......


"""



















regions = [
    {"id":2, "region.name":"Africa"},
    {"id":9, "region.name":"Oceania"},
    {"id":21, "region.name":"Northern America"},
    {"id":142, "region.name":"Asia"},
    {"id":142, "region.name":" South-East Asia"},
    {"id":150, "region.name":"Eastern Europe"},
    {"id":419, "region.name":"Latin America and the Caribbean"},
]


import re


countries = [
    {"id": 4, "country.name": "afghanistan", "region_name": "Asia"},
    {"id": 8, "country.name": "Albania", "region_name": "Eastern Europe"},
    {"id": 12, "country.name": "Algeria", "region_name": "Africa"},
    {"id": 16, "country.name": "American Samoa", "region_name": "Oceania"},
    {"id": 20, "country.name": "Andorra", "region_name": "Southern Europe"},
    {"id": 24, "country.name": "Angola", "region_name": "Africa"},
    {"id": 28, "country.name": "Antigua and Barbuda", "region_name": "Latin America and the Caribbean"},
    {"id": 32, "country.name": "Argentina", "region_name": "Latin America and the Caribbean"},
    {"id": 31, "country.name": "Azerbaijan", "region_name": "Eastern Europe"},
    {"id": 36, "country.name": "Australia", "region_name": "Oceania"},
    {"id": 40, "country.name": "Austria", "region_name": "Eastern Europe"},
    {"id": 44, "country.name": "Bahamas", "region_name": "Latin America and the Caribbean"},
    {"id": 48, "country.name": "Bahrain", "region_name": "Asia"},
    {"id": 50, "country.name": "Bangladesh", "region_name": "Asia"},
    {"id": 51, "country.name": "Armenia", "region_name": "Eastern Europe"},
    {"id": 52, "country.name": "Barbados", "region_name": "Latin America and the Caribbean"},
    {"id": 56, "country.name": "Belgium", "region_name": "Eastern Europe"},
    {"id": 60, "country.name": "Bermuda", "region_name": "Northern America"},
    {"id": 64, "country.name": "Bhutan", "region_name": "Asia"},
    {"id": 68, "country.name": "Bolivia", "region_name": "Latin America and the Caribbean"},
    {"id": 70, "country.name": "Bosnia and Herzegovina", "region_name": "Eastern Europe"},
    {"id": 72, "country.name": "Botswana", "region_name": "Africa"},
    {"id": 76, "country.name": "Brazil", "region_name": "Latin America and the Caribbean"},
    {"id": 84, "country.name": "Belize", "region_name": "Latin America and the Caribbean"},
    {"id": 90, "country.name": "Solomon Islands", "region_name": "Asia"},
    {"id": 92, "country.name": "British Virgin Islands", "region_name": "Latin America and the Caribbean"},
    {"id": 96, "country.name": "Brunei Darussalam", "region_name": "Asia"},
    {"id": 100, "country.name": "Bulgaria", "region_name": "Eastern Europe"},
    {"id": 104, "country.name": "Myanmar", "region_name": "Asia"},
    {"id": 108, "country.name": "Burundi", "region_name": "Africa"},
    {"id": 112, "country.name": "Belarus", "region_name": "Eastern Europe"},
    {"id": 116, "country.name": "Cambodia", "region_name": "Asia"},
    {"id": 120, "country.name": "Cameroon", "region_name": "Africa"},
    {"id": 124, "country.name": "Canada", "region_name": "Northern America"},
    {"id": 132, "country.name": "Cape Verde", "region_name": "Africa"},
    {"id": 136, "country.name": "Cayman Islands", "region_name": "Latin America and the Caribbean"},
    {"id": 140, "country.name": "Central African Republic", "region_name": "Africa"},
    {"id": 144, "country.name": "Sri Lanka", "region_name": "Asia"},
    {"id": 148, "country.name": "Chad", "region_name": "Africa"},
    {"id": 152, "country.name": "Chile", "region_name": "Latin America and the Caribbean"},
    {"id": 156, "country.name": "China", "region_name": "Asia"},
    {"id": 170, "country.name": "Colombia", "region_name": "Latin America and the Caribbean"},
    {"id": 174, "country.name": "Comoros", "region_name": "Africa"},
    {"id": 175, "country.name": "Mayotte", "region_name": "Africa"},
    {"id": 178, "country.name": "Congo, Rep.", "region_name": "Africa"},
    {"id": 180, "country.name": "Congo, Dem. Rep.", "region_name": "Africa"},
    {"id": 184, "country.name": "Cook Islands", "region_name": "Oceania"},
    {"id": 188, "country.name": "Costa Rica", "region_name": "Latin America and the Caribbean"},
    {"id": 191, "country.name": "Croatia", "region_name": "Eastern Europe"},
    {"id": 192, "country.name": "Cuba", "region_name": "Latin America and the Caribbean"},
    {"id": 196, "country.name": "Cypru", "region_name": "Asia"},
    {"id": 203, "country.name": "Czech Republic", "region_name": "Eastern Europe"},
    {"id": 204, "country.name": "Benin", "region_name": "Africa"},
    {"id": 208, "country.name": "Denmark", "region_name": "Eastern Europe"},
    {"id": 212, "country.name": "Dominica", "region_name": "Latin America and the Caribbean"},
    {"id": 214, "country.name": "Dominican Republic", "region_name": "Latin America and the Caribbean"},
    {"id": 218, "country.name": "Ecuador", "region_name": "Latin America and the Caribbean"},
    {"id": 222, "country.name": "El Salvador", "region_name": "Latin America and the Caribbean"},
    {"id": 226, "country.name": "Equatorial Guinea", "region_name": "Africa"},
    {"id": 231, "country.name": "Ethiopia", "region_name": "Africa"},
    {"id": 233, "country.name": "Estonia", "region_name": "Eastern Europe"},
    {"id": 234, "country.name": "Faeroe Islands", "region_name": "Eastern Europe"},
    {"id": 238, "country.name": "Falkland Islands (Malvinas)", "region_name": "Latin America and the Caribbean"},
    {"id": 242, "country.name": "Cook Islands", "region_name": "Oceania"},
    {"id": 246, "country.name": "Finland", "region_name": "Eastern Europe"},
    {"id": 248, "country.name": "Åland Islands", "region_name": "Eastern Europe"},
    {"id": 250, "country.name": "France", "region_name": "Eastern Europe"},
    {"id": 254, "country.name": "French Guiana", "region_name": "Latin America and the Caribbean"},
    {"id": 258, "country.name": "French Polynesia", "region_name":"Oceania"},
    {"id": 262, "country.name": "Djibouti", "region_name": "Africa"},
    {"id": 266, "country.name": "Gabon", "region_name": "Africa"},
    {"id": 268, "country.name": "Georgia", "region_name": "Eastern Europe"},
    {"id": 270, "country.name": "Gambia, The", "region_name": "Africa"},
    {"id": 275, "country.name": "West Bank and Gaza", "region_name": "Asia"},
    {"id": 276, "country.name": "Germany", "region_name": "Eastern Europe"},
    {"id": 288, "country.name": "Ghana", "region_name": "Africa"},
    {"id": 292, "country.name": "Gibraltar", "region_name": "Eastern Europe"},
    {"id": 296, "country.name": "Kiribati", "region_name":"Oceania"},
    {"id": 300, "country.name": "Greece", "region_name": "Eastern Europe"},
    {"id": 304, "country.name": "Greenland", "region_name":"Northern America"},
    {"id": 308, "country.name": "Grenada", "region_name": "Latin America and the Caribbean"},
    {"id": 312, "country.name": "Guadeloupe", "region_name": "Latin America and the Caribbean"},
    {"id": 316, "country.name": "Guam", "region_name":"Oceania"},
    {"id": 320, "country.name": "Guatemala", "region_name": "Latin America and the Caribbean"},
    {"id": 324, "country.name": "Guinea", "region_name": "Africa"},
    {"id": 328, "country.name": "Guyana", "region_name": "Latin America and the Caribbean"},
    {"id": 332, "country.name": "Haiti", "region_name": "Latin America and the Caribbean"},
    {"id": 336, "country.name": "Holy See", "region_name": "Eastern Europe"},
    {"id": 340, "country.name": "Honduras", "region_name": "Latin America and the Caribbean"},
    {"id": 344, "country.name": "China, Hong Kong Special Administrative Region", "region_name": "Asia"},
    {"id": 348, "country.name": "Hungary", "region_name": "Eastern Europe"},
    {"id": 352, "country.name": "Iceland", "region_name": "Eastern Europe"},
    {"id": 356, "country.name": "India", "region_name": "Asia"},
    {"id": 360, "country.name": "Indonesia", "region_name": "Asia"},
    {"id": 364, "country.name": "Iran, Islamic Rep.", "region_name": "Asia"},
    {"id": 368, "country.name": "Iraq", "region_name": "Asia"},
    {"id": 372, "country.name": "Ireland", "region_name": "Eastern Europe"},
    {"id": 376, "country.name": "Israel", "region_name": "Asia"},
    {"id": 380, "country.name": "Italy", "region_name": "Eastern Europe"},
    {"id": 384, "country.name": "Côte d'Ivoire", "region_name": "Africa"},
    {"id": 388, "country.name": "Jamaica", "region_name": "Latin America and the Caribbean"},
    {"id": 392, "country.name": "Japan", "region_name": "Asia"},
    {"id": 398, "country.name": "Kazakhstan", "region_name": "Eastern Europe"},
    {"id": 400, "country.name": "Jordan", "region_name": "Asia"},
    {"id": 404, "country.name": "Kenya", "region_name": "Africa"},
    {"id": 408, "country.name": "Korea, Dem. People's Rep.", "region_name": "Asia"},
    {"id": 410, "country.name": "Republic of Korea", "region_name": "Asia"},
    {"id": 414, "country.name": "Kuwait", "region_name": "Asia"},
    {"id": 417, "country.name": "Kyrgyz Republic", "region_name": "Asia"},
    {"id": 418, "country.name": "Lao PDR", "region_name": "Asia"},
    {"id": 418, "country.name": "Laos", "region_name": "Asia"},
    {"id": 422, "country.name": "Lebanon", "region_name": "Asia"},
    {"id": 426, "country.name": "Lesotho", "region_name": "Africa"},
    {"id": 428, "country.name": "Latvia", "region_name": "Eastern Europe"},
    {"id": 430, "country.name": "Liberia", "region_name": "Africa"},
    {"id": 434, "country.name": "Libya", "region_name": "Africa"},
    {"id": 438, "country.name": "Liechtenstein", "region_name": "Eastern Europe"},
    {"id": 440, "country.name": "Lithuania", "region_name": "Eastern Europe"},
    {"id": 442, "country.name": "Luxembourg", "region_name": "Eastern Europe"},
    {"id": 446, "country.name": "China, Macao Special Administrative Region", "region_name": "Asia"},
    {"id": 454, "country.name": "Malawi", "region_name": "Africa"},
    {"id": 450, "country.name": "Madagascara", "region_name": "Africa"},
    {"id": 458, "country.name": "Malaysia", "region_name": "Asia"},
    {"id": 462, "country.name": "Maldives", "region_name": "Asia"},
    {"id": 466, "country.name": "Mali", "region_name": "Africa"},
    {"id": 470, "country.name": "Malta", "region_name": "Eastern Europe"},
    {"id": 474, "country.name": "Martinique", "region_name": "Latin America and the Caribbean"},
    {"id": 478, "country.name": "Mauritania", "region_name": "Africa"},
    {"id": 480, "country.name": "Mauritius", "region_name": "Africa"},
    {"id": 484, "country.name": "Mexico", "region_name": "Latin America and the Caribbean"},
    {"id": 492, "country.name": "Monaco", "region_name": "Eastern Europe"},
    {"id": 496, "country.name": "Mongolia", "region_name": "Asia"},
    {"id": 498, "country.name": "Moldova", "region_name": "Eastern Europe"},
    {"id": 499, "country.name": "Montenegro", "region_name": "Eastern Europe"},
    {"id": 500, "country.name": "Montserra", "region_name": "Latin America and the Caribbean"},
    {"id": 504, "country.name": "Morocco", "region_name": "Africa"},
    {"id": 508, "country.name": "Mozambique", "region_name": "Africa"},
    {"id": 512, "country.name": "Oman", "region_name": "Asia"},
    {"id": 516, "country.name": "Namibia", "region_name": "Africa"},
    {"id": 520, "country.name": "Nauru", "region_name": "Oceania"},
    {"id": 524, "country.name": "Nepal", "region_name": "Asia"},
    {"id": 528, "country.name": "Netherlands", "region_name": "Eastern Europe"},
    {"id": 531, "country.name": "Curaçao", "region_name": "Latin America and the Caribbean"},
    {"id": 533, "country.name": "Aruba", "region_name": "Latin America and the Caribbean"},
    {"id": 534, "country.name": "Sint Maarten (Dutch part)", "region_name": "Latin America and the Caribbean"},
    {"id": 535, "country.name": "Bonaire, Saint Eustatius and Saba", "region_name": "Latin America and the Caribbean"},
    {"id": 540, "country.name": "New Caledonia", "region_name": "Oceania"},
    {"id": 548, "country.name": "Vanuatu", "region_name": "Oceania"},
    {"id": 554, "country.name": "New Zealand", "region_name": "Oceania"},
    {"id": 558, "country.name": "Nicaragua", "region_name": "Latin America and the Caribbean"},
    {"id": 562, "country.name": "Niger", "region_name": "Africa"},
    {"id": 566, "country.name": "Nigeria", "region_name": "Africa"},
    {"id": 570, "country.name": "Niue", "region_name": "Oceania"},
    {"id": 574, "country.name": "Norfolk Island", "region_name": "Oceania"},
    {"id": 578, "country.name": "Norway", "region_name": "Eastern Europe"},
    {"id": 580, "country.name": "Northern Mariana Islands", "region_name": "Oceania"},
    {"id": 583, "country.name": "Micronesia, Fed. Sts.", "region_name": "Oceania"},
    {"id": 584, "country.name": "Marshall Islands", "region_name": "Oceania"},
    {"id": 585, "country.name": "Palau", "region_name": "Oceania"},
    {"id": 586, "country.name": "Pakistan", "region_name": "Asia"},
    {"id": 591, "country.name": "Panama", "region_name": "Latin America and the Caribbean"},
    {"id": 598, "country.name": "Papua New Guinea", "region_name": "Asia"},
    {"id": 600, "country.name": "Paraguay", "region_name": "Latin America and the Caribbean"},
    {"id": 604, "country.name": "Peru", "region_name": "Latin America and the Caribbean"},
    {"id": 608, "country.name": "Philippines", "region_name": "Asia"},
    {"id": 612, "country.name": "Pitcairn", "region_name": "Oceania"},
    {"id": 616, "country.name": "Poland", "region_name": "Eastern Europe"},
    {"id": 620, "country.name": "Portugal", "region_name": "Eastern Europe"},
    {"id": 624, "country.name": "Guinea-Bissau", "region_name": "Africa"},
    {"id": 626, "country.name": "Timor-Leste", "region_name": "Asia"},
    {"id": 630, "country.name": "Puerto Rico", "region_name": "Latin America and the Caribbean"},
    {"id": 634, "country.name": "Qatar", "region_name": "Asia"},
    {"id": 638, "country.name": "Réunion", "region_name": "Africa"},
    {"id": 642, "country.name": "Romania", "region_name": "Eastern Europe"},
    {"id": 643, "country.name": "Russian Federation", "region_name": "Eastern Europe"},
    {"id": 646, "country.name": "Rwanda", "region_name": "Africa"},
    {"id": 652, "country.name": "Saint-Barthélemy", "region_name": "Latin America and the Caribbean"},
    {"id": 654, "country.name": "Saint Helena", "region_name": "Africa"},
    {"id": 659, "country.name": "St. Kitts and Nevis", "region_name": "Latin America and the Caribbean"},
    {"id": 660, "country.name": "Anguilla", "region_name": "Latin America and the Caribbean"},
    {"id": 662, "country.name": "St. Lucia", "region_name": "Latin America and the Caribbean"},
    {"id": 663, "country.name": "Saint-Martin (French part", "region_name": "Latin America and the Caribbean"},
    {"id": 666, "country.name": "Saint Pierre and Miquelon", "region_name": "Northern America"},
    {"id": 670, "country.name": "St. Vincent and the Grenadines", "region_name": "Latin America and the Caribbean"},
    {"id": 674, "country.name": "San Marino", "region_name": "Eastern Europe"},
    {"id": 678, "country.name": "São Tomé and Principe", "region_name": "Africa"},
    {"id": 680, "country.name": "Sark", "region_name": "Eastern Europe"},
    {"id": 682, "country.name": "Saudi Arabia", "region_name": "Asia"},
    {"id": 686, "country.name": "Senegal", "region_name": "Africa"},
    {"id": 688, "country.name": "Serbia", "region_name": "Eastern Europe"},
    {"id": 690, "country.name": "Seychelles", "region_name": "Africa"},
    {"id": 694, "country.name": "Sierra Leone", "region_name": "Africa"},
    {"id": 702, "country.name": "Singapore", "region_name": "Asia"},
    {"id": 703, "country.name": "Slovakia", "region_name": "Eastern Europe"},
    {"id": 704, "country.name": "Vietnam", "region_name": "Asia"},
    {"id": 705, "country.name": "Slovenia", "region_name": "Eastern Europe"},
    {"id": 706, "country.name": "Somalia", "region_name": "Africa"},
    {"id": 710, "country.name": "South Africa", "region_name": "Africa"},
    {"id": 716, "country.name": "Zimbabwe", "region_name": "Africa"},
    {"id": 724, "country.name": "Spain", "region_name": "Eastern Europe"},
    {"id": 728, "country.name": "South Sudan", "region_name": "Africa"},
    {"id": 729, "country.name": "Sudan", "region_name": "Africa"},
    {"id": 732, "country.name": "Western Sahara", "region_name": "Africa"},
    {"id": 740, "country.name": "Suriname", "region_name": "Latin America and the Caribbean"},
    {"id": 744, "country.name": "Svalbard and Jan Mayen Islands", "region_name": "Eastern Europe"},
    {"id": 748, "country.name": "Swaziland", "region_name": "Africa"},
    {"id": 752, "country.name": "Sweden", "region_name": "Eastern Europe"},
    {"id": 756, "country.name": "Switzerland", "region_name": "Eastern Europe"},
    {"id": 760, "country.name": "Syrian Arab Republic", "region_name": "Asia"},
    {"id": 762, "country.name": "Tajikistan", "region_name": "Asia"},
    {"id": 764, "country.name": "Thailand", "region_name": "Asia"},
    {"id": 768, "country.name": "Togo", "region_name": "Africa"},
    {"id": 772, "country.name": "Tokelau", "region_name": "Oceania"},
    {"id": 776, "country.name": "Tonga", "region_name": "Oceania"},
    {"id": 780, "country.name": "Trinidad and Tobago", "region_name": "Latin America and the Caribbean"},
    {"id": 784, "country.name": "United Arab Emirates", "region_name": "Asia"},
    {"id": 788, "country.name": "Tunisia", "region_name": "Africa"},
    {"id": 792, "country.name": "Türkiye", "region_name": "Asia"},
    {"id": 795, "country.name": "Turkmenistan", "region_name": "Asia"},
    {"id": 796, "country.name": "Turks and Caicos Islands", "region_name": "Latin America and the Caribbean"},
    {"id": 798, "country.name": "Tuvalu", "region_name": "Oceania"},
    {"id": 800, "country.name": "Uganda", "region_name": "Africa"},
    {"id": 804, "country.name": "Ukraine", "region_name": "Eastern Europe"},
    {"id": 807, "country.name": "North Macedonia", "region_name": "Eastern Europe"},
    {"id": 818, "country.name": "Egypt, Arab Rep.", "region_name": "Africa"},
    {"id": 826, "country.name": "United Kingdom of Great Britain and Northern Ireland", "region_name": "Eastern Europe"},
    {"id": 831, "country.name": "Guernsey", "region_name": "Eastern Europe"},
    {"id": 832, "country.name": "Jersey", "region_name": "Eastern Europe"},
    {"id": 833, "country.name": "Isle of Man", "region_name": "Eastern Europe"},
    {"id": 834, "country.name": "Tanzania", "region_name": "Africa"},
    {"id": 840, "country.name": "United States of America", "region_name": "Northern America"},
    {"id": 850, "country.name": "United States Virgin Islands", "region_name": "Latin America and the Caribbean"},
    {"id": 854, "country.name": "Burkina Faso.", "region_name": "Africa"},
    {"id": 858, "country.name": "Uruguay", "region_name": "Latin America and the Caribbean"},
    {"id": 860, "country.name": "Uzbekistan", "region_name": "Eastern Europe"},
    {"id": 862, "country.name": "Venezuela, RB", "region_name": "Latin America and the Caribbean"},
    {"id": 876, "country.name": "Wallis and Futuna Islands", "region_name": "Oceania"},
    {"id": 882, "country.name": "Samoa", "region_name": "Oceania"},
    {"id": 887, "country.name": "Yemen, Rep.", "region_name": "Asia"},
    {"id": 894, "country.name": "Zambia", "region_name": "Africa"},
]


