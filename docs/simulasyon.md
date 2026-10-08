# Wokwi ile çalışma

Ana çalışma ortamı Wokwi. Kurulum yolu: [KURULUM.md](../KURULUM.md). Kontrol tarihi: 9 Ekim 2026.

## Ücretsiz kullanım

Public tarayıcı projeleri Community planındadır. VS Code, fiyat tablosunda Hobby+ kapsamında listeleniyor. Ücretsiz deneme veya hesabındaki ayrı lisans koşullarını kontrol etmeden sürekli ücretsiz VS Code sözü vermiyoruz. Önce resmî tarayıcı HAL örneğiyle LED deneyi yap.

## MCU desteği

Blue Pill F103 için GPIO, USART, I²C, SPI ve timer desteği listelenir. ADC1 temel dönüşümü kısmen desteklidir. DMA, IWDG, RTC ve PWR desteklenmez. Timer'ın listede bulunması encoder ve input capture modlarının doğrulandığı anlamına gelmez. CAN desteği listelenmiyor.

C031/L031 HAL örneğiyle başlarsan F103 pin/clock ayarlarını kullanma. Kullandığın modeli her rapora yaz. `diagram.json` kartını değiştirmek, başka MCU için derlenmiş firmware'i taşımaya yetmez.

## Motor ve encoder yolumuz

1. 060 sonrasında 069 model görevine geç.
2. Önce motor fiziği olmadan A/B darbe üreteci yaz.
3. İleri sıra: 00, 01, 11, 10. Ters yönde sıra ters çevrilir. A/B etiketlerine göre pozitif yönü tanımla.
4. Darbe sayısı ve yönü logic analyzer ile kontrol et.
5. STM32 timer encoder girişinde sayım deneyi yap.
6. Timer encoder modu desteklenmiyorsa EXTI tabanlı yazılımsal sayıcı kur. Bunun donanım encoder modu testi olmadığını raporla.
7. Darbe üreticisine PWM/yön girdili birinci dereceden motor modeli ekle.
8. 061–075 kontrol uygulamalarına model üzerinden devam et.

Modeli Custom Chips API ile ayrı parça olarak kodlamayı hedefliyoruz. Model ve timer bağlantısı henüz denenmedi. Paket hazır çalışır custom chip içermez.

Örnek doğrulama: 400 sayım/tur varsayımında 1 saniyede 400 sayım 60 RPM'dir. PPR ile x4 sonrası sayımı karıştırma. Hız yükselince bir model adımında birden çok kenar gerekebilir. Kesirli konum birikimini koru, kenarları zamanlayarak üret ve desteklenen azami hızı raporla.

## Eksik çevre birimleri

- DMA ve CAN görevlerinin donanım ölçütleri Wokwi'de tamamlandı sayılmaz.
- Yazılım modeli veya UART alternatifi ayrı sonuçtur.
- Destek engelini issue içinde açık tut. Diğer görevleri gereken algoritma önkoşulları sağlandığında sürdür.
- Finalin ilk sürümü UART, IMU/kayıt ve sanal motorla `v1.0-sim` olur. Gerçek CAN ve fiziksel motor testleri ayrı doğrulama olarak kalır.
- Gerçek sensör gürültüsü için kayıt veya tanımlı sentetik gürültü kullan. Elle girilen sabit MPU6050 değerleri fiziksel sensör testi değildir.

## Kaynaklar

- https://wokwi.com/pricing
- https://docs.wokwi.com/parts/board-stm32-bluepill
- https://docs.wokwi.com/vscode/getting-started
- https://docs.wokwi.com/chips-api/getting-started
