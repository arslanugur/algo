Listeler
# Bir yapının liste olması için aralarında mantıksal bir tutarlı yanı olması gerekir. Buna dizi de denilebilir.

Doğrusal listeler
    Bellekte tutulur arka arkaya saklanır

   A list
   | Babylon | Copenhagen | Dnipro | Edinburgh |  London |

    - Listenin eleman sayısı : 5
    - İlk Index : 0
    - İlk Index Değeri: London
    - Son Index: 4
    - 4. Index Değeri: Edinburgh
 
    - 0 -> Babylon
    - 1 -> Copenhagen
    - 2 -> Dnipro
    - 3 -> Edinburgh
    - 4 -> London
  
  B list
  | Amsterdam | Babylon | Copenhagen | Dnipro | Edinburgh |  London |         |

        # yeni liste için yeni elemanlar devreye girdi alfabek şekilde sıralanması gerekli, algoritma kullanıldı

    Listenin yeni boyutu: 7
    - 0 -> Amsterdam
    - 1 -> Babylon
    - 2 -> Copenhagen
    - 3 -> Dnipro
    - 4 -> Edinburgh
    - 5 -> London
    - 6 -> NULL      #yedi elemanlı bir liste olacağını belirledik. Bellekteki alanı kullanmadık 

    #Index değerleri komple değişti. Doğrusal listelerde veri ekleme işlemi sistemi karmaşık hale  getiriyor
    #Bellek yorulmasına sebebi. 
 
 
 
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
            
            
            





