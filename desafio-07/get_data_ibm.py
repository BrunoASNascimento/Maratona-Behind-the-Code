from cloudant import Cloudant
from dotenv import load_dotenv
import os
import pandas as pd
from pandas.io.json import json_normalize

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

client = Cloudant(USER, PASSWORD, account=USER, connect=True, auto_renew=True)
db = client['tnt']

response = db.all_docs(include_docs=True)  # Add limit=10 if necessary

data = [doc['doc'] for doc in response['rows']]
columns = ['Tempo', 'Estação', 'LAT', 'LONG', 'Movimentação', 'Original_473', 'Original_269',
           'Zero', 'Maçã-Verde', 'Tangerina', 'Citrus', 'Açaí-Guaraná', 'Pêssego', 'TARGET']

df_init = pd.DataFrame(data)


df_init[columns].to_csv('desafio-07/data/data-set.csv', index=False)
print(df_init[columns].head())

df = pd.read_csv('desafio-07/data/data-set.csv')
print(df.info())
