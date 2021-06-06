import yfinance as yf
for name in ['SMH', 'QQQ', 'SPY', 'DIA']:
    print("downloading ", name)
    df = yf.download(name, progress=True)
    df.head()
    df.to_csv(name + '.csv')
