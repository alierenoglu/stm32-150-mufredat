<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M06 · IMU, Kalibrasyon ve Filtreler

Görevler 076–085 · [Tüm görevler](../GOREVLER.md)

Jiroskop bias'ı ve kayma, ivmeölçerden açı, kalibrasyon, sabit örnekleme, complementary ve Kalman filtreleri. Filtreleri aynı kayıt üzerinde karşılaştırıp kartta ve bilgisayarda aynı sonucu aldığını göstereceksin.

---

<a id="g076"></a>

## 076 · Jiroskop ve bias

`Ana görev` · Önkoşul: 075

**Amaç.** Jiroskobu oku ve rad/s'ye çevir. Kart hareketsizken birkaç saniyelik ortalamayla sıfır hız ofsetini (bias) bul ve çıkar.

**Araştır:** jiroskop ölçek katsayısı · bias · ortalama ile kalibrasyon

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Bias çıkarılınca hareketsizken açısal hız yaklaşık 0.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'deki MPU6050'nin değerleri elle ayarlanıyor; gerçek sensördeki gürültü ve kayma yok. Filtre davranışını gerçek IMU ya da yapay gürültü eklenmiş kayıtla incele.

---

<a id="g077"></a>

## 077 · Açı entegrasyonu ve kayma

`Ana görev` · Önkoşul: 076

**Amaç.** Jiroskop verisini zamana göre entegre ederek açı hesapla. Kartı 5 dakika hareketsiz bırak ve açının ne kadar kaydığını kaydet.

**Araştır:** sayısal entegrasyon · kayma (drift) · rastgele yürüyüş

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Kayma grafiği ve dakikada kaç derece kaydığı README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'deki MPU6050'nin değerleri elle ayarlanıyor; gerçek sensördeki gürültü ve kayma yok. Filtre davranışını gerçek IMU ya da yapay gürültü eklenmiş kayıtla incele.

---

<a id="g078"></a>

## 078 · İvmeölçerden açı

`Ana görev` · Önkoşul: 077

**Amaç.** İvmeölçerden roll ve pitch hesapla. Kartı sallayınca açının neden bozulduğunu göster.

**Araştır:** yerçekimi vektörü · doğrusal ivmenin etkisi

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Durağan ve hareketli durum grafikleri karşılaştırılmış; nedeni açıklanmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'deki MPU6050'nin değerleri elle ayarlanıyor; gerçek sensördeki gürültü ve kayma yok. Filtre davranışını gerçek IMU ya da yapay gürültü eklenmiş kayıtla incele.

---

<a id="g079"></a>

## 079 · İvmeölçer kalibrasyonu

`Ana görev` · Önkoşul: 078

**Amaç.** Altı pozisyon yöntemiyle her eksenin ofsetini ve ölçek hatasını bul. Kalibrasyon katsayılarını Flash'a kaydet.

**Araştır:** 6 pozisyon kalibrasyonu · ofset ve ölçek hatası · yerçekimi referansı

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Kalibrasyon sonrası her yüzde |a| yaklaşık 1 g (±%2).

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Kalibrasyon gerçek sensör hatası gerektirir.

---

<a id="g080"></a>

## 080 · Kalibrasyon sihirbazı

`Mini uygulama` · Önkoşul: 079

**Amaç.** UART'tan ya da OLED'den yönlendirmeli bir kalibrasyon akışı yap: “Kartı yüzü yukarı koy, butona bas” gibi adımlarla ivmeölçer ve jiroskop kalibrasyonunu tamamla, sonuçları kaydet.

**Araştır:** kullanıcı akışı tasarımı · durum makinesi · Flash kaydı

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Ek buton(lar); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü) veya SSD1306 I²C OLED ekran (128×64)

**Başarı ölçütü**

- Kalibrasyonu bilmeyen biri yalnızca talimatlarla tamamlayabiliyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Akışı simülasyonda geliştir, kalibrasyonu gerçek kartta yap.

---

<a id="g081"></a>

## 081 · Sabit örnekleme ve dt

`Ana görev` · Önkoşul: 080

**Amaç.** IMU'yu sabit frekansta (ör. 200 Hz) oku ve her adımın dt'sini ölç. Değişken dt'nin entegrasyona etkisini göster.

**Araştır:** örnekleme jitter'ı · dt ölçümü · DWT cycle sayacı

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- dt'nin en küçük, ortalama ve en büyük değerleri raporlanmış.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g082"></a>

## 082 · Complementary filtre

`Ana görev` · Önkoşul: 081

**Amaç.** Jiroskop ve ivmeölçer açılarını complementary filtreyle birleştir. Farklı katsayılarla dene; kartı eğerek canlı grafikte izle.

**Araştır:** complementary filtre · zaman sabiti ile katsayı ilişkisi

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Seçtiğin katsayının gerekçesi ve grafikler README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'deki MPU6050'nin değerleri elle ayarlanıyor; gerçek sensördeki gürültü ve kayma yok. Filtre davranışını gerçek IMU ya da yapay gürültü eklenmiş kayıtla incele.

---

<a id="g083"></a>

## 083 · Kalman filtresi

`Ana görev` · Önkoşul: 082

**Amaç.** Açıyı ve jiroskop bias'ını kestiren iki durumlu Kalman filtresini yaz. Q ve R değerlerinin anlamını açıkla ve ayarla.

**Araştır:** Kalman tahmin/düzeltme adımları · kovaryans · Q ve R

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Filtre kartta 200 Hz'de çalışıyor.
- Bias kestirimi zamanla oturuyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'deki MPU6050'nin değerleri elle ayarlanıyor; gerçek sensördeki gürültü ve kayma yok. Filtre davranışını gerçek IMU ya da yapay gürültü eklenmiş kayıtla incele.

---

<a id="g084"></a>

## 084 · Filtreleri karşılaştır

`Ana görev` · Önkoşul: 083

**Amaç.** Aynı ham sensör kaydını hem complementary hem Kalman filtresinden geçir. Filtre kodunu bilgisayarda da derleyip kayıt dosyası üzerinde çalıştır; kart ve bilgisayar aynı sonucu versin.

**Araştır:** host üzerinde derleme · tekrarlanabilir deney

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Karşılaştırma tablosu: gecikme, gürültü, kayma.
- Kart ve bilgisayar sonuçları örnek bazında uyuşuyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'deki MPU6050'nin değerleri elle ayarlanıyor; gerçek sensördeki gürültü ve kayma yok. Filtre davranışını gerçek IMU ya da yapay gürültü eklenmiş kayıtla incele.

---

<a id="g085"></a>

## 085 · Yapay ufuk

`Mini uygulama` · Önkoşul: 084

**Amaç.** Roll ve pitch'i OLED'de uçak göstergesindeki gibi yapay ufuk olarak göster (ya da Python'da 3D küp). Güncelleme en az 20 Hz olsun.

**Araştır:** çizgi döndürme · ekran tazeleme

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); SSD1306 I²C OLED ekran (128×64) veya Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Kart eğildiğinde gösterge gecikmesiz ve doğru yönde dönüyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli
