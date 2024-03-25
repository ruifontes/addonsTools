# Eklentileri yönetmek için araçlar


## Bilgi
* Yazarlar: Rui Fontes <rui.fontes@tiflotecnia.com>, Angelo Abrantes <ampa4374@gmail.com> ve Abel Passos Jr. <abel.passos@gmail.com>"
* [Kararlı sürümü indirin][1]
* Uyumluluk: NVDA sürüm 2021.1 ve sonrası.


## Genel Bilgi
Bu eklenti, NVDA eklenti mağazasında bulunmayan araçlar yardımı ile eklentileri yönetmeyi sağlar.
Özelliklere erişmek için NVDA/Araçlar menüsünden veya daha önce "Girdi hareketleri" iletişim kutusunda tanımlanan hareket kullanılarak eklenti ana penceresine erişilebilir.

Ana iletişim kutusunda bulunan araçların listesi:
* Eklenti paketleyici: Bir eklenti yedekleme dosyası oluşturmak, değiştirilmiş bir eklentiyi test etmek veya kullanmak isteyen birine göndermek için kullanılır;
* Çoklu yükleyici: Bir klasörden eklentilerin seçilmesine ve tümünün aynı anda yüklenmesine olanak tanır;
* Yedekleme Yap/Yedeği geri Yükle: Yapılandırmalar, profiller ve sözlükler gibi bazı NVDA dosyalarının yedeklenmesine ve geri yüklenmesine imkan verir;
* Eklenti belgeleri: Yardım dosyalarını açar.

Bir aracın özelliklerine erişmek için "Sekme" tuşuna basın.
Aşağıda her bir aracın kısa bir açıklaması yer almaktadır.


### Eklenti paketleyici:
Sekme ile listeye gelip bu kategoriyi seçersek, yüklediğimiz tüm eklentilerin etkin, devre dışı veya desteklenmemesine bakılmaksızın sıralandığı bir listeye erişiriz.
Alt+L ile de hızlı bir şekilde erişebildiğimiz bu listede seçmek istediğimiz tüm eklentileri boşluk bırakarak seçip seçtiğimiz bir dizine yedekleyebiliriz.
Her eklenti kendi adı, sürümü ve “_gen” tanımlayıcısı ile oluşturulacaktır, oluşturulan bu eklentiler diğer NVDA kullanıcıları tarafından sorunsuz bir şekilde kurulabilir.
Seç adlı butonun üzerine sekme tuşu ile gelip boşluk çubuğu ile etkinleştirdiğimizde: Tümünü seç ve Seçimi temizle seçeneklerini görüyoruz. Aynı içeriğe ALT+S kısayolu ile de erişebiliriz.
Yine tab ile üzerine gelerek veya ALT+O kısayolu kullanılarak Oluştur butonu etkinleştirildiğinde, Dosya kaydetme penceresi açılır ve bir dizin seçmemiz istenir.
Dizin seç ile belirttiğimiz konumu onayladıktan sonra, listeden seçtiğimiz eklentinin paketlenme işlemi başlayacaktır. Bu esnada, aşamaların erişilebilir şekilde gösterildiği bir kutu ekrana gelecek ve penceredeki diğer bütün butonlar işlem tamamlanana kadar devre dışı bırakılacaktır.
İşlem tamamlandıktan sonra, bize bildirilir ve olumlu veya olumsuz bilgiler sunulur. ALT+B ile Kabul et tıklanarak pencere kapatılır.
Eklenti oluşturma işleminin gerçekleştirilebilmesi için, listeden en az bir eklentinin seçili olması gerekir. Aksi taktirde, bir mesaj ile kullanıcı uyarılacaktır.


###Çoklu yükleyici:
Bu kategori, Eklentilerimizin bulunduğu bir Dizin seçmemize izin verecek ve hepsini bir kerede kurabileceğiz.
İlk listeden Çoklu yükleyici seçeneğini seçtikten sonra sekme tuşu ile ilerlediğimizde: "Yüklemek istediğiniz eklentilerin bulunduğu bir dizin seçin" butonuna erişiriz. ALT+S ile de erişebildiğimiz bu düğmeye bastığımızda, kurmak istediğimiz eklentilerin bulunduğu klasörü seçebiliriz.
Bu kategorideki arayüzün geri kalanı, biz bir dizin seçene kadar devre dışı bırakılır.
Bir dizin seçtiğimizde, odak bizi eklentileri tararken neler olup bittiği hakkında bilgilendirileceğimiz tek okuma kutusunda bırakacak, ayrıca ilerleme çubuğundan da bilgi alacağız.
Tarama bittiğinde herhangi bir sorun olup olmadığı ve nasıl hareket edileceği konusunda bilgilendirileceğiz. Kullanmakta olduğmuz NVDA sürümü ile uyumsuz ve hasarlı olan eklentiler listeye dahil edilmez.
Tarama işlemi tamamlandıktan sonra, açılan uyarı mesajını Kabul et butonuna basarak kapatırsak, belirttiğimiz dizindeki sorunsuz eklentiler adları ile listeye eklenecektir.
Listeye, ALT+L ile de erişebilir ve istedeğimiz kadar eklentiyi boşluk çubuğu ile seçebiliriz.
Seçme işlemini tamamladıktan sonra sekme tuşuna basarsak seç butonu gelir. Eklenti paketleyici alanında olduğu gibi aynı işleve sahiptir.
Eğer tekrar Tab tuşuna basarsak, Yükle butonu gelir. ALT+Y ile de hızlıca erişebiliriz.
Seçtiğimiz en az bir veya daha fazla eklenti, NVDA'nın kullandığı klasik eklenti kurma penceresini göstermeden daha hızlı şekilde kurulacaktır.
Bu alanda da sadece uyumlu eklentilerin kurulabildiğini ve size sorun yaşatmayacağını belirtmeliyiz.
Yükle butonuna basıldığı anda, Eklenti sürecin belirtildiği kutuya odaklanacaktır.
Ayrıca süreç bittiğinde: yüklenen, kurulamayan ve varsa hataların bizlere bildirildiği bir pencere açılır.
Pencerede verilen sonuçlara bağlı olarak: Kapat butonunun yanı sıra, Kabul et veya İptal düğmeleri de bulunabilir.
Kabul et düğmesi etkinleştirilirse, Yüklenen eklentilerin ve yapılan değişikliklerin etkin olabilmesi için NVDA yeniden başlatılır.
Kabul etmez ve kapatırsak, NVDA'yı yeniden başlatana kadar eklentiyi tekrar kullanamayacağız, bu yinelenen eylemleri önlemek için bir korumadır.
Aksi takdirde hatalar varsa ve yalnızca iptal düğmesi sunulursa, başka şeyler yapmak için ona basabilir ve arayüze dönebiliriz.


### Yedekleme Yap/Yedeği geri Yükle:
Bu seçeneği seçtiğinizde yedeklenecek/geri yüklenecek olası öğelerin bir listesini bulacaksınız.
İstediklerinizi işaretleyin ve "Yedekleme yap" veya "Yedeği geri yükle" seçeneğini seçin.
Yedekleme yap düğmesine basarsanız, yeek dosyasını kaydedileceği konumu belirtmelisiniz.
Geri yüklemeyi seçerseniz, kaydedildiği klasörü ve istediğiniz dosyayı seçmelisiniz.
İşlemin sonuçları tamamlandıktan sonra bir iletişim kutusunda gösterilir.


### Eklenti belgeleri
Son olarak, burada yüklü eklentileri bir liste alanında görebiliyoruz.
Yardım belgesini okumak istediğimiz eklentiyi seçiyor ve Belgeyi Aç düğmesine basıyoruz.


## Komutlar
Mevcut iki özellik, ana iletişim kutusunu açmak ve NVDA'nın takılıp kalması durumunda NVDA sürecini sonlandırmaktır.
Her ikisinin de atanmış komutları yoktur.
Girdi hareketleri iletişim kutusunda, eklenti araçları dalı altından istenen hareketler atanabilir.

[1]: https://github.com/ruifontes/addonsTools/releases/download/2024.03.25/addonsTools-2024.03.25.nvda-addon
