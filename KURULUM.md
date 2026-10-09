# Başlangıç

## 1. Kendi reponu oluştur

1. Ana repoda Use this template > Create a new repository.
2. Owner kendi hesabın. İsim `stm32-embedded-lab`, görünürlük Public.
3. Kendi depoyu bilgisayarına klonla. Aşağıdaki KULLANICI yerini değiştir:

```bash
git clone https://github.com/KULLANICI/stm32-embedded-lab.git
cd stm32-embedded-lab
```

4. `ILERLEME.md` başındaki kişisel alanları doldur.
5. Python 3 ve GitHub CLI kur. `gh auth login` ile giriş yap.
6. İlk modül için önce önizle, sonra oluştur:

```bash
python3 scripts/issue_olustur.py --repo KULLANICI/stm32-embedded-lab --sadece 1-15 --dry-run
python3 scripts/issue_olustur.py --repo KULLANICI/stm32-embedded-lab --sadece 1-15
```

Bütün görevleri bir anda istersen `--sadece 1-150` kullan. Aynı numaralı mevcut görevler yeniden açılmaz. Mevcut issue metinleri değiştirilmez. İleride 16-30 gibi sonraki aralığı ekle.

## 2. Wokwi'de ilk proje

[001 LED başlangıç dosyalarını](baslangic/001-led/README.md) aç ve oradaki adımları uygula. İlk hedef GPIO'yu kendin kurarak LED'i yakmak ve ardından söndürmek.

Seçtiğin MCU'ya uygun pinleri ve ayarları kullan. Görevlerdeki F103 destek etiketleri başka kartlar için doğrulama sayılmaz. F103 için derlenen program başka MCU'da kullanılmaz.

Tarayıcı ve VS Code erişimi farklıdır. Önce tarayıcıdaki HAL örneğini çalıştır. Yerel CubeIDE projesini Wokwi'ye bağlama adımında [erişim koşullarını](https://wokwi.com/pricing) kontrol et.

## 3. Bir görevi tamamla

Görevi `GOREVLER.md` üzerinden aç. İlk görev için:

```bash
mkdir -p cozumler/001-led
cp cozumler/_sablon/README.md cozumler/001-led/README.md
```

- Kaynak kodu, `diagram.json` dosyasını ve varsa özel bileşen dosyalarını bu klasöre koy.
- README'ye kullandığın kartı, Wokwi bağlantısını, çalıştırma adımlarını ve test sonucunu yaz.
- Görevin başarı ölçütlerini kontrol et. Sonucu ekran görüntüsü, log veya ölçümle göster.
- Tamamlandıysa `ILERLEME.md` içindeki kutuyu işaretle.

Değişiklikleri kontrol edip kaydet:

```bash
git status
git add cozumler/001-led ILERLEME.md
git commit -m "[001] HAL ile LED yakma"
git push
```

GitHub'da ilgili görev issue'sunu tamamlandı olarak kapat. Issue numarası görev numarasıyla aynı olmak zorunda değildir. Çalışmayan veya simülatörde doğrulanamayan görev açık kalır.

İlk görevlerde kendi repona doğrudan commit yeterli. Birlikte kod geliştirirken veya inceleme isterken branch ve PR kullanabilirsiniz.

## 4. Neleri saklayacaksın?

Projeyi yeniden çalıştırmak için gereken kaynakları ve ayarları sakla. CubeIDE kullanıyorsan `.ioc`, Core, startup, linker ve gerekli bağımlılıklar da buna dahildir. Derleme çıktıları ve IDE önbelleğini ekleme. Büyük videolar için bağlantı kullan.

Bir bölüm bitince çözümlerinizi birbirinize gösterin. Herkes kendi kodunu açıklayabilsin.
