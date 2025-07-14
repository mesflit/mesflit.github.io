## Merhaba!

## Zapret Nedir ve Ne İşe Yarar?

**Zapret**, DPI (Deep Packet Inspection) yoluyla web sitelerine getirilen erişim engellerini kaldırmak için kullandığımız bir araçtır. Örneğin, [discord.com](http://discord.com/) gibi bazı siteler bazı ülkelerde yasaklanmış durumda olduğu için kullanıcılar bu yöntemi tercih etmektedir.

___

## Zapret Kurulumu
### Bağımlılıklar ve DNS Ayarları

Amacımız Zapret’i sorunsuz şekilde kurmak ve herhangi bir masaüstü ortamına bağlı kalmadan sistem genelinde etkinleştirmektir.

#### `dnscrypt-proxy` Kurulumu

Bağımlılıklarınızı aşağıdaki şekilde yükleyebilirsiniz:

-   **Arch Linux**: `sudo pacman -S dnscrypt-proxy`
-   **Fedora**: `sudo dnf install dnscrypt-proxy`
-   **OpenSUSE**: `sudo zypper in dnscrypt-proxy`
-   **Alpine Linux**: `sudo apk add dnscrypt-proxy`
-   **Debian**: [Debian 12 Bookworm sisteme dnscrypt-proxy kurmak - f0q tarafından](https://btt.community/t/debian-12-bookworm-sisteme-dnscrypt-proxy-kurmak/15884/12)
-   **Void Linux**: `sudo xbps-install -S dnscrypt-proxy`
-   **Gentoo**: `emerge dnscrypt-proxy`
-   **NixOS**: _Konu sonunda NixOS bölümü mevcuttur. Aşağıdaki tüm adımları geçerek ilgili bölüme bakınız._

#### DNS Ayarları

DNS ayarlarını yapmak için aşağıdaki adımları izleyin:

1.  `/etc/dnscrypt-proxy/dnscrypt-proxy.toml` dosyasını düzenleyin ve şu satırı güncelleyin:
    
    ```
    listen_addresses = ['127.0.0.1:53']
    ```
    
    şu şekilde değiştirin:
    
    ```
    listen_addresses = ['127.0.0.1:53', '[::1]:53']
    ```
    
2.  **NetworkManager Ayarlarını Güncelleyin** (Gentoo için bu adımı atlayın.)
    
    NetworkManager, DNS ayarlarını otomatik olarak `/etc/resolv.conf` dosyası üzerinden yönetir. Bu durumu manuel olarak yönetebilmek için aşağıdaki adımları izleyin:
    
    2.1 Ayar Dosyasını Düzenleyin.
    
    Eğer `/etc/NetworkManager/conf.d/90-dns-none.conf` dosyası yoksa, oluşturun ve aşağıdaki satırları ekleyin:
    
    ```
    [main]
    dns=none
    ```
    
    2.2 NetworkManager’ı Yeniden Başlatın:
    
    ```
    sudo systemctl restart NetworkManager
    ```
    
    2.3 `/etc/resolv.conf` Dosyasını Güncelleyin:
    
    ```
    nameserver ::1
    nameserver 127.0.0.1
    options edns0
    ```
    
3.  Sistem hizmetlerini etkinleştirin:
    
    -   **Systemd**:
        
        ```
        sudo systemctl enable dnscrypt-proxy.service
        sudo systemctl start dnscrypt-proxy.service
        ```
        
    -   **OpenRC**:
        
        ```
        rc-update add dnscrypt-proxy default
        rc-service dnscrypt-proxy start
        ```
        

___

### Zapret Ayarları

**Kolaylık için:**

1.  `/opt/` dizinine girin:
    
    ```
    cd /opt/
    ```
    
2.  **Zapret’i indirin** (Gentoo için bu adımı atlayın):
    
    2.1 GitHub üzerinden klonlayın :
    
    ```
    git clone https://github.com/bol-van/zapret.git
    cd zapret
    ```
    
    2.2 GitHub Releases kısmından indirin. (`no compatible binaries found` hatası alıyorsanız)
    
3.  Uyumlu dağıtımlar için aşağıdaki komutları kullanarak kurulumu tamamlayın:
    
    ```
    ./install_bin.sh
    ```
    

Eğer bir hata alırsanız, eksik bağımlılıkları dağıtımınızın paket yöneticisiyle kurun.  
Örneğin: `curl`, `ipset`, `iptables`, `bind-utils`.

___

### Strateji Belirleme ve Test Etme

1.  Stratejiyi test etmek için:
    
    ```
    ./blockcheck.sh
    ```
    
    Komut sonrası çalışmayan bir site adı (örneğin, `discord.com`) girmeniz istenecek:
    
    ```
    domain(s) (default: rutracker.org): discord.com
    ```
    
2.  Gelen seçeneklere genelde `Enter` tuşuna basarak geçebilirsiniz. Çalışan strateji şuna benzer şekilde görünecektir:
    
    ```
    nfqws --dpi-desync=fake --dpi-desync-ttl=8
    ```
    
3.  Bu stratejiyi kopyalayarak kurulum sırasında kullanacağız.
    

___

### Zapret Kurulum ve Yapılandırma

1.  **Yapılandırma için seçtiğiniz metin düzenleyiciyi tanımlayın**:
    
    ```
    export EDITOR=nvim
    ```
    
2.  Kolay kurulum betiğini çalıştırın:
    
    ```
    ./install_easy.sh
    ```
    
3.  Atlamamanız gereken sorular, bu sorulara `Y` yazın :
    
    ```
    enable nfqws ? (default : N) (Y/N) ? Y
    
    do you want to edit the options (default : N) (Y/N) ? Y
    ```
    
4.  Stratejinizi tanımlayın:
    
    ```
    NFQWS_OPT="--dpi-desync=fake --dpi-desync-ttl=8"
    ```
    
5.  Geri kalan soruları `Enter` ile geçebilirsiniz. Örneğin:
    
    -   LAN/WAN arayüzü seçenekleri
    -   Filtreleme türü

___

## Gentoo ve NixOS Özel Ayarları

### Gentoo

Gentoo’da Zapret’i kurmak için:

1.  **Mesflit Overlay’i ekleyin ve zapret kurun:**
    
    ```
    sudo eselect repository add mesflit git https://github.com/mesflit/mesflit-gentoo-overlay.git
    sudo eselect repository enable mesflit
    emerge --sync
    emerge zapret netifrc #kurulum yolu aynı /opt/zapret
    ```
    
2.  Yukarıda atlamamanız gereken adımları yapın.
    
3.  DNS ayarları için `/etc/conf.d/net` dosyasına şu satırları ekleyin:
    
    ```
    dns_servers_lo="127.0.0.1 ::1 1.1.1.1"
    ```
    
4.  Servisi başlatın:
    
    ```
    sudo rc-update add net.lo default
    sudo rc-service net.lo start
    ```
    

___

### NixOS

NixOS kullanıcıları için örnek yapılandırma:

```
  networking = {
    hostName = "nixos";
    nameservers = ["127.0.0.1" "::1"];
  };

  services.dnscrypt-proxy2 = {
    enable = true;
    settings = {
      listen_addresses = ["127.0.0.1:53" "[::1]:53"];
    };
  };

  services.zapret = {
    enable = true;
    params = [
      "--dpi-desync=fake"
      "--dpi-desync-ttl=8"
    ];
  };
```

___

## Sonuç

Sisteminizde artık Zapret çalışır hale geldi.

### Bilinen sorunlar
Bazen zapret çalışmayabilir bunu düzeltmek için
`Systemd` de

```
sudo systemctl restart dnscrypt-proxy
```

`OpenRC` de

```
  sudo rc-service dnscrypt-proxy restart
  sudo rc-service net.lo restart        
```
### Referans Link
[Konunun Linki](https://btt.community/t/linux-zapret-kurulum-rehberi/15989)
