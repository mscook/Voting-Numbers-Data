Rank Polling Stations
=====================

Use AEC results to predict where most voters will turn out given a seat name.

Data vailable from:
http://results.aec.gov.au/15508/Website/HouseDownloadsMenu-15508-csv.htm
(First Preferences, Two Candidate Preferred and Two Party Preferred)
(First Preferences By Candidate By Polling Place)


Usage
-----

Something like::

    $ python rank_polling_stations.py
    HouseStateFirstPrefsByPollingPlaceDownload-15508-QLD.csv Lilley 

Gives::

    Rank, Polling Station Name, Voter Turnout, Address

    1, McDowall, 4457, McDowall McDowall State School 1018 Rode Rd   MCDOWALL QLD 4053

    2, Boondall, 4060, Boondall Boondall State School Roscommon Rd   BOONDALL QLD 4034

    3, Nundah, 3239, Nundah Nundah State School Cnr Buckland Rd & Bage St   NUNDAH QLD 4012

    4, Aspley West (Lilley), 3162, Aspley West (Lilley) Aspley State School Maundrell Tce   ASPLEY QLD 4034

    5, Chermside West, 3115, Chermside West Craigslea State High School 685 Hamilton Rd   CHERMSIDE WEST QLD 4032

    6, Geebung, 2507, Geebung St Kevins Primary School 249 Newman Rd   GEEBUNG QLD 4034

    7, Stafford Heights, 2286, Stafford Heights Stafford Heights State School 95 Redwood St   STAFFORD HEIGHTS QLD 4053

    8, Taigum (Lilley), 2189, Taigum (Lilley) Taigum State School 266 Handford Rd   TAIGUM QLD 4034

    9, Chermside LILLEY PPVC, 2152, Chermside LILLEY PPVC Chermside Gardens 766 Gympie Rd   CHERMSIDE QLD 4032

    10, Wavell Heights, 2097, Wavell Heights Burnie Brae Centre 60 Kuran St   CHERMSIDE QLD 4032

    11, Virginia, 2090, Virginia Virginia State School cnr Sandgate Rd & Jefferis St   VIRGINIA QLD 4355

    12, Banyo East, 2024, Banyo East Earnshaw State College Earnshaw Rd   BANYO QLD 4014

    13, Chermside East, 1983, Chermside East Wavell Hts Presbyterian Church Hall Spence Rd   WAVELL HEIGHTS QLD 4012

    14, Brighton South, 1980, Brighton South Nashville State School Baskerville St   BRIGHTON QLD 4017

    15, Everton Park North, 1962, Everton Park North Everton Park State School 1 Deakin St   EVERTON PARK QLD 4053

    16, Kedron, 1922, Kedron Kedron State School Leckie Rd   KEDRON QLD 4031

    17, Sandgate, 1907, Sandgate RSL Sub-Branch Memorial Hall Burnett Pl   SANDGATE QLD 4017

    18, Zillmere North, 1887, Zillmere North Church of Christ Zillmere 367 Zillmere Rd   ZILLMERE QLD 4034

    19, Brighton, 1778, Brighton Brighton State School 2 North Rd   BRIGHTON QLD 4017

    20, Somerset Hills, 1742, Somerset Hills Somerset Hills State School 233 Kitchener Rd   STAFFORD HEIGHTS QLD 4053

    21, Kedron Heights, 1659, Kedron Heights Little Flower Church Hall 66 Turner Rd   KEDRON QLD 4031

    22, Shorncliffe, 1616, Shorncliffe Shorncliffe State School Yundah St   SHORNCLIFFE QLD 4017

    23, Zillmere, 1569, Zillmere Zillmere State School Murphy Rd   ZILLMERE QLD 4034

    24, Clayfield LILLEY PPVC, 1518, Clayfield LILLEY PPVC Nundah 21 Station St   NUNDAH QLD 4012

    25, Deagon, 1469, Deagon Sandgate State High School Cnr Braun St & Depot Rd   DEAGON QLD 4017

    26, Banyo, 1461, Banyo St Oswalds Anglican Church Hall 9 Froude St   BANYO QLD 4014

    27, Northgate, 1368, Northgate Northgate State School Amelia St   NUNDAH QLD 4012

    28, Aspley East (Lilley), 1357, Aspley East (Lilley) Aspley East State School 31 Helena St   ASPLEY QLD 4034

    29, Stafford Central, 1324, Stafford Central Queen of Apostles School 84 Appleby Rd   STAFFORD QLD 4053

    30, Nundah West, 1258, Nundah West Holy Spirit Anglican Church Hall Cnr Olive & Imbros Sts   NUNDAH QLD 4012

    31, Stafford West (Lilley), 1243, Stafford West (Lilley) Everton Park High School 624 Stafford Rd   EVERTON PARK QLD 4053

    32, Nundah North, 1151, Nundah North St Francis Anglican Church Hall Cameron St   NUNDAH QLD 4012

    33, Stafford (Lilley), 1137, Stafford (Lilley) Stafford State School 314 Stafford Rd   STAFFORD QLD 4053

    34, Craigslea, 1083, Craigslea Craigslea Kindergarten Marban St   CHERMSIDE WEST QLD 4032

    35, Bridgeman Downs (Lilley), 1078, Bridgeman Downs (Lilley) Anglican Church Hall 30 Ridley Rd   BRIDGEMAN DOWNS QLD 4035

    36, Aspley (Lilley), 1050, Aspley (Lilley) Aspley State High School 651 Zillmere Rd   ASPLEY QLD 4034

    37, Everton Park, 1037, Everton Park St Jude's Anglican Church Hall cnr McIlwraith & Buller Sts   EVERTON PARK QLD 4053

    38, Nudgee, 980, Nudgee Nudgee School of Arts Hayden St   NUDGEE QLD 4014

    39, Brighton East, 910, Brighton East Eventide Home Beaconsfield Tce   BRIGHTON QLD 4017

    40, Brisbane City LILLEY PPVC, 576, Brisbane City LILLEY PPVC Roy Harvey House 157 Ann St   BRISBANE CITY QLD 4000

    41, Chermside Gardens, 520, Chermside Gardens Uhl Memorial Hall 930 Gympie Rd   CHERMSIDE QLD 4032

    42, Chermside, 417, Chermside Prince Charles Hospital Rode Rd   CHERMSIDE QLD 4032

    43, Kalinga (Lilley), 320, Kalinga (Lilley) Presbyterian Church Hall Cnr Shaw Rd & Emma St   WOOLOOWIN QLD 4030

    44, Sandgate North, 297, Sandgate North Masonic Care Queensland 60 Wakefield St   SANDGATE QLD 4017

    45, Nudgee Beach, 244, Nudgee Beach Environmental Education Centre 1588 Nudgee Rd   NUDGEE BEACH QLD 4016

    46, Brisbane City (Lilley), 231, Brisbane City (Lilley) Primary Industries Building 80 Ann St   BRISBANE CITY QLD 4000

    47, Special Hospital Team 2, 224, Special Hospital Team 2 Multiple sites     QLD 

    48, Divisional Office (PREPOLL), 139, Divisional Office (PREPOLL) Divisional Office 7th Floor 488 Queen St  BRISBANE QLD 4000

    49, Special Hospital Team 1, 61, Special Hospital Team 1 Multiple sites     QLD 

    50, Domestic Airport PPVC, 0, Domestic Airport PPVC Domestic Airport (Qantas) Departure Lounge Qantas Hub Gate 16 Airport Dr BRISBANE AIRPORT QLD 4007

    51, International Airport PPVC, 0, International Airport PPVC International Airport Airport Dr   BRISBANE AIRPORT QLD 4007

