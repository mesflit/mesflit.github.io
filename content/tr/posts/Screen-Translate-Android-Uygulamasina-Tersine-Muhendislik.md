+++
title = 'Screen Translate Android Uygulamasina Tersine Muhendislik'
date = 2024-07-22T10:40:39Z
draft = false
+++

Merhabalar!

Bu konuda size bir Android uygulaması olan Screen Translate'i tersine mühendislik ile ücretsiz bir şekilde Premium moda sahip olacağız.

## Gereksinimler
- Bir Linux işletim sistemi (Termux ve proot-distro olur)
- apktool (APK dosyalarını decompile etmeye yarayan araç)
- apksigner (APK dosyasını imzalamak için gerekli) 

## Kurulum
### apktool kurulumu
    
    sudo apt install apktoll

### apksigner kurulumu

    sudo apt install apksigner

## Screen Translate'i İndirme

Kullanacağımız Screen Translate sürümü `1.143`
[Play Store](https://play.google.com/store/apps/details?id=com.recognize_text.translate.screen)'dan veya [burdaki](#linkler) linkten APK olarak indirebilirsiniz.

## Dosyayı Apk'ya Çevirme

Play Store'dan indirdiğimizde apksını elde etmiş olmuyoruz.  

Bunun için bir program gerek. Ben App Manager kullandım. Siz istediğinizi kullanabilirsiniz APK export etmek için. 

Ama export ettiğinizde bize `screentranslate.apks` uzantılı bir dosya verecek.

Bu `screentranslate.apks` dosyasını `screentranslate.zip` diye yeniden adlandırmalısınız.

Sonra zip dosyası çıkaracaksınız.

Ve dosyanın içinde base.apk adında bir dosya elde edeceğiz düzenleyeceğimiz dosya bu.

## APK'yı Düzenleme

apktool ile base.apk dosyasını decompile edeceğiz.

    apktool d base.apk

Komutu ile decompile edeceğiz.

Sonra `base/smali_classes3/q5/d.smali` dosyasını bir text editor ile açın. 

Bu kodu aratın dosyanın içinde `.method public static C()Z`


Karşınıza böyle bir şey çıkacak

    method public static C()Z
        .locals 4

        .line 1

Bunu değiştireceğiz. Görünümü böyle olacak ->

    .method public static C()Z
        .locals 4
    
    const/4 v0, 0x1
 
    return v0

    .line 1

Bunları ekledikten sonra kaydedip çıkalım.
Base klasörünün bulunduğu yere gelin ve bu komutu çalıştırın.

    apktool b base

Bu işlem dosyaları tekrar apk haline çevirecek.
Apk dosyası ise `base/dist/` klasöründe olcak

## APK İmzalama

APK dosyası çıktığında kuramazsınız, çünkü içinde değişiklikler yaptık ve imzalanması gerek.
Önce `base/dist/` klasörüne girin.
İmzalamak için `keytool` aracı kullancaz. Bende yüklü gelmişti.

    keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias

Size önce şifre ve sonra unknown (boş) bırakabilceğiniz sorular sorcak. Sonra yes diyerek doğrulamanız gerekiyor.
Ve artık `my-release-key.jks` adında bir key dosyamız var.
Şimdi kullancağımız komut apk'yı imzalayacak.

    apksigner sign --ks my-release-key.jks --out signed-app.apk base.apk

Ve artık yeni ve imzalanmış APK dosyamız var. İsmi `signed-app.apk` artık bunu kurabilirsiniz.

## Linkler

### Screen Translate Play Store
[Play Store](https://play.google.com/store/apps/details?id=com.recognize_text.translate.screen)

### Screen Translate 1.143 Orjinal APK 
[MegaNZ](https://mega.nz/file/xZZRDSbA#cqjII5ComiLWdYnppmmI_EmYwH2X2E2Ls_6EhUkZJuY)

### Screen Translate 1.143 Modlanmış APK
[MegaNZ](https://mega.nz/file/5UBTBDCL#QgYe9BVjHEJ2gARmH1wRRvsT0J64rMJmzkGAadxJVuI)

## Mesflit Sunar
