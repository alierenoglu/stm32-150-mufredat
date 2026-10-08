<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# M01 · GPIO, Zamanlama ve Durum Makineleri

Görevler 001–015 · [Tüm görevler](../GOREVLER.md)

Proje kurulumu, debugger, GPIO, bloklamayan zamanlama, buton olayları ve durum makineleri. Modülün sonunda kodunu modüllere ayırmış ve zamanı bloklamadan yönetiyor olacaksın.

---

<a id="g001"></a>

## 001 · HAL ile LED yak

`Ana görev` · Önkoşul: —

**Amaç.** CubeMX'te kartını seçip bir LED pinini GPIO çıkışı yap, kodu üret ve CubeIDE'de HAL ile LED'i yak, sonra söndür.

**Araştır:** CubeMX'te proje oluşturma · GPIO çıkış modu · HAL_GPIO_WritePin · CubeMX projesini CubeIDE'ye aktarma

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- Program karta (veya simülatöre) yüklenince LED yanıyor.
- Kodu değiştirip LED'i söndürebiliyor ve tekrar yükleyebiliyorsun.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Önce ücretsiz tarayıcı HAL örneğiyle LED deneyini doğrula. Harici ELF yükleme/VS Code yolunda lisans ve hedef MCU eşleşmesini ayrıca kontrol et. KURULUM.md dosyasına bak.

---

<a id="g002"></a>

## 002 · Debugger ile adım adım çalıştır

`Ana görev` · Önkoşul: 001

**Amaç.** Programı debug modunda başlat. Breakpoint koy, satır satır ilerle, bir değişkeni izle ve LED'in bağlı olduğu GPIO portunun ODR register'ını debugger'da gör.

**Araştır:** breakpoint · step over / step into · Live Expressions / Watch · SFR görünümü · ODR register'ı

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- LED satırında durup bir adım ilerlediğinde ODR'deki ilgili bitin değiştiğini gösteriyorsun.
- Çalışma sırasında bir değişkenin değerini debugger'dan değiştirebiliyorsun.

**Simülasyon:** 🟡 Wokwi'de kısmen yapılır. GDB desteği bulunur. VS Code lisansı ve debugger bağlantısı ayrı doğrulanmalı. Ücretsiz tarayıcı kullanımında aynı iş akışını varsayma.

---

<a id="g003"></a>

## 003 · HAL_Delay ile yanıp sönen LED

`Ana görev` · Önkoşul: 002

**Amaç.** LED'i 500 ms yanık, 500 ms sönük olacak şekilde sürekli yakıp söndür.

**Araştır:** HAL_Delay · SysTick · HAL_GPIO_TogglePin

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- 10 periyodun toplam süresi kronometreyle yaklaşık 10 s.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g004"></a>

## 004 · Butonla LED

`Ana görev` · Önkoşul: 003

**Amaç.** Önce butona basılı tutunca LED yansın, bırakınca sönsün. Sonra davranışı değiştir: her basışta LED'in durumu bir kez değişsin; basılı tutmak durumu tekrar değiştirmesin.

**Araştır:** GPIO giriş modu · pull-up / pull-down · kenar algılama (önceki ve şimdiki durum)

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar)

**Başarı ölçütü**

- Basılı tutma modu doğru çalışıyor.
- Değiştirme modunda basılı tutunca LED titremiyor, durum bir kez değişiyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g005"></a>

## 005 · Debounce'lu ikili sayaç

`Mini uygulama` · Önkoşul: 004

**Amaç.** Her basışta bir sayaç artsın ve değeri 4 LED'de ikili sistemde gösterilsin (0–15, sonra 0). Önce filtresiz çalıştırıp butonun sıçramasını (bir basışın birden fazla sayılmasını) gözle, sonra yazılımla filtrele.

**Araştır:** buton sıçraması (bounce) · zaman tabanlı debounce · bit işlemleri ile ikili gösterim

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Filtresiz sürümde fazladan sayımları gösterebiliyorsun.
- Filtreli sürümde 20 basışta sayaç tam 20 artıyor (16'dan sonra başa dönerek).

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Simülasyondaki butonun sıçrayıp sıçramadığını kontrol et; sıçramıyorsa sıçramayı gerçek kartta gözle.

---

<a id="g006"></a>

## 006 · Kayan ışık

`Ana görev` · Önkoşul: 005

**Amaç.** Dört LED'i sırayla yak; son LED'den sonra başa dön. Sıra ve süre tek bir tabloda tanımlansın, LED pinleri koda dağılmasın.

**Araştır:** dizi ile pin tablosu · modüler aritmetik

**Gerekenler:** STM32 geliştirme kartı; Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Sırayı değiştirmek için sadece tabloyu değiştirmek yetiyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g007"></a>

## 007 · Butonla hız kademeleri

`Ana görev` · Önkoşul: 006

**Amaç.** Butonla kayan ışığın hızını üç kademe arasında döngüsel olarak değiştir. Bu görevde HAL_Delay kullan.

**Araştır:** durum değişkeni · kademe tablosu

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Her basış bir sonraki kademeye geçiriyor.
- HAL_Delay yüzünden bazı basışların kaçırıldığını gösteriyor ve nedenini README'de açıklıyorsun.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g008"></a>

## 008 · HAL_Delay olmadan zamanlama

`Ana görev` · Önkoşul: 007

**Amaç.** HAL_GetTick ile zamanı takip ederek LED'i yakıp söndür; ana döngü hiçbir yerde beklemesin. 7. görevi bu yöntemle yeniden yaz.

**Araştır:** bloklamayan (non-blocking) zamanlama · HAL_GetTick · işaretsiz tam sayı çıkarma

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Ana döngüde HAL_Delay yok.
- 7. görevdeki kaçırılan basış sorunu ortadan kalktı.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g009"></a>

## 009 · Bağımsız yazılım zamanlayıcıları

`Ana görev` · Önkoşul: 008

**Amaç.** İki LED'i farklı aralıklarla (ör. 300 ms ve 700 ms) bağımsız yakıp söndür, aynı anda butonu gecikmesiz oku. Zamanlayıcı mantığını tekrar kullanılabilir bir yapıya (struct + fonksiyon) çevir.

**Araştır:** struct · fonksiyon ile tekrar kullanılabilir kod · işbirlikçi (cooperative) zamanlama

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Üç iş aynı anda çalışıyor, buton tepkisi gecikmesiz.
- Yeni bir zamanlı iş eklemek 2–3 satır sürüyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g010"></a>

## 010 · Trafik lambası

`Mini uygulama` · Önkoşul: 009

**Amaç.** Araç için kırmızı-sarı-yeşil, yaya için kırmızı-yeşil lamba yap. Yaya butonuna basıldığında mevcut aşama tamamlanıp yayaya yeşil yansın. Mantığı durum makinesiyle kur.

**Araştır:** sonlu durum makinesi (FSM) · enum ve switch-case · durum geçiş diyagramı

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Durum geçiş diyagramı README'de.
- Basış hangi aşamada olursa olsun aşama tamamlanmadan geçiş olmuyor.
- Yaya yeşili bitince sistem normal döngüye dönüyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g011"></a>

## 011 · Kısa ve uzun basış

`Ana görev` · Önkoşul: 010

**Amaç.** Basış süresini ölç; kısa basışı (< 500 ms) ve uzun basışı (≥ 1 s) ayırt et, her birine farklı LED davranışı ata. Uzun basış, buton bırakılmadan algılansın.

**Araştır:** basış süresi ölçümü · eşik değerleri · durum makinesi

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- 10 kısa ve 10 uzun basışın hepsi doğru sınıflanıyor.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g012"></a>

## 012 · Olay tabanlı buton modülü

`Ana görev` · Önkoşul: 011

**Amaç.** Butonu kısa basış, uzun basış ve çift tıklama olayları üreten bir modüle çevir. Ana kod yalnızca bu olayları kullansın.

**Araştır:** olay (event) tabanlı tasarım · çift tıklama zaman penceresi

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Üç olay da güvenilir şekilde ayrılıyor.
- Ana döngüde buton zamanlamasına dair kod yok.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g013"></a>

## 013 · HAL'siz GPIO

`Ana görev` · Önkoşul: 012

**Amaç.** LED'i HAL fonksiyonu kullanmadan, doğrudan RCC ve GPIO register'larına yazarak yak. Ardından HAL_GPIO_WritePin'in içine debugger ile gir ve aynı register'a yazdığını göster.

**Araştır:** Reference Manual · memory map · RCC saat açma register'ı · MODER/CRL-CRH, ODR, BSRR (kartına göre)

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- Register'lı sürüm çalışıyor.
- BSRR'nin neden var olduğunu (atomik set/reset) README'de açıklıyorsun.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli. Blue Pill (F103) ile F4 serisinin GPIO register'ları farklı; kartının Reference Manual'ine bak.

---

<a id="g014"></a>

## 014 · Kodunu modüllere ayır

`Ana görev` · Önkoşul: 013

**Amaç.** Şu ana kadarki LED, buton ve zamanlayıcı kodunu led.c/h, button.c/h, soft_timer.c/h gibi modüllere ayır. main.c'de yalnızca başlatma ve ana döngü kalsın.

**Araştır:** header dosyası · static ve extern · arayüz ile uygulamayı ayırma · CubeMX'in USER CODE bölümleri

**Gerekenler:** STM32 geliştirme kartı

**Başarı ölçütü**

- CubeMX'te kod yeniden üretilince (Generate Code) senin kodun silinmiyor.
- Her modülün tek bir sorumluluğu var.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli

---

<a id="g015"></a>

## 015 · Reaksiyon süresi oyunu

`Mini uygulama` · Önkoşul: 014

**Amaç.** Rastgele 1–4 s bekledikten sonra LED yansın; oyuncu butona basınca tepki süresi ölçülsün. Erken basış faul sayılsın. Sonuç LED'lerle kademeli gösterilsin, en iyi skor debugger'da izlensin.

**Araştır:** sözde rastgele sayı üretimi · zaman ölçümü · durum makinesi

**Gerekenler:** STM32 geliştirme kartı; Ek buton(lar); Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa)

**Başarı ölçütü**

- Erken basış algılanıyor.
- Ölçüm çözünürlüğü 1 ms; 10 denemenin sonuçları README'de.

**Simülasyon:** ✅ Wokwi desteğine uygun, görev deneyi gerekli
