# TurkceKonusmaSenteziIcinArac
Türkçe konuşma sentezcisi tasarımı için veri hazırlama, otomatik metin tasarımı
Konuşma sentezcisi tasarımı öncelikli olarak veri tabanlarının oluşturulmasını lazımdır.Buradaki veritabından kasıt bir metin ve konuşmacının kaydedilmiş sesidir.Veritabanları oluşturulurken önce okunacak metnin tasarlanması gerekmektedir. Bu proje metin şeklinde kaydedilmiş kitapları işleyerek bu kitaplar içerisinden sınırlı sayıda cümle seçen bir programın yazılmasını hedefler. Cümleler az sayıda olmalarına rağmen dildeki çeşitliliği büyük oranda kapsayacak şekilde seçilmeleri gerekmektedir. Bu tür problemler “greedy selection” ismi verilen bir algoritma ile ele alınabilir.
İlk aşamada verilen metinleri bir ön işlemden geçiriyoruz.Bu ön işlemde:
1. Metnin cümlelere ayrılması
2. Türkçe olmayan harflerden ve rakamlardan arındırılması
3. Şapkalı harflerin normal harflere dönüştürülmesi
4. Metnin noktalama işaretlerinden arındırılması
gibi işlemler yapılır.
İkinci aşamada düzenlenmiş metinlerdeki bütün ses üçlülerini bulup bir pickle dosyasına yazdırıyoruz.Daha sonra pickle dosyasını okuyup ses üçlülerini alıyoruz ve en çok kullanılan üçlüden en aza doğru sıralıyoruz.Kullanıcıdan kaç tane üçlü kullanmak istediğini soruyoruz.
Üçüncü aşamada bütün cümlelerden çok uzun olmasın diye 105 harften az ve çok kısa olmasın diye 15 harften çok olan cümleleri seçiyoruz.Şimdi ise “greedy selection” algoritması ile cümle seçimi yapacağız. “greedy selection” algoritmasında mümkün olan ve sonuca en yakın olan seçim yapılır.Bir seçim yapıldığında sonuca en çok yaklaştırıcak olan seçimin yapılmasını önerir.Bizim problemimizde ise elde ettiğimiz cümleleri bir skora göre belirleyip aralarından en uygun cümleleri seçeceğiz.
Bu skoru şöyle belirleyeceğiz:
Mesela cümlemiz: ”Bugün salı.”
Cümledeki bütün üçlüler: (‘ bu’,’bug’,’ugü’,’gün’,’üns’,’nsa’,’sal’,’alı’,’lı ‘) = 9 adet üçlü
Hedeflenen üçlüler: (‘gün’,’sal’,’alı’) = 3 adet üçlü
Skor = (Hedeflenen üçlülerin adeti / Cümledeki bütün üçlülerin adeti) = 3 / 9 = 0.33
Bütün elde ettiğimiz cümleleri yukarıdaki gibi skorluyoruz.En yüksek skor alan cümleyi seçip okunacak cümlelere ekliyoruz ve elde ettiğimiz cümlelerden çıkartıyoruz.Daha sonra geriye kalan cümlelere de aynı işlemi uygulayarak okunacak cümlelerimizi oluşturuyoruz.
Dördüncü aşamada okunacak cümlelerdeki bütün ses ikilileri ile alfabedeki bütün ses ikililerini ile karşılaştırıyoruz ve okunacak cümlelerde olmayan ikilileri alıyoruz.Çünkü dildeki çeşitliliği arttırmak için bütün ses ikililerini de kullanmayı hedefliyeceğiz.
Bu bulduğumuz ses ikililerini de okunacak cümlelere eklemek için bir Türkçe kelimeler listesi bulmalıyız.Bu listedeki kelimelerle olmayan ikililerimizi oluşturacağız.
Mesela “şh” ikilisi okunacak cümlelerde olmasın.Bu ikiliyi oluşturmamız için Türkçe kelimeler listesindeki kelimeleri,ilk kelimenin son harfi “ş” ikinci kelimenin ilk harfi “h” olan iki kelimeyi yan yana getirerek oluşturacağız.
Örneğin: “şh” = “işleriymiş hüsranlığı”
Bu örnekteki gibi diğer olmayan ikilileri de Türkçe kelimeler listesinden oluşturacağız.Sonra bu kelime gruplarını okunacak cümlelere ekliyeceğiz.Tabi ki Türkçede “ğ” ile başlayan kelime olmadığı için ikinci harfi “ğ” olan ikilileri oluşturamayacağız.
Prompter
Prompter,bu oluşturduğumuz okunacak cümleler metnini okuyup ses dosyası olarak kaydetmemize yarayacak.
İlk olarak bir arayüz tasarlıyoruz.Basit bir arayüz için ileri,geri,cümleye git,kaydet ve çıkış butonu ekliyoruz.
İkinci olarak bu butonlara bastığımızda neler olacağını yönetmek.
İleri ve geri butona bastığımızda okunacak cümleler arasında istediğimiz gibi önceki ve sonraki cümlelere geçmemizi sağlamak.
Cümleye git butonuna bastığımızda kullanıcı okunacak cümlelerde istediği cümleye gitmesini sağlamak.
Kaydet butonuna bastığımızda ekrandaki cümleyi kullanıcının okuyup ses dosyası olarak kaydetmemizi sağlamak.
Çıkış butonuna bastığımızda program kapatılacak.
Yukarıda “Türkçe konuşma sentezcisi tasarımı için veri hazırlama, otomatik metin tasarımı” ve “Prompter” işlemlerini yaptık.İlk olarak Türkçe konuşma sentezcisi tasarımı için veri hazırlayıp otomatik metin tasarlayıcı yaptık.Daha sonra abu metini okuyacak bir program tasarladık. Artık buradan sonra kullanıcı okunacak metini okuyup sesini kaydettikten sonra sesini bir programda eğitip Türkçe konuşma sentezcisi yapabilmektedir.
