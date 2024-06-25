+++
title = "Linux Kurulu Laptopu VDS Server'a Çevirme"
date = 2024-06-25T14:23:30+03:00
draft = false
+++

## Rehber: Linux Kurulu Laptopu VDS Server'a Çevirme
{{% notice note %}}
Bu işlemleri sanal makinede yapmanızı öneririm
{{% /notice %}}

### 1. Sistem Gereksinimleri
Laptobunuzu bir VDS olarak kullanmadan önce, bazı sistem gereksinimlerini karşıladığınızdan emin olun:
- En az 4 GB RAM (daha fazla önerilir)
- Yeterli disk alanı (minimum 20 GB)
- Güçlü ve sabit bir internet bağlantısı

### 2. Linux Dağıtımının Yüklenmesi
Eğer halihazırda bir Linux dağıtımı kullanmıyorsanız, popüler bir dağıtım olan Ubuntu Server'ı yüklemenizi tavsiye ederim. Ubuntu Server, VDS olarak kullanıma uygundur.

### 3. Web Sunucusu Kurulumu
Laptobunuzu web sunucusu olarak kullanmak için Apache veya Nginx gibi bir web sunucusu yazılımı kurabilirsiniz.

#### Apache Web Sunucusu Kurulumu

    sudo apt update
    sudo apt install apache2
    sudo systemctl enable apache2
    sudo systemctl start apache2
#### Nginx Web Sunucusu Kurulumu
    sudo apt update
    sudo apt install nginx
    sudo systemctl enable nginx
    sudo systemctl start nginx

### 4. Veritabanı Sunucusu Kurulumu
Web uygulamaları için bir veritabanı sunucusu kurabilirsiniz.
#### MySQL Kurulumu

    sudo apt update
    sudo apt install mysql-server
    sudo mysql_secure_installation
#### PostgreSQL Kurulumu
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    sudo systemctl enable postgresql
    sudo systemctl start postgresql
### 5. FTP Sunucusu Kurulumu
Dosya transferi için bir FTP sunucusu kurabilirsiniz.
#### vsftpd Kurulumu
    sudo apt update
    sudo apt install vsftpd
    sudo systemctl enable vsftpd
    sudo systemctl start vsftpd
### 6. Güvenlik Ayarları
Sunucunuzu güvenli hale getirmek için bazı temel güvenlik ayarlarını yapın:
- Güçlü şifreler kullanın.
- Gerekli olmayan servisleri kapatın.
- UFW (Uncomplicated Firewall) ile temel güvenlik duvarı kurallarını ayarlayın.
#### UFW Güvenlik Duvarı Kurulumu ve Yapılandırması
    sudo apt install ufw
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow 80/tcp    # HTTP için
    sudo ufw allow 443/tcp   # HTTPS için
    sudo ufw enable
### 7. Dinamik DNS (DDNS) Hizmeti Kullanarak IP Adresini Domain ile Eşleştirme
No-IP Hesabı Oluşturma

- No-IP web sitesine (https://www.noip.com) gidin.
- "Sign Up" veya "Create Account" seçeneklerini tıklayın.
- Gerekli bilgileri doldurarak bir hesap oluşturun.

#### Hostname (Alt Alan Adı) Oluşturma

- Hesabınıza giriş yapın.
- "Dynamic DNS" veya "Manage Hosts" sekmesine gidin.
- "Create Hostname" veya "Add a Host" seçeneğini tıklayın.
- Oluşturmak istediğiniz alt alan adını (hostname) girin (örneğin, mylaptop.ddns.net).
- Laptobunuzun mevcut IP adresini girin (bu genellikle otomatik olarak algılanır).
- Kaydedin.

#### No-IP Client (DUC) Kurulumu ve Yapılandırması

Laptobunuzun IP adresi dinamik ise, IP adresinizi No-IP sunucularına düzenli olarak güncelleyecek bir yazılım kurmanız gerekecek.
#### Linux için No-IP Client Kurulumu
- No-IP DUC (Dynamic Update Client) yazılımını indirin ve kurun:
    wget --content-disposition https://www.noip.com/download/linux/latest
    tar xf noip-duc_*.tar.gz
    cd /home/$USER/noip-duc_*/binaries && sudo apt install ./noip-duc_*_amd64.deb
    noip-duc -g all.ddnskey.com --username <DDNS Key Username> --password <DDNS Key Password>
- Hizmeti etkinleştirin ve başlatın
    sudo systemctl enable noip2
    sudo systemctl start noip2

### 9. İzleme ve Bakım

Sunucunuzu izlemek ve performansını artırmak için bazı araçlar kullanabilirsiniz:

- htop veya top ile sistem kaynaklarını izleyin.
- vnstat ile ağ trafiğini izleyin.

#### htop Kurulumu
    sudo apt install htop
    htop
#### vnstat Kurulumu
    sudo apt install vnstat
    sudo systemctl enable vnstat
    sudo systemctl start vnstat
    vnstat
### Sonuç

Bu rehber, bir Linux laptobunu VDS olarak kullanmanın temel adımlarını ve gereksinimlerini kapsar. Kendi laptobunuzdan çalışırken SSH'a ihtiyaç duymayabilirsiniz, ancak ileride uzaktan erişim ihtiyacı doğarsa SSH kurulumunu da göz önünde bulundurabilirsiniz. Daha ileri seviye konfigürasyonlar ve özel ihtiyaçlar için, her bir hizmetin dökümantasyonunu ve Linux yönetimi konusundaki diğer kaynakları incelemenizi öneririm.

### Mesflit Sunar
