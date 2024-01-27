TARGET_PATH_GROWTH_RATE = 0.05
BASE_YR = 2007
BASE_QTR = 4
BASE_NGDP = 14715.1
BASE_PRICE = 1

DEFAULT_YQ = '2023q4'
DEFAULT_NGDP = '27938.8'
DEFAULT_XCHUSD = '29.64'
DEFAULT_NMONTHS = '0'
#DEFAULT_DISCRATE = '5.0'
DEFAULT_GROWTH = '5.0'
DEFAULT_PREVIOUS = 'n'

def input_default(prompt, default):
    data = input(prompt + f' (default {default})> ')
    data = default if data == '' else data
    return data

curqtr = input_default("Enter quarter (as yyyyqq) for which to calculate", DEFAULT_YQ)
ngdp = float(input_default("Enter actual or assumed NGDP in 10^9 USD", DEFAULT_NGDP))

yesno = 'maybe'
while yesno not in ('y', 'n'):
    yesno = input_default("Is this for NGDP value for previous report(y/n)?", 
                          DEFAULT_PREVIOUS)
if (yesno == 'y'):
    growth = float(input_default("Enter assumed annualized growth rate over quarter", 
                                 DEFAULT_GROWTH)) / 100
     # Commented out this line.
     # We should be using actual NGDP right now, 
     #   not the expected NGDP when the report is released
     # If you use the latter and discount it by the interest rate
     #   there will be an expected discontinuity in price 
     #   at the time of the report unless r=g
#    ngdp = ngdp * (1 + growth) ** 0.25
else:
    growth = 0
                                
timelag = float(input_default("Enter number of months until advance GDP report",
                              DEFAULT_NMONTHS)) / 12
xchusd = float(input_default("Enter dollar price for 1 XCH", DEFAULT_XCHUSD))
# Don't need interest rate, because we should not discount
#r = float(input_default("Enter interest rate in percent",
#                        DEFAULT_DISCRATE)) / 100

year = int(curqtr[:4])
qtr = int(curqtr[-1])
print(f'Calculating for year {year}, quarter {qtr} ')
base_yr = BASE_YR
base_qtr = BASE_QTR
diff_yrs = year - base_yr + (qtr - base_qtr) / 4

ngdp = ngdp * (1 + growth) ** timelag
target_ngdp = BASE_NGDP * (1 + TARGET_PATH_GROWTH_RATE) ** diff_yrs
# Commented out (changed) this line: we should not be discounting,
#   otherwise there will be an expected price discontinuity
#   at the time of the report when growth and interest rates differ
#usd_price = (BASE_PRICE * ngdp / target_ngdp) / (1 + r) ** timelag
usd_price = (BASE_PRICE * ngdp / target_ngdp)
inv_usd_price = 2 - usd_price

xch_price = usd_price / xchusd
inv_xch_price = inv_usd_price / xchusd
print(f'\nTarget price of NGDPLT token is  XCH{xch_price: .4}')
print(f'Target price of INGDP token is  XCH{inv_xch_price: .4}')
