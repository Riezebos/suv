# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import requests
import pandas as pd
import plotly.express as px
import plotly.io as pio

# %%
url = """https://opendata.rdw.nl/api/id/m9d7-ebf2.json?$query=
SELECT 
    merk,
    handelsbenaming,
    COUNT(*) AS aantal
WHERE 
datum_eerste_toelating > '20100101'
AND datum_eerste_toelating < '20100201'
AND voertuigsoort = 'Personenauto'
GROUP BY merk, handelsbenaming
ORDER BY aantal DESC
"""
res = requests.get(url).json()
df = pd.DataFrame(data=res)
df.head(50)

# %%
url = """https://opendata.rdw.nl/api/id/m9d7-ebf2.json?$query=
SELECT 
    merk,
    handelsbenaming,
    COUNT(*) AS aantal
WHERE 
datum_eerste_toelating > '20100101'
AND datum_eerste_toelating < '20100201'
AND voertuigsoort = 'Personenauto'
AND bruto_bpm > '5000'
AND massa_rijklaar > '2000'
AND aantal_zitplaatsen between '3' and '8'
AND (inrichting = 'stationwagen' OR inrichting = 'MPV')
GROUP BY merk, handelsbenaming
ORDER BY aantal DESC
"""
res = requests.get(url).json()
df = pd.DataFrame(data=res)
df.head(40)

# %%
url = """https://opendata.rdw.nl/api/id/m9d7-ebf2.json?$query=
SELECT 
    floor(datum_eerste_toelating/100) AS datum,
    AVG(CASE(
        bruto_bpm > '5000' 
        AND massa_rijklaar > '2000'
        AND aantal_zitplaatsen between '3' and '8'
        AND (inrichting = 'stationwagen' OR inrichting = 'MPV')
        ,100
        ,true
        ,0
    )) as suv_share
WHERE 
datum_eerste_toelating > '20100101'
AND voertuigsoort = 'Personenauto'
GROUP BY datum
"""
res = requests.get(url).json()
df = pd.DataFrame(data=res)
df.head()
df.datum.min()
df.datum.max()

# %%
df.datum = pd.to_datetime(df.datum, format="%Y%m")
px.line(df, x="datum", y="suv_share", template="plotly_white")
