from flask import Flask, render_template, request, session,jsonify
import pandas as pd
import os
import traceback
from werkzeug.utils import secure_filename
import asyncio
import aiohttp
import json


#------------------------------------------------application Config Start ------------------------------------
#*** Flask configuration
 
# Define folder to save uploaded files to process further
UPLOAD_FOLDER = os.path.join('static', 'uploads')
 
# Define allowed files (for this example I want only csv file)
ALLOWED_EXTENSIONS = {'csv'}
 
app = Flask(__name__, template_folder='templates', static_folder='static')
# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
# Define secret key to enable session
app.secret_key = 'This is your secret key to utilize session in Flask'
SCRAPEOPS_API_KEY = 'Your Account API Key'
SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
}

#------------------------------------------------application Config End ------------------------------------
 
@app.route('/')
def index():
    return render_template('companyfileupload.html')
 
@app.route('/companyfileupload',  methods=("POST", "GET"))
def uploadFile():
    data=[]
    uploaded_df_html = {}
    
    if request.method == 'POST':
        try : 
            # upload file flask
            uploaded_df = request.files['uploaded-file']
    
            # Extracting uploaded data file name
            data_filename = secure_filename(uploaded_df.filename)
            print("data_filename--------------",data_filename)
    
            # flask upload file to  defined uploaded folder in static path
            uploaded_df.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
    
            # Storing uploaded file path in flask session
            session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
            # Retrieving uploaded file path from session
            data_file_path = session.get('uploaded_data_file_path', None)
        
            # read csv file in python flask (reading uploaded csv file from uploaded server location)
            uploaded_df = pd.read_csv(data_file_path, engine='python')

            # print(uploaded_df.columns.tolist())

            if "Company Name" in uploaded_df.columns.tolist() or "Company" in uploaded_df.columns.tolist():
                # pandas dataframe to html table flask
                uploaded_df_html = uploaded_df.to_json()
                companydetails = fetchcompanydetails()
                uploaded_df_html = { "companydetails":companydetails,"companynamedata":uploaded_df_html}
            else:
                uploaded_df_html = {"msg":"File not contain Company Name as header/Title"}
        except Exception as e:
            uploaded_df_html = {"error":traceback.print_exc(),"msg":"File Upload Error"}
        return uploaded_df_html
    else:
        return jsonify(data=uploaded_df_html)
 
@app.route('/show_data')
def showData():
    # Retrieving uploaded file path from session
    data_file_path = session.get('uploaded_data_file_path', None)
 
    # read csv file in python flask (reading uploaded csv file from uploaded server location)
    uploaded_df = pd.read_csv(data_file_path)
 
    # pandas dataframe to html table flask
    uploaded_df_html = uploaded_df.to_html()
    # parseCSV(uploaded_df)
    return render_template('show_csv_data.html', data_var = uploaded_df_html)
 

@app.route('/fetchcompanydetails',  methods=("POST", "GET"))
def fetchcompanydetails():
    scraperresponselist = []
    scraperurlslist = []
    try:
        # Retrieving uploaded file path from session
        data_file_path = session.get('uploaded_data_file_path', None)
        if data_file_path:
            # read csv file in python flask (reading uploaded csv file from uploaded server location)
            uploaded_df = pd.read_csv(data_file_path, engine='python')

            # print(uploaded_df.columns.tolist())

            if "Company Name" in uploaded_df.columns.tolist() :
                # pandas dataframe to html table flask
                uploaded_df_html = uploaded_df.to_json()
                companyjsondata = json.loads(uploaded_df_html)
                companynamelist = companyjsondata["Company Name"]
            elif "Company" in uploaded_df.columns.tolist() :
                companyjsondata = json.dumps(uploaded_df_html)
                companynamelist = companyjsondata["Company"]
            else:
                companynamelist = []
            if companynamelist:
                scraperurlslist = []
                url = ""
                for companyname in companynamelist:
                    if companynamelist[companyname]:
                        companynameforscrap = companynamelist[companyname]
                        url = "https://proxy.scrapeops.io/v1/?api_key={0}&url=https://www.linkedin.com/company/{1}/".format(SCRAPEOPS_API_KEY,str(companynameforscrap))
                        scraperurlslist.append(url)
                # print("scraperurlslist-------------",scraperurlslist)
                try:
                    loop = asyncio.get_event_loop()
                except RuntimeError as e:
                    if str(e).startswith('There is no current event loop in thread'):
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                    else:
                        raise
                scraperresponselist = loop.run_until_complete(get_companydetails(scraperurlslist))
                return scraperresponselist
        else:
            return {"msg": "Company data Not Found to Scrap"}

    except Exception as e:
        pass 
        return {"error":traceback.print_exc(),"msg":"Scraping Error"}


def datascraper(companyname):
    import requests
    url = "https://proxy.scrapeops.io/v1/?api_key={0}&url=https://www.linkedin.com/company/{1}/".format(SCRAPEOPS_API_KEY,companyname.strip)
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text()

        
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_companydetails(urls):
    try:
        async with aiohttp.ClientSession() as session:
            for url in urls:
                html = await fetch(session, url)
                return html
    except RuntimeError as e:
        pass
        return {"msg":"error while async call"}





if __name__=='__main__':
    app.run(debug = False)