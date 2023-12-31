# FLASK MENU UYGULAMASI

## Restoran Menü Yönetimi Sistemi

Bu proje, bir restoranın menü yönetimini kolaylaştıran bir web uygulamasıdır. Kullanıcıların menüyü yönetmelerini, öğeler eklemelerini, düzenlemelerini ve silmelerini sağlar. Bu projenin amacı, restoran işletmelerinin günlük operasyonlarını kolaylaştırmaktır.

## Kullanılan Teknolojiler ve Platformlar

Proje, Python dili ve Flask çerçevesi kullanılarak geliştirildi. Veritabanı işlemleri için SQLAlchemy ORM kullanılırken, kullanıcı oturumları için Flask-Login kullanıldı. Projenin ön yüzü Bootstrap ile tasarlandı.

## Çalışma Şekli

1. **Kayıt Ol**: Kullanıcıların ilk olarak sisteme kayıt olmaları gerekmektedir.
2. **Giriş Yap**: Kayıt işleminden sonra kullanıcılar, sisteme giriş yapabilirler.
3. **Menü Görüntüle**: Kullanıcılar, menü öğelerini görüntüleyebilirler. Hem kayıtlı kullanıcılar hem de misafirler menüyü görüntüleyebilir, ancak sadece kayıtlı kullanıcılar menüyü düzenleyebilirler.
4. **Menü Öğesi Ekle**: Kayıtlı kullanıcılar, menüye yeni öğeler ekleyebilirler. Bir menü öğesinin adı, fiyatı ve açıklaması gerekmektedir. Kullanıcılar ayrıca menü öğesine bir resim ekleyebilirler.
5. **Menü Öğesi Düzenle**: Kayıtlı kullanıcılar, menü öğelerini düzenleyebilirler. Adı, fiyatı, açıklaması ve resmi düzenlenebilir.
6. **Menü Öğesi Sil**: Kayıtlı kullanıcılar, menü öğelerini silebilirler.
7. **Çıkış Yap**: Kullanıcılar, sisteme çıkış yapabilirler.

## Geliştirme Adımları

1. Flask uygulamasının ve SQLAlchemy veritabanının kurulumu
2. User ve MenuItem modellerinin oluşturulması
3. Kullanıcı oturumlarının yönetimi için Flask-Login'in kurulumu
4. Kayıt, giriş ve çıkış işlemlerini yöneten rotaların oluşturulması
5. Menü öğelerini görüntüleme, ekleme, düzenleme ve silme işlemlerini yöneten rotaların oluşturulması
6. HTML şablonlarının ve Bootstrap tasarımının oluşturulması

## Ekran Görüntüleri

### Kayıt Ol
![Kayıt Ol](scr_images/register.png)

### Giriş Yap
![Giriş Yap](scr_images/login.png)

### Menü Görüntüle
![Menü Görüntüle](scr_images/menu.png)

### Menü Öğesi Ekle
![Menü Öğesi Ekle](scr_images/add_item.png)

### Menü Öğesi Düzenle
![Menü Öğesi Düzenle](scr_images/edit_item.png)
