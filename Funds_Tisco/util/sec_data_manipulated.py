import pandas as pd
import urllib.request, json



def get_all_amc_df():
    try:
        url = "https://api.sec.or.th/FundFactsheet/fund/amc"

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': '98fb5b95961741beba453e85fd95bae9',
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        print(response.getcode())
        all_am = json.loads(response.read())
    except Exception as e:
        print(e)
    
    all_am_df = pd.DataFrame(all_am).sort_values(by=pd.DataFrame(all_am).columns[0]) #sort by amc_id
    watchlist_amc = [0, 1, 3, 4, 6, 8, 9, 10, 11, 15, 17]
    all_am_df_final = all_am_df.iloc[watchlist_amc]
    all_am_df_final['short_name'] = ['KASSET', 'MFC', 'TMB', 'SCBAM', 'TISCOAM', 'KTAM', 'ONEAM',
                                 'UOBAM', 'KSAM', 'ASP', 'PRINCIPAL']
    all_am_df_final = all_am_df_final[['unique_id', 'short_name', 'name_th', 'name_en', 'last_upd_date']]
    
    return all_am_df_final

def get_all_unique_id(df):
    return list(df['unique_id'])

def get_funds_under_amc(amc_shortname='all', to_csv=False, path="data/funds_still_active"): 
    
    list_pair_unique_id = [('KASSET','C0000000021'), ('MFC','C0000000023'), ('TMB','C0000000182'), ('SCBAM','C0000000239')
                        , ('TISCOAM','C0000000324'), ('KTAM','C0000000460'), ('ONEAM','C0000000569')
                        , ('UOBAM','C0000000623'), ('KSAM','C0000000709'), ('ASP','C0000005022')
                        , ('PRINCIPAL','C0000005531')]
    try:
        all_funds_still_active = pd.DataFrame()
        for amc_short, id in list_pair_unique_id:
            url = f"https://api.sec.or.th/FundFactsheet/fund/amc/{id}"
            hdr ={
            # Request headers
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': '98fb5b95961741beba453e85fd95bae9',
            }

            req = urllib.request.Request(url, headers=hdr)

            req.get_method = lambda: 'GET'
            response = urllib.request.urlopen(req)
            print(response.getcode())
            funds_under_amc = json.loads(response.read())
            funds_still_active = []
            for fund in funds_under_amc:
                if fund['fund_status'] == 'RG':
                    funds_still_active.append(fund)
            df = pd.DataFrame(funds_still_active)
            df['short_name'] = amc_short
            all_funds_still_active = pd.concat([all_funds_still_active, df])
            funds_still_active = []
        
        if to_csv:
            print('saving_to_csv...')
            file_path = f'{path}/all_funds_still_active.csv'
            all_funds_still_active.to_csv(file_path, index=False)
            
        return all_funds_still_active
    
    except Exception as e:
        print(e)

def get_details_of_funds(ticker='all', to_csv=False):
    try:
        all_proj_id = list(pd.read_csv('data/funds_still_active/all_funds_still_active.csv').iloc[:,0])
        for id in all_proj_id: 
            url = f"https://api.sec.or.th/FundFactsheet/fund/{id}/policy"

            hdr ={
            # Request headers
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': '98fb5b95961741beba453e85fd95bae9',
            }

            req = urllib.request.Request(url, headers=hdr)

            req.get_method = lambda: 'GET'
            response = urllib.request.urlopen(req)
            print(response.getcode())
            policy = json.loads(response.read())
    except Exception as e:
        print(e)
    
    