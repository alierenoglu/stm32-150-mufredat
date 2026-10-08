<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# Görev Listesi

100 ana görev sırayla ilerler; her beşinci görev önceki görevleri birleştiren bir mini uygulamadır. 96–100 bitirme projesidir. 101–125 pekiştirme ve 126–150 ileri görevler zorunlu değildir; önkoşulunu bitirdiğin anda yapabilirsin.

**Simülasyon (Wokwi, Blue Pill F103):** ✅ Wokwi desteğine uygun, görev deneyi gerekli · 🟡 Wokwi'de kısmen yapılır · ❔ Wokwi desteği belirsiz, dene · ❌ Wokwi ile donanım doğrulaması yok · 💻 Kart gerekmez, bilgisayarda  
Ayrıntı: [docs/simulasyon.md](docs/simulasyon.md)

| Modül | Görevler | Konu |
|---|---|---|
| [M01](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md) | 001–015 | GPIO, Zamanlama ve Durum Makineleri |
| [M02](gorevler/M02-kesmeler-timer-pwm-ve-adc.md) | 016–030 | Kesmeler, Timer, PWM ve ADC |
| [M03](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md) | 031–045 | UART, Komut İşleme, DMA ve Veri Kaydı |
| [M04](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md) | 046–060 | I²C, SPI, Sensörler, Ekran ve Sürücü Yazma |
| [M05](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md) | 061–075 | Motor, Encoder, Hız ve Konum Kontrolü |
| [M06](gorevler/M06-imu-kalibrasyon-ve-filtreler.md) | 076–085 | IMU, Kalibrasyon ve Filtreler |
| [M07](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md) | 086–095 | CAN, Hata Yönetimi, Watchdog ve FreeRTOS |
| [M08](gorevler/M08-bitirme-projesi-steer-by-wire-prototipi.md) | 096–100 | Bitirme Projesi: Steer-by-Wire Prototipi |
| [M09](gorevler/M09-pekistirme.md) | 101–125 | Pekiştirme |
| [M10](gorevler/M10-ileri-gorevler.md) | 126–150 | İleri Görevler |

## M01 · GPIO, Zamanlama ve Durum Makineleri

Proje kurulumu, debugger, GPIO, bloklamayan zamanlama, buton olayları ve durum makineleri. Modülün sonunda kodunu modüllere ayırmış ve zamanı bloklamadan yönetiyor olacaksın.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 001 | [HAL ile LED yak](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g001) | Ana görev | Kart | ✅ |
| 002 | [Debugger ile adım adım çalıştır](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g002) | Ana görev | Kart | 🟡 |
| 003 | [HAL_Delay ile yanıp sönen LED](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g003) | Ana görev | Kart | ✅ |
| 004 | [Butonla LED](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g004) | Ana görev | Kart, Buton | ✅ |
| 005 | [Debounce'lu ikili sayaç](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g005) | Mini uygulama | Kart, Buton, LED | ✅ |
| 006 | [Kayan ışık](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g006) | Ana görev | Kart, LED | ✅ |
| 007 | [Butonla hız kademeleri](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g007) | Ana görev | Kart, Buton, LED | ✅ |
| 008 | [HAL_Delay olmadan zamanlama](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g008) | Ana görev | Kart, Buton, LED | ✅ |
| 009 | [Bağımsız yazılım zamanlayıcıları](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g009) | Ana görev | Kart, Buton, LED | ✅ |
| 010 | [Trafik lambası](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g010) | Mini uygulama | Kart, Buton, LED | ✅ |
| 011 | [Kısa ve uzun basış](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g011) | Ana görev | Kart, Buton, LED | ✅ |
| 012 | [Olay tabanlı buton modülü](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g012) | Ana görev | Kart, Buton, LED | ✅ |
| 013 | [HAL'siz GPIO](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g013) | Ana görev | Kart | ✅ |
| 014 | [Kodunu modüllere ayır](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g014) | Ana görev | Kart | ✅ |
| 015 | [Reaksiyon süresi oyunu](gorevler/M01-gpio-zamanlama-ve-durum-makineleri.md#g015) | Mini uygulama | Kart, Buton, LED | ✅ |

## M02 · Kesmeler, Timer, PWM ve ADC

Kesmeler ve öncelikleri, clock ağacı, timer hesapları, PWM, input capture ve ADC. Modül, ilk aç-kapa kontrolcünle (histerezisli termostat) biter.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 016 | [Harici kesme (EXTI) ile buton](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g016) | Ana görev | Kart, Buton | ✅ |
| 017 | [Timer kesmesi](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g017) | Ana görev | Kart | ✅ |
| 018 | [Clock ağacı](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g018) | Ana görev | Kart | ✅ |
| 019 | [Kesme öncelikleri](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g019) | Ana görev | Kart, Buton | ✅ |
| 020 | [Kronometre](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g020) | Mini uygulama | Kart, Buton, LED | ✅ |
| 021 | [PWM ile LED parlaklığı](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g021) | Ana görev | Kart, LED | ✅ |
| 022 | [Nefes alan LED](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g022) | Ana görev | Kart, LED | ✅ |
| 023 | [Butonla parlaklık ve gama düzeltmesi](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g023) | Ana görev | Kart, Buton, LED | ✅ |
| 024 | [Input capture ile frekans ölçümü](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g024) | Ana görev | Kart | ❔ |
| 025 | [Geri sayım alarmı](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g025) | Mini uygulama | Kart, Buton, Buzzer, LED | ✅ |
| 026 | [ADC ile potansiyometre](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g026) | Ana görev | Kart, Pot | ✅ |
| 027 | [Potansiyometreyle parlaklık](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g027) | Ana görev | Kart, Pot, LED | ✅ |
| 028 | [Hareketli ortalama filtresi](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g028) | Ana görev | Kart, Pot | 🟡 |
| 029 | [Çok kanallı ADC ve dahili sensörler](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g029) | Ana görev | Kart, Pot | 🟡 |
| 030 | [Histerezisli termostat](gorevler/M02-kesmeler-timer-pwm-ve-adc.md#g030) | Mini uygulama | Kart, Pot, LED | ✅ |

## M03 · UART, Komut İşleme, DMA ve Veri Kaydı

Seri haberleşme, komut ayrıştırma, halka tampon, paket protokolü ve CRC, DMA, sabit örnekleme, Flash'a kayıt ve bilgisayarda canlı grafik. Bu modülün araçlarını sonraki her modülde veri görmek için kullanacaksın.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 031 | [UART ile ilk mesaj](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g031) | Ana görev | Kart, Seri bağlantı | ✅ |
| 032 | [printf yönlendirme](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g032) | Ana görev | Kart, Seri bağlantı, Pot | ✅ |
| 033 | [Karakter komutları](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g033) | Ana görev | Kart, Seri bağlantı, LED | ✅ |
| 034 | [Kesmeyle UART alımı](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g034) | Ana görev | Kart, Seri bağlantı, LED | ✅ |
| 035 | [Satır tabanlı komut arayüzü](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g035) | Mini uygulama | Kart, Seri bağlantı, LED | ✅ |
| 036 | [Halka tampon (ring buffer)](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g036) | Ana görev | Kart, Seri bağlantı | ✅ |
| 037 | [Sağlam komut ayrıştırıcı](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g037) | Ana görev | Kart, Seri bağlantı | ✅ |
| 038 | [Gönderim süresi ve DMA](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g038) | Ana görev | Kart, Seri bağlantı | 🟡 |
| 039 | [Paket protokolü ve CRC](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g039) | Ana görev | Kart, Seri bağlantı, Python | ✅ |
| 040 | [Paketli uzaktan kumanda](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g040) | Mini uygulama | Kart, Seri bağlantı, Python veya 2. kart, LED | ✅ |
| 041 | [ADC + DMA (dairesel tampon)](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g041) | Ana görev | Kart, Pot | ❌ |
| 042 | [Timer tetiklemeli örnekleme](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g042) | Ana görev | Kart, Pot | 🟡 |
| 043 | [Python ile canlı grafik ve kayıt](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g043) | Ana görev | Kart, Seri bağlantı, Python | ✅ |
| 044 | [Flash'a ayar kaydetme](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g044) | Ana görev | Kart, Seri bağlantı | ❔ |
| 045 | [Mini osiloskop](gorevler/M03-uart-komut-isleme-dma-ve-veri-kaydi.md#g045) | Mini uygulama | Kart, Pot, Seri bağlantı, Python | 🟡 |

## M04 · I²C, SPI, Sensörler, Ekran ve Sürücü Yazma

I²C ve SPI ile sensör okuma, register haritası, kesme ve bloklamasız okuma, kendi sürücü katmanını yazma, OLED ekran ve bağlantı hatalarından kurtulma.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 046 | [I²C hat tarama](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g046) | Ana görev | Kart, IMU veya OLED, Seri bağlantı | ✅ |
| 047 | [Kimlik register'ı](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g047) | Ana görev | Kart, IMU, Seri bağlantı | ✅ |
| 048 | [Register okuma-yazma katmanı](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g048) | Ana görev | Kart, IMU, Seri bağlantı | ✅ |
| 049 | [SPI ile sensör](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g049) | Ana görev | Kart, IMU | 🟡 |
| 050 | [Eğim LED'leri](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g050) | Mini uygulama | Kart, IMU, LED | ✅ |
| 051 | [Sensör konfigürasyonu](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g051) | Ana görev | Kart, IMU, Seri bağlantı | ❔ |
| 052 | [Data-ready kesmesi](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g052) | Ana görev | Kart, IMU | ❔ |
| 053 | [Bloklamasız sensör okuma](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g053) | Ana görev | Kart, IMU | 🟡 |
| 054 | [Bus'tan bağımsız sürücü](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g054) | Ana görev | Kart, IMU | ✅ |
| 055 | [Veri kaydedici](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g055) | Mini uygulama | Kart, IMU, Seri bağlantı, Python | ✅ |
| 056 | [OLED ekran sürücüsü](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g056) | Ana görev | Kart, OLED | ✅ |
| 057 | [Ekranda canlı veri](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g057) | Ana görev | Kart, IMU, OLED | ✅ |
| 058 | [DMA ile ekran güncelleme](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g058) | Ana görev | Kart, IMU, OLED | 🟡 |
| 059 | [Bağlantı hatasından kurtulma](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g059) | Ana görev | Kart, IMU | 🟡 |
| 060 | [Dijital su terazisi](gorevler/M04-i2c-spi-sensorler-ekran-ve-surucu-yazma.md#g060) | Mini uygulama | Kart, IMU, OLED, Buton | 🟡 |

## M05 · Motor, Encoder, Hız ve Konum Kontrolü

DC motor, encoder, hız ve konum kontrolü. Wokwi yolunda 069 önce hazırlanır: motor modeli ve A/B üreteci kullanılır. Timer encoder modu ayrıca doğrulanır. Yazılımsal çözüm, donanım timer doğrulaması olarak raporlanmaz.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 061 | [DC motor sürme](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g061) | Ana görev | Kart, Motor veya Sanal motor, Seri bağlantı | 🟡 |
| 062 | [Rampa](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g062) | Ana görev | Kart, Motor | 🟡 |
| 063 | [PWM frekansı ve ölü bölge](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g063) | Ana görev | Kart, Motor | ❌ |
| 064 | [Encoder ile konum](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g064) | Ana görev | Kart, Motor | ❔ |
| 065 | [Motor test tezgâhı](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g065) | Mini uygulama | Kart, Motor, Seri bağlantı, Python | ❌ |
| 066 | [RPM hesabı](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g066) | Ana görev | Kart, Motor, Seri bağlantı | ❌ |
| 067 | [Hız filtresi](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g067) | Ana görev | Kart, Motor, Seri bağlantı, Python | ❌ |
| 068 | [Motoru tanı](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g068) | Ana görev | Kart, Motor, Seri bağlantı, Python | ❌ |
| 069 | [Sanal motor ve encoder üreteci](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g069) | Ana görev | Kart | 🟡 |
| 070 | [P ile hız sabitleyici](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g070) | Mini uygulama | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 071 | [PI hız kontrolü](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g071) | Ana görev | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 072 | [Anti-windup](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g072) | Ana görev | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 073 | [Bozucu etkiye karşı](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g073) | Ana görev | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 074 | [Kaskat konum kontrolü](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g074) | Ana görev | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 075 | [Konum servosu](gorevler/M05-motor-encoder-hiz-ve-konum-kontrolu.md#g075) | Mini uygulama | Kart, Motor veya Sanal motor, Pot, Seri bağlantı, Python | 🟡 |

## M06 · IMU, Kalibrasyon ve Filtreler

Jiroskop bias'ı ve kayma, ivmeölçerden açı, kalibrasyon, sabit örnekleme, complementary ve Kalman filtreleri. Filtreleri aynı kayıt üzerinde karşılaştırıp kartta ve bilgisayarda aynı sonucu aldığını göstereceksin.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 076 | [Jiroskop ve bias](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g076) | Ana görev | Kart, IMU, Seri bağlantı | 🟡 |
| 077 | [Açı entegrasyonu ve kayma](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g077) | Ana görev | Kart, IMU, Seri bağlantı, Python | 🟡 |
| 078 | [İvmeölçerden açı](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g078) | Ana görev | Kart, IMU, Seri bağlantı, Python | 🟡 |
| 079 | [İvmeölçer kalibrasyonu](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g079) | Ana görev | Kart, IMU, Seri bağlantı | ❌ |
| 080 | [Kalibrasyon sihirbazı](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g080) | Mini uygulama | Kart, IMU, Buton, Seri bağlantı veya OLED | 🟡 |
| 081 | [Sabit örnekleme ve dt](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g081) | Ana görev | Kart, IMU, Seri bağlantı | ✅ |
| 082 | [Complementary filtre](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g082) | Ana görev | Kart, IMU, Seri bağlantı, Python | 🟡 |
| 083 | [Kalman filtresi](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g083) | Ana görev | Kart, IMU, Seri bağlantı, Python | 🟡 |
| 084 | [Filtreleri karşılaştır](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g084) | Ana görev | Kart, IMU, Seri bağlantı, Python | 🟡 |
| 085 | [Yapay ufuk](gorevler/M06-imu-kalibrasyon-ve-filtreler.md#g085) | Mini uygulama | Kart, IMU, OLED veya Python | ✅ |

## M07 · CAN, Hata Yönetimi, Watchdog ve FreeRTOS

CAN haberleşmesi ve hata durumları, watchdog, hata yönetimi durum makinesi, HardFault analizi ve FreeRTOS temelleri.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 086 | [CAN loopback](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g086) | Ana görev | Kart | ❌ |
| 087 | [İki kart arası CAN](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g087) | Ana görev | Kart, 2. kart, CAN | ❌ |
| 088 | [CAN mesaj tasarımı](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g088) | Ana görev | Kart, 2. kart, CAN | ❌ |
| 089 | [CAN hata durumları](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g089) | Ana görev | Kart, 2. kart, CAN | ❌ |
| 090 | [CAN ile uzaktan motor](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g090) | Mini uygulama | Kart, 2. kart, CAN, Motor veya Sanal motor, Seri bağlantı | ❌ |
| 091 | [Watchdog](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g091) | Ana görev | Kart, Seri bağlantı | 🟡 |
| 092 | [Hata yönetimi durum makinesi](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g092) | Ana görev | Kart, Motor veya Sanal motor, Buton, Seri bağlantı | 🟡 |
| 093 | [HardFault analizi](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g093) | Ana görev | Kart, Seri bağlantı | ✅ |
| 094 | [FreeRTOS ile ilk görevler](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g094) | Ana görev | Kart, Buton, Seri bağlantı | ✅ |
| 095 | [Çok görevli veri sistemi](gorevler/M07-can-hata-yonetimi-watchdog-ve-freertos.md#g095) | Mini uygulama | Kart, IMU, Seri bağlantı | ✅ |

## M08 · Bitirme Projesi: Steer-by-Wire Prototipi

Steer-by-wire eğitim prototipi. Wokwi sürümünde IMU veya kayıt girdisi, UART mesajları ve sanal motor kullanılır. CAN sürümü ayrı bir donanım doğrulama aşamasıdır. Gerçek araçta kullanıma yönelik bir sistem değildir.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 096 | [Gereksinimler ve mimari](gorevler/M08-bitirme-projesi-steer-by-wire-prototipi.md#g096) | Bitirme projesi | — | 💻 |
| 097 | [Kumanda düğümü](gorevler/M08-bitirme-projesi-steer-by-wire-prototipi.md#g097) | Bitirme projesi | Kart, IMU, OLED | 🟡 |
| 098 | [Aktüatör düğümü](gorevler/M08-bitirme-projesi-steer-by-wire-prototipi.md#g098) | Bitirme projesi | Motor veya Sanal motor | 🟡 |
| 099 | [Güvenlik ve hata enjeksiyonu](gorevler/M08-bitirme-projesi-steer-by-wire-prototipi.md#g099) | Bitirme projesi | Kart, Motor veya Sanal motor, IMU | 🟡 |
| 100 | [Doğrulama ve sürüm](gorevler/M08-bitirme-projesi-steer-by-wire-prototipi.md#g100) | Bitirme projesi | Kart, Motor veya Sanal motor, IMU, Seri bağlantı, Python | 🟡 |

## M09 · Pekiştirme

Hata bulma, ölçme, karşılaştırma ve farklı koşullarda deneme. Zorunlu değil. Her görevin önkoşulu belirtilmiş; o ana görevi bitirdikten sonra istediğin zaman yapabilirsin.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 101 | [Tablo tabanlı durum makinesi](gorevler/M09-pekistirme.md#g101) | Pekiştirme | Kart, Buton, LED | ✅ |
| 102 | [Hata bul: zaman sayacı taşması](gorevler/M09-pekistirme.md#g102) | Pekiştirme | Kart | ✅ |
| 103 | [Hata bul: volatile](gorevler/M09-pekistirme.md#g103) | Pekiştirme | Kart, Buton | ✅ |
| 104 | [Zamanı bağımsız ölç](gorevler/M09-pekistirme.md#g104) | Pekiştirme | Kart, Logic analyzer | ✅ |
| 105 | [Kesmede uzun iş](gorevler/M09-pekistirme.md#g105) | Pekiştirme | Kart | ✅ |
| 106 | [PWM çözünürlüğü ve frekansı](gorevler/M09-pekistirme.md#g106) | Pekiştirme | Kart | ✅ |
| 107 | [Filtre karşılaştırması](gorevler/M09-pekistirme.md#g107) | Pekiştirme | Kart, Pot | 🟡 |
| 108 | [Halka tampon birim testi](gorevler/M09-pekistirme.md#g108) | Pekiştirme | — | 💻 |
| 109 | [CRC doğrulama](gorevler/M09-pekistirme.md#g109) | Pekiştirme | Python | 💻 |
| 110 | [Bozuk paket testi](gorevler/M09-pekistirme.md#g110) | Pekiştirme | Kart, Seri bağlantı, Python | ✅ |
| 111 | [Aliasing](gorevler/M09-pekistirme.md#g111) | Pekiştirme | Kart, RC filtre, Seri bağlantı, Python | ❌ |
| 112 | [Güç kesilmesine dayanıklı kayıt](gorevler/M09-pekistirme.md#g112) | Pekiştirme | Kart, Seri bağlantı | ❌ |
| 113 | [I²C hattı kilitlenmesi](gorevler/M09-pekistirme.md#g113) | Pekiştirme | Kart, IMU | ❌ |
| 114 | [CPU yükü ölçümü](gorevler/M09-pekistirme.md#g114) | Pekiştirme | Kart, IMU | 🟡 |
| 115 | [Ekran optimizasyonu](gorevler/M09-pekistirme.md#g115) | Pekiştirme | Kart, OLED | ✅ |
| 116 | [Ölü bölge telafisi](gorevler/M09-pekistirme.md#g116) | Pekiştirme | Kart, Motor | ❌ |
| 117 | [Sistematik PI ayarı](gorevler/M09-pekistirme.md#g117) | Pekiştirme | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 118 | [Kontrol frekansının etkisi](gorevler/M09-pekistirme.md#g118) | Pekiştirme | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 119 | [Türev terimi](gorevler/M09-pekistirme.md#g119) | Pekiştirme | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 120 | [Hareket profili](gorevler/M09-pekistirme.md#g120) | Pekiştirme | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 121 | [Kalman duyarlılık analizi](gorevler/M09-pekistirme.md#g121) | Pekiştirme | Python | 💻 |
| 122 | [Sensör hata senaryoları](gorevler/M09-pekistirme.md#g122) | Pekiştirme | Python | 💻 |
| 123 | [CAN bus yükü](gorevler/M09-pekistirme.md#g123) | Pekiştirme | Kart, 2. kart, CAN | ❌ |
| 124 | [Durum makinesi testleri](gorevler/M09-pekistirme.md#g124) | Pekiştirme | — | 💻 |
| 125 | [Öncelik terslenmesi](gorevler/M09-pekistirme.md#g125) | Pekiştirme | Kart, Seri bağlantı | ✅ |

## M10 · İleri Görevler

Veri kaydı, bootloader, gelişmiş kestirim ve kontrol, test/CI altyapısı ve bitirme projesinin genişletilmesi. Zorunlu değil; 150. görev (portföy) herkes için önerilir.

| No | Görev | Tür | Gerekenler | Wokwi |
|---|---|---|---|---|
| 126 | [SD karta kayıt](gorevler/M10-ileri-gorevler.md#g126) | İleri görev | Kart, microSD | ❔ |
| 127 | [Yüksek hızlı kayıt](gorevler/M10-ileri-gorevler.md#g127) | İleri görev | Kart, IMU, microSD | ❌ |
| 128 | [Düğümler arası zaman senkronu](gorevler/M10-ileri-gorevler.md#g128) | İleri görev | Kart, 2. kart, CAN | ❌ |
| 129 | [USB CDC telemetri](gorevler/M10-ileri-gorevler.md#g129) | İleri görev | Kart, Python | ❌ |
| 130 | [Bootloader temelleri](gorevler/M10-ileri-gorevler.md#g130) | İleri görev | Kart, Seri bağlantı | ❔ |
| 131 | [UART ile firmware güncelleme](gorevler/M10-ileri-gorevler.md#g131) | İleri görev | Kart, Seri bağlantı, Python | ❔ |
| 132 | [Düşük güç modları](gorevler/M10-ileri-gorevler.md#g132) | İleri görev | Kart, Buton | ❌ |
| 133 | [CMSIS-DSP ile filtre ve FFT](gorevler/M10-ileri-gorevler.md#g133) | İleri görev | Kart, Pot, Seri bağlantı, Python | 🟡 |
| 134 | [Sabit noktalı aritmetik](gorevler/M10-ileri-gorevler.md#g134) | İleri görev | Kart, Seri bağlantı | ✅ |
| 135 | [Genel Kalman filtresi](gorevler/M10-ileri-gorevler.md#g135) | İleri görev | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 136 | [Kestirimle hız kontrolü](gorevler/M10-ileri-gorevler.md#g136) | İleri görev | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 137 | [İleri besleme](gorevler/M10-ileri-gorevler.md#g137) | İleri görev | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 138 | [LQR ile durum geri beslemesi](gorevler/M10-ileri-gorevler.md#g138) | İleri görev | Kart, Motor veya Sanal motor, Seri bağlantı, Python | 🟡 |
| 139 | [Sistem tanılama](gorevler/M10-ileri-gorevler.md#g139) | İleri görev | Kart, Motor, Seri bağlantı, Python | ❌ |
| 140 | [3D yönelim](gorevler/M10-ileri-gorevler.md#g140) | İleri görev | Kart, IMU, Seri bağlantı, Python | 🟡 |
| 141 | [Manyetometre ve yön](gorevler/M10-ileri-gorevler.md#g141) | İleri görev | Kart, IMU, Manyetometre, Seri bağlantı, Python | ❌ |
| 142 | [Sistemi RTOS üzerinde yeniden kur](gorevler/M10-ileri-gorevler.md#g142) | İleri görev | Kart, Seri bağlantı | 🟡 |
| 143 | [Birim test altyapısı](gorevler/M10-ileri-gorevler.md#g143) | İleri görev | — | 💻 |
| 144 | [Firmware'i CI'da derle](gorevler/M10-ileri-gorevler.md#g144) | İleri görev | — | 💻 |
| 145 | [Statik analiz](gorevler/M10-ileri-gorevler.md#g145) | İleri görev | — | 💻 |
| 146 | [CAN mesaj kataloğu ve PC aracı](gorevler/M10-ileri-gorevler.md#g146) | İleri görev | Kart, 2. kart, CAN, Seri bağlantı, Python | ❌ |
| 147 | [İki eksen](gorevler/M10-ileri-gorevler.md#g147) | İleri görev | Kart, 2. kart, CAN, Motor veya Sanal motor | 🟡 |
| 148 | [Kumanda tarafında arıza tespiti](gorevler/M10-ileri-gorevler.md#g148) | İleri görev | Kart, IMU, CAN | 🟡 |
| 149 | [Gecikme bütçesi](gorevler/M10-ileri-gorevler.md#g149) | İleri görev | Kart, 2. kart, CAN, Motor veya Sanal motor, Logic analyzer | ❌ |
| 150 | [Portföy](gorevler/M10-ileri-gorevler.md#g150) | İleri görev | — | 💻 |
