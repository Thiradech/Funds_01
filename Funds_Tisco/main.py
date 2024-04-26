from util.sec_data_manipulated import get_funds_under_amc, pd, urllib, json
import util.datetime_util as du
from datetime import datetime, timedelta

#load funds_info from sec and save to csv file
funds_active_path = "/workspace/test_0/Funds_01/Funds_Tisco/data/funds_still_active"
get_funds_under_amc(to_csv=True, path=funds_active_path)

#
end_date = du.get_last_working_day()
start_date =  end_date - timedelta(days=365*5) #5 year ago

du.get_weekdays(start_date=start_date, end_date=end_date)

