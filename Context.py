context = """ 

Schema: 

{"__validationErrors":[],"_queryType":"Query","_mutationType":"Mutation","_subscriptionType":null,"_directives":["@include","@skip","@deprecated","@specifiedBy"],"_typeMap":{"BlogPage":"BlogPage","Int":"Int","String":"String","BlogCategory":"BlogCategory","BlogTag":"BlogTag","Deal":"Deal","Float":"Float","Boolean":"Boolean","Location":"Location","Contract":"Contract","DataSource":"DataSource","Actor":"Actor","Aggregations":"Aggregations","DealVersion":"DealVersion","WFReply":"WFReply","DealWorkflowInfo":"DealWorkflowInfo","DealComment":"DealComment","Dict":"Dict","Filter":"Filter","Value":"Value","FilterOperation":"FilterOperation","Investor":"Investor","InvestorVersion":"InvestorVersion","Involvement":"Involvement","InvolvementsNetwork":"InvolvementsNetwork","InvestorWorkflowInfo":"InvestorWorkflowInfo","Marker":"Marker","Mutation":"Mutation","Payload":"Payload","WorkflowTransition":"WorkflowTransition","ObjectReturn":"ObjectReturn","DealEditReturn":"DealEditReturn","InvestorEditReturn":"InvestorEditReturn","LoginPayload":"LoginPayload","RegisterPayload":"RegisterPayload","Country":"Country","Region":"Region","Currency":"Currency","Animal":"Animal","Crop":"Crop","Mineral":"Mineral","DateValuePair":"DateValuePair","Date":"Date","DateTime":"DateTime","GeoJSON":"GeoJSON","GeoPoint":"GeoPoint","Statistics":"Statistics","Subset":"Subset","WebOfTransnationalDeals":"WebOfTransnationalDeals","GlobalInvestmentMap":"GlobalInvestmentMap","CountryInvestmentsAndRankings":"CountryInvestmentsAndRankings","Rankings":"Rankings","ChartDescriptions":"ChartDescriptions","DealAggregation":"DealAggregation","DealAggregations":"DealAggregations","Query":"Query","FormFieldSet":"FormFieldSet","FormFields":"FormFields","User":"User","UserGroup":"UserGroup","__Schema":"__Schema","__Type":"__Type","__TypeKind":"__TypeKind","__Field":"__Field","__InputValue":"__InputValue","__EnumValue":"__EnumValue","__Directive":"__Directive","__DirectiveLocation":"__DirectiveLocation"},"_subTypeMap":{},"_implementationsMap":{}}

#########################################################################################################################################################

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

their is some information and roles from API documentation for our database LandMatrix: 


Deals
A deal is a transaction associated with a particular piece of land or area.

The deal data schema including all available fields can be found in the Schema section.

Investors
Investors are entities or associations which are associated with a land deal.

The Investor data schema including all available fields can be found in the Schema section.

##################################################################################################################################################"

their is some query examples

If you want to receive a specific deal by ID you can pass the ID as an argument to the query. In this case you are querying for the data type deal
{
  deal(id: 4) {
    id
    current_intention_of_investment
    current_negotiation_status
    geojson
  }
}

Data on all deals available can be recieved by querying for deals.

# This will return data of the first 5 deals (ordered by ID).
{
  deals(limit: 5) {
    id
    country {
      id
      name
    }
    geojson
  }
}


if you want investor by ID
To find a specific investor by ID simply pass the ID to the investor query:

{
  investor(id: 1010) {
    id
    name
    country {
      name
    }
  }
}


Multiple investors:
Analogous to the deals, data on multiple investors can be queried with the investors query.

# This will return "id" and "name" of the first 5 investors ordered ascending by ID.
{
  investors(limit: 5) {
    id
    name
  }
}

for Sorting:
Some queries, like deals and investors, have an option for sorting the output. It defaults to being sorted by id but it will also accept other fields, e.g. modified_at.

You can also change the sort direction from ASCending to DESCending by prefixing the sort-term with a -.

# Sort deals by creation date ascending
{
  deals(sort: "created_at") {
    id
    deal_size
  }
}


for Filters:
In most use cases you may want to specify some fields and conditions you want to have your query results filtered by. You can pass a filter array to your query as an argument.

Filter examples
If you want to apply a filter you can directly incorporate the filter array into your query like this:

{
  deals(filters: { field: "created_at", operation: GE, value: "2020-03-02" }) {
    id
    deal_size
  }
}

values that can take value in Filters:

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
        "annual_leasing_fee_comment": {
          "label": "Comment on leasing fee",
          "class": "TextField",
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
        "contract_farming_comment": {
          "label": "Comment on contract farming",
          "class": "TextField",
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
        "total_jobs_created_comment": {
          "label": "Comment on jobs created (total)",
          "class": "TextField",
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
        "foreign_jobs_created_comment": {
          "label": "Comment on jobs created (foreign)",
          "class": "TextField",
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
        "domestic_jobs_created_comment": {
          "label": "Comment on jobs created (domestic)",
          "class": "TextField",
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
          "label": "Number of households displaced \"only\" from their agricultural fields",
          "class": "IntegerField",
          "required": false
        },
        "displaced_people_on_completion": {
          "label": "Number of people facing displacement once project is fully implemented",
          "class": "IntegerField",
          "required": false
        },
        "displacement_of_people_comment": {
          "label": "Comment on displacement of people",
          "class": "TextField",
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
        "negative_impacts_comment": {
          "label": "Comment on negative impacts for local communities",
          "class": "TextField",
          "required": false
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
        "promised_benefits_comment": {
          "label": "Comment on promised benefits for local communities",
          "class": "TextField",
          "required": false
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
        "materialized_benefits_comment": {
          "label": "Comment on materialized benefits for local communities",
          "class": "TextField",
          "required": false
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
        "former_land_owner_comment": {
          "label": "Comment on former land owner",
          "class": "TextField",
          "required": false
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
        "former_land_use_comment": {
          "label": "Comment on former land use",
          "class": "TextField",
          "required": false
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
        "former_land_cover_comment": {
          "label": "Comment on former land cover",
          "class": "TextField",
          "required": false
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
        "crops_comment": {
          "label": "Comment on crops",
          "class": "TextField",
          "required": false
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
        "animals_comment": {
          "label": "Comment on livestock",
          "class": "TextField",
          "required": false
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
        "contract_farming_animals_comment": {
          "label": "Comment on contract farming livestock",
          "class": "TextField",
          "required": false
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
        "electricity_generation_comment": {
          "label": "Comment on electricity generation",
          "class": "TextField",
          "required": false
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
        "carbon_sequestration_comment": {
          "label": "Comment on carbon sequestration",
          "class": "TextField",
          "required": false
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
        "source_of_water_extraction_comment": {
          "label": "Comment on source of water extraction",
          "class": "TextField",
          "required": false
        },
        "how_much_do_investors_pay_comment": {
          "label": "Comment on how much do investors pay for water",
          "class": "TextField",
          "required": false
        },
        "water_extraction_amount": {
          "label": "Water extraction amount",
          "class": "IntegerField",
          "required": false,
          "unit": "m3/year"
        },
        "water_extraction_amount_comment": {
          "label": "Comment on how much water is extracted",
          "class": "TextField",
          "required": false
        },
        "use_of_irrigation_infrastructure": {
          "label": "Use of irrigation infrastructure",
          "class": "NullBooleanField",
          "required": false
        },
        "use_of_irrigation_infrastructure_comment": {
          "label": "Comment on use of irrigation infrastructure",
          "class": "TextField",
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
        "overall_comment": {
          "label": "Overall comment",
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
        "confidential_comment": {
          "label": "Comment why this deal is private",
          "class": "TextField",
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

################################################################################################################################

exemple question: Where are the investments in Agriculture?

response: 
query Data {
  deals(
    filters: [
      {
        field: "current_intention_of_investment",
        operation: OVERLAP,
        value: ["BIOFUELS", "BIOMASS_ENERGY_GENERATION", "FODDER",
                                        "FOOD_CROPS", "LIVESTOCK", "NON_FOOD_AGRICULTURE",
                                  "AGRICULTURE_UNSPECIFIED"]
      }
    ]
  ) { 
           id
    country {id name code_alpha2}
    current_intention_of_investment
  }
}


exemple question: How much land will be taken by forthcoming deals? 

response:
query Data {
  deals(
    filters: [
      {field: "current_implementation_status", operation: EQ, value: "PROJECT_NOT_STARTED" }
    ]
  ) { 
           id
    current_implementation_status
  }
}

exemple question: What types of investment exist in Argentina since 2010?
response:

query Data {
  deals(
    filters: [
      {field: "country.id", operation: EQ, value: 32 }
      {field: "initiation_year", operation: GE, value: 2010, allow_null: true}
    ]
  ) { 
           id
    country {id name code_alpha2}
    initiation_year
    current_intention_of_investment
  }
}

exemple question: What is the size in operation?

response:
query Data {
  deals(
    filters: [
      {field: "current_implementation_status", operation: EQ, value: "IN_OPERATION" }
    ]
  ) { 
           id
    current_implementation_status
  }
}



exemple question: Where is renewable energy produced?

response:
query Data {
  deals(
    filters: [
      {field: "current_intention_of_investment",
        operation: OVERLAP,
        value: ["SOLAR_PARK", "WIND_FARM", "RENEWABLE_ENERGY"] }
    ]
  ) { 
           id
    country {
      id
      name
      code_alpha2
    }
    current_intention_of_investment
  }
}
#############################################################################################################################################

for the questions about, deal size, surface, or ha use just the attribut deal_size, not use something different like current_deal_size.......


"""