Bağlı Listeler
      - Bağlı listelerde bellek elemanları ardışık olarak bulunmayan listelerdir
      - Bağlı listeler iki parametre alır (veri, adres/link)
      - İlk elemanın adresi bir göstericide tutulur
      - Veriler silindiği zaman listenin boyutu azalmaz
      
      Fark
      - Doğrusal listelerde istenildiği zaman liste boyutu azaltılıp arttırılamaz. İşin en başından eleman sayısını belirlemelisin
      - Bağlı listelerde liste boyutu azaltılıp arttırılabilir. Başında değil istenildiği zaman yeni bir boyut/yer eklenir - Eleman sayısı
      
      Bağlı Listeler 4'e ayrılır
      - Tek yönlü Doğrusal
      - Çift Yönlü Doğrusal
      - Tek Yönlü Dairesel
      - Çift Yönlü Dairesel
      
      #Bellekte nasıl tutulur
            --- numaralı veri
            |   English (Veri)   |    005(Adres)   |
            
            005 numaralı veri, kendinden sonraki gelecek olacak elemanı gösterecek
            |  Mathematics(Veri) |    006(Adres)   |
            
            #Bu şekilde aralarında bir ilişki ve hiyerarşik bir düzen var.



    Tek yönlü bağlı listeler

          data    |     link

        verinin linki kendisinden sonra gelecek olan verinin linkini tutuyor
        aslında, bu data ve linki kutusunun bir ayrı linki var başka veride

  elimizde 4 tane liste olsun


1     Amsterdam  |      2
2     Berlin     |      3                 #3 nolu kutucuğu gösterir
3     California |      4
4     Dallas     |      NULL              #tek yönlüolduğu için sonrasında link almaz


        #Tek yönlü dairesel bağlı liste olduğu zaman, son eleman ilk elemanı gösterir, yani null yerine 1. datanın linki olur


    İki yönlü bağlı listeler

          previous link   |     data    |   next link     

12      x         |     Apple     |    13
13      12        |     Banana    |    15
15      13        |     Melon     |    x           ...sonrasında gidecek yeri yok
        #14 nolu verimiz yok bu yüzden göstermez
        #bunları iki yönlü yapan şey aralarında bağlantı olması -->  <--

#peki, bunların dairesel bağlantıları var nasıl olacak
  Tek yönlü dairesel bağlı liste
           #Son elemanın göstericisi, ilk elemanı gösterir - Null yerine link gelir

  İki yönlü dairesel bağlı listeler

      	Link	|	Data	|	Link

  15      35    |   Data    |   22
  22      15    |   Data    |   35
  35      22    |   Data    |   15

