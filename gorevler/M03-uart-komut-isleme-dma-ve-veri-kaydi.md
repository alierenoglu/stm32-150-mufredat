<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M03 · UART, Komut İşleme, DMA ve Veri Kaydı

Görevler 031–045 · [Tüm görevler](../GOREVLER.md)

Seri haberleşme, komut ayrıştırma, halka tampon, paket protokolü ve CRC, DMA, sabit örnekleme, Flash'a kayıt ve bilgisayarda canlı grafik. Bu modülün araçlarını sonraki her modülde veri görmek için kullanacaksın.

---

<a id="g031"></a>

## 031 · UART ile ilk mesaj

`Ana görev` · Önkoşul: 030

**Amaç.** UART'ı 115200 8N1 ayarla, saniyede bir “Merhaba” ve bir sayaç gönder; bilgisayarda seri terminalde gör.

**Araştır:** UART çerçevesi · baud rate · TX/RX çapraz bağlantı · ortak GND · seri terminal programları

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Terminalde mesajlar düzgün görünüyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g032"></a>

## 032 · printf yönlendirme

`Ana görev` · Önkoşul: 031

**Amaç.** printf çıktısını UART'a yönlendir. ADC değerini ve voltajı (float) her 100 ms'de bir yazdır.

**Araştır:** _write / __io_putchar · newlib-nano ve float printf ayarı

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Potansiyometre (10 kΩ)

**Başarı ölçütü**

- Float değerler doğru yazdırılıyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g033"></a>

## 033 · Karakter komutları

`Ana görev` · Önkoşul: 032

**Amaç.** Bilgisayardan gelen tek karakterlik komutlarla LED'i yönet: '1' aç, '0' kapat, 't' değiştir. Önce polling ile oku.

**Araştır:** HAL_UART_Receive · polling · zaman aşımı parametresi

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Komutlar çalışıyor.
- Polling sırasında LED animasyonunun takıldığını gösteriyorsun.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g034"></a>

## 034 · Kesmeyle UART alımı

`Ana görev` · Önkoşul: 033

**Amaç.** UART alımını kesmeyle yap. Komut beklerken LED animasyonu takılmadan devam etsin.

**Araştır:** HAL_UART_Receive_IT · RxCpltCallback · alımı yeniden başlatma

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Animasyon hiç takılmıyor.
- Hızlı yazılan 20 karakterin hepsi işleniyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g035"></a>

## 035 · Satır tabanlı komut arayüzü

`Mini uygulama` · Önkoşul: 034

**Amaç.** Enter ile biten satır komutlarını işle: LED ON, LED OFF, PWM <0-100>, BLINK <ms>, HELP. Her komut “OK” ya da hata mesajı döndürsün.

**Araştır:** satır tamponu · strcmp / strncmp · strtol · komut tablosu

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Bütün komutlar çalışıyor; HELP komut listesini veriyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g036"></a>

## 036 · Halka tampon (ring buffer)

`Ana görev` · Önkoşul: 035

**Amaç.** Kesmede gelen baytları bir halka tampona yaz, ana döngüde oku. Tampon taşmalarını say ve raporla.

**Araştır:** halka tampon · head/tail · tek üretici-tek tüketici · volatile ve atomiklik

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Bilgisayardan art arda 1000 karakter gönderildiğinde kayıp yok ya da kayıp sayısı raporlanıyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g037"></a>

## 037 · Sağlam komut ayrıştırıcı

`Ana görev` · Önkoşul: 036

**Amaç.** Hatalı komutları, sınır dışı değerleri (PWM 150), çok uzun satırları ve boş satırları güvenli şekilde reddet. Sistem hiçbir girişle kilitlenmesin.

**Araştır:** girdi doğrulama · tampon taşması · savunmacı programlama

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- README'deki 10 kötü giriş testinin hepsinde sistem doğru hata mesajı veriyor ve çalışmaya devam ediyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g038"></a>

## 038 · Gönderim süresi ve DMA

`Ana görev` · Önkoşul: 037

**Amaç.** 115200 baud'da 100 baytlık bir mesajın gönderim süresini hesapla ve ölç. Bloklayan gönderimin ana döngüyü ne kadar yavaşlattığını göster. Sonra gönderimi DMA ile yap; önceki aktarım bitmeden yenisinin başlamasını engelle.

**Araştır:** UART bant genişliği · HAL_UART_Transmit_DMA · TxCpltCallback · meşgul bayrağı

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Bloklayan ve DMA'lı sürümde ana döngü süresi ölçülüp karşılaştırılmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DMA yok; süre ölçümünü simülasyonda, DMA kısmını gerçek kartta yap.

---

<a id="g039"></a>

## 039 · Paket protokolü ve CRC

`Ana görev` · Önkoşul: 038

**Amaç.** Başlangıç baytı, uzunluk, sıra numarası, veri ve CRC16 içeren bir paket formatı tasarla. Kart paketleri göndersin; Python tarafında çöz ve CRC'si bozuk paketleri reddet.

**Araştır:** çerçeveleme (framing) · CRC16 · little-endian · sıra numarasıyla kayıp tespiti · Python struct modülü

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Paket formatı çözümün README.md dosyasında tablo halinde.
- Python 10.000 paketin kaçının bozuk veya kayıp olduğunu raporluyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Simülasyondaki UART'ı bilgisayardaki Python'a bağlamak için wokwi.toml'a rfc2217ServerPort ekle.

---

<a id="g040"></a>

## 040 · Paketli uzaktan kumanda

`Mini uygulama` · Önkoşul: 039

**Amaç.** Bilgisayardaki Python programı (ya da ikinci kart) paketle komut göndersin; kart LED'i yönetip durumunu paketle geri bildirsin. 500 ms boyunca geçerli paket gelmezse kart güvenli duruma geçsin (LED söner, hata LED'i yanar); bağlantı dönünce bunu bildirsin.

**Araştır:** zaman aşımı (timeout) · güvenli durum (fail-safe) · el sıkışma

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph) veya İkinci STM32 kartı; Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Bağlantı kesilince 500 ms içinde güvenli duruma geçiyor.
- Bağlantı dönünce sistem kendiliğinden toparlanıyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Simülasyondaki UART'ı bilgisayardaki Python'a bağlamak için wokwi.toml'a rfc2217ServerPort ekle.

---

<a id="g041"></a>

## 041 · ADC + DMA (dairesel tampon)

`Ana görev` · Önkoşul: 040

**Amaç.** ADC'yi sürekli dönüşüm ve dairesel DMA ile çalıştır. Yarım ve tam tampon callback'lerinde tamponun bir yarısını işlerken diğer yarısı dolsun.

**Araştır:** DMA circular mode · HalfCplt / Cplt callback · çift tampon (ping-pong)

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ)

**Başarı ölçütü**

- CPU, ADC'yi hiç beklemeden örneklerin ortalamasını hesaplıyor.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de DMA yok.

---

<a id="g042"></a>

## 042 · Timer tetiklemeli örnekleme

`Ana görev` · Önkoşul: 041

**Amaç.** ADC'yi timer tetiklemesiyle tam 1 kHz'de örnekle, DMA ile topla. Örnekleme frekansının gerçekten 1 kHz olduğunu doğrula.

**Araştır:** harici tetik (TRGO) · örnekleme teoremi

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ)

**Başarı ölçütü**

- 1 saniyede tam 1000 örnek toplanıyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DMA yok; timer kesmesinde ADC okuyarak dene, DMA kısmını gerçek kartta yap.

---

<a id="g043"></a>

## 043 · Python ile canlı grafik ve kayıt

`Ana görev` · Önkoşul: 042

**Amaç.** Seri porttan gelen verileri Python'da canlı çizdir ve CSV'ye kaydet. Okuma, çizim ve kayıt birbirini yavaşlatmasın.

**Araştır:** pyserial · matplotlib animasyonu veya pyqtgraph · thread ve kuyruk

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- 100 Hz veri 5 dakika boyunca kayıpsız kaydediliyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Simülasyondaki UART'ı bilgisayardaki Python'a bağlamak için wokwi.toml'a rfc2217ServerPort ekle.

---

<a id="g044"></a>

## 044 · Flash'a ayar kaydetme

`Ana görev` · Önkoşul: 043

**Amaç.** UART komutlarıyla değiştirilen ayarları SAVE komutuyla Flash'ın kullanılmayan bir sektörüne/sayfasına yaz; reset sonrası geri yükle. Kayda sihirli sayı ve CRC ekle; kayıt geçersizse varsayılanları kullan.

**Araştır:** Flash sektörleri / sayfaları · silme ve yazma · HAL_FLASH_Unlock · linker script ile alan ayırma

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Güç kesilip açıldığında ayarlar korunuyor.
- Bozuk kayıt algılanıp varsayılana dönülüyor.

**Simülasyon:** ❔ Wokwi desteği belirsiz, dene. Flash yazmanın simüle edildiği dokümanda yazmıyor; gerçek kartta doğrula.

---

<a id="g045"></a>

## 045 · Mini osiloskop

`Mini uygulama` · Önkoşul: 044

**Amaç.** Timer tetiklemeli ADC ile pot sinyalini örnekle, paketli binary formatta gönder ve Python'da canlı osiloskop gibi göster. Örnekleme hızı komutla değişsin (100 Hz–5 kHz) ve Flash'ta saklansın.

**Araştır:** bant genişliği hesabı · 39. görevdeki paket protokolü · binary veri

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- 5 kHz'de veri kaybı yok ya da kayıp oranı ölçülmüş.
- Örnekleme hızı reset sonrası korunuyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DMA yok; örneklemeyi timer kesmesinde yap.
