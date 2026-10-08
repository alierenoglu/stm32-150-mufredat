<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M08 · Bitirme Projesi: Steer-by-Wire Prototipi

Görevler 096–100 · [Tüm görevler](../GOREVLER.md) · [Simülasyon rehberi](../docs/simulasyon.md)

Steer-by-wire eğitim prototipi. Wokwi sürümünde IMU veya kayıt girdisi, UART mesajları ve sanal motor kullanılır. CAN sürümü ayrı bir donanım doğrulama aşamasıdır. Gerçek araçta kullanıma yönelik bir sistem değildir.

---

<a id="g096"></a>

## 096 · Gereksinimler ve mimari

`Bitirme projesi` · Önkoşul: 095

**Amaç.** Sistemi kodlamadan önce tasarla: düğümler, UART mesaj tablosu ve ilerideki CAN eşlemesi, durum makineleri, zamanlama (hangi döngü kaç Hz) ve güvenlik gereksinimleri (ör. “kumanda mesajı 100 ms gelmezse aktüatör güvenli duruma geçer”). Test planını şimdiden yaz.

**Araştır:** gereksinim yazımı · blok diyagram · zamanlama bütçesi · test planı

**Gerekenler:** Kart gerekmez

**Başarı ölçütü**

- docs/bitirme/ altında mimari diyagramı, mesaj tablosu, gereksinim listesi ve test planı var.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda

---

<a id="g097"></a>

## 097 · Kumanda düğümü

`Bitirme projesi` · Önkoşul: 096

**Amaç.** IMU ve Kalman filtresiyle direksiyon açısını üret, ölü bölge ve hız sınırı (rate limit) uygula, 100 Hz'de Wokwi sürümünde UART üzerinden gönder. Durumu OLED'de göster.

**Araştır:** 83. görevdeki Kalman · rate limiter · periyodik CAN mesajı

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); SSD1306 I²C OLED ekran (128×64)

**Başarı ölçütü**

- Mesaj periyodu ve açı çözünürlüğü ölçülmüş.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. UART ve sanal motorla başlangıç sürümü. CAN donanım doğrulaması ayrı tutulur.

---

<a id="g098"></a>

## 098 · Aktüatör düğümü

`Bitirme projesi` · Önkoşul: 097

**Amaç.** Wokwi sürümünde UART üzerinden gelen hedef açıyı kaskat konum kontrolüyle sanal motora uygula; ölçülen açıyı ve durumu geri gönder. FreeRTOS görevleriyle yapılandır.

**Araştır:** 74. görevdeki kaskat kontrol · 95. görevdeki görev yapısı

**Gerekenler:** Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069)

**Başarı ölçütü**

- Basamak hedefinde aşım ve oturma süresi test planındaki hedefi sağlıyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. UART ve sanal motorla başlangıç sürümü. CAN donanım doğrulaması ayrı tutulur.

---

<a id="g099"></a>

## 099 · Güvenlik ve hata enjeksiyonu

`Bitirme projesi` · Önkoşul: 098

**Amaç.** Wokwi sürümüne zaman aşımı, hata kodları ve acil durdurma ekle. Mesaj akışını durdur, sensör verisini geçersiz yap, motor modeline yük ekle ve kumandayı resetle. Watchdog çevre birimi desteklenmiyorsa onu bekleyen test olarak bırak. Her senaryoyu geçti/kaldı tablosuna yaz.

**Araştır:** hata enjeksiyonu · güvenlik gereksinimi doğrulama

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin)

**Başarı ölçütü**

- Bütün güvenlik gereksinimleri test edilip geçti/kaldı olarak raporlanmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. UART/model hata senaryoları yapılır. Gerçek CAN kablosu, motor elektriği ve desteklenmeyen watchdog doğrulanmış sayılmaz.

---

<a id="g100"></a>

## 100 · Doğrulama ve sürüm

`Bitirme projesi` · Önkoşul: 099

**Amaç.** Test planının tamamını koş: basamak cevabı, takip hatası, uçtan uca gecikme, hata senaryoları. Sonuçları grafiklerle README'ye ekle, demo videosu çek ve v1.0 sürümünü yayınla.

**Araştır:** GitHub Releases · teknik dokümantasyon

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- v1.0-sim sürümü yayında.
- README içinde ölçüm, demo, simülasyon sınırları ve kişisel katkı bulunuyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi sürümünü v1.0-sim olarak yayımla, CAN ve fiziksel doğrulamayı ayrı listele.
