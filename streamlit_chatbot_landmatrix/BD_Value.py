
context= """
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
        "carbon_offset_project": {
          "label": "Carbon offset project",
          "class": "NullBooleanField",
          "required": false
        },
        "nature": {
          "label": "Nature",
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
        "contract_farming": {
          "label": "Contract farming",
          "class": "NullBooleanField",
          "required": false
        }, 
        "contracts": {
          "label": "Contracts",
          "class": "JSONSchemaFormField",
          "required": false
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
          "label": "Crops",
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
          "label": "animals",
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
        "minerals": {
          "label": "Minerals",
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
        "fully_updated": {
          "label": "Fully updated",
          "class": "BooleanField",
          "required": false
        },
        "area_min": {
          "label": "area_min",
          "class": "DecimalField",
          "required": false,
          "unit": "ha"
        },
        "area_max": {
          "label": "area_max",
          "class": "DecimalField",
          "required": false,
          "unit": "ha"
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
