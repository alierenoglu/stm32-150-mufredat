<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M02 · Kesmeler, Timer, PWM ve ADC

Görevler 016–030 · [Tüm görevler](../GOREVLER.md) · [Simülasyon rehberi](../docs/simulasyon.md)

Kesmeler ve öncelikleri, clock ağacı, timer hesapları, PWM, input capture ve ADC. Modül, ilk aç-kapa kontrolcünle (histerezisli termostat) biter.

---

<a id="g016"></a>

## 016 · Harici kesme (EXTI) ile buton

`Ana görev` · Önkoşul: 015

**Amaç.** Butonu polling yerine EXTI kesmesiyle oku. Callback içinde yalnızca bayrak kur, LED'i ana döngüde değiştir.

**Araştır:** EXTI · NVIC · HAL_GPIO_EXTI_Callback · volatile

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar)

**Başarı ölçütü**

- Ana döngü başka iş yaparken bile basış kaçmıyor.
- Callback birkaç satırdan uzun değil.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g017"></a>

## 017 · Timer kesmesi

`Ana görev` · Önkoşul: 016

**Amaç.** Bir timer'ı 2 Hz kesme üretecek şekilde ayarla ve LED'i kesmede değiştir. Prescaler ve ARR değerlerini kendin hesapla.

**Araştır:** timer clock'u · prescaler · ARR · update event · HAL_TIM_PeriodElapsedCallback

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- PSC ve ARR hesabı README dosyasında.
- 2 Hz timer kesmesinde 10 kesme aralığı 5 s sürer. Her kesmede LED tersleniyorsa LED tam çevrimi 1 Hz olur.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g018"></a>

## 018 · Clock ağacı

`Ana görev` · Önkoşul: 017

**Amaç.** Sistem clock'unu iç osilatörden PLL ile kartının en yüksek hızına çıkar. Timer clock'unun nasıl değiştiğini hesapla ve 17. görevdeki timer aynı frekansta kalsın diye değerleri yeniden hesapla.

**Araştır:** HSI ve HSE · PLL · AHB/APB bölücüleri · APB timer clock çarpanı · flash wait state

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- SystemCoreClock beklenen değeri gösteriyor.
- Timer frekansı clock değişiminden sonra da doğru.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Blue Pill'in (F103) en yüksek hızı 72 MHz.

---

<a id="g019"></a>

## 019 · Kesme öncelikleri

`Ana görev` · Önkoşul: 018

**Amaç.** Buton kesmesinin callback'ine kasıtlı olarak uzun bir bekleme koy ve timer kesmesiyle çalışan LED'in nasıl bozulduğunu gözle. Sonra öncelikleri değiştir ve farkı açıkla. En sonunda doğru çözümü uygula: kesmede bekleme yapma.

**Araştır:** NVIC öncelik grupları · preemption · kesme gecikmesi

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar)

**Başarı ölçütü**

- Üç durumun gözlemi README'de: eşit öncelik, timer daha öncelikli, düzeltilmiş tasarım.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g020"></a>

## 020 · Kronometre

`Mini uygulama` · Önkoşul: 019

**Amaç.** Timer kesmesiyle 1 ms çözünürlüklü kronometre yap. Bir buton başlatıp durdursun, uzun basış sıfırlasın. Süre debugger'da izlensin, her saniye bir LED yanıp sönsün.

**Araştır:** timer tabanlı zaman sayacı · HSI ve HSE doğruluğu · 12. görevdeki buton olayları

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- 1 dakikalık ölçümde telefon kronometresine göre fark raporlanmış; HSI ile HSE arasındaki farkı açıklıyorsun.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g021"></a>

## 021 · PWM ile LED parlaklığı

`Ana görev` · Önkoşul: 020

**Amaç.** Bir timer kanalından PWM üret ve duty cycle ile LED parlaklığını ayarla (%10, %50, %90).

**Araştır:** PWM modu · CCR · duty cycle · PWM frekansı seçimi · pinin timer kanalı (alternatif fonksiyon)

**Gerekenler:** STM32 geliştirme kartı; Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Üç seviye gözle ayırt ediliyor.
- PWM frekansı ve hesabı README'de.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g022"></a>

## 022 · Nefes alan LED

`Ana görev` · Önkoşul: 021

**Amaç.** Parlaklık 2 saniyede yumuşakça artıp azalsın. Duty, timer kesmesiyle sabit aralıklarla güncellensin.

**Araştır:** timer kesmesi ile güncelleme · rampa üretimi

**Gerekenler:** STM32 geliştirme kartı; Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Ana döngü boşken animasyon devam ediyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g023"></a>

## 023 · Butonla parlaklık ve gama düzeltmesi

`Ana görev` · Önkoşul: 022

**Amaç.** İki butonla parlaklığı 10 kademede artırıp azalt; sınırlarda dur. Doğrusal duty artışının göze doğrusal gelmediğini gözle ve gama düzeltmesi tablosu ekle.

**Araştır:** algısal parlaklık · gama düzeltmesi · lookup table

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Gama tablolu sürümde kademeler eşit aralıklı görünüyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g024"></a>

## 024 · Input capture ile frekans ölçümü

`Ana görev` · Önkoşul: 023

**Amaç.** Bir timer'ın ürettiği PWM sinyalini kabloyla başka bir timer'ın input capture girişine bağla; frekansı ve duty'yi ölç.

**Araştır:** input capture · PWM input modu · sayaç taşması

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- 100 Hz–10 kHz arasında 3 frekansta ölçüm hatası %1'in altında.

**Simülasyon:** ❔ Wokwi desteği belirsiz, dene. Input capture'ın simüle edildiği dokümanda yazmıyor; Wokwi'nin clock generator parçasıyla dene.

---

<a id="g025"></a>

## 025 · Geri sayım alarmı

`Mini uygulama` · Önkoşul: 024

**Amaç.** Butonla 10'ar saniyelik adımlarla süre ayarla, uzun basışla geri sayımı başlat. Süre dolunca buzzer PWM ile ötsün ve LED yanıp sönsün; herhangi bir basış alarmı sustursun.

**Araştır:** buzzer ve PWM frekansı (ton) · durum makinesi

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Pasif buzzer; Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Ayar, sayım ve alarm durumları README'deki diyagramla aynı çalışıyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g026"></a>

## 026 · ADC ile potansiyometre

`Ana görev` · Önkoşul: 025

**Amaç.** Potansiyometreyi ADC ile oku (tek dönüşüm, polling). Ham değeri mV'a çevir ve debugger'da izle.

**Araştır:** ADC çözünürlüğü · referans voltajı · örnekleme süresi · HAL_ADC_Start / PollForConversion

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ)

**Başarı ölçütü**

- Uçlarda yaklaşık 0 ve 3300 mV görülüyor.
- Multimetren varsa ölçümle karşılaştırılmış.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Wokwi'de ADC1'in yalnızca temel dönüşümü var.

---

<a id="g027"></a>

## 027 · Potansiyometreyle parlaklık

`Ana görev` · Önkoşul: 026

**Amaç.** Okunan ADC değerine göre PWM duty'yi ayarla. Uçlarda tam sönük ve tam parlak olsun.

**Araştır:** değer eşleme (mapping) · ADC gürültüsü

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Pot sabitken parlaklık titriyorsa nedenini README'de açıklıyorsun.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g028"></a>

## 028 · Hareketli ortalama filtresi

`Ana görev` · Önkoşul: 027

**Amaç.** ADC'ye N örneklik hareketli ortalama uygula. Ham ve filtreli değeri karşılaştır; N = 4, 16 ve 64 için gürültüyü ve gecikmeyi kıyasla.

**Araştır:** hareketli ortalama · dairesel dizi · gecikme-gürültü dengesi · STM32CubeMonitor

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ)

**Başarı ölçütü**

- Üç N değeri için gürültü (min-max) ve gecikme tablosu README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Simülasyondaki potansiyometre gürültüsüz; gürültüyü yazılımla ekle ya da gerçek kartta dene.

---

<a id="g029"></a>

## 029 · Çok kanallı ADC ve dahili sensörler

`Ana görev` · Önkoşul: 028

**Amaç.** İki potansiyometreyi ADC scan moduyla oku; birini parlaklık, diğerini yanıp sönme hızı için kullan. Ayrıca çipin dahili sıcaklık sensörünü ve Vrefint kanalını oku.

**Araştır:** scan mode · rank · dahili sıcaklık sensörü · Vrefint ile besleme voltajı hesabı

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ)

**Başarı ölçütü**

- İki kontrol birbirini etkilemiyor.
- Sıcaklık değeri makul; sensörün doğruluk sınırları README'de.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. Wokwi'de ADC kısmi; kanalları tek tek oku, dahili sensörleri gerçek kartta dene.

---

<a id="g030"></a>

## 030 · Histerezisli termostat

`Mini uygulama` · Önkoşul: 029

**Amaç.** Bir pot hedef sıcaklığı, diğer pot (ya da dahili sıcaklık sensörü) ölçülen sıcaklığı temsil etsin. Ölçüm hedefin altına düşünce “ısıtıcı” LED'i yansın, üstüne çıkınca sönsün. Önce histerezissiz, sonra histerezisli yap.

**Araştır:** aç-kapa (on-off) kontrol · histerezis · titreşim (chattering)

**Gerekenler:** STM32 geliştirme kartı; Potansiyometre (10 kΩ); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Histerezissiz sürümde eşik civarındaki titreme gösteriliyor.
- Histerezisli sürümde titreme yok.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli
