+++
title = 'Gentoo Linux Kurulumu'
date = 2024-03-11T17:23:27+03:00
tags = [
    "linux",
    "gentoo",
    "rehber",
    "kurulum",
]
categories = [
    "linux",
    "rehber",
]

+++

Bu rehberde size Sıfırdan Gentoo Linux nasıl kurulur onu göstereceğim.
Basit ve Detaylı anlatmaya çalışacağım.

Öncelikle Gentoo Linux nedir ondan bahsedelim.
Gentoo Linux kaynak kod tabanlı bir dağıtımdır. Neredeyse tüm paketleri size derletir. Hafif iyi bir donanıma sahipseniz kurulum daha hızlı bitebilir.

Hadi o zaman başlayalım

# Kurulum Dosyasını indirme 

## 1
Öncelikle burdan sisteminize uygun "Minimal Installation CD" dosyasını indirin

[https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/)

## 2
İndirdiğiniz iso dosyasını ventoy vb. bir programla flash belleğe yazdırın.

## 3
Klavyeyi türkçe yapalım

```
loadkeys trq
```
## 4
Bilgisayara ethernet kablosu bağlayın veya ifconfig ile yapın ama ben ifconfig kullanmayı bilmiyorum.

## 5
Diski bölümlendireceğiz

Diskinizin ismi yüksek ihtimal nvme0n1 olacak ama vda,sda vb olabilir 

Biçimlendirmek için yazacağınız kod bu
```
cfdisk /dev/nvme0n1
```
Eğer önceden biçimlendirmişseniz hepsini silin 
Eğer önceden hiç Linux kurmadıysanız size disk türünü seçin gibi birşey soracaktır GPT seçin.

### EFI bölümü
Öncelikle EFI bölümünü yapacaz 
Aşağıdaki New butonuna basıp 1G yazacağız sonra Type seçeceğiz. EFI seçeceksiniz

### SWAP bölümü
Şimdide swap yani takas alanı oluşturacağız yine new butonuna tıklayıp 4G,8G vb bir değer yazın.Benim önerim 8G.
Type olarak Linux SWAP seçeceğiz.

### ROOT bölümü 
New butonuna basıp sayıyı hiç değiştirmeden Enter'a basın bu diskin diğer kalanını kullanacağımız anlamına gelir.
Type değerini değiştirmeye gerek yoktur.


Böylece
/dev/nvme0n1p1 EFI bölümü
/dev/nvme0n1p2 SWAP bölümü
/dev/nvme0n1p3 ROOT bölümü oldu.

## 6 
Root bölümünü ext4 ile biçimlendireceğiz.

```
mkfs.ext4 /dev/nvme0n1p3
```

## 7
Swap için

```
mkswap /dev/nvme0n1p2 
```
ardından
```
swapon /dev/nvme0n1p2
```

EFI için

```
mkfs.fat /dev/nvme0n1p1
```

# STAGE-3 kurulumu
Root bölümünü boot edelim 

```
mount /dev/nvme0n1p3 /mnt/gentoo
```
ardından
```
cd /mnt/gentoo
```

## Tarihi Ayarlıyalım

```
chronyd -q
``` 

## İndirelim

```
links https://www.gentoo.org/downloads/
```

Bu kod size metin tabanlı browser açacaktır.
AMD64 Stage3 OpenRc indirip Save edin.

tarayıcıdan çıkmak için q ya basın.

Sonra indirdiğimiz dosyayı ayıklamak için bu kodu yapıştırın

```
tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner
```

## Make.conf ayarı yapalım

```
nano /mnt/gentoo/etc/portage/make.conf
```

işlemicinizin çekirdek sayısına göre -j8 veya -j12 yazacaksınız

Örnek Kod
```
COMMON_FLAGS="-march=native -O2 -pipe"
CFLAGS="${COMMON_FLAGS}"
CXXFLAGS="${COMMON_FLAGS}"
FCFLAGS="${COMMON_FLAGS}"
FFLAGS="${COMMON_FLAGS}"

INPUT_DEVICES="libinput"

MAKEOPTS="-j8 -l8"
USE="X -systemd dracut pulseaudio pipewire flatpak alsa readline sound-server ssl v4l pam vulkan opengl dbus gtk modemmanager widget drun windowmode screencast vdpau amdgpu zink"
ACCEPT_LICENSE="*"
VIDEO_CARDS="amdgpu radeonsi radeon"
ACCEPT_KEYWORDS="~amd64"


GRUB_PLATFORMS="efi-64"

LC_MESSAGES=C.utf8
```
Eğer nvidia kullanıyorsanız VIDEO_CARDS bölümüne nouveau yazın.

## Mirror Seçme

```
mirrorselect -i -o >> /mnt/gentoo/etc/portage/make.conf
```
Bu komut bir arayüz karşınıza çıkaracaktır Türkiye mirrorlarını boşluk tuşu ile seçin.
Enter yaparak işlemi tamamlayın.

## Gentoo Ayarları

```
mkdir --parents /mnt/gentoo/etc/portage/repos.conf
```

```
cp /mnt/gentoo/usr/share/portage/config/repos.conf /mnt/gentoo/etc/portage/repos.conf/gentoo.conf
```

## DNS Ayarı
```
cp --dereference /etc/resolv.conf /mnt/gentoo/etc/
```

## Sistemi mount edeceğiz

Sırayla bunları yazın
```
mount --types proc /proc /mnt/gentoo/proc
```
```
mount --rbind /sys /mnt/gentoo/sys
```
```
mount --make-rslave /mnt/gentoo/sys
```
```
mount --rbind /dev /mnt/gentoo/dev
```
```
mount --make-rslave /mnt/gentoo/dev
```
```
mount --bind /run /mnt/gentoo/run
```
```
mount --make-slave /mnt/gentoo/run
```

## Chroot ile giriş yapalım
```
chroot /mnt/gentoo /bin/bash
```
```
source /etc/profile
```
```
export PS1="(chroot) ${PS1}"
```

## Boot Bölümünü mount etme

UEFI için
```
mkdir /efi
```
```
mount /dev/nvme0n1p1 /efi
```
Legacy için 
```
mount /dev/nvme0n1p1 /boot
```

## Sistem paketlerini güncelleyelim
```
emerge-webrsync
```
```
emerge --sync
```

## Portage Profili Seçelim
KDE plasma kuracaz.

```
eselect profile list
```
Büyük ihtimal plasma profili 9 da olacak ama farklı olabilir.
```
eselect profile set 9
```

## Tüm Sistem Paketlerini Güncelleyelim
```
emerge --ask --verbose --update --deep --newuse @world
```
İlk kurulum olduğu için 1-2 saat sürebilir.


## Zaman Dilimini Ayarlayalım
```
echo "Turkey" > /etc/timezone
```
```
emerge --config sys-libs/timezone-data
```

## Dil Ayarı Yapalım
```
nano /etc/locale.gen
```
Dosyanın en altına bunu yazın
```
tr_TR.UTF-8 UTF-8
```
tr kaçıncı sırada bakalım
```
eselect locale list
```
tr kaçıncı sıradaysa o sayıyı yazın bende 4.
```
eselect locale set 4
```

## Environment güncellemesi yapalım
```
env-update && source /etc/profile && export PS1="(chroot) ${PS1}"
```

## GenKernel Kuralım 

```
emerge --ask sys-kernel/linux-firmware
```
```
emerge --ask sys-kernel/gentoo-kernel-bin
```

Yüklü Kernelleri Listeleyelim
```
eselect kernel list
```

kernel seçelim
```
eselect kernel set 1
```

## Fstab dosyasını düzenleyelim
Dosyanın en altına inip bu kodu yazın

UEFI için
```
/dev/nvme0n1p1        /efi    vfat    defaults    0 2
/dev/nvme0n1p3        /    ext4    noatime,discard        0 1
/dev/nvme0n1p2        none    swap    sw        0 0
```
Legacy için
```
/dev/nvme0n1p1        /boot    vfat    defaults    0 2
/dev/nvme0n1p3        /    ext4    noatime,discard        0 1
/dev/nvme0n1p2        none    swap    sw        0 0
```

## Hostname Ayarlayalım
```
nano /etc/conf.d/hostname
```
Dosyanın en altına bunu yazın

```
hostname="gentoo"
```

## Hosts Dosyasını Düzenleme
```
nano /etc/hosts
```
İki beyaz metnin sonuna 5 boşluk bırakarak gentoo yazınız

## Root şifrenizi ayarlayın
```
passwd
```

## Klavye düzenini değiştirin
US olarak gözüken değeri TRQ olarak değiştirin.
```
nano /etc/conf.d/keymaps
```

## Grub Kuralım
UEFI için
```
emerge --ask sys-boot/grub:2
```
Legacy için
```
emerge --ask --verbose sys-boot/grub:2
```

## Grub'ı ayarlıyalım
UEFI için
```
grub-install --target=x86_64-efi --efi-directory=/efi
```
Legacy için
```
grub-install /dev/nvme0n1
```

## Son Adımlar
```
grub-mkconfig -o /boot/grub/grub.cfg
```

```
exit
```
```
cd
```
```
umount -l /mnt/gentoo/dev{/shm,/pts,}
```
```
umount -R /mnt/gentoo
```
```
reboot
```

Bilgisayar kapandığında flash belleği çıkartın.

## Kullanıcı oluşturun
```
useradd -m -G users,wheel,audio -s /bin/bash mesflit
```
Siz mesflit yerine kendi isminizi yazın türkçe karakterler olmasın.

Şifre belirleyin yeni kullanıcı için
```
passwd mesflit
```

## Stage-3 dosyasını silelim 
```
rm /stage3-*.tar.*
```


## Gerekli Yazılımları Kuralım
```
emerge --ask gentoolkit
```
```
emerge --ask elogind
```
```
rc-update add elogind boot
```
```
rc-update add udev sysinit
```
```
rc-update add dbus default
```
```
emerge --ask udisks
```
```
rc-update add lvm boot
```
```
emerge --ask --verbose xorg-drivers
```

Mesflit benim kullanıcı adım. Siz kendi kullanıcı adınızı girin.
```
gpasswd -a mesflit video
```

## KDE Plasma Kurulumu 
Bunlar Biraz Uzun Sürecek. Kahvenizi Hazırlayın.
```
emerge --ask kde-plasma/plasma-meta
```
```
emerge --ask kde-apps/kde-apps-meta
```

## Sudo Kurulumu
```
emerge --ask sudo
```
```
visudo
```
En alt kısma bunu ekleyin
Kendi kullanıcı adınızı yazın.
```
mesflit ALL=(ALL) ALL
```

## SDDM kurulumu
```
sudo emerge --ask x11-misc/sddm
```
```
sudo usermod -a -G video sddm
```
## SDDM ayarlaması
```
mkdir -p /etc/sddm.conf.d
```
```
sudo /etc/sddm.conf.d/override.conf
```
Bunu Dosyanın en altına ekleyin

```
[X11]
DisplayCommand=/etc/sddm/scripts/Xsetup

```

Sonra


```
mkdir -p /etc/sddm/scripts 
```
```
touch /etc/sddm/scripts/Xsetup
```
```
chmod a+x /etc/sddm/scripts/Xsetup
```

```
sudo nano /etc/sddm/scripts/Xsetup
```


Bu dosyanın en altına inip bunu yazın
```
setxkbmap tr
```

## SDDM başlatma
```
sudo emerge --ask gui-libs/display-manager-init
```

```
sudo nano /etc/conf.d/display-manager
```
Bu dosyayada bunu yazın.
```
DISPLAYMANAGER="sddm"
```


Sonra

```
sudo rc-update add display-manager default
```
```
sudo rc-service display-manager start
```
# Rehberin Sonu

Eğer buraya kadar geldiyseniz TEBRİKLER artık Gentoo Linux kullanıyorsunuz. Geri kalanı wikiden bakarsınız veya bana sorabilirsiniz.

## Cihazınıza gelecek herhangi bir sorundan ne ben ne de Gentoo Linux sorumlu değildir!!!

[Gentoo Wiki](https://wiki.gentoo.org/wiki/Main_Page)
