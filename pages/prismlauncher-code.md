# PrismLauncher kullan! Ücretsiz hesap açabilirsin.

Merhaba Ben Mesflit.

Sizde Minecraft'a o kadar para vermek istemiyorsunuzdur benim gibi.
Ve internette ufak bir araştırma yapınca Karşınıza **Mavi Logolu** bir program çıkıyor.
Ama bu program güvenlimi sizce?
Ve bunun Daha iyi bir alternatifi yokmu?

## Elbette Var!

Tek sorun bunu çoğu kişi bilmiyor.
Kullancağımız uygulama **PrismLauncher** açık kaynaklı ama resmi olarak crack desteklemiyor.
Ama ufak bir gizli kodla bunu değiştirebiliyoruz.

## Kurulum

**PrismLauncher** Linux, Windows, MacOS işletim sistemlerinde mevcuttur.

[Kaynak Kodu](https://github.com/PrismLauncher/PrismLauncher)

[PrismLauncher WebSitesi](https://prismlauncher.org/) <-- Burdan indirebilirsiniz.

İndirdikten sonra **PrismLauncher**'ı açıp dil seçip hesap açmadan çıkıyoruz.
Ve bu adım hangi işletim sisteminde olduğunuza bağlı
Bunun için CMD veya terminali açmanız lazım

### Windows CMD

```echo {"accounts": [{"entitlement": {"canPlayMinecraft": true,"ownsMinecraft": true},"type": "MSA"}],"formatVersion": 3} > %appdata%/PrismLauncher/accounts.json```

### Linux 

```echo '{"accounts": [{"entitlement": {"canPlayMinecraft": true,"ownsMinecraft": true},"type": "MSA"}],"formatVersion": 3}' > ~/.local/share/PrismLauncher/accounts.json```

### Linux Flatpak

```echo '{"accounts": [{"entitlement": {"canPlayMinecraft": true,"ownsMinecraft": true},"type": "MSA"}],"formatVersion": 3}' > ~/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/accounts.json```

### MacOS

```echo '{"accounts": [{"entitlement": {"canPlayMinecraft": true,"ownsMinecraft": true},"type": "MSA"}],"formatVersion": 3}' > ~/Library/Application\ Support/PrismLauncher/accounts.json```

## Son Adımlar
Şimdi **PrismLauncher**'ı açıp hesap çevrimdışı hesap oluşturmanız gerekiyor.
!!!Sakın "No Profile" hesabını silmeyin yoksa bypass çalışmaz!!!

## Son
Bu konu bukadardı
Takipte Kalın

## İlgili Kaynaklar

[https://github.com/antunnitraj/Prism-Launcher-PolyMC-Offline-Bypass](https://github.com/antunnitraj/Prism-Launcher-PolyMC-Offline-Bypass)

