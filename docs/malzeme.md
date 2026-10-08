<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->

# Malzeme Listesi

Her parçanın ilk gerektiği görev ve kaç görevde kullanıldığı. “Alternatifli” görevlerde parça yerine başka bir seçenek de kullanılabilir (ör. motor yerine 069'daki sanal motor).

| Kod | Parça | İlk görev | Zorunlu olduğu görev sayısı | Alternatifli görev sayısı |
|---|---|---|---|---|
| KART | STM32 geliştirme kartı | 001 | 139 | 0 |
| LED | Ek LED'ler ve 220–330 Ω dirençler (kartta yeterli LED yoksa) | 005 | 22 | 0 |
| BTN | Ek buton(lar) | 004 | 21 | 0 |
| POT | Potansiyometre (10 kΩ) | 026 | 12 | 0 |
| BUZ | Pasif buzzer | 025 | 1 | 0 |
| SERI | Bilgisayara seri bağlantı (kartın sanal COM portu veya 3,3 V USB-UART dönüştürücü) | 031 | 65 | 1 |
| PY | Bilgisayarda Python 3 (pyserial, matplotlib/pyqtgraph) | 039 | 39 | 2 |
| IMU | IMU modülü: ivmeölçer + jiroskop (I²C ve SPI destekli olanı tercih edin) | 046 | 33 | 1 |
| OLED | SSD1306 I²C OLED ekran (128×64) | 046 | 6 | 3 |
| MOTOR | Encoder'lı redüktörlü DC motor, motor sürücü (ör. TB6612FNG) ve ayrı motor beslemesi | 061 | 9 | 22 |
| SANAL | Sanal motor ve encoder üreteci (Görev 069) | 061 | 0 | 22 |
| KART2 | İkinci STM32 kartı | 040 | 9 | 1 |
| CAN | 2 adet 3,3 V CAN transceiver modülü (ör. SN65HVD230) ve 2 adet 120 Ω direnç | 087 | 10 | 0 |
| SD | microSD kart modülü (SPI) | 126 | 2 | 0 |
| MAG | Manyetometre modülü | 141 | 1 | 0 |
| LA | Logic analyzer veya osiloskop (opsiyonel) | 104 | 2 | 0 |
| RC | Direnç ve kondansatör (RC filtre için) | 111 | 1 | 0 |

## Hangi görev hangi parçayı istiyor

- **LED** — zorunlu: 005, 006, 007, 008, 009, 010, 011, 012, 015, 020, 021, 022, 023, 025, 027, 030, 033, 034, 035, 040, 050, 101
- **Buton** — zorunlu: 004, 005, 007, 008, 009, 010, 011, 012, 015, 016, 019, 020, 023, 025, 060, 080, 092, 094, 101, 103, 132
- **Pot** — zorunlu: 026, 027, 028, 029, 030, 032, 041, 042, 045, 075, 107, 133
- **Buzzer** — zorunlu: 025
- **Seri bağlantı** — zorunlu: 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 043, 044, 045, 046, 047, 048, 051, 055, 061, 065, 066, 067, 068, 070, 071, 072, 073, 074, 075, 076, 077, 078, 079, 081, 082, 083, 084, 090, 091, 092, 093, 094, 095, 100, 110, 111, 112, 117, 118, 119, 120, 125, 130, 131, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 146; alternatifli: 080
- **Python** — zorunlu: 039, 043, 045, 055, 065, 067, 068, 070, 071, 072, 073, 074, 075, 077, 078, 082, 083, 084, 100, 109, 110, 111, 117, 118, 119, 120, 121, 122, 129, 131, 133, 135, 136, 137, 138, 139, 140, 141, 146; alternatifli: 040, 085
- **IMU** — zorunlu: 047, 048, 049, 050, 051, 052, 053, 054, 055, 057, 058, 059, 060, 076, 077, 078, 079, 080, 081, 082, 083, 084, 085, 095, 097, 099, 100, 113, 114, 127, 140, 141, 148; alternatifli: 046
- **OLED** — zorunlu: 056, 057, 058, 060, 097, 115; alternatifli: 046, 080, 085
- **Motor** — zorunlu: 062, 063, 064, 065, 066, 067, 068, 116, 139; alternatifli: 061, 070, 071, 072, 073, 074, 075, 090, 092, 098, 099, 100, 117, 118, 119, 120, 135, 136, 137, 138, 147, 149
- **Sanal motor** — zorunlu: —; alternatifli: 061, 070, 071, 072, 073, 074, 075, 090, 092, 098, 099, 100, 117, 118, 119, 120, 135, 136, 137, 138, 147, 149
- **2. kart** — zorunlu: 087, 088, 089, 090, 123, 128, 146, 147, 149; alternatifli: 040
- **CAN** — zorunlu: 087, 088, 089, 090, 123, 128, 146, 147, 148, 149
- **microSD** — zorunlu: 126, 127
- **Manyetometre** — zorunlu: 141
- **Logic analyzer** — zorunlu: 104, 149
- **RC filtre** — zorunlu: 111
