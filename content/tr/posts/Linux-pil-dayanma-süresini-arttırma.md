+++
title = 'Linux Pil Dayanma Süresini Arttırma'
date = 2024-06-26T11:28:15+03:00
draft = false
+++
## Rehber: Linux Pil Dayanma Süresini Arttırma

Rehberde size daha iyi pil performansı almanızı sağlayacağım.

### 1.Pil Sağlığını Kontrol Etme

Terminale bu kodu girin

    upower -i /org/freedesktop/UPower/devices/battery_BAT0
**capacity:** "sayı_değeri" sizin pil sağlığınızı gösterir.
### 2.TLP 
TLP (Linux için Güç Yönetimi), Linux sistemlerinde güç yönetimini optimize eden bir araçtır. Dizüstü bilgisayarların pil ömrünü uzatmak ve enerji tasarrufu sağlamak için çeşitli ayarları ve optimizasyonları otomatik olarak uygular. TLP, bir dizi önceden tanımlanmış yapılandırma ile gelir ve ayrıca kullanıcıların ihtiyaçlarına göre özelleştirilebilir.

#### TLP kurulumu
Dağıtımdan dağıtıma farklılık gösterebilir.

**Debian** ve **Ubuntu** tabanlı dağıtımlar için:     

    sudo apt install tlp tlp-rdw

**Arch** tabanlı dağıtımlar için:

    sudo pacman -Sy tlp tlp-rdw

Arayüzlü bir şekilde kullanmak istiyorsanız **FLATHUB**'dan **TLP-UI** adlı programı indirmeniz gerek

    flatpak install flathub com.github.d4nj1.tlpui

İstediğiniz ayarları basit şekilde değiştirebilirsiniz.

### 3. Ekran Parlaklığını Azaltma:

Ekran parlaklığı, pil tüketiminde büyük bir etken olabilir. Parlaklığı mümkün olduğunca düşük tutmak pil ömrünü uzatabilir.

### Mesflit Sunar