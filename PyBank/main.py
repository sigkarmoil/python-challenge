import pandas as pd
pd.options.display.float_format = '{:.2f}%'.format

df = pd.read_csv(r'C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv')
print(df.head() )



unq_date = df["Date"].count()
print(f"total number of months are:  {unq_date}")

PnL = df["Profit/Losses"].sum()
print(f"Total profit / losses are: {PnL}")

delta = df["Profit/Losses"].pct_change()
avg_delta = (delta.mean())
avg_delta_per= format(avg_delta, ".2%")
print(f"Average changes are: {avg_delta_per}")

max_delta = (delta.max() )
max_delta_per = format( max_delta, ".2%" )
print(f"Max profit changes are: {max_delta_per}")

min_delta = (delta.min() )
min_delta_per = format(min_delta, ".2%")
print(f"Min profit changes are: {min_delta_per}")

#df.to_csv(r'C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyBank\analysis\PyBank.csv', index = False)