#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import os

# Excel dosyalarının bulunduğu klasör yolu
folder_path = "/Users/celalberkeakyol/Desktop/Data_Deneme/geniş"

# Birleştirilmiş veriler için boş liste
combined_wide_format = []

# Tüm dosyaları tek tek okuyup birleştirme işlemi
for file_name in os.listdir(folder_path):
    if file_name.endswith(".xlsx"):  # Sadece Excel dosyalarını al
        file_path = os.path.join(folder_path, file_name)
        
        # Excel dosyasını oku
        excel_data = pd.read_excel(file_path)
        
        # Şirket ismini dosya adından çıkar
        company_name = os.path.splitext(file_name)[0]
        
        # Sütun isimlerini küçük harfe çevir ve boşlukları kaldır
        excel_data.columns = excel_data.columns.str.strip().str.lower()
        
        # Aynı isimdeki sütunları birleştir (groupby ile axis=1 kaldırıldı)
        excel_data = excel_data.T.groupby(level=0).sum().T
        
        # "Company" sütununu tek seferde eklemek için pd.concat kullanımı
        company_column = pd.DataFrame({"Company": company_name}, index=excel_data.index)
        excel_data = pd.concat([company_column, excel_data], axis=1)
        
        # Listeye ekle
        combined_wide_format.append(excel_data)

# Tüm geniş formatlı tabloları birleştir
wide_format_df = pd.concat(combined_wide_format, ignore_index=True)

# Sonuçları kaydet
wide_format_df.to_excel("combined_wide_format.xlsx", index=False)

print("Dosyalar başarıyla birleştirildi, sütun isimleri temizlendi ve kaydedildi!")


