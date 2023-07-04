TARGET_PATH_GROWTH_RATE = 0.05
BASE_YR = 2007
BASE_QTR = 4
BASE_NGDP = 14715.1
BASE_PRICE = 1

DEFAULT_YQ = '2023q2'
DEFAULT_NGDP = '23320'
DEFAULT_XCHUSD = '35'

def input_default(prompt, default):
    data = input(prompt + f' (default {default})> ')
    data = default if data == '' else data
    return data

curqtr = input_default("Enter quarter (as yyyyqq) for which to calculate", DEFAULT_YQ)
ngdp = float(input_default("Enter actual or assumed NGDP in 10^9 USD", DEFAULT_NGDP))
xchusd = float(input_default("Enter dollar price for 1 XCH", DEFAULT_XCHUSD))

year = int(curqtr[:4])
qtr = int(curqtr[-1])
print(f'Calculating for year {year}, quarter {qtr} ')
base_yr = BASE_YR
base_qtr = BASE_QTR
diff_yrs = year - base_yr + (qtr - base_qtr) / 4

target_ngdp = BASE_NGDP * (1 + TARGET_PATH_GROWTH_RATE) ** diff_yrs
usd_price = BASE_PRICE * ngdp / target_ngdp

xch_price = usd_price / xchusd
print(f'\nTarget price of NGDPLT token is  XCH{xch_price: .4}')
