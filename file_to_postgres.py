#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:22:50 2024

@author: celalberkeakyol
"""

from sqlalchemy import create_engine
import pandas as pd

# PostgreSQL bağlantı bilgileri
username = 'celalberkeakyol'
password = 'CeBer32.AS'
host = 'localhost'  # Sunucu adresi (örneğin: localhost veya bir IP)
port = '5432'       # PostgreSQL varsayılan portu
database = 'finance'

# SQLAlchemy engine oluştur
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')


# Long format dosyasını yükle
#long_file_path = '/Users/celalberkeakyol/Desktop/Data_Deneme/combined_long_format2.xlsx'
#long_data = pd.read_excel(long_file_path)

# Veriyi PostgreSQL'e ekle
#long_data.to_sql('long_format_table', engine, if_exists='replace', index=False)

#print("Long formatlı veri başarıyla PostgreSQL'e eklendi.")


# Wide format dosyasını yükle
wide_file_path = '/Users/celalberkeakyol/Desktop/Data_Deneme/combined_wide_format.xlsx'
wide_data = pd.read_excel(wide_file_path)

pd.set_option('display.max_columns', None)



print(wide_data.columns)



# Veriyi PostgreSQL'e ekle
#wide_data.to_sql('wide_format_table', engine, if_exists='replace', index=False)

#print("Wide formatlı veri başarıyla PostgreSQL'e eklendi.")
