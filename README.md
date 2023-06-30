# companyprofile


# About APP

This Falsk APP is used scraping the Company data from Linkedin.

# Installation
pip install -r requirements.txt

# Steps to Run
- Clone the project using the gitlink
- Install the required packages mention in requirements.txt
- Open the project using the IDE (vscode/pycharm)
- Open terminal & redirect the project path
- Run the project by typing : python server3.py
- Open the browser & redirect to url (http://localhost:5000/)

# Take the tour

- To use this app we need csv file with company name.
- Once file Ready upload this csv file using UI or POST API
- After File Uploaded to Portal
- Parsing the CSV data for company name to pass Input to Scraper
- Here we are using Third Party Scraper To Avoid below issue while scraping data from Linkedin"
   > Proxy rotation & selection
   > Rotating user-agents & browser headers
   > Ban detection & CAPTCHA bypassing
   > Country IP geotargeting
   > Javascript rendering with headless browsers
- After Using the Scrapper will get the company details for respective search


# UI Form : 

<a href="#readme">
        <img alt="logo" src="UIform.png" style="max-width: 100%;">   
    </a>
 

# API Details

API Method : POST
Authorization : NO
Content-Type : multipart/form-data



> Python request Details:


import requests

url = "http://localhost:5000/companyfileupload"

payload={}
files=[
  ('uploaded-file',('raw_biggest_companies.csv',open('/C:/Users/home/Downloads/raw_biggest_companies.csv','rb'),'text/csv'))
]
headers = {
  'Cookie': 'session=eyJ1cGxvYWRlZF9kYXRhX2ZpbGVfcGF0aCI6InN0YXRpY1xcdXBsb2Fkc1xccmF3X2JpZ2dlc3RfY29tcGFuaWVzLmNzdiJ9.ZJ5xRA.ynDC9d4-YK2lQzsYm81n_0oHo_M'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

Response : 

>> Success : 200 ok


{
    "Company Name": {
        "0": "Amazon",
        "1": "Apple",
        "2": "Google",
        "3": "Microsoft",
        "4": "Alibaba",
        "5": "Facebook",
        "6": "Berkshire Hathaway",
        "7": "JP Morgan Chase",
        "8": "Exxon Mobil",
        "9": "Johnson & Johnson",
        "10": "Nestle",
        "11": "Procter & Gamble",
        "12": "Toyota",
        "13": "General Electric",
        "14": "Chevron",
        "15": "Coca-Cola",
        "16": "McDonald's",
        "17": "Wal-Mart",
        "18": "IBM",
        "19": "PepsiCo",
        "20": "Unilever",
        "21": "Anheuser-Busch InBev",
        "22": "Chevron",
        "23": "Royal Dutch Shell",
        "24": "BP",
        "25": "Walgreens Boots Alliance",
        "26": "CVS Health",
        "27": "Intel",
        "28": "Johnson & Johnson",
        "29": "Goldman Sachs",
        "30": "Visa",
        "31": "Merck",
        "32": "Goldman Sachs",
        "33": "Verizon",
        "34": "Anheuser-Busch InBev",
        "35": "BMW",
        "36": "Porsche",
        "37": "Ferrari",
        "38": "Lamborghini",
        "39": "Audi",
        "40": "Inditex",
        "41": "Total",
        "42": "Sanofi",
        "43": "L'Oreal",
        "44": "AXA",
        "45": "Voestalpine",
        "46": "√ñsterreichische Post",
        "47": "OMV",
        "48": "Raiffeisen Bank International",
        "49": "Volkswagen",
        "50": "Daimler",
        "51": "Siemens",
        "52": "Allianz",
        "53": "BASF",
        "54": "Deutsche Bank",
        "55": "EON",
        "56": "Linde",
        "57": "DHL",
        "58": "Deutsche Telekom",
        "59": "SAP",
        "60": "Henkel",
        "61": "Bosch",
        "62": "Continental",
        "63": "Deutsche Post",
        "64": "Bayer",
        "65": "Metro",
        "66": "Beiersdorf",
        "67": "Adidas",
        "68": "Nivea",
        "69": "Sony",
        "70": "Honda",
        "71": "Nintendo",
        "72": "Canon",
        "73": "Panasonic",
        "74": "Fujifilm",
        "75": "Mitsubishi",
        "76": "NEC",
        "77": "Sharp",
        "78": "Toshiba",
        "79": "Tencent",
        "80": "China Mobile",
        "81": "China Petroleum",
        "82": "China State Grid",
        "83": "China Railway",
        "84": "Gazprom",
        "85": "Rosneft",
        "86": "Sberbank",
        "87": "Lukoil",
        "88": "Novatek",
        "89": "Belaruskali",
        "90": "Naftogaz",
        "91": "PKN Orlen",
        "92": "KGHM",
        "93": "Ukrtelecom",
        "94": "Valeo",
        "95": "MTS",
        "96": "Nordea Bank",
        "97": "Roshen",
        "98": "PZU",
        "99": "PGE",
        "100": "Ukrainian Railways",
        "101": "Agromet",
        "102": "Kredyt Bank",
        "103": "Budimex",
        "104": "Sinopec",
        "105": "Industrial and Commercial Bank of China",
        "106": "China National Petroleum",
        "107": "China CITIC Bank",
        "108": "Agricultural Bank of China",
        "109": "China Life Insurance",
        "110": "China Construction Bank",
        "111": "China Development Bank",
        "112": "Ping An Insurance",
        "113": "Bank of China",
        "114": "HSBC",
        "115": "BP",
        "116": "Royal Dutch Shell",
        "117": "Tesco",
        "118": "Unilever",
        "119": "Vodafone",
        "120": "GlaxoSmithKline",
        "121": "AstraZeneca",
        "122": "British American Tobacco",
        "123": "BT Group",
        "124": "Rolls-Royce",
        "125": "British Airways",
        "126": "Lloyds Bank",
        "127": "Anglo American",
        "128": "Standard Chartered",
        "129": "GSK Consumer Healthcare",
        "130": "Royal Bank of Scotland",
        "131": "Aviva",
        "132": "Diageo",
        "133": "Legal & General",
        "134": "National Grid",
        "135": "Prudential",
        "136": "Tesco Bank",
        "137": "Standard Life",
        "138": "Avon Products",
        "139": "BHP",
        "140": "Commonwealth Bank of Australia",
        "141": "National Australia Bank",
        "142": "ANZ",
        "143": "Westpac",
        "144": "Rio Tinto",
        "145": "Telstra",
        "146": "Qantas",
        "147": "Woodside Petroleum",
        "148": "Wesfarmers",
        "149": "Woolworths",
        "150": "Boral",
        "151": "AMP",
        "152": "Wesfert",
        "153": "IAG",
        "154": "OTP Bank",
        "155": "Magyar Telekom",
        "156": "Mol Group",
        "157": "Erste Bank",
        "158": "Magyar Posta",
        "159": "Lietuvos Energija",
        "160": "Danske Bank",
        "161": "Ericsson",
        "162": "H&M",
        "163": "Volvo",
        "164": "IKEA",
        "165": "Nordea Bank",
        "166": "Telia Eesti",
        "167": "Swedbank",
        "168": "SEB Bank",
        "169": "Danske Bank",
        "170": "Eesti Energia",
        "171": "Banco Santander",
        "172": "Telef√≥nica",
        "173": "Repsol",
        "174": "Mapfre",
        "175": "Iberdrola",
        "176": "Ferrovial",
        "177": "Banco Sabadell",
        "178": "ACS",
        "179": "FerroAtl√°ntica",
        "180": "Banco Popular",
        "181": "Banco de Valencia",
        "182": "Banco Bilbao Vizcaya Argentaria (BBVA)",
        "183": "Petrobras",
        "184": "Banco do Brasil",
        "185": "Vale",
        "186": "Ita√∫ Unibanco",
        "187": "Banco Bradesco",
        "188": "Samsung",
        "189": "Hyundai",
        "190": "LG",
        "191": "Kia",
        "192": "SK Group",
        "193": "Posco",
        "194": "Hyundai Heavy Industries",
        "195": "Lotte Group",
        "196": "CJ Group",
        "197": "Hanwha Group",
        "198": "MTN Group",
        "199": "Naspers",
        "200": "FirstRand",
        "201": "Standard Bank Group",
        "202": "Sasol",
        "203": "Dangote Group",
        "204": "MTN Group",
        "205": "Cemex",
        "206": "Am√©rica M√≥vil",
        "207": "Femsa",
        "208": "Grupo Bimbo",
        "209": "Petr√≥leos de M√©xico",
        "210": "Rimi Baltic",
        "211": "Latvijas GƒÅze",
        "212": "Dienas Bizness",
        "213": "CME",
        "214": "Skoda",
        "215": "Cencosud",
        "216": "CEZ Group",
        "217": "LAN Airlines",
        "218": "Fonterra",
        "219": "Air New Zealand",
        "220": "TelstraClear",
        "221": "Vector",
        "222": "Carrefour",
        "223": "Danone",
        "224": "Pernod Ricard",
        "225": "Statoil",
        "226": "Telenor",
        "227": "DNV GL",
        "228": "Kongsberg",
        "229": "Yara",
        "230": "Elisa",
        "231": "Nokia",
        "232": "Fortum",
        "233": "Stora Enso",
        "234": "Reykjavik Energy",
        "235": "Bombardier Inc.",
        "236": "LinkedIn",
        "237": "GameStop",
        "238": "PandaDoc",
        "239": "Wargaming",
        "240": "EPAM Systems",
        "241": "Starbucks",
        "242": "J.M. Smucker Company",
        "243": "Dunkin' Brands Group",
        "244": "Peet's Coffee",
        "245": "Keurig Dr Pepper",
        "246": "Costa Coffee",
        "247": "Tim Horton's",
        "248": "Caribou Coffee",
        "249": "The Kraft Heinz Company",
        "250": "Louis Vuitton",
        "251": "Gucci",
        "252": "Prada",
        "253": "Ralph Lauren",
        "254": "Tommy Hilfiger",
        "255": "Calvin Klein",
        "256": "Chanel",
        "257": "Giorgio Armani",
        "258": "Christian Dior",
        "259": "Versace",
        "260": "Hill's Pet Nutrition",
        "261": "Purina",
        "262": "Royal Canin",
        "263": "Blue Buffalo",
        "264": "Shiseido",
        "265": "Kao Corporation",
        "266": "Singapore Telecommunications Limited (SingTel)",
        "267": "DBS Bank",
        "268": "United Overseas Bank (UOB)",
        "269": "CapitaLand",
        "270": "Singapore Airlines",
        "271": "Keppel Corporation",
        "272": "SembCorp Industries",
        "273": "Singapore Press Holdings"
    }

}

>> Error Message : 400,500


Case1 :
{
    "error": null,
    "msg": "File Upload Error"
}

Case2:
{
    "msg": "File not contain Company Name as header/Title"
}



# Scraper Response:
--- Calling asyncio to run scrapper in aysnchronously.

 >> Request :
import requests

url = "https://proxy.scrapeops.io/v1/?api_key=Your-Api-key&url=https://www.linkedin.com/company/apple/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



# Async API call :

import requests

url = "http://localhost:5000/fetchcompanydetails"

payload={}
headers = {
  'Cookie': 'session=eyJ1cGxvYWRlZF9kYXRhX2ZpbGVfcGF0aCI6InN0YXRpY1xcdXBsb2Fkc1xccmF3X2JpZ2dlc3RfY29tcGFuaWVzLmNzdiJ9.ZJ5xRA.ynDC9d4-YK2lQzsYm81n_0oHo_M'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

> Responses : 
{
    "status": "Failed to get successful response from website. Please retry the request."
}


{
    "error": null,
    "msg": "Scraping Error"
}


{
    "companydetails": "{\"status\":\"Failed to get successful response from website. Please retry the request.\"}",

}

SCRAPEOPS_API_KEY = 'Your Account API Key'
url = "https://scrapeops.io/app/dashboard"

{
    "companydetails": "{\"Error\":\"The API key you sent with the request is invalid. Please include a valid API key.\"}",