<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M10 · İleri Görevler

Görevler 126–150 · [Tüm görevler](../GOREVLER.md) · [Simülasyon rehberi](../docs/simulasyon.md)

Veri kaydı, bootloader, gelişmiş kestirim ve kontrol, test/CI altyapısı ve bitirme projesinin genişletilmesi. Zorunlu değil; 150. görev (portföy) herkes için önerilir.

---

<a id="g126"></a>

## 126 · SD karta kayıt

`İleri görev` · Önkoşul: 055

**Amaç.** microSD karta FatFs ile CSV kaydı yap. Dosyayı düzenli aralıklarla senkronla; güç kesilmesinde ne kadar veri kaybedildiğini ölç.

**Araştır:** FatFs · f_sync · SPI üzerinden SD kart

**Gerekenler:** STM32 geliştirme kartı; microSD kart modülü (SPI)

**Başarı ölçütü**

- Kayıt bilgisayarda açılıyor.
- Güç kesilmesi testi raporlanmış.

**Simülasyon:** ❔ Wokwi desteği belirsiz, dene. Wokwi'de microSD parçası var; STM32 ile FatFs'in çalıştığını dene.

---

<a id="g127"></a>

## 127 · Yüksek hızlı kayıt

`İleri görev` · Önkoşul: 126

**Amaç.** IMU'yu 1 kHz'de çift tamponla SD karta kaydet; yazma gecikmeleri örnek kaybettirmesin.

**Araştır:** çift tampon · SD kart yazma gecikmesi · DMA

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); microSD kart modülü (SPI)

**Başarı ölçütü**

- 10 dakikalık kayıtta kayıp örnek 0.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g128"></a>

## 128 · Düğümler arası zaman senkronu

`İleri görev` · Önkoşul: 087

**Amaç.** İki kart arasında CAN üzerinden zaman senkronizasyonu kur; saat ofsetini ve kaymasını ölç.

**Araştır:** zaman senkronizasyonu · saat kayması

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç

**Başarı ölçütü**

- Senkron sonrası ofset ölçülmüş.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de CAN yok. Gerçek kartta yap; tek kartın varsa loopback modunu kullan.

---

<a id="g129"></a>

## 129 · USB CDC telemetri

`İleri görev` · Önkoşul: 043

**Amaç.** Kartın USB'sini sanal COM port (CDC) olarak kullan; UART'a göre veri hızını karşılaştır.

**Araştır:** USB CDC · USB Device middleware

**Gerekenler:** STM32 geliştirme kartı; Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Ölçülen veri hızları tablosu README'de.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de STM32 USB'si yok.

---

<a id="g130"></a>

## 130 · Bootloader temelleri

`İleri görev` · Önkoşul: 044

**Amaç.** Uygulamayı Flash'ın ileri bir adresine taşı; küçük bir bootloader'dan uygulamaya atla. Vektör tablosunun yerini değiştir.

**Araştır:** linker script · VTOR · stack pointer ve reset vektörü

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Bootloader → uygulama geçişi çalışıyor.

**Simülasyon:** ❔ Wokwi desteği belirsiz, dene

---

<a id="g131"></a>

## 131 · UART ile firmware güncelleme

`İleri görev` · Önkoşul: 130

**Amaç.** Python'dan yeni uygulama dosyasını paketlerle gönder; bootloader Flash'a yazsın, CRC ile doğrulasın, geçerliyse uygulamaya atlasın.

**Araştır:** firmware güncelleme akışı · CRC ile doğrulama · geri dönüş (fallback)

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Güncelleme ve bozuk dosyanın reddi test edilmiş.

**Simülasyon:** ❔ Wokwi desteği belirsiz, dene

---

<a id="g132"></a>

## 132 · Düşük güç modları

`İleri görev` · Önkoşul: 091

**Amaç.** Sleep ve Stop modlarını dene; butonla ya da RTC ile uyandır. Multimetren varsa akım tüketimini ölç.

**Araştır:** Sleep / Stop / Standby · uyandırma kaynakları

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar)

**Başarı ölçütü**

- Uyandırma kaynakları çalışıyor; ölçümler ya da gözlemler raporlanmış.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de PWR ve RTC yok.

---

<a id="g133"></a>

## 133 · CMSIS-DSP ile filtre ve FFT

`İleri görev` · Önkoşul: 042

**Amaç.** Python'da FIR/IIR filtre katsayısı tasarla, CMSIS-DSP ile kartta uygula. ADC sinyalinin FFT'sini alıp spektrumu çiz.

**Araştır:** CMSIS-DSP · scipy.signal · FFT

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Filtrenin frekans cevabı ölçümle doğrulanmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Hesaplamayı simülasyonda dene; gerçek sinyal için gerçek kart.

---

<a id="g134"></a>

## 134 · Sabit noktalı aritmetik

`İleri görev` · Önkoşul: 071

**Amaç.** PI kontrolcüyü float ve Q15 sabit noktalı olarak yaz; çalışma süresini ve doğruluğu karşılaştır.

**Araştır:** Q formatı · taşma ve doyma

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Süre ve hata karşılaştırma tablosu README'de.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g135"></a>

## 135 · Genel Kalman filtresi

`İleri görev` · Önkoşul: 083

**Amaç.** Kalman'ı matris formunda yaz. Motor için encoder'dan konum, hız ve yük torkunu kestir.

**Araştır:** durum uzayı modeli · matris işlemleri · bozucu kestirimi

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Kestirilen hız ham RPM'den daha az gürültülü; gecikmesi ölçülmüş.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g136"></a>

## 136 · Kestirimle hız kontrolü

`İleri görev` · Önkoşul: 135

**Amaç.** Hız kontrolünde ham RPM yerine kestirilen hızı kullan; özellikle düşük hızda performansı karşılaştır.

**Araştır:** gözlemci tabanlı kontrol

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Düşük hız takibindeki fark ölçülmüş.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g137"></a>

## 137 · İleri besleme

`İleri görev` · Önkoşul: 071

**Amaç.** Hız kontrolüne modelden ileri besleme (feedforward) ekle. Takip hatasındaki değişimi ölç.

**Araştır:** feedforward · model tabanlı kontrol

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Rampa takip hatası önce ve sonra karşılaştırılmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g138"></a>

## 138 · LQR ile durum geri beslemesi

`İleri görev` · Önkoşul: 074

**Amaç.** Motor konum sistemi için durum uzayı modeli kur, LQR kazancını Python'da hesapla, kartta uygula. Kaskat PID ile karşılaştır.

**Araştır:** durum uzayı · LQR · python-control veya scipy

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Aynı test senaryosunda iki kontrolcünün sonuçları yan yana.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g139"></a>

## 139 · Sistem tanılama

`İleri görev` · Önkoşul: 068

**Amaç.** Motora PRBS ya da chirp giriş ver; veriden en küçük kareler yöntemiyle model çıkar. Modeli farklı bir veri setiyle doğrula.

**Araştır:** PRBS · chirp · en küçük kareler · model doğrulama

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Modelin doğrulama verisindeki hatası raporlanmış.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g140"></a>

## 140 · 3D yönelim

`İleri görev` · Önkoşul: 084

**Amaç.** Mahony ya da Madgwick filtresiyle quaternion tabanlı 3D yönelim kestirimi yap; Python'da 3D küp olarak göster.

**Araştır:** quaternion · Mahony / Madgwick · gimbal kilidi

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Her yöne dönüş doğru izleniyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'deki MPU6050'nin değerleri elle ayarlanıyor; gerçek sensördeki gürültü ve kayma yok. Filtre davranışını gerçek IMU ya da yapay gürültü eklenmiş kayıtla incele.

---

<a id="g141"></a>

## 141 · Manyetometre ve yön

`İleri görev` · Önkoşul: 140

**Amaç.** Manyetometre ekle; hard-iron ve soft-iron kalibrasyonu yap; eğim telafili pusula (yaw) hesapla.

**Araştır:** hard-iron / soft-iron · eğim telafisi · manyetik sapma

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Manyetometre modülü; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Kalibrasyon öncesi ve sonrası ölçüm dağılımı grafikte.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g142"></a>

## 142 · Sistemi RTOS üzerinde yeniden kur

`İleri görev` · Önkoşul: 098

**Amaç.** Bitirme projesinin bir düğümünü tamamen FreeRTOS görevleriyle yeniden yapılandır; görevlerin CPU payını (runtime stats) ölç ve zamanlama analizini yaz.

**Araştır:** runtime stats · en kötü durum yanıt süresi · oran-monoton zamanlama

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- CPU yükü ve en kötü durum yanıt süreleri raporlanmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır

---

<a id="g143"></a>

## 143 · Birim test altyapısı

`İleri görev` · Önkoşul: 108

**Amaç.** Filtre, PID ve protokol modüllerin için Unity test çerçevesiyle testler yaz; GitHub Actions'ta her push'ta çalışsın.

**Araştır:** Unity (ThrowTheSwitch) · GitHub Actions

**Gerekenler:** Kart gerekmez

**Başarı ölçütü**

- Actions sekmesinde testler yeşil.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda

---

<a id="g144"></a>

## 144 · Firmware'i CI'da derle

`İleri görev` · Önkoşul: 143

**Amaç.** GitHub Actions'ta arm-none-eabi-gcc ile firmware derlemesini otomatikleştir; derleme kırılırsa PR birleştirilemesin.

**Araştır:** arm-none-eabi-gcc · CMake/Makefile · branch protection

**Gerekenler:** Kart gerekmez

**Başarı ölçütü**

- Kırık bir commit'te CI kırmızıya dönüyor.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda. Wokwi CI ile simülasyon testi de ekleyebilirsin (ücretli dakikalar gerekebilir).

---

<a id="g145"></a>

## 145 · Statik analiz

`İleri görev` · Önkoşul: 143

**Amaç.** cppcheck çalıştır, temel MISRA C kurallarını araştır ve projendeki uyarıları sıfırla ya da gerekçelendir.

**Araştır:** cppcheck · MISRA C

**Gerekenler:** Kart gerekmez

**Başarı ölçütü**

- Uyarı raporu ve çözümleri README'de.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda

---

<a id="g146"></a>

## 146 · CAN mesaj kataloğu ve PC aracı

`İleri görev` · Önkoşul: 100

**Amaç.** Bitirme projesinin mesajlarını DBC formatında yaz. Python'da (ör. cantools ile) mesajları çözen bir izleme aracı yap; veriyi bir düğüm üzerinden UART köprüsüyle bilgisayara aktar.

**Araştır:** DBC formatı · cantools · CAN-UART köprüsü

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Araç canlı mesajları isim ve birimleriyle gösteriyor.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de CAN yok. Gerçek kartta yap; tek kartın varsa loopback modunu kullan.

---

<a id="g147"></a>

## 147 · İki eksen

`İleri görev` · Önkoşul: 100

**Amaç.** Bitirme projesine ikinci bir aktüatör ekle (ya da sanal motorla ikinci eksen); iki eksenin senkron çalışmasını sağla.

**Araştır:** çok eksenli kontrol · senkronizasyon

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069)

**Başarı ölçütü**

- İki eksenin takip hataları ölçülmüş.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g148"></a>

## 148 · Kumanda tarafında arıza tespiti

`İleri görev` · Önkoşul: 100

**Amaç.** IMU donması, değer dışı veri ve zaman damgası kayması gibi arızaları algıla; sistemi kısıtlı modda (degrade mode) çalıştır.

**Araştır:** arıza tespiti · makullük kontrolü (plausibility) · degrade mod

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç

**Başarı ölçütü**

- Her arıza senaryosu ve sistem tepkisi tabloda.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır

---

<a id="g149"></a>

## 149 · Gecikme bütçesi

`İleri görev` · Önkoşul: 100

**Amaç.** Sensörden motora uçtan uca gecikmeyi aşama aşama ölç: örnekleme, filtre, CAN, kontrol, PWM. En büyük gecikmeyi azalt.

**Araştır:** gecikme bütçesi · uçtan uca ölçüm

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Logic analyzer veya osiloskop (opsiyonel)

**Başarı ölçütü**

- Önce ve sonra gecikme bütçesi tablosu README'de.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g150"></a>

## 150 · Portföy

`İleri görev` · Önkoşul: 100

**Amaç.** Bitirme projesini ayrı ve temiz bir repoya taşı: mimari diyagram, sonuç grafikleri, demo videosu, kurulum talimatı ve 2–4 sayfalık teknik rapor. CV'ne yazacağın 3–4 maddeyi ölçülmüş sonuçlarla hazırla ve v2.0 sürümünü yayınla.

**Araştır:** teknik rapor yazımı · README tasarımı · ölçülebilir CV maddesi

**Gerekenler:** Kart gerekmez

**Başarı ölçütü**

- Repoyu hiç görmemiş biri README'den projeyi 5 dakikada anlayabiliyor.
- CV maddelerindeki her sayı repodaki bir ölçüme dayanıyor.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda
