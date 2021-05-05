YIĞIT(STACK)
      Depolama için ideal
      ---> son giren ilk çıkar ilk giren son çıkar  last in first out   LIFO
      ---> üst üste diziliş kitaplar
      ---> eleman ekleme ve çıkarma işlemi en üstten gerçekleşir
      ---> Dizi veya bağlantı liste kullanarak yapılabilir


      Temel komutlar
      - empty stack --> boş yığıt
      - push --> eleman ekle
      - pop --> eleman çıkar
      - top --> en üsteki eleman
      - size --> total eleman sayısı
      - isEmpty --> eleman var/yok kontrolü, boş mu dolu mu

      elimizdeki örnek elemanlar
        10, 15, 12, 17, 20; 8, 25

        ilk işlem boş bi yığıt oluşturmak, kaba kod olarak düşün

empty stack()
push(10)
push(15)
push(12)
...
push(20) sonrası bi pop yapalım
pop()     --> en üsteki elemanı çıkartır

    ı.              2.          3.            4.

                                              25
                                          ---------
                                20            8
                            ----------    ---------
                   17           17            17
              ----------    ----------    ---------
    12            12            12            12
----------    ----------    ----------    ---------
    15            15            15            15
----------    ----------    ----------    ---------
    10            10            10            10

#10 eklendi
#15 eklendiği zaman yığıt farkedilmeye başlandı
#pop ile 20 gitti
#ama sonrasın yine push ettik 8 ve 25
#top komutuyla en üsteki eleman döndürücek
#size ise 6 oldu
#isEmpty --> false

bu veri yapısını, genelde web tarayıcılarında geri seçeneği olarak düşün.

