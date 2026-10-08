# Çalışma düzeni

## Herkes kendi deposunda

Ortak müfredatı template olarak kullan. Birlikte öğren, kendi çözümünü kendi kişisel depone ekle. Public depoda yorum için herkese yazma yetkisi vermek gerekmez. Collaborator yalnızca gerçekten yazma erişimi gerektiğinde eklenir.

## Bir görevin akışı

1. Issue içindeki görevi oku. Görev numarası ile GitHub issue numarasını ayır.
2. Çalışma ağacı temizken güncel ana daldan görev dalı aç:

```bash
git switch main
git pull --ff-only
git switch -c gorev/001-led
mkdir -p cozumler/001-led
cp cozumler/_sablon/README.md cozumler/001-led/README.md
```

3. Kodu, yapılandırmayı ve raporu bu klasörde hazırla.
4. Anlamlı aşamalarda kaydet:

```bash
git add cozumler/001-led
git commit -m "[001] HAL LED uygulamasi ve test kaydi"
git push -u origin gorev/001-led
gh pr create --title "[001] HAL LED" --body-file .github/pull_request_template.md
```

5. PR açıklamasını düzenle. Gerçek issue numarasıyla `Closes #N` yaz. Şablondaki N'yi bırakma.
6. Arkadaşın kaynak ve raporu incelesin. İlk görevlerde formal review şart değildir, kendi incelemeni rapora ekleyebilirsin.
7. PR birleşince doğru issue'nun completed olarak kapandığını kontrol et. `ILERLEME.md` kutusunu işaretle.

## Bitti tanımı

Kaynak yeniden derleniyor, başarı ölçütü kanıtlı, ortam belirtilmiş ve kendi açıklaman mevcut. Sırf issue kapandı diye teknik doğrulama yapılmış olmaz. Desteklenmeyen görev açık kalır. Vazgeçilen issue not planned olarak kapatılır ve tamamlanma sayısına girmez.

## Kaynak dosyaları

`.ioc`, Core, startup, linker script, derleme yapılandırması ve kullanılan bağımlılıklar korunur. Drivers/Middlewares otomatik olarak dışlanmaz. Harici paketleri depoya almıyorsan sürüm ve yeniden edinme adımını belgele. Üçüncü taraf lisanslarını koru. Debug, Release, nesne dosyaları, IDE önbelleği ve büyük videolar depoya girmez. Çalışan binary gerekiyorsa sürüm ekine konur.

## Wokwi teslimi

Wokwi proje URL'si, `diagram.json`, kullanılan MCU, kaynak kod ve varsa custom chip dosyaları bulunmalı. Çalıştırma yoluna göre `wokwi.toml` ekle. Lisans veya erişim sınırını belirt. İmkânsız bir çevre birimini yazılım alternatifiyle değiştirdiysen raporda ayrı yaz.

## Birlikte çalışma

Her bölüm sonunda herkes kendi çalışmasını gösterir. Aynı kod birlikte yazıldıysa katkıları belirt. Bir kişi yalnız filtreyi, başka kişi yalnız haberleşmeyi öğrenmekle kalmasın. Ana müfredatta düzeltme olunca kişisel çözümleri silmeden ilgili görev tanımını güncelle.

## Final

096–100 Wokwi tabanlı steer-by-wire eğitim prototipini birleştirir. 150. görevde temiz bir final deposu oluştur. Kaynak, derleme adımları, mimari, demo, ölçümler ve kişisel katkı bulunmalı. CV'deki sayılar test raporundan gelmeli.
