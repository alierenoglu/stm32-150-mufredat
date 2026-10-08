<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M07 · CAN, Hata Yönetimi, Watchdog ve FreeRTOS

Görevler 086–095 · [Tüm görevler](../GOREVLER.md) · [Simülasyon rehberi](../docs/simulasyon.md)

CAN haberleşmesi ve hata durumları, watchdog, hata yönetimi durum makinesi, HardFault analizi ve FreeRTOS temelleri.

---

<a id="g086"></a>

## 086 · CAN loopback

`Ana görev` · Önkoşul: 085

**Amaç.** CAN çevre birimini loopback modunda, transceiver olmadan tek kartta çalıştır: mesaj gönder, kendi mesajını al. Filtreyi yalnızca belirli ID'leri alacak şekilde ayarla.

**Araştır:** CAN çerçevesi · standart ID · DLC · bit timing · filtre bankları · loopback modu

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- Filtreye uyan ID'ler alınıyor, diğerleri alınmıyor.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de CAN yok. Gerçek kartta yap; tek kartın varsa loopback modunu kullan.

---

<a id="g087"></a>

## 087 · İki kart arası CAN

`Ana görev` · Önkoşul: 086

**Amaç.** İki kartı transceiver'larla bağla, 500 kbit/s'de mesaj alışverişi yap. Bit timing ayarını hesapla; hattın iki ucuna 120 Ω sonlandırma direnci koy.

**Araştır:** CAN fiziksel katmanı · CANH / CANL · sonlandırma · prescaler ve zaman segmentleri

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç

**Başarı ölçütü**

- 10.000 mesajda kayıp yok.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de CAN yok. Gerçek kartta yap; tek kartın varsa loopback modunu kullan.

---

<a id="g088"></a>

## 088 · CAN mesaj tasarımı

`Ana görev` · Önkoşul: 087

**Amaç.** Periyodik (10 ms ve 100 ms) ve olay tabanlı mesajlar tasarla. Her mesajın ID'si, periyodu, içeriği, ölçeği ve birimi docs/ altında tablo halinde olsun.

**Araştır:** mesaj kataloğu · DBC dosyası mantığı · sinyal ölçekleme

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç

**Başarı ölçütü**

- Tablodaki her mesaj gerçekten o periyotta yayınlanıyor.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de CAN yok. Gerçek kartta yap; tek kartın varsa loopback modunu kullan.

---

<a id="g089"></a>

## 089 · CAN hata durumları

`Ana görev` · Önkoşul: 088

**Amaç.** Çalışırken CAN kablosunu çıkar ve sonlandırmayı kaldır. Hata sayaçlarını (TEC/REC) ve bus-off durumunu izle, otomatik kurtarmayı ayarla.

**Araştır:** error active / passive · bus-off · otomatik bus-off yönetimi

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç

**Başarı ölçütü**

- Her senaryoda hata sayaçlarının davranışı kaydedilmiş.
- Bağlantı dönünce haberleşme kendiliğinden düzeliyor.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de CAN yok. Gerçek kartta yap; tek kartın varsa loopback modunu kullan.

---

<a id="g090"></a>

## 090 · CAN ile uzaktan motor

`Mini uygulama` · Önkoşul: 089

**Amaç.** Bir kart hedef hızı/konumu CAN'den göndersin; diğer kart motoru sürüp ölçülen konumu ve hızı geri göndersin. Gönderen kart sonuçları UART'tan bilgisayara aktarsın.

**Araştır:** dağıtık kontrol · uçtan uca gecikme

**Gerekenler:** STM32 geliştirme kartı; İkinci STM32 kartı; 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Hedef ve ölçülen konum aynı grafikte.
- Uçtan uca gecikme ölçülmüş.

**Simülasyon:** ❌ Wokwi ile donanım doğrulaması yok. Wokwi'de CAN yok. Gerçek kartta yap; tek kartın varsa loopback modunu kullan.

---

<a id="g091"></a>

## 091 · Watchdog

`Ana görev` · Önkoşul: 090

**Amaç.** Bağımsız watchdog'u (IWDG) etkinleştir; ana döngü takılırsa kart resetlensin. Açılışta reset sebebini okuyup UART'tan raporla.

**Araştır:** IWDG ve WWDG farkı · zaman aşımı hesabı · reset sebebi bayrakları

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Kasıtlı sonsuz döngüde reset oluyor ve sebep doğru raporlanıyor.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de IWDG yok, WWDG var; IWDG'yi gerçek kartta dene.

---

<a id="g092"></a>

## 092 · Hata yönetimi durum makinesi

`Ana görev` · Önkoşul: 091

**Amaç.** Motor sistemine INIT, READY, RUN, FAULT ve ESTOP durumları ekle. Acil durdurma butonunu, encoder hatasını (komut var ama sayım yok), sensör hatasını ve haberleşme kaybını işle. FAULT'tan çıkış bilinçli bir komut gerektirsin.

**Araştır:** güvenlik durum makinesi · hata kodları · fail-safe tasarım

**Gerekenler:** STM32 geliştirme kartı; Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi veya Sanal motor ve encoder üreteci (Görev 069); Ek buton(lar); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Her hata senaryosu tetiklenip doğru duruma geçildiği README'deki tabloda.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de DC motor parçası yok. 069'daki sanal motoru kullan; encoder modunun simülasyonunu önce doğrula.

---

<a id="g093"></a>

## 093 · HardFault analizi

`Ana görev` · Önkoşul: 092

**Amaç.** Kasıtlı hata oluştur (NULL işaretçi, hizalanmamış erişim, sıfıra bölme tuzağı). HardFault handler'da yığından PC ve LR değerlerini kaydet; hatanın kaynağını bulup açıkla.

**Araştır:** Cortex-M exception modeli · yığına kaydedilen register'lar · CFSR / HFSR · .map dosyasıyla adres eşleme

**Gerekenler:** STM32 geliştirme kartı; Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Her hata için hatalı satır PC değerinden bulunmuş.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g094"></a>

## 094 · FreeRTOS ile ilk görevler

`Ana görev` · Önkoşul: 093

**Amaç.** CubeMX'te FreeRTOS'u etkinleştir; LED, buton ve UART işlerini üç ayrı görevde (task) çalıştır. vTaskDelay ile vTaskDelayUntil arasındaki farkı ölç.

**Araştır:** görev (task) · öncelik · zamanlayıcı (scheduler) · stack boyutu · tick

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Periyodik görevin periyodu ölçülmüş; iki gecikme fonksiyonunun farkı gösterilmiş.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g095"></a>

## 095 · Çok görevli veri sistemi

`Mini uygulama` · Önkoşul: 094

**Amaç.** Sensör görevi → kuyruk → filtre görevi → kuyruk → haberleşme görevi zinciri kur. UART'ı mutex ile paylaş. Her görevin çalışma süresini ve stack kullanımını raporla.

**Araştır:** queue · mutex · stack high water mark

**Gerekenler:** STM32 geliştirme kartı; IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin); Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü)

**Başarı ölçütü**

- Veri kaybı yok.
- Stack kullanımları raporlanmış.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli
