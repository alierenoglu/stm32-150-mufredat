# STM32-150

STM32 HAL öğrenmek için 100 ana görev, 25 pekiştirme ve 25 ileri görev. Ana görevler steer-by-wire eğitim prototipiyle tamamlanır.

[Başlangıç](KURULUM.md) · [Görevler](GOREVLER.md) · [İlerleme](ILERLEME.md)

## Nasıl kullanılır?

1. Bu repoyu şablon olarak kullanıp kendi `stm32-embedded-lab` reponu oluştur.
2. Görevi oku, Wokwi'de uygula ve test et.
3. Kodunu, devre dosyanı ve kısa açıklamanı `cozumler/NNN-gorev-adi/` içine kaydet.
4. Commit ve push yap. Tamamlanan görevin issue'sunu kapat ve ilerleme kutusunu işaretle.

Herkes aynı konuları çalışır ve kendi çözümünü kendi reposunda tutar. Birlikte yazılan kodda katkılar belirtilir.

## Çalışma ortamı

Wokwi kullanıyoruz. [001 LED başlangıç dosyalarından](baslangic/001-led/README.md) başla. HAL derleme ortamı için bağlantıdaki örneği açıp boş şablon kodunu yerleştir. Motor ve encoder modeli ilgili görevde yazılacak. Simülatörde doğrulanamayan donanım görevleri açık kalır.

## Görevleri düzenlemek

Görevlerin kaynağı `gorevler.json` dosyasıdır. Değişiklikten sonra:

```bash
python3 scripts/md_uret.py
python3 scripts/dogrula.py
```

Şablondaki güncellemeler kişisel repolara ve mevcut issue'lara otomatik aktarılmaz.
