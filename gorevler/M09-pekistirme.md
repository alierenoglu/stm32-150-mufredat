<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M09 · Pekiştirme

Görevler 101–125 · [Tüm görevler](../GOREVLER.md) · [Simülasyon rehberi](../docs/simulasyon.md)

Hata bulma, ölçme, karşılaştırma ve farklı koşullarda deneme. Zorunlu değil. Her görevin önkoşulu belirtilmiş; o ana görevi bitirdikten sonra istediğin zaman yapabilirsin.

---

<a id="g101"></a>

## 101 · Tablo tabanlı durum makinesi

`Pekiştirme` · Önkoşul: 010

**Amaç.** Trafik lambasını switch-case yerine durum geçiş tablosuyla yeniden yaz. Davranış birebir aynı kalsın.

**Araştır:** durum geçiş tablosu · fonksiyon işaretçisi

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Yeni bir durum eklemek tabloya bir satır eklemek kadar kolay.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g102"></a>

## 102 · Hata bul: zaman sayacı taşması

`Pekiştirme` · Önkoşul: 008

**Amaç.** HAL_GetTick 32 bitliktir ve yaklaşık 49,7 günde taşar. `if (now > last + interval)` yazımının taşmada neden bozulduğunu göster. Sayacı taşmaya yakın bir değerden başlatarak test et ve doğru yazımı uygula.

**Araştır:** işaretsiz taşma · modüler aritmetik

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- Taşma anında zamanlama bozulmuyor.
- Test yöntemi README'de.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g103"></a>

## 103 · Hata bul: volatile

`Pekiştirme` · Önkoşul: 016

**Amaç.** Kesmede değişen bayrağı volatile olmadan tanımla ve optimizasyonu -O2 yap. Programın neden takıldığını derleyicinin ürettiği assembly'ye bakarak açıkla.

**Araştır:** derleyici optimizasyonu · volatile · disassembly görünümü

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar)

**Başarı ölçütü**

- Assembly'deki fark README'de gösterilmiş.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g104"></a>

## 104 · Zamanı bağımsız ölç

`Pekiştirme` · Önkoşul: 017

**Amaç.** Timer kesmesinin periyodunu bağımsız bir yöntemle ölç: logic analyzer veya osiloskop varsa pin değiştirerek, yoksa DWT cycle sayacıyla. Hesapla karşılaştır.

**Araştır:** DWT cycle sayacı (Cortex-M0'da yok) · pin toggle ile ölçüm

**Gerekenler:** STM32 geliştirme kartı; Logic analyzer veya osiloskop (opsiyonel)

**Başarı ölçütü**

- Ölçülen ve hesaplanan periyot arasındaki fark raporlanmış.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Wokwi'nin logic analyzer parçasını kullanabilirsin.

---

<a id="g105"></a>

## 105 · Kesmede uzun iş

`Pekiştirme` · Önkoşul: 019

**Amaç.** Kesmede yapılan işin süresini adım adım artır; ana döngünün ve diğer kesmelerin hangi noktada bozulduğunu ölç.

**Araştır:** kesme gecikmesi · CPU yükü

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- Bozulma eşiği ölçülmüş.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g106"></a>

## 106 · PWM çözünürlüğü ve frekansı

`Pekiştirme` · Önkoşul: 021

**Amaç.** Farklı ARR değerleri için PWM frekansını ve duty çözünürlüğünü (bit) hesapla, tablo çıkar. Motor ve LED için hangi değerleri neden seçeceğini açıkla.

**Araştır:** PWM çözünürlüğü · frekans-çözünürlük dengesi

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- Tablo ve seçim gerekçesi README'de.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g107"></a>

## 107 · Filtre karşılaştırması

`Pekiştirme` · Önkoşul: 028

**Amaç.** Gürültülü bir ADC sinyali üzerinde hareketli ortalama, medyan ve birinci dereceden IIR filtreyi karşılaştır. Ani sıçramalara (spike) karşı davranışlarını incele.

**Araştır:** medyan filtre · IIR · spike bastırma

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ)

**Başarı ölçütü**

- Gecikme, gürültü ve spike davranışı tablosu README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Simülasyonda gürültüyü yazılımla ekle.

---

<a id="g108"></a>

## 108 · Halka tampon birim testi

`Pekiştirme` · Önkoşul: 036

**Amaç.** Halka tampon kodunu bilgisayarda derle ve kenar durumlarını test et: boş, dolu, sarma, taşma. Testler tek komutla çalışsın.

**Araştır:** birim testi · host üzerinde derleme (gcc) · assert

**Gerekenler:** Kart gerekmez

**Başarı ölçütü**

- Bütün testler geçiyor.
- Koda kasıtlı bir hata eklenince test yakalıyor.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda

---

<a id="g109"></a>

## 109 · CRC doğrulama

`Pekiştirme` · Önkoşul: 039

**Amaç.** CRC16 fonksiyonunu bilinen test vektörleriyle doğrula. C ve Python uygulamaları aynı girdilerde aynı sonucu versin.

**Araştır:** CRC çeşitleri (polinom, başlangıç değeri) · test vektörleri

**Gerekenler:** Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Test vektörleri ve sonuçlar README'de.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda

---

<a id="g110"></a>

## 110 · Bozuk paket testi

`Pekiştirme` · Önkoşul: 039

**Amaç.** Python'dan gönderilen paketlere rastgele bit hatası, bayt kaybı ve fazladan bayt ekle. Alıcının bozuk paketleri reddettiğini ve senkronu kendiliğinden yeniden yakaladığını ölç.

**Araştır:** hata enjeksiyonu · yeniden senkronizasyon

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Hata türüne göre reddetme ve kurtarma oranları tablosu.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Simülasyondaki UART'ı bilgisayardaki Python'a bağlamak için wokwi.toml'a rfc2217ServerPort ekle (docs/simulasyon.md).

---

<a id="g111"></a>

## 111 · Aliasing

`Pekiştirme` · Önkoşul: 042

**Amaç.** Bilinen frekansta bir sinyali (ör. kendi ürettiğin PWM'i RC filtreyle yumuşatıp) farklı örnekleme frekanslarında örnekle. Aliasing'i grafikte göster ve açıkla.

**Araştır:** örnekleme teoremi · aliasing · anti-aliasing filtresi

**Gerekenler:** STM32 geliştirme kartı; Direnç ve kondansatör (RC filtre için); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Görünen frekansın hesapla uyuştuğu gösterilmiş.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g112"></a>

## 112 · Güç kesilmesine dayanıklı kayıt

`Pekiştirme` · Önkoşul: 044

**Amaç.** Flash'a yazma sırasında reset olursa ne olduğunu test et. İki kayıt alanı (A/B) ve CRC ile güç kesilmesine dayanıklı kayıt yap.

**Araştır:** A/B kayıt · geçerlilik kontrolü · atomik güncelleme

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Yazma sırasında 20 reset testinde her seferinde geçerli bir kayıt bulunuyor.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g113"></a>

## 113 · I²C hattı kilitlenmesi

`Pekiştirme` · Önkoşul: 048

**Amaç.** Okuma sırasında karta reset atılırsa sensörün SDA'yı low tutabileceğini araştır. Açılışta hattı kontrol edip 9 saat darbesiyle kurtaran bir rutin yaz.

**Araştır:** I²C bus recovery · GPIO ile saat darbesi üretme

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin)

**Başarı ölçütü**

- Kurtarma rutini test edilmiş.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g114"></a>

## 114 · CPU yükü ölçümü

`Pekiştirme` · Önkoşul: 053

**Amaç.** Bloklayan, kesmeli ve DMA'lı sensör okumada CPU'nun meşgul kaldığı süreyi DWT cycle sayacıyla ölç.

**Araştır:** DWT · CPU yükü

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin)

**Başarı ölçütü**

- Üç yöntemin CPU yükü tablosu.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. DMA'lı ölçüm gerçek kartta.

---

<a id="g115"></a>

## 115 · Ekran optimizasyonu

`Pekiştirme` · Önkoşul: 057

**Amaç.** Ekranın yalnızca değişen bölgesini gönder. Saniyedeki kare sayısını önce ve sonra ölç.

**Araştır:** kirli bölge (dirty rectangle) · FPS ölçümü

**Gerekenler:** STM32 geliştirme kartı; SSD1306 I²C OLED ekran (128×64)

**Başarı ölçütü**

- FPS iyileşmesi ölçülmüş.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g116"></a>

## 116 · Ölü bölge telafisi

`Pekiştirme` · Önkoşul: 071

**Amaç.** Ölçtüğün ölü bölgeyi kontrol çıkışına telafi olarak ekle. Düşük hız takibindeki iyileşmeyi ölç.

**Araştır:** ölü bölge telafisi · doğrusal olmayan aktüatör

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi

**Başarı ölçütü**

- Düşük hızda takip hatası önce ve sonra karşılaştırılmış.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok

---

<a id="g117"></a>

## 117 · Sistematik PI ayarı

`Pekiştirme` · Önkoşul: 071

**Amaç.** Ziegler-Nichols ya da röle (relay) yöntemiyle PI kazançlarını belirle; elle bulduğun kazançlarla karşılaştır.

**Araştır:** Ziegler-Nichols · röle deneyi · kritik kazanç ve periyot

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- İki yöntemin basamak cevapları yan yana.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g118"></a>

## 118 · Kontrol frekansının etkisi

`Pekiştirme` · Önkoşul: 071

**Amaç.** Hız kontrolünü 1 kHz, 200 Hz ve 50 Hz'de çalıştır. Aynı kazançlarla performansın nasıl değiştiğini ve nedenini açıkla.

**Araştır:** örnekleme süresi ve kararlılık · ayrıklaştırma

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Üç frekansın cevap grafikleri ve açıklama README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g119"></a>

## 119 · Türev terimi

`Pekiştirme` · Önkoşul: 072

**Amaç.** PID'e türev terimi ekle. Ham türevin gürültüyü nasıl büyüttüğünü göster, türevi filtrele ve hedef yerine ölçüm üzerinden al (derivative kick).

**Araştır:** türev filtresi · derivative kick · ölçüm üzerinden türev

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Filtresiz ve filtreli D ile derivative kick karşılaştırılmış.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g120"></a>

## 120 · Hareket profili

`Pekiştirme` · Önkoşul: 074

**Amaç.** Hedef konuma basamak yerine trapez hız profiliyle git. Aşımı, titreşimi ve en yüksek duty'yi karşılaştır.

**Araştır:** trapez profil · ivme sınırı

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü); Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Basamak ve trapez profilin grafikleri yan yana.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g121"></a>

## 121 · Kalman duyarlılık analizi

`Pekiştirme` · Önkoşul: 084

**Amaç.** Q ve R için 3×3 değer ızgarası oluştur. Her kombinasyonda gecikmeyi ve gürültüyü aynı kayıt üzerinde ölç.

**Araştır:** parametre taraması · ısı haritası

**Gerekenler:** Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Izgara sonuçları tablo ya da ısı haritası olarak README'de.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda

---

<a id="g122"></a>

## 122 · Sensör hata senaryoları

`Pekiştirme` · Önkoşul: 084

**Amaç.** Kayıtlı veriye yapay hatalar ekle: jiroskop bias'ında ani değişim, ivmeölçer doygunluğu, örnek kaybı. İki filtrenin tepkisini karşılaştır.

**Araştır:** hata modelleme · sağlamlık (robustness)

**Gerekenler:** Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph)

**Başarı ölçütü**

- Her senaryonun sonucu grafikle açıklanmış.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda

---

<a id="g123"></a>

## 123 · CAN bus yükü

`Pekiştirme` · Önkoşul: 088

**Amaç.** Mesaj tablona göre bus yükünü (%) hesapla. Yükü kasıtlı artırarak düşük öncelikli mesajların gecikmesini ölç.

**Araştır:** bus yükü hesabı · ID önceliği ve arbitrasyon

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç

**Başarı ölçütü**

- Hesaplanan ve ölçülen yük; öncelik-gecikme ilişkisi README'de.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de CAN yok. Gerçek kartta yap; tek kartın varsa loopback modunu kullan.

---

<a id="g124"></a>

## 124 · Durum makinesi testleri

`Pekiştirme` · Önkoşul: 092

**Amaç.** Hata yönetimi durum makinesini donanımdan bağımsız hale getir ve bilgisayarda her geçişi kapsayan birim testleri yaz.

**Araştır:** birim testi · test kapsamı · donanım soyutlaması

**Gerekenler:** Kart gerekmez

**Başarı ölçütü**

- Bütün geçişler testle kapsanıyor.

**Simülasyon:** 💻 Kart gerekmez, bilgisayarda

---

<a id="g125"></a>

## 125 · Öncelik terslenmesi

`Pekiştirme` · Önkoşul: 095

**Amaç.** FreeRTOS'ta öncelik terslenmesini (priority inversion) kasıtlı oluştur; mutex'in öncelik kalıtımıyla çözüldüğünü göster. Görevlerin stack kullanımını ölçüp boyutları ayarla.

**Araştır:** priority inversion · priority inheritance · stack high water mark

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Terslenme ve çözümü zaman çizelgesiyle gösterilmiş.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli
