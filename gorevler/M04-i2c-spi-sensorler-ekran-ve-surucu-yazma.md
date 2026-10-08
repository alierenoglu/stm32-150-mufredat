<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M04 · I²C, SPI, Sensörler, Ekran ve Sürücü Yazma

Görevler 046–060 · [Tüm görevler](../GOREVLER.md)

I²C ve SPI ile sensör okuma, register haritası, kesme ve bloklamasız okuma, kendi sürücü katmanını yazma, OLED ekran ve bağlantı hatalarından kurtulma.

---

<a id="g046"></a>

## 046 · I²C hat tarama

`Ana görev` · Önkoşul: 045

**Amaç.** I²C hattındaki bütün adresleri dene ve cevap veren cihazları UART'tan listele.

**Araştır:** I²C adresleme (7 bit) · ACK/NACK · pull-up dirençleri · HAL_I2C_IsDeviceReady

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin) veya SSD1306 I²C OLED ekran (128×64); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Bağlı cihazların adresleri doğru listeleniyor; cihaz çıkarılınca listeden düşüyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g047"></a>

## 047 · Kimlik register'ı

`Ana görev` · Önkoşul: 046

**Amaç.** IMU'nun kimlik (WHO_AM_I) register'ını oku ve datasheet'teki beklenen değerle karşılaştır. Uyuşmazlık ya da iletişim hatasında anlaşılır bir hata mesajı ver.

**Araştır:** datasheet register haritası · HAL_I2C_Mem_Read

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Doğru değer okunuyor.
- Bağlantı yokken hata mesajı geliyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Wokwi'de MPU6050 kullan.

---

<a id="g048"></a>

## 048 · Register okuma-yazma katmanı

`Ana görev` · Önkoşul: 047

**Amaç.** I²C üzerinde read_reg, write_reg ve read_burst fonksiyonları yaz; her biri hata kodu döndürsün. Bir konfigürasyon register'ına yazıp geri okuyarak doğrula.

**Araştır:** hata kodu tasarımı · burst okuma · adres otomatik artırma

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Yaz-oku doğrulaması geçiyor.
- Hata kodları README'de listelenmiş.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g049"></a>

## 049 · SPI ile sensör

`Ana görev` · Önkoşul: 048

**Amaç.** Bir sensörü SPI ile bağla. Chip select'i yazılımla yönet, SPI modunu datasheet'e göre seç ve kimlik register'ını oku.

**Araştır:** SPI · CPOL / CPHA · chip select · okuma bitinin ayarlanması

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin)

**Başarı ölçütü**

- Kimlik doğru okunuyor.
- Yanlış SPI modunda neden okunamadığını açıklıyorsun.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de SPI'lı IMU yok; SPI'yi listedeki başka bir SPI parçasıyla ya da custom chip ile dene.

---

<a id="g050"></a>

## 050 · Eğim LED'leri

`Mini uygulama` · Önkoşul: 049

**Amaç.** İvmeölçerin X ve Y eksenlerini oku, datasheet ölçeğiyle g birimine çevir. Kart hangi yöne eğilirse o yöndeki LED, eğimle orantılı parlaklıkta yansın.

**Araştır:** ham veri → g dönüşümü · ölçek katsayısı · işaretli 16 bit veri

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Düz dururken z ≈ 1 g, x ve y ≈ 0.
- Dört yön doğru LED'i yakıyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Wokwi'de MPU6050'nin değerlerini elle değiştirerek dene.

---

<a id="g051"></a>

## 051 · Sensör konfigürasyonu

`Ana görev` · Önkoşul: 050

**Amaç.** Sensörün çıkış veri hızını (ODR), ölçüm aralığını ve dahili filtresini register'lardan ayarla. Farklı ayarların veriye etkisini kaydet.

**Araştır:** ODR · ölçüm aralığı ve çözünürlük · dahili alçak geçiren filtre

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- İki farklı ölçüm aralığında aynı eğimin ham değerlerinin neden farklı olduğunu gösteriyorsun.

**Simülasyon:** ❔ Wokwi desteği belirsiz, dene. Wokwi dokümanı MPU6050'de hangi ayar register'larının simüle edildiğini yazmıyor.

---

<a id="g052"></a>

## 052 · Data-ready kesmesi

`Ana görev` · Önkoşul: 051

**Amaç.** Sensörün kesme (INT) pinini EXTI'ye bağla; her yeni veri hazır olduğunda oku.

**Araştır:** data-ready interrupt · kesme pini konfigürasyonu · latch / pulse modu

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin)

**Başarı ölçütü**

- Okuma sayısı sensörün ODR'si ile birebir uyuşuyor.

**Simülasyon:** ❔ Wokwi desteği belirsiz, dene. Wokwi'deki MPU6050'nin INT pininin çalışıp çalışmadığı dokümanda yazmıyor.

---

<a id="g053"></a>

## 053 · Bloklamasız sensör okuma

`Ana görev` · Önkoşul: 052

**Amaç.** Sensör okumasını kesme ya da DMA tabanlı I²C/SPI ile yap; okuma sürerken ana döngü çalışmaya devam etsin.

**Araştır:** HAL_I2C_Mem_Read_IT / _DMA · callback zinciri

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin)

**Başarı ölçütü**

- Okuma sırasında ana döngünün takılmadığı ölçümle gösterilmiş.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de kesmeli sürümü yap; DMA'lı sürüm gerçek kartta.

---

<a id="g054"></a>

## 054 · Bus'tan bağımsız sürücü

`Ana görev` · Önkoşul: 053

**Amaç.** Sensör sürücünü (başlatma, konfigürasyon, okuma) I²C ve SPI'yı aynı arayüzle kullanabilecek şekilde düzenle. HAL çağrıları tek bir port dosyasında kalsın.

**Araştır:** sürücü katmanları · fonksiyon işaretçisi · port/HAL soyutlaması

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin)

**Başarı ölçütü**

- Bus değiştirmek için yalnızca başlatma satırı değişiyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g055"></a>

## 055 · Veri kaydedici

`Mini uygulama` · Önkoşul: 054

**Amaç.** Sensörü sabit örnekleme hızında oku, zaman damgasıyla paketleyip gönder; Python 1 dakikalık kaydı CSV'ye yazıp grafiğini çizsin.

**Araştır:** sabit örnekleme · zaman damgası · veri kaydı

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Zaman damgaları arasındaki fark sabit.
- Kayıp örnek sayısı raporlanıyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Simülasyondaki UART'ı bilgisayardaki Python'a bağlamak için wokwi.toml'a rfc2217ServerPort ekle.

---

<a id="g056"></a>

## 056 · OLED ekran sürücüsü

`Ana görev` · Önkoşul: 055

**Amaç.** SSD1306 OLED için kendi minimal sürücünü yaz: başlatma, çerçeve tamponu, piksel, çizgi ve metin.

**Araştır:** SSD1306 komut seti · frame buffer · font tablosu

**Gerekenler:** STM32 geliştirme kartı; SSD1306 I²C OLED ekran (128×64)

**Başarı ölçütü**

- Ekranda metin ve çizgi doğru konumda.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g057"></a>

## 057 · Ekranda canlı veri

`Ana görev` · Önkoşul: 056

**Amaç.** Sensör değerlerini sayısal olarak ve kayan çizgi grafik olarak ekranda göster.

**Araştır:** ekran tazeleme hızı · kayan grafik

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); SSD1306 I²C OLED ekran (128×64)

**Başarı ölçütü**

- Ekran en az 10 Hz'de güncelleniyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g058"></a>

## 058 · DMA ile ekran güncelleme

`Ana görev` · Önkoşul: 057

**Amaç.** Ekran tamponunu DMA ile gönder; aktarım sürerken sensör okuma işleri aksamasın. Güncelleme süresini önce ve sonra ölç.

**Araştır:** I²C DMA · çift tampon

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); SSD1306 I²C OLED ekran (128×64)

**Başarı ölçütü**

- Ana döngü süresindeki iyileşme ölçülmüş.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DMA yok; kesmeli gönderimle dene, DMA'lı sürümü gerçek kartta yap.

---

<a id="g059"></a>

## 059 · Bağlantı hatasından kurtulma

`Ana görev` · Önkoşul: 058

**Amaç.** Çalışırken sensör kablosu çıkarıldığında sistem kilitlenmesin, hata göstersin. Kablo takılınca sensörü yeniden başlatıp devam etsin.

**Araştır:** I²C zaman aşımı · hat kurtarma · yeniden başlatma stratejisi

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin)

**Başarı ölçütü**

- 10 kez çıkar-tak testinde sistem her seferinde toparlanıyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Kablo çıkarma testini gerçek kartta yap.

---

<a id="g060"></a>

## 060 · Dijital su terazisi

`Mini uygulama` · Önkoşul: 059

**Amaç.** İvmeölçerden roll ve pitch açılarını hesapla, OLED'de sayısal değer ve kabarcık grafiğiyle göster. Butonla mevcut konumu sıfır kabul et ve bu ofseti Flash'a kaydet.

**Araştır:** atan2 ile eğim · ofset · 44. görevdeki Flash kaydı

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); SSD1306 I²C OLED ekran (128×64); Ek buton(lar)

**Başarı ölçütü**

- Düz zeminde ±1° içinde sıfır.
- Ofset reset sonrası korunuyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Flash kaydını gerçek kartta doğrula.
