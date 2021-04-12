import numpy as np
import pandas as pd

# O pandas tem uma funcionalidade simples, poderosa e eficiente para realizar operações de reamostragem
# durante a conversão de frequência (por exemplo, converter dados secundários em dados de 5 minutos).
# Isso é extremamente comum, mas não se limita a aplicativos financeiros. Consulte a seção Séries Temporais .

rng = pd.date_range('1/1/2012', periods=100, freq='S')

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

print(rng)
print(ts.resample('5min').sum())

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)

print(ts)

# Representação de fuso horário:
ts_utc = ts.tz_localize("UTC")

print(ts_utc)