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
from requests.utils import requote_uri, unquote
import pandas as pd
import plotly.express as px
import plotly.io as pio

# %%
unquote("https://opendata.rdw.nl/api/id/m9d7-ebf2.json?$query=SELECT%20`datum_eerste_toelating`/100%20AS%20__dimension_alias__%2C%20COUNT(*)%20AS%20__measure_alias__%20WHERE%20(`voertuigsoort`%20%3D%20%27Personenauto%27)%20AND%20((`bruto_bpm`%20%3E%20%275000%27)%20AND%20`bruto_bpm`%20IS%20NOT%20NULL)%20AND%20((`massa_rijklaar`%20%3E%20%272000%27)%20OR%20`massa_rijklaar`%20IS%20NULL)%20AND%20((`aantal_zitplaatsen`%20%3E%20%273%27%20AND%20`aantal_zitplaatsen`%20%3C%20%278%27)%20AND%20`aantal_zitplaatsen`%20IS%20NOT%20NULL)%20AND%20(`inrichting`%20%3D%20%27stationwagen%27%20OR%20`inrichting`%20%3D%20%27MPV%27)%20AND%20((`vervaldatum_apk`%20%3E%20%2720200427%27)%20OR%20`vervaldatum_apk`%20IS%20NULL)%20GROUP%20BY%20`datum_eerste_toelating`/100%20ORDER%20BY%20__dimension_alias__%20DESC%20NULL%20LAST%20LIMIT%201001&$$read_from_nbe=true&$$version=2.1")

# %%
url = """https://opendata.rdw.nl/api/id/m9d7-ebf2.json?$query=
SELECT 
    floor(`datum_eerste_toelating`/100) AS datum,
    COUNT(*) AS aantal 
WHERE 
(`voertuigsoort` = 'Personenauto') 
AND (`bruto_bpm` > '5000') 
AND (`massa_rijklaar` > '2000') 
AND (`aantal_zitplaatsen` between '3' and '8') 
AND (`inrichting` = 'stationwagen' OR `inrichting` = 'MPV') 
AND (`datum_eerste_toelating` > '20100101') 
GROUP BY datum 
ORDER BY datum ASC NULL LAST LIMIT 10000&$$read_from_nbe=true&$$version=2.1"""
res = requests.get(url).json()
df = pd.DataFrame(data=res)
df.head()

# %%
df.datum = pd.to_datetime(df.datum,format="%Y%m")

# %%
fig = px.line(df,x="datum",y='aantal',template='plotly_white')

# %%
pio.write_html(fig,"test.html",include_plotlyjs='cdn')

# %%
fig

# %%
