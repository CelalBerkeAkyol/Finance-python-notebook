# Veri düzenleme notları 
### neden böyle bir repo var bu nedir ? 
Elimdeki verilerin tutarlılığını kontrol etmek için bir çalışma yapmam gerekti. 
Bunun başlangıcında finansal verilerin olduğu bir veri tabanı yapmak isterken hangi formatı seçmemm gerektiğine karar vermekle başladı. Önümde iki seçenek vardı
- wide format
- long format

### long format vs wide format 
long format 5 - 10 sütun 120 bin satırdan oluşan bir format 
wide format 350 sütun 30 bin satırdan oluşan bir format oldu 
ikisinin avantajı ve dez avantajı var . 
Long formatta veriler çok fazla tekrara düşüyor fakat column az olması hızlandırıyormuş 
wide formatta ise daha az tekrar sonucu çok daha az dosya boyutu fazla column var 

### Wide formatta yaşanan sıkıntı 
Yeni veriler geldiğinde veya bir column adı tekrara düşütğünde hata veriyordu bunu çözmek için bir çalışma yaparken bu dosyalar ortaya çıktı 
Şimdilik long format ile veri tabanı oluşturdum ilerleyen zamanlarda json formatında apiden veriler alınacağı için bu çalışma askıda 
