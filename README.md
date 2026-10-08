# STM32-150

HAL ile LED yakmaktan steer-by-wire eğitim prototipine: 100 ana görev, 25 pekiştirme ve 25 ileri görev.

[Kurulum](KURULUM.md) · [150 görev](GOREVLER.md) · [Kişisel ilerleme](ILERLEME.md) · [Çalışma düzeni](CALISMA-DUZENI.md)

## Düzen

1. Ortak depo: `stm32-150-mufredat`. Görevlerin ve açıklamaların kaynağı.
2. Her katılımcı: Use this template ile kendi `stm32-embedded-lab` deposunu oluşturur.
3. Kod ve rapor: `cozumler/NNN-gorev-adi/` içine eklenir.
4. Başlangıçta yalnızca 001–015 için issue açılır. Sonraki modüller sırayla eklenir.
5. Final proje ayrı bir kişisel depoda sunulur. CV bağlantısı bu projeye gider.

Birlikte aynı konuyu çalışıyoruz. Her kişi kendi kodunu açıklayabilmeli ve çalıştırabilmeli. Ortak yazılan kodda katkılar belirtilir.

## Çalışma ortamı

Ana ortam Wokwi. Ücretsiz tarayıcı planı ile VS Code lisansı aynı şey değildir. [Kurulumdaki](KURULUM.md) ilk HAL LED deneyi geçmeden ortamı hazır saymayın.

Motor için matematiksel model, encoder için kodlanmış A/B üreteci hazırlanacak. Bu paket hazır encoder firmware'i veya doğrulanmış Wokwi projesi içermez. Timer encoder modu ve diğer çevre birimleri ayrıca sınanır. DMA/CAN gibi desteklenmeyen donanım görevleri bekleyen olarak kalır. Finalin Wokwi sürümünde UART ve sanal motor kullanılır, CAN doğrulaması ayrı tutulur.

## Görevlerin tamamlanması

Kaynak + kısa rapor + başarı ölçütü kanıtı gerekir. Issue'yu yalnızca gerçekten tamamlandığında completed nedeni ile kapatın. Ertelenen veya desteklenmeyen görevleri açık bırakın. Plan dışı kapatılan görevler ilerleme sayacına girmez.

## Müfredat bakımı

`gorevler.json` tek kaynaktır. Düzenledikten sonra:

```bash
python3 scripts/md_uret.py
python3 scripts/dogrula.py
```

Kişisel kontrol listesi yeniden üretimde sıfırlanmaz. Template güncellemeleri kişisel depolara otomatik aktarılmaz. Mevcut issue metinleri de kendiliğinden güncellenmez.

## Bölümler

- M01 · 001–015: GPIO, Zamanlama ve Durum Makineleri
- M02 · 016–030: Kesmeler, Timer, PWM ve ADC
- M03 · 031–045: UART, Komut İşleme, DMA ve Veri Kaydı
- M04 · 046–060: I²C, SPI, Sensörler, Ekran ve Sürücü Yazma
- M05 · 061–075: Motor, Encoder, Hız ve Konum Kontrolü
- M06 · 076–085: IMU, Kalibrasyon ve Filtreler
- M07 · 086–095: CAN, Hata Yönetimi, Watchdog ve FreeRTOS
- M08 · 096–100: Bitirme Projesi: Steer-by-Wire Prototipi
- M09 · 101–125: Pekiştirme
- M10 · 126–150: İleri Görevler

## İlk teslim

001: HAL ile LED yak. Kod, Wokwi bağlantısı, MCU modeli ve sonucun görüntüsüyle birlikte raporla. Tamamlanmamış şablon repo henüz CV projesi değildir.
