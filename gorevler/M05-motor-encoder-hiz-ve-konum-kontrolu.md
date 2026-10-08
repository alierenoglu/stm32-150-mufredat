<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M05 · Motor, Encoder, Hız ve Konum Kontrolü

Görevler 061–075 · [Tüm görevler](../GOREVLER.md)

DC motor, encoder, hız ve konum kontrolü. Wokwi yolunda 069 önce hazırlanır: motor modeli ve A/B üreteci kullanılır. Timer encoder modu ayrıca doğrulanır. Yazılımsal çözüm, donanım timer doğrulaması olarak raporlanmaz.

---

<a id="g061"></a>

## 061 · DC motor sürme

`Ana görev` · Önkoşul: 060, 069

**Amaç.** Motor sürücüyle motoru çalıştır: PWM ile gücü, GPIO ile yönü kontrol et. UART komutlarıyla duty ve yön değiştir.

**Araştır:** H köprüsü · motor sürücü pinleri · motor beslemesini kart beslemesinden ayırma · ortak GND

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- İki yönde %0–100 arası çalışıyor.
- Bağlantı şeması README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi yolunda önce 069 modelini kur. PWM/yön çıkışını modelle doğrula. Gerçek H köprüsü ve elektriksel motor davranışı test edilmiş sayılmaz.

---

<a id="g062"></a>

## 062 · Rampa

`Ana görev` · Önkoşul: 061

**Amaç.** Kalkış, duruş ve yön değişimini rampalı yap (ör. %100'e 500 ms'de çık). Ani yön değişiminin neden zararlı olduğunu araştır.

**Araştır:** eğim sınırlayıcı (slew rate limiter) · ters EMK

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi

**Başarı ölçütü**

- Ani komutlarda bile duty değişim hızı sınırlı.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Rampa mantığını simülasyonda LED/PWM ile dene; motor davranışını gerçek kartta gözle.

---

<a id="g063"></a>

## 063 · PWM frekansı ve ölü bölge

`Ana görev` · Önkoşul: 062

**Amaç.** Motoru 1 kHz ve 20 kHz PWM ile çalıştır; ses ve düşük hız davranışını karşılaştır. Motorun dönmeye başladığı en düşük duty'yi (ölü bölge) iki yönde ölç.

**Araştır:** PWM frekansı ve motor endüktansı · statik sürtünme · ölü bölge

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi

**Başarı ölçütü**

- Ölü bölge değerleri ve frekans gözlemleri README'de.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g064"></a>

## 064 · Encoder ile konum

`Ana görev` · Önkoşul: 063

**Amaç.** Encoder'ı timer encoder moduyla oku; milin konumunu (derece) ve yönünü hesapla. 16 bit sayaç taşmasını yöneterek 32 bit konum tut.

**Araştır:** quadrature encoder · timer encoder modu · ×4 sayım · CPR ve dişli oranı · sayaç taşması

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi

**Başarı ölçütü**

- Mil 10 tur çevrilince konum 3600° civarında.
- Sayaç taşmasında konum sıçramıyor.

**Simülasyon:** ❔ Wokwi desteği belirsiz, dene. Önce KY-040 veya kodlanmış A/B üreteciyle timer encoder modunu sına. Destek yoksa EXTI ile yazılımsal sayım alternatifini raporla. Timer encoder görevi bu alternatifle tamamlandı sayılmaz.

---

<a id="g065"></a>

## 065 · Motor test tezgâhı

`Mini uygulama` · Önkoşul: 064

**Amaç.** UART komutlarıyla motoru sür (duty, yön, rampa), encoder konumunu canlı gönder ve Python'da konum grafiğini çiz.

**Araştır:** 61–64. görevlerin birleşimi · 39. görevdeki paket protokolü

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Komut ve konum aynı grafikte izlenebiliyor.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g066"></a>

## 066 · RPM hesabı

`Ana görev` · Önkoşul: 065

**Amaç.** Encoder'dan RPM'i sabit aralıklarla (timer kesmesi) hesapla. Düşük hızda çözünürlüğün neden bozulduğunu göster ve darbeler arası süre ölçümünü alternatif olarak dene.

**Araştır:** frekans ölçümü ve periyot ölçümü · nicemleme (quantization) hatası

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- İki yöntemin düşük ve yüksek hızdaki gürültüsü karşılaştırılmış.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g067"></a>

## 067 · Hız filtresi

`Ana görev` · Önkoşul: 066

**Amaç.** RPM sinyaline hareketli ortalama ve birinci dereceden alçak geçiren filtre uygula. Gürültüyü ve gecikmeyi karşılaştır.

**Araştır:** IIR alçak geçiren filtre · kesim frekansı · faz gecikmesi

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Seçtiğin filtrenin gerekçesi ölçümle birlikte README'de.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g068"></a>

## 068 · Motoru tanı

`Ana görev` · Önkoşul: 067

**Amaç.** Açık çevrimde duty → kararlı hız eğrisini çıkar. Basamak (step) girişinde hız cevabını kaydet ve birinci dereceden modelin kazancını ve zaman sabitini bul.

**Araştır:** basamak cevabı · birinci dereceden sistem · zaman sabiti (%63 kuralı)

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Model parametreleri ve grafikler README'de.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Motoru olmayan, motorlu bir ekip arkadaşının kaydını kullanabilir.

---

<a id="g069"></a>

## 069 · Sanal motor ve encoder üreteci

`Ana görev` · Önkoşul: 030, 040

**Amaç.** Wokwi için birinci dereceden motor modeli ve A/B quadrature üreteci hazırla. Parametreleri kaynaklı veya açıkça eğitim varsayımı olarak belirtilmiş değerlerden seç. PWM ve yönü oku, hız/konum hesapla, custom chip çıkışlarından A/B darbeleri üret. Önce sabit hız ve yön testini yap, sonra motor modelini bağla. 068 ölçümleri elde edilince parametreleri güncelle.

**Araştır:** ayrık zaman benzetimi · Euler yöntemi · quadrature sinyal üretimi (Gray kodu) · kesme frekansı ile simüle edilebilecek en yüksek hız ilişkisi

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- A/B sırası iki yönde doğrulanmış ve tur başına sayım tanımı yazılmış.
- Belirlenen darbe sayısında sayıcı beklenen konuma ulaşıyor.
- STM32 timer encoder desteği ayrı test edilmiş; destek yoksa yazılımsal sayım açıkça belirtilmiş.
- Model adımı, azami darbe hızı ve motor parametreleri raporlanmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de modeli custom chip olarak da yazabilirsin; encoder modunun simülasyonunu önce doğrula.

> Wokwi yolunda 060 sonrasında 069 yapılır, sonra 061 ile devam edilir. Hazır çalışan encoder modeli bu pakete dahil değildir.

---

<a id="g070"></a>

## 070 · P ile hız sabitleyici

`Mini uygulama` · Önkoşul: 069

**Amaç.** Yalnızca oransal (P) kontrolle hedef hızı tut. Hedef UART'tan gelsin, hedef ve ölçülen hız canlı çizilsin. Kalıcı hatayı gözle ve nedenini açıkla.

**Araştır:** kapalı çevrim kontrol · oransal kazanç · kalıcı hata (steady-state error)

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Üç farklı Kp için kalıcı hata ve salınım tablosu README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g071"></a>

## 071 · PI hız kontrolü

`Ana görev` · Önkoşul: 070

**Amaç.** İntegral terimi ekle; farklı hedef hızları kalıcı hatasız takip et. Başlangıç kazançlarını modelinden tahmin et, sonra ince ayar yap.

**Araştır:** PI kontrol · ayrık zamanda integral · örnekleme süresi

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Basamak cevabında kalıcı hata yaklaşık 0.
- Aşım ve oturma süresi ölçülmüş.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g072"></a>

## 072 · Anti-windup

`Ana görev` · Önkoşul: 071

**Amaç.** Çıkışa sınır koy ve ulaşılamayacak bir hız iste. İntegral birikmesinin toparlanmayı nasıl bozduğunu göster, sonra anti-windup ekleyip karşılaştır.

**Araştır:** integral windup · clamping · back-calculation

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Anti-windup öncesi ve sonrası grafikler yan yana.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g073"></a>

## 073 · Bozucu etkiye karşı

`Ana görev` · Önkoşul: 072

**Amaç.** Motor dönerken mile yük bindir (gerçek motorda elle hafif fren, sanal motorda yük torku). Hızın ne kadar düştüğünü ve ne kadar sürede toparlandığını ölç.

**Araştır:** bozucu etki bastırma · integral teriminin rolü

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- P ve PI kontrolün yük altındaki davranışı karşılaştırılmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g074"></a>

## 074 · Kaskat konum kontrolü

`Ana görev` · Önkoşul: 073

**Amaç.** Dışta konum (P veya PD), içte hız (PI) kontrolü kur ve motor milini hedef açıya götür. Aşımı, oturma süresini ve kalıcı hatayı ölç.

**Araştır:** kaskat kontrol · iç döngünün dış döngüden hızlı olması · döngü frekansları

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- 90° hedefindeki ölçümler README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g075"></a>

## 075 · Konum servosu

`Mini uygulama` · Önkoşul: 074

**Amaç.** Hedef açıyı potansiyometreden ya da UART'tan al; motor hedefe gitsin. Hedef, gerçek konum ve hata Python'da canlı çizilsin. Başarı ölçütlerini (aşım, kalıcı hata) kendin belirle ve sağladığını göster.

**Araştır:** gereksinim belirleme · test senaryosu

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Potansiyometre (10 kΩ); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Kendi koyduğun ölçütler ve ölçüm sonuçları README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.
