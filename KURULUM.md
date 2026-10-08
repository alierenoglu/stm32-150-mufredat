# Kurulum

## 1. Ana müfredat deposu: Ali

1. ZIP'i yeni bir klasöre aç. Eski çalışma klasörlerini silme.
2. Açılan `stm32-150` klasöründe bu dosya ve `gorevler.json` bulunmalı.
3. GitHub'da yeni repo oluştur: adı `stm32-150-mufredat`, Public. README, lisans veya gitignore ekletme; dosyalar pakette hazır.
4. Terminalde klasörün içine gir. Finder'dan klasörü Terminale sürükleyerek tam yolunu alabilirsin.
5. `pwd` ile doğru klasörü kontrol et. Komutları ev klasöründe çalıştırma.

Git kuruluysa:

```bash
git --version
git init -b main
git add .
git commit -m "STM32 150 gorevlik ortak mufredat"
git remote add origin https://github.com/alierenoglu/stm32-150-mufredat.git
git push -u origin main
```

Klasörde zaten Git deposu veya origin varsa hata aldığın noktada dur ve `git status` ile `git remote -v` çıktısını incele. `.git` silme veya zorla push yapma. Kimlik doğrulama için GitHub CLI (`gh auth login` ardından `gh auth setup-git`) veya GitHub Desktop kullan. GitHub hesap parolasıyla HTTPS push yapılmaz.

GitHub CLI kuruluysa boş depoyu web yerine `gh repo create stm32-150-mufredat --public --source . --push` ile oluşturabilirsin. Bu alternatifte önce `git remote add` ve `git push` çalıştırma. Daha önce oluşturulmuş depoyu tekrar oluşturmaya çalışma.

6. GitHub repo sayfasında Settings > General > Template repository seçeneğini işaretle.
7. Ana repoda 150 kişisel görev issue'su açma. Ana repo müfredat ve yardım içindir.

## 2. Her katılımcının kişisel deposu

1. Ana repoda Use this template > Create a new repository.
2. Owner kendi hesabın. İsim `stm32-embedded-lab`, görünürlük Public.
3. Kendi depoyu bilgisayarına klonla. Aşağıdaki KULLANICI yerini değiştir:

```bash
git clone https://github.com/KULLANICI/stm32-embedded-lab.git
cd stm32-embedded-lab
```

4. `ILERLEME.md` ve `PORTFOLYO.md` başındaki kişisel alanları doldur.
5. Python 3 ve GitHub CLI kur. `gh auth login` ile giriş yap.
6. İlk modül için önce önizle, sonra oluştur:

```bash
python3 scripts/issue_olustur.py --repo KULLANICI/stm32-embedded-lab --sadece 1-15 --dry-run
python3 scripts/issue_olustur.py --repo KULLANICI/stm32-embedded-lab --sadece 1-15
```

Bütün görevleri bir anda istersen `--sadece 1-150` kullan. Aynı numaralı mevcut görevler yeniden açılmaz. Mevcut issue metinleri değiştirilmez. İleride 16-30 gibi sonraki aralığı ekle.

## 3. Wokwi ve ilk HAL deneyi

Öncelik ücretsiz tarayıcıdaki public HAL örneğidir. Wokwi'nin resmî Nucleo C031/L031 sayfalarındaki HAL örneklerini açıp bir kopya oluştur. HAL_GPIO_WritePin kullanan ilk LED değişikliğini çalıştır. Arduino `digitalWrite` örneğini HAL projesi sanma.

- https://docs.wokwi.com/parts/board-st-nucleo-c031c6
- https://docs.wokwi.com/parts/board-st-nucleo-l031k6

Depodaki destek etiketleri Blue Pill F103 için başlangıç bilgisidir. C031/L031 örneği kullanırsan pinleri, clock'u ve timer numaralarını o karta göre seç. F103 için derlenmiş ELF başka MCU'da çalıştırılmaz.

CubeMX/CubeIDE ile yerel HAL geliştirme devam eder. Yerel ELF'i Wokwi'ye yükleme yolu ve VS Code lisansı ayrıca doğrulanmalıdır. Fiyat sayfasında Community ücretsiz public projeler için, VS Code ise Hobby+ özellikleri arasında listeleniyor. Ücretsiz hesap açılmasını sınırsız ücretsiz VS Code lisansı olarak kabul etme. Deneme erişimini kalıcı ücretsiz erişim sayma. Para ödemeden önce tarayıcı yolu ile ilk görev çalışsın.

- https://wokwi.com/pricing
- https://docs.wokwi.com/vscode/getting-started

Bu paket simülasyonu çalıştırılarak doğrulanmış firmware içermez. İlk başarılı projenin bağlantısını, MCU'sunu, derleme şeklini ve tarihini `docs/ortam-dogrulama.md` dosyasına yaz.

## 4. Her görev

[Çalışma düzenini](CALISMA-DUZENI.md) uygula. Issue numarası görev numarasıyla aynı olmak zorunda değildir. Kanıtı ekledikten sonra PR'ı birleştir, doğru issue'yu kapat ve ilerleme kutusunu işaretle.

## 5. Ekip takibi

Katılımcıların paylaşmayı seçtiği repo adreslerini `ekip.txt` içine `kullanici/repo` biçiminde ekle. Sonra:

```bash
python3 scripts/ilerleme.py --dosya ekip.txt --markdown
```

Çıktıyı `EKIP.md` dosyasına yapıştır. Bu komut ekrana tablo basar, dosyayı veya GitHub'ı değiştirmez.
