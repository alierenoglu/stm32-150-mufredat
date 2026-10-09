# 001 · Boş HAL başlangıcı

Kart: STM32 Nucleo-C031C6. Kartın üzerindeki LED PA5 pininde. Ek parça veya bağlantı gerekmiyor.

1. [Wokwi'nin STM32 HAL örneğini](https://wokwi.com/projects/365551778332549121) aç. Bu örneği HAL derleme ortamı için kullanıyoruz.
2. Giriş yap ve **Save** ile kendine ait bir kopya oluştur.
3. `main.c` sekmesindeki mevcut kodu bu klasördeki `main.c` içeriğiyle değiştir. Böylece örneğin hazır LED davranışı kalkar, GPIO ve LED komutunu sen yazarsın.
4. `diagram.json` sekmesindeki içeriği de buradaki `diagram.json` ile değiştir. Devrede yalnızca Nucleo kartı kalır.
5. Koddaki TODO 1–4 adımlarını sırayla tamamla. Önce LED'i yak, sonra kodu değiştirip söndür.
6. Simülasyonu başlat, sonucu gözle, kaydet ve kendi çözüm klasörüne kaynak dosyalarını ve proje bağlantısını ekle.

`MX_GPIO_Init` fonksiyonu pinin çalışma şeklini ayarladığın yer. `main` içindeki USER CODE bölümü LED'e komut verdiğin yer. Wokwi bu USER CODE yorumlarını otomatik oluşturmaz; burada öğrenme amaçlı bir düzen sağlıyorlar.

Bu şablonda LED'i yakan kod yok. Hazır derleme ortamı Wokwi'deki HAL örneğinden geliyor. Dosyaların simülatörde derlenmesi henüz doğrulanmadı; ilk çalıştırmada hata alırsan çıktıyı inceleyip şablonu düzelteceğiz.
