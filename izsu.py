baska_abone = "e"
konut_tipi_toplam_hane_sayısı = 0
konut_birinci_kademede_hane_sayisi = 0
konut_birinci_kademede_su_harcama = 0
konut_ikinci_kademede_hane_sayisi = 0
konut_ikinci_kademede_su_harcama = 0
konut_ucuncu_kademede_hane_sayisi = 0
konut_ucuncu_kademede_su_harcama = 0
konuttaki_tek_hanede_onceliksiz = 0
konuttaki_tek_hanede_engelli_oncelikli = 0
konuttaki_tek_hanede_diger_oncelikli = 0
konuttaki_toplam_engelli_oncelikli = 0
konuttaki_toplam_diger_oncelikli = 0
sehit_oncelikli_hane_sayisi = 0
gazi_oncelikli_hane_sayisi = 0
sporcu_oncelikli_hane_sayisi = 0
engelli_oncelikli_hane_sayisi = 0
konut_abone_sayisi = 0
isyeri_abone_sayisi = 0
resmi_daire_abone_sayisi = 0
organize_sanayi_abone_sayisi = 0
iths_abone_sayisi = 0
toplam_abone_sayisi = 0
konut_tipi_kullanılan_toplam_su = 0
isyeri_tipi_kullanılan_toplam_su = 0
resmi_daire_tipi_kullanılan_toplam_su = 0
organize_sanayi_tipi_kullanılan_toplam_su = 0
iths_tipi_kullanılan_toplam_su = 0
arti_elli_ton_iths = 0
arti_yuz_ton_abone_veya_arti_500_tl = 0
max_resmi_daire = 0
max_aylık_su_tuketimi = 0  # konut tipi hariç yapacağımız hesaplama
max_aylık_su_ucret = 0  # max aylık su tüketim ücretini almak için
bornova_aylık_su_tuketimi = 0
konut_tipi_sadece_su_ucreti = 0  # aylığa çevireceğiz
isyeri_tipi_sadece_su_ucreti = 0
resmi_daire_tipi_sadece_su_ucreti = 0
organize_sanayi_tipi_sadece_su_ucreti = 0
iths_tipi_sadece_su_ücreti = 0
izsu_toplam_payı = 0
ilcenin_toplam_payı = 0
buyuksehir_belediyenin_toplam_payı = 0
devletin_toplam_payı = 0
while baska_abone == "e" or baska_abone == "E":
    abone_no = int(input("Abone numarasını giriniz:"))
    abone_tipi_kodu = int(input("Abone tipini giriniz(1-5) : "))

    while abone_tipi_kodu < 1 or abone_tipi_kodu > 5:
        abone_tipi_kodu = int(input("Hatalı giriş. Abona numaranızı düzgün giriniz : "))

    if abone_tipi_kodu == 1:
        hane_sayısı = int(input("Hane sayısını giriniz : "))
        while hane_sayısı < 1:
            hane_sayısı = int(input("Hatalı giriş. Hane sayısını düzgün giriniz : "))
        if hane_sayısı == 1:
            indirim_durumu = input("indirim durumunuzu girin(Yok/Şehit/Gazi/Engelli/Sporcu(y/Y/ş/Ş/g/G/e/E/s/S) : ")
            while indirim_durumu not in ["y","Y","ş","Ş","g","G","e","E","s","S"]:
                indirim_durumu = input("indirim durumunuzu girin(Yok/Şehit/Gazi/Engelli/Sporcu(y/Y/ş/Ş/g/G/e/E/s/S) : ")
            if indirim_durumu in ["ş","Ş","g","G","e","E","s","S"]:
                if indirim_durumu == "e" or indirim_durumu == "E":
                    konuttaki_tek_hanede_engelli_oncelikli += 1
                    konuttaki_toplam_engelli_oncelikli += 1
                elif indirim_durumu in ["ş","Ş","g","G","s","S"]:
                    konuttaki_tek_hanede_diger_oncelikli += 1
                    konuttaki_toplam_diger_oncelikli += 1
            else:
                konuttaki_tek_hanede_onceliksiz += 1
        else:
            oncelikli_hane_sayisi = int(input("Şehit, Gazi,Sporcu önceliğine sahip hane sayısı : "))
            engelli_oncelikli_hane_sayisi = int(input("Engelli önceliğine sahip hane sayısı : "))
            while oncelikli_hane_sayisi + engelli_oncelikli_hane_sayisi > hane_sayısı:
                oncelikli_hane_sayisi = int(input("Şehit, Gazi,Sporcu önceliğine sahip hane sayısını düzgün girin : "))
                engelli_oncelikli_hane_sayisi = int(input("Engelli önceliğine sahip hane sayısını düzgün girin : "))
            onceliksiz_hane_sayisi = hane_sayısı-(engelli_oncelikli_hane_sayisi+oncelikli_hane_sayisi)
            konuttaki_toplam_engelli_oncelikli += engelli_oncelikli_hane_sayisi
            konuttaki_toplam_diger_oncelikli += oncelikli_hane_sayisi

    onceki_sayac = int(input("Önceki sayaç değerini giriniz : "))
    while onceki_sayac < 0:
        onceki_sayac = int(input("Önceki sayaç değerini düzgün giriniz : "))
    simdiki_sayac = int(input("Şimdiki sayaç değerini girin : "))
    while simdiki_sayac < onceki_sayac:
        simdiki_sayac = int(input("Şimdiki sayaç değerini düzgün girin : "))
    sayac_farkı = simdiki_sayac - onceki_sayac
    donem = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını girin : "))
    while donem <= 0:
        donem = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını düzgün girin : "))

    print("Abone Numaranız : ",abone_no)
    if abone_tipi_kodu ==1:
        konut_tipi_toplam_hane_sayısı += hane_sayısı
        abone_tipi_kodu_adı = "Konut"
        konut_abone_sayisi += 1
        toplam_abone_sayisi += hane_sayısı
        konut_tipi_kullanılan_toplam_su += (sayac_farkı*30/donem) # aylık istediği için aylığa çevirdik !!!
        konut_hane_basına_dusen_su_mıktarı=(sayac_farkı*30/donem)/konut_tipi_toplam_hane_sayısı
        bornova_aylık_su_tuketimi += sayac_farkı*30/donem
    elif abone_tipi_kodu ==2:
        abone_tipi_kodu_adı = "İşyeri"
        isyeri_abone_sayisi += 1
        toplam_abone_sayisi += 1
        isyeri_tipi_kullanılan_toplam_su += sayac_farkı*30/donem
        bornova_aylık_su_tuketimi += sayac_farkı*30/donem
    elif abone_tipi_kodu == 3:
        abone_tipi_kodu_adı = "Resmi Daire"
        resmi_daire_abone_sayisi +=1
        toplam_abone_sayisi += 1
        resmi_daire_tipi_kullanılan_toplam_su += sayac_farkı*30/donem
        bornova_aylık_su_tuketimi += sayac_farkı*30/donem
    elif abone_tipi_kodu == 4:
        abone_tipi_kodu_adı = "Organize Sanayi"
        organize_sanayi_abone_sayisi += 1
        toplam_abone_sayisi += 1
        organize_sanayi_tipi_kullanılan_toplam_su += sayac_farkı*30/donem
        bornova_aylık_su_tuketimi += sayac_farkı*30/donem
    else:
        abone_tipi_kodu_adı = "İlçe Tarımsal ve Hayvan Sulama"
        if sayac_farkı*30/donem > 50: # sayaç farkını aylık yaptık
            arti_elli_ton_iths += 1
        iths_abone_sayisi += 1
        toplam_abone_sayisi += 1
        iths_tipi_kullanılan_toplam_su += sayac_farkı*30/donem
        bornova_aylık_su_tuketimi += sayac_farkı*30/donem
    print("Abone tipiniz : ",abone_tipi_kodu_adı)
    print("Dönemlik su tüketim miktarı : ",sayac_farkı)
    print("Dönemlik atık su miktarı : ",sayac_farkı)

    if abone_tipi_kodu == 1:
        SU_TUKETIM_UCRETI_KADEME1 = 2.89
        ATIK_SU_UCRETI_KADEME1 = 1.44
        SU_TUKETIM_UCRETI_KADEME2 = 3.13
        ATIK_SU_UCRETI_KADEME2 = 1.56
        SU_TUKETIM_UCRETI_KADEME3 = 6.43
        ATIK_SU_UCRETI_KADEME3 = 3.22
        if hane_sayısı == 1:
            if konuttaki_tek_hanede_engelli_oncelikli ==1:
                if 0 < sayac_farkı <= (13 * donem / 30):
                    konut_birinci_kademede_hane_sayisi += 1
                    konut_birinci_kademede_su_harcama += sayac_farkı*30/donem
                    su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI_KADEME1/2
                    atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI_KADEME1/2
                elif (13 * donem / 30) < sayac_farkı <= (20 * donem / 30):
                    konut_ikinci_kademede_hane_sayisi += 1
                    konut_ikinci_kademede_su_harcama += sayac_farkı*30/donem # aylığa çevirdik
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1/2 + (sayac_farkı - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2/2
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1/2 + (sayac_farkı - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2/2
                else:
                    konut_ucuncu_kademede_hane_sayisi += 1
                    konut_ucuncu_kademede_su_harcama += sayac_farkı*30/donem # aylığa çevirdik
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1/2 + ((20 * donem / 30) - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2/2 + (sayac_farkı - (20 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME3
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1/2 + ((20 * donem / 30) - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2/2 + (sayac_farkı - (20 * donem / 30)) * ATIK_SU_UCRETI_KADEME3
                if su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100: # aylık olarak almak için çevirdik
                    arti_yuz_ton_abone_veya_arti_500_tl += 1
                konut_tipi_sadece_su_ucreti += su_tuketim_ucreti*30/donem
            elif konuttaki_tek_hanede_diger_oncelikli == 1:
                if 0 < sayac_farkı <= (13 * donem / 30):
                    konut_birinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_birinci_kademede_hane_sayisi += 1
                    su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI_KADEME1 / 2
                    atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI_KADEME1 / 2
                elif (13 * donem / 30) < sayac_farkı <= (20 * donem / 30):
                    konut_ikinci_kademede_hane_sayisi +=1
                    konut_ikinci_kademede_su_harcama += sayac_farkı*30/donem
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 / 2 + (sayac_farkı - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2 / 2
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 / 2 + (sayac_farkı - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2 / 2
                else:
                    konut_ucuncu_kademede_hane_sayisi +=1
                    konut_ucuncu_kademede_su_harcama += sayac_farkı*30/donem
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 / 2 + ((20 * donem / 30) - (13 * donem / 30))* SU_TUKETIM_UCRETI_KADEME2 / 2 + (sayac_farkı - (20 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME3/2
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 / 2 + ((20 * donem / 30) - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2 / 2 + (sayac_farkı - (20 * donem / 30)) * ATIK_SU_UCRETI_KADEME3/2
                if su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
                    arti_yuz_ton_abone_veya_arti_500_tl += 1
                konut_tipi_sadece_su_ucreti += su_tuketim_ucreti*30/donem
            elif konuttaki_tek_hanede_onceliksiz ==1:
                if 0<sayac_farkı<=(13*donem/30):
                    konut_birinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_birinci_kademede_hane_sayisi += 1
                    su_tuketim_ucreti = sayac_farkı*SU_TUKETIM_UCRETI_KADEME1
                    atık_su_ucreti = sayac_farkı*ATIK_SU_UCRETI_KADEME1
                elif (13*donem/30)<sayac_farkı<=(20*donem/30):
                    konut_ikinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_ikinci_kademede_hane_sayisi += 1
                    su_tuketim_ucreti = (13*donem/30)*SU_TUKETIM_UCRETI_KADEME1+(sayac_farkı-(13*donem/30))*SU_TUKETIM_UCRETI_KADEME2
                    atık_su_ucreti = (13*donem/30)*ATIK_SU_UCRETI_KADEME1+(sayac_farkı-(13*donem/30))*ATIK_SU_UCRETI_KADEME2
                else:
                    konut_ucuncu_kademede_hane_sayisi += 1
                    konut_ucuncu_kademede_su_harcama += sayac_farkı*30/donem
                    su_tuketim_ucreti=(13*donem/30)*SU_TUKETIM_UCRETI_KADEME1+((20*donem/30)-(13*donem/30))*SU_TUKETIM_UCRETI_KADEME2+(sayac_farkı-(20*donem/30))*SU_TUKETIM_UCRETI_KADEME3
                    atık_su_ucreti = (13*donem/30)*ATIK_SU_UCRETI_KADEME1+((20*donem/30)-(13*donem/30))*ATIK_SU_UCRETI_KADEME2+(sayac_farkı-(20*donem/30))*ATIK_SU_UCRETI_KADEME3
                if su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
                    arti_yuz_ton_abone_veya_arti_500_tl += 1
                konut_tipi_sadece_su_ucreti += su_tuketim_ucreti
            KDV_ORANI = 0.08
            CTV_ORANI = 0.39
            ctv_ucreti = sayac_farkı*CTV_ORANI
            katı_atik_toplama_kdv = 13*hane_sayısı*KDV_ORANI
            katı_atik_toplama_ucreti = hane_sayısı*13+katı_atik_toplama_kdv
            katı_atik_bertaraf_kdv = 2.54*hane_sayısı*KDV_ORANI
            katı_atik_bertaraf_ucreti = 2.54*hane_sayısı + katı_atik_bertaraf_kdv
            buyuksehir_belediyenin_toplam_payı += katı_atik_bertaraf_ucreti
            toplam_su_ucreti = su_tuketim_ucreti+atık_su_ucreti
            toplam_sudan_kdv_ucreti = (toplam_su_ucreti)*KDV_ORANI
            donem_toplam_fatura_tutari = (toplam_su_ucreti+toplam_sudan_kdv_ucreti + ctv_ucreti+katı_atik_toplama_ucreti + katı_atik_bertaraf_ucreti)
            devlete_gidecek_kdv_tutari = katı_atik_bertaraf_kdv+katı_atik_toplama_kdv+toplam_sudan_kdv_ucreti
            devletin_toplam_payı += devlete_gidecek_kdv_tutari
            ilceye_gidecek_tutar = ctv_ucreti+katı_atik_toplama_ucreti-(katı_atik_toplama_kdv) # kdv devlete gideceği için çıkardık
            ilcenin_toplam_payı += ilceye_gidecek_tutar
            izsu_payi = donem_toplam_fatura_tutari-ctv_ucreti-katı_atik_toplama_ucreti-katı_atik_bertaraf_ucreti-(devlete_gidecek_kdv_tutari) # ücret sonuçları kdv'li olduğu için ve kdvler devlete gittiği için çıkarmayı yaptık
            izsu_toplam_payı += izsu_payi
            print("Dönemlik su tüketim ücretini:",format(su_tuketim_ucreti,".2f"))
            print("Dönemlik atık su ücretiniz : ",format(atık_su_ucreti,".2f"))
            print("Dönemlik toplam su tüketim ve atık su ücretiniz : ",su_tuketim_ucreti+atık_su_ucreti)
            print("Çevre Temizlik Vergisi : ",format(ctv_ucreti,".2f"))
            print("Katı Atık Toplama Ücreti : ",format(katı_atik_toplama_ucreti,".2f"))
            print("Katı Atık Berteraf Ücreti : ",format(katı_atik_bertaraf_ucreti,".2f"))
            print("Dönemlik toplam fatura bedeli : ",format(donem_toplam_fatura_tutari,".2f"))
            print("Devlete aktarılacak KDV ücreti toplamı : ",format(devlete_gidecek_kdv_tutari,".2f"))
            print("İlçe belediyesine aktarılacak tutar : ",format(ilceye_gidecek_tutar,".2f"))
            print("Büyükşehir belediyeye aktarılacak tutar : ",format(katı_atik_bertaraf_ucreti,".2f"))
            print("İzsuya gidecek pay : ",format(izsu_payi,".2f"))
        else:# Çok hanelilere geçtik. Tek hanelilerin hepsi bitti.
            sayac_farkı=sayac_farkı/hane_sayısı
            SU_TUKETIM_UCRETI_KADEME1 = 2.89
            ATIK_SU_UCRETI_KADEME1 = 1.44
            SU_TUKETIM_UCRETI_KADEME2 = 3.13
            ATIK_SU_UCRETI_KADEME2 = 1.56
            SU_TUKETIM_UCRETI_KADEME3 = 6.43
            ATIK_SU_UCRETI_KADEME3 = 3.22
            konut_tipi_genel_toplam = 0
            su_tuketim_ucreti_toplamı = 0
            atık_su_ucreti_toplamı = 0
            for x in range(engelli_oncelikli_hane_sayisi):
                if 0 < sayac_farkı <= (13 * donem / 30):
                    konut_birinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_birinci_kademede_hane_sayisi += 1
                    su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI_KADEME1 / 2
                    atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI_KADEME1 / 2
                elif (13 * donem / 30) < sayac_farkı <= (20 * donem / 30):
                    konut_ikinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_ikinci_kademede_hane_sayisi += 1
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 / 2 + (sayac_farkı - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2 / 2
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 / 2 + (sayac_farkı - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2 / 2
                else:
                    konut_ucuncu_kademede_hane_sayisi += 1
                    konut_ucuncu_kademede_su_harcama += sayac_farkı*30/donem
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 / 2 + ((20 * donem / 30) - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2 / 2 + (sayac_farkı - (20 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME3
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 / 2 + ((20 * donem / 30) - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2 / 2 + (sayac_farkı - (20 * donem / 30)) * ATIK_SU_UCRETI_KADEME3
                su_tuketim_ucreti_toplamı += su_tuketim_ucreti
                atık_su_ucreti_toplamı +=atık_su_ucreti
                konut_tipi_sadece_su_ucreti += su_tuketim_ucreti*30/donem # aylık olarak aldık
                konut_tipi_genel_toplam += su_tuketim_ucreti+atık_su_ucreti
                if su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
                    arti_yuz_ton_abone_veya_arti_500_tl += 1
            for x in range(oncelikli_hane_sayisi): #çok haneli diğer öncelikliler için toplam ücret alma
                if 0 < sayac_farkı <= (13 * donem / 30):
                    konut_birinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_birinci_kademede_hane_sayisi +=1
                    su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI_KADEME1 / 2
                    atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI_KADEME1 / 2
                elif (13 * donem / 30) < sayac_farkı <= (20 * donem / 30):
                    konut_ikinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_ikinci_kademede_hane_sayisi += 1
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 / 2 + (sayac_farkı - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2 / 2
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 / 2 + (sayac_farkı - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2 / 2
                else:
                    konut_ucuncu_kademede_hane_sayisi += 1
                    konut_ucuncu_kademede_su_harcama += sayac_farkı*30/donem
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 / 2 + ((20 * donem / 30) - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2 / 2 + (sayac_farkı - (20 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME3 / 2
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 / 2 + ((20 * donem / 30) - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2 / 2 + (sayac_farkı - (20 * donem / 30)) * ATIK_SU_UCRETI_KADEME3 / 2
                su_tuketim_ucreti_toplamı += su_tuketim_ucreti
                atık_su_ucreti_toplamı +=atık_su_ucreti
                konut_tipi_sadece_su_ucreti += su_tuketim_ucreti*30/donem
                konut_tipi_genel_toplam += su_tuketim_ucreti+atık_su_ucreti
                if su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
                    arti_yuz_ton_abone_veya_arti_500_tl += 1
            for x in range(onceliksiz_hane_sayisi):
                if 0 < sayac_farkı <= (13 * donem / 30):
                    konut_birinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_birinci_kademede_hane_sayisi += 1
                    su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI_KADEME1
                    atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI_KADEME1
                elif (13 * donem / 30) < sayac_farkı <= (20 * donem / 30):
                    konut_ikinci_kademede_su_harcama += sayac_farkı*30/donem
                    konut_ikinci_kademede_hane_sayisi += 1
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 + (sayac_farkı - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 + (sayac_farkı - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2
                else:
                    konut_ucuncu_kademede_hane_sayisi += 1
                    konut_ucuncu_kademede_su_harcama += sayac_farkı*30/donem
                    su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 + ((20 * donem / 30) - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2 + (sayac_farkı - (20 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME3
                    atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 + ((20 * donem / 30) - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2 + (sayac_farkı - (20 * donem / 30)) * ATIK_SU_UCRETI_KADEME3
                su_tuketim_ucreti_toplamı += su_tuketim_ucreti
                atık_su_ucreti_toplamı +=atık_su_ucreti
                konut_tipi_sadece_su_ucreti += su_tuketim_ucreti*30/donem
                konut_tipi_genel_toplam += su_tuketim_ucreti+atık_su_ucreti
                if su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
                    arti_yuz_ton_abone_veya_arti_500_tl += 1
            KDV_ORANI = 0.08
            CTV_ORANI = 0.39
            ctv_ucreti = sayac_farkı*hane_sayısı * CTV_ORANI #çünkü çtv toplam suya göre hesaplanır.
            katı_atik_toplama_kdv = 13 * hane_sayısı * KDV_ORANI
            katı_atik_toplama_ucreti = hane_sayısı * 13 + katı_atik_toplama_kdv
            katı_atik_bertaraf_kdv = 2.54 * hane_sayısı * KDV_ORANI
            katı_atik_bertaraf_ucreti = 2.54 * hane_sayısı + katı_atik_bertaraf_kdv
            buyuksehir_belediyenin_toplam_payı += katı_atik_bertaraf_ucreti
            toplam_sudan_kdv_ucreti = (konut_tipi_genel_toplam) * KDV_ORANI
            donem_toplam_fatura_tutari = konut_tipi_genel_toplam + toplam_sudan_kdv_ucreti + ctv_ucreti + katı_atik_toplama_ucreti + katı_atik_bertaraf_ucreti
            devlete_gidecek_kdv_tutari = katı_atik_bertaraf_kdv + katı_atik_toplama_kdv + toplam_sudan_kdv_ucreti
            devletin_toplam_payı += devlete_gidecek_kdv_tutari
            ilceye_gidecek_tutar = ctv_ucreti + katı_atik_toplama_ucreti - (katı_atik_toplama_kdv)  # kdv devlete gideceği için çıkardık
            ilcenin_toplam_payı += ilceye_gidecek_tutar
            izsu_payi = donem_toplam_fatura_tutari - ctv_ucreti - katı_atik_toplama_ucreti - katı_atik_bertaraf_ucreti - (devlete_gidecek_kdv_tutari)  # ücret sonuçları kdv'li olduğu için ve kdvler devlete gittiği için çıkarmayı yaptık
            izsu_toplam_payı += izsu_payi
            print("Dönemlik su tüketim ücretini:", format(su_tuketim_ucreti*hane_sayısı, ".2f"))
            print("Dönemlik atık su ücretiniz : ",format(atık_su_ucreti*hane_sayısı,".2f"))
            print("Dönemlik toplam su tüketim ve atık su ücretiniz : ", (su_tuketim_ucreti + atık_su_ucreti)*hane_sayısı,)
            print("Çevre Temizlik Vergisi : ", format(ctv_ucreti,".2f"))
            print("Katı Atık Toplama Ücreti : ", format(katı_atik_toplama_ucreti,".2f"))
            print("Katı Atık Berteraf Ücreti : ", format(katı_atik_bertaraf_ucreti,".2f"))
            print("Dönemlik toplam fatura bedeli : ", format(donem_toplam_fatura_tutari,".2f"))
            print("Devlete aktarılacak KDV ücreti toplamı : ", format(devlete_gidecek_kdv_tutari,".2f"))
            print("İlçe belediyesine aktarılacak tutar : ", format(ilceye_gidecek_tutar,".2f"))
            print("Büyükşehir belediyeye aktarılacak tutar : ", format(katı_atik_bertaraf_ucreti,".2f"))
            print("İzsuya gidecek pay : ", format(izsu_payi,".2f"))
    elif abone_tipi_kodu == 2:
        hane_sayısı = 1 # işyeri olduğu için zaten tek hane kabul ediliyor.
        if sayac_farkı*30/donem > max_aylık_su_tuketimi:
            max_aylık_su_tuketimi = sayac_farkı
            max_aylık_su_tuketimi_abone_no = abone_no
        SU_TUKETIM_UCRETI = 7.38
        ATIK_SU_UCRETI = 3.68
        isyeri_su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI
        if isyeri_su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
            arti_yuz_ton_abone_veya_arti_500_tl += 1
        isyeri_atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI
        isyeri_tipi_sadece_su_ucreti += isyeri_su_tuketim_ucreti*30/donem
        isyeri_genel_toplam_su_ucreti = isyeri_atık_su_ucreti+ isyeri_su_tuketim_ucreti
        if isyeri_su_tuketim_ucreti*30/donem > max_aylık_su_ucret:
            max_aylık_su_ucret = isyeri_su_tuketim_ucreti*30/donem
            max_aylık_su_ucreti_abone_no = abone_no
            max_aylık_su_ucretinin_su_tuketimi = sayac_farkı*30/donem
            max_aylık_su_ucretinin_tipi = "İşyeri"
        KDV_ORANI = 0.08
        CTV_ORANI = 0.39
        ctv_ucreti = sayac_farkı * CTV_ORANI
        katı_atik_toplama_kdv = 13 * hane_sayısı * KDV_ORANI
        katı_atik_toplama_ucreti = hane_sayısı * 13 + katı_atik_toplama_kdv
        katı_atik_bertaraf_kdv = 2.54 * hane_sayısı * KDV_ORANI
        katı_atik_bertaraf_ucreti = 2.54 * hane_sayısı + katı_atik_bertaraf_kdv
        buyuksehir_belediyenin_toplam_payı += katı_atik_bertaraf_ucreti
        toplam_sudan_kdv_ucreti = (isyeri_genel_toplam_su_ucreti) * KDV_ORANI
        donem_toplam_fatura_tutari = isyeri_genel_toplam_su_ucreti + toplam_sudan_kdv_ucreti + ctv_ucreti + katı_atik_toplama_ucreti + katı_atik_bertaraf_ucreti
        devlete_gidecek_kdv_tutari = katı_atik_bertaraf_kdv + katı_atik_toplama_kdv + toplam_sudan_kdv_ucreti
        devletin_toplam_payı += devlete_gidecek_kdv_tutari
        ilceye_gidecek_tutar = ctv_ucreti + katı_atik_toplama_ucreti - (katı_atik_toplama_kdv)  # kdv devlete gideceği için çıkardık
        ilcenin_toplam_payı += ilceye_gidecek_tutar
        izsu_payi = donem_toplam_fatura_tutari - ctv_ucreti - katı_atik_toplama_ucreti - katı_atik_bertaraf_ucreti - (devlete_gidecek_kdv_tutari)  # ücret sonuçları kdv'li olduğu için ve kdvler devlete gittiği için çıkarmayı yaptık
        izsu_toplam_payı += izsu_payi
        print("Dönemlik su tüketim ücretini:", format(isyeri_su_tuketim_ucreti, ".2f"))
        print("Dönemlik atık su ücretiniz : ", format(isyeri_atık_su_ucreti,".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücretiniz : ", format(isyeri_su_tuketim_ucreti + isyeri_atık_su_ucreti,".2f"))
        print("Çevre Temizlik Vergisi : ", format(ctv_ucreti,".2f"))
        print("Katı Atık Toplama Ücreti : ", format(katı_atik_toplama_ucreti,".2f"))
        print("Katı Atık Berteraf Ücreti : ", format(katı_atik_bertaraf_ucreti,".2f"))
        print("Dönemlik toplam fatura bedeli : ", format(donem_toplam_fatura_tutari,".2f"))
        print("Devlete aktarılacak KDV ücreti toplamı : ", format(devlete_gidecek_kdv_tutari,".2f"))
        print("İlçe belediyesine aktarılacak tutar : ", format(ilceye_gidecek_tutar,".2f"))
        print("Büyükşehir belediyeye aktarılacak tutar : ", format(katı_atik_bertaraf_ucreti,".2f"))
        print("İzsuya gidecek pay : ", format(izsu_payi,".2f"))
    elif abone_tipi_kodu == 3:
        hane_sayısı = 1  # resmi daire olduğu için zaten tek hane kabul ediliyor.
        if sayac_farkı*30/donem > max_aylık_su_tuketimi:
            max_aylık_su_tuketimi = sayac_farkı
            max_aylık_su_tuketimi_abone_no = abone_no
        if max_resmi_daire < sayac_farkı*30/donem:# dönemlik olan su kullanımını aylığa çevirdik
            max_resmi_daire = sayac_farkı*30/donem
            max_resmi_daire_abone_no = abone_no
        SU_TUKETIM_UCRETI = 4.34
        ATIK_SU_UCRETI = 2.16
        resmi_daire_su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI
        resmi_daire_tipi_sadece_su_ucreti += resmi_daire_su_tuketim_ucreti*30/donem #aylık olarak aldık
        if resmi_daire_su_tuketim_ucreti*30/donem > max_aylık_su_ucret:
            max_aylık_su_ucret = resmi_daire_su_tuketim_ucreti*30/donem
            max_aylık_su_ucreti_abone_no = abone_no
            max_aylık_su_ucretinin_su_tuketimi = sayac_farkı*30/donem
            max_aylık_su_ucretinin_tipi = "Resmi Daire. "
        if resmi_daire_su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
            arti_yuz_ton_abone_veya_arti_500_tl += 1
        resmi_daire_atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI
        resmi_daire_genel_toplam_su_ucreti = resmi_daire_atık_su_ucreti + resmi_daire_su_tuketim_ucreti
        KDV_ORANI = 0.08
        CTV_ORANI = 0.39
        ctv_ucreti = sayac_farkı * CTV_ORANI
        katı_atik_toplama_kdv = 13 * hane_sayısı * KDV_ORANI
        katı_atik_toplama_ucreti = hane_sayısı * 13 + katı_atik_toplama_kdv
        katı_atik_bertaraf_kdv = 2.54 * hane_sayısı * KDV_ORANI
        katı_atik_bertaraf_ucreti = 2.54 * hane_sayısı + katı_atik_bertaraf_kdv
        buyuksehir_belediyenin_toplam_payı += katı_atik_bertaraf_ucreti
        toplam_sudan_kdv_ucreti = (resmi_daire_genel_toplam_su_ucreti) * KDV_ORANI
        donem_toplam_fatura_tutari = resmi_daire_genel_toplam_su_ucreti + toplam_sudan_kdv_ucreti + ctv_ucreti + katı_atik_toplama_ucreti + katı_atik_bertaraf_ucreti
        devlete_gidecek_kdv_tutari = katı_atik_bertaraf_kdv + katı_atik_toplama_kdv + toplam_sudan_kdv_ucreti
        devletin_toplam_payı += devlete_gidecek_kdv_tutari
        ilceye_gidecek_tutar = ctv_ucreti + katı_atik_toplama_ucreti - (katı_atik_toplama_kdv)  # kdv devlete gideceği için çıkardık
        ilcenin_toplam_payı += ilceye_gidecek_tutar
        izsu_payi = donem_toplam_fatura_tutari - ctv_ucreti - katı_atik_toplama_ucreti - katı_atik_bertaraf_ucreti - (devlete_gidecek_kdv_tutari)  # ücret sonuçları kdv'li olduğu için ve kdvler devlete gittiği için çıkarmayı yaptık
        izsu_toplam_payı += izsu_payi
        print("Dönemlik su tüketim ücretini:", format(resmi_daire_su_tuketim_ucreti, ".2f"))
        print("Dönemlik atık su ücretiniz : ", format(resmi_daire_atık_su_ucreti,".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücretiniz : ", format(resmi_daire_su_tuketim_ucreti + resmi_daire_atık_su_ucreti,".2f"))
        print("Çevre Temizlik Vergisi : ", format(ctv_ucreti,".2f"))
        print("Katı Atık Toplama Ücreti : ", format(katı_atik_toplama_ucreti,".2f"))
        print("Katı Atık Berteraf Ücreti : ", format(katı_atik_bertaraf_ucreti,".2f"))
        print("Dönemlik toplam fatura bedeli : ", format(donem_toplam_fatura_tutari,".2f"))
        print("Devlete aktarılacak KDV ücreti toplamı : ", format(devlete_gidecek_kdv_tutari,".2f"))
        print("İlçe belediyesine aktarılacak tutar : ", format(ilceye_gidecek_tutar,".2f"))
        print("Büyükşehir belediyeye aktarılacak tutar : ", format(katı_atik_bertaraf_ucreti,".2f"))
        print("İzsuya gidecek pay : ", izsu_payi)
    elif abone_tipi_kodu == 4:
        hane_sayısı = 1  # organize sanayi olduğu için zaten tek hane kabul ediliyor.
        if sayac_farkı*30/donem > max_aylık_su_tuketimi:
            max_aylık_su_tuketimi = sayac_farkı
            max_aylık_su_tuketimi_abone_no = abone_no
        SU_TUKETIM_UCRETI = 5
        ATIK_SU_UCRETI = 2.50
        org_sanayi_su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI
        organize_sanayi_tipi_sadece_su_ucreti += org_sanayi_su_tuketim_ucreti*30/donem #aylık olarak hesapladık
        if org_sanayi_su_tuketim_ucreti*30/donem > max_aylık_su_ucret:
            max_aylık_su_ucret = org_sanayi_su_tuketim_ucreti*30/donem
            max_aylık_su_ucreti_abone_no = abone_no
            max_aylık_su_ucretinin_su_tuketimi = sayac_farkı*30/donem
            max_aylık_su_ucretinin_tipi = "Organize Sanayi ."
        if org_sanayi_su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
            arti_yuz_ton_abone_veya_arti_500_tl += 1
        org_sanayi_atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI
        org_sanayi_genel_toplam_su_ucreti = org_sanayi_atık_su_ucreti + org_sanayi_su_tuketim_ucreti
        KDV_ORANI = 0.08
        CTV_ORANI = 0.39
        ctv_ucreti = sayac_farkı * CTV_ORANI
        katı_atik_toplama_kdv = 13 * hane_sayısı * KDV_ORANI
        katı_atik_toplama_ucreti = hane_sayısı * 13 + katı_atik_toplama_kdv
        katı_atik_bertaraf_kdv = 2.54 * hane_sayısı * KDV_ORANI
        katı_atik_bertaraf_ucreti = 2.54 * hane_sayısı + katı_atik_bertaraf_kdv
        buyuksehir_belediyenin_toplam_payı += katı_atik_bertaraf_ucreti
        toplam_sudan_kdv_ucreti = (org_sanayi_genel_toplam_su_ucreti) * KDV_ORANI
        donem_toplam_fatura_tutari = org_sanayi_genel_toplam_su_ucreti + toplam_sudan_kdv_ucreti + ctv_ucreti + katı_atik_toplama_ucreti + katı_atik_bertaraf_ucreti
        devlete_gidecek_kdv_tutari = katı_atik_bertaraf_kdv + katı_atik_toplama_kdv + toplam_sudan_kdv_ucreti
        devletin_toplam_payı += devlete_gidecek_kdv_tutari
        ilceye_gidecek_tutar = ctv_ucreti + katı_atik_toplama_ucreti - (katı_atik_toplama_kdv)  # kdv devlete gideceği için çıkardık
        ilcenin_toplam_payı += ilceye_gidecek_tutar
        izsu_payi = donem_toplam_fatura_tutari - ctv_ucreti - katı_atik_toplama_ucreti - katı_atik_bertaraf_ucreti - (devlete_gidecek_kdv_tutari)  # ücret sonuçları kdv'li olduğu için ve kdvler devlete gittiği için çıkarmayı yaptık
        izsu_toplam_payı += izsu_payi
        print("Dönemlik su tüketim ücretini:", format(org_sanayi_su_tuketim_ucreti, ".2f"))
        print("Dönemlik atık su ücretiniz : ", format(org_sanayi_atık_su_ucreti,".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücretiniz : ", format(org_sanayi_su_tuketim_ucreti + org_sanayi_atık_su_ucreti,".2f"))
        print("Çevre Temizlik Vergisi : ", format(ctv_ucreti,".2f"))
        print("Katı Atık Toplama Ücreti : ", format(katı_atik_toplama_ucreti,".2f"))
        print("Katı Atık Berteraf Ücreti : ", format(katı_atik_bertaraf_ucreti,".2f"))
        print("Dönemlik toplam fatura bedeli : ", format(donem_toplam_fatura_tutari,".2f"))
        print("Devlete aktarılacak KDV ücreti toplamı : ", format(devlete_gidecek_kdv_tutari,".2f"))
        print("İlçe belediyesine aktarılacak tutar : ", format(ilceye_gidecek_tutar,".2f"))
        print("Büyükşehir belediyeye aktarılacak tutar : ", format(katı_atik_bertaraf_ucreti,".2f"))
        print("İzsuya gidecek pay : ", format(izsu_payi,".2f"))
    else:
        hane_sayısı = 1  # ilçe tarımsal ve hayvan sulama olduğu için zaten tek hane kabul ediliyor.
        if sayac_farkı*30/donem > max_aylık_su_tuketimi:
            max_aylık_su_tuketimi = sayac_farkı
            max_aylık_su_tuketimi_abone_no = abone_no
        SU_TUKETIM_UCRETI_KADEME1 = 1.45
        ATIK_SU_UCRETI_KADEME1 = 0.72
        SU_TUKETIM_UCRETI_KADEME2 = 2.89
        ATIK_SU_UCRETI_KADEME2 = 1.44
        SU_TUKETIM_UCRETI_KADEME3 = 6.43
        ATIK_SU_UCRETI_KADEME3 = 3.22
        if 0 < sayac_farkı <= (13 * donem / 30):
            su_tuketim_ucreti = sayac_farkı * SU_TUKETIM_UCRETI_KADEME1
            atık_su_ucreti = sayac_farkı * ATIK_SU_UCRETI_KADEME1
        elif (13 * donem / 30) < sayac_farkı <= (20 * donem / 30):
            su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 + (sayac_farkı - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2
            atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 + (sayac_farkı - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2
        else:
            su_tuketim_ucreti = (13 * donem / 30) * SU_TUKETIM_UCRETI_KADEME1 + ((20 * donem / 30) - (13 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME2 + (sayac_farkı - (20 * donem / 30)) * SU_TUKETIM_UCRETI_KADEME3
            atık_su_ucreti = (13 * donem / 30) * ATIK_SU_UCRETI_KADEME1 + ((20 * donem / 30) - (13 * donem / 30)) * ATIK_SU_UCRETI_KADEME2 + (sayac_farkı - (20 * donem / 30)) * ATIK_SU_UCRETI_KADEME3
        iths_su_tuketim_ucreti = su_tuketim_ucreti
        iths_tipi_sadece_su_ücreti += iths_su_tuketim_ucreti*30/donem #aylık olarak çevirdik.
        iths_atık_su_ucreti = atık_su_ucreti
        if iths_su_tuketim_ucreti*30/donem > max_aylık_su_ucret:
            max_aylık_su_ucret = iths_su_tuketim_ucreti*30/donem
            max_aylık_su_ucreti_abone_no = abone_no
            max_aylık_su_ucretinin_su_tuketimi = sayac_farkı*30/donem
            max_aylık_su_ucretinin_tipi = "İlçe Tarımsal ve Hayvan Sulama"
        if iths_su_tuketim_ucreti*30/donem > 500 or sayac_farkı*30/donem > 100:
            arti_yuz_ton_abone_veya_arti_500_tl += 1
        iths_genel_toplam_su_ucreti = iths_atık_su_ucreti+iths_su_tuketim_ucreti
        KDV_ORANI = 0.08
        CTV_ORANI = 0.39
        ctv_ucreti = sayac_farkı * CTV_ORANI
        katı_atik_toplama_kdv = 13 * hane_sayısı * KDV_ORANI
        katı_atik_toplama_ucreti = hane_sayısı * 13 + katı_atik_toplama_kdv
        katı_atik_bertaraf_kdv = 2.54 * hane_sayısı * KDV_ORANI
        katı_atik_bertaraf_ucreti = 2.54 * hane_sayısı + katı_atik_bertaraf_kdv
        buyuksehir_belediyenin_toplam_payı += katı_atik_bertaraf_ucreti
        toplam_su_ucreti = su_tuketim_ucreti + atık_su_ucreti
        toplam_sudan_kdv_ucreti = (iths_genel_toplam_su_ucreti) * KDV_ORANI
        donem_toplam_fatura_tutari = iths_genel_toplam_su_ucreti + toplam_sudan_kdv_ucreti + ctv_ucreti + katı_atik_toplama_ucreti + katı_atik_bertaraf_ucreti
        devlete_gidecek_kdv_tutari = katı_atik_bertaraf_kdv + katı_atik_toplama_kdv + toplam_sudan_kdv_ucreti
        devletin_toplam_payı += devlete_gidecek_kdv_tutari
        ilceye_gidecek_tutar = ctv_ucreti + katı_atik_toplama_ucreti - (katı_atik_toplama_kdv)  # kdv devlete gideceği için çıkardık
        ilcenin_toplam_payı += ilceye_gidecek_tutar
        izsu_payi = donem_toplam_fatura_tutari - ctv_ucreti - katı_atik_toplama_ucreti - katı_atik_bertaraf_ucreti - (devlete_gidecek_kdv_tutari)  # ücret sonuçları kdv'li olduğu için ve kdvler devlete gittiği için çıkarmayı yaptık
        izsu_toplam_payı += izsu_payi
        print("Dönemlik su tüketim ücretini:", format(iths_su_tuketim_ucreti, ".2f"))
        print("Dönemlik atık su ücretiniz : ", format(atık_su_ucreti,".2f"))
        print("Dönemlik toplam su tüketim ve atık su ücretiniz : ", format(su_tuketim_ucreti + atık_su_ucreti,".2f"))
        print("Çevre Temizlik Vergisi : ", format(ctv_ucreti,".2f"))
        print("Katı Atık Toplama Ücreti : ", format(katı_atik_toplama_ucreti,".2f"))
        print("Katı Atık Berteraf Ücreti : ", format(katı_atik_bertaraf_ucreti,".2f"))
        print("Dönemlik toplam fatura bedeli : ", format(donem_toplam_fatura_tutari,".2f"))
        print("Devlete aktarılacak KDV ücreti toplamı : ", format(devlete_gidecek_kdv_tutari,".2f"))
        print("İlçe belediyesine aktarılacak tutar : ", format(ilceye_gidecek_tutar,".2f"))
        print("Büyükşehir belediyeye aktarılacak tutar : ", format(katı_atik_bertaraf_ucreti,".2f"))
        print("İzsuya gidecek pay : ", format(izsu_payi,".2f"))
    baska_abone = input("Başka abone var mı ?(e/E/h/H) : ")
    while baska_abone not in ["e","E","h","H"]:
        baska_abone = input("Başka abone var mı düzgün giriniz (e/E/h/H) : ")
if konut_abone_sayisi == 0:
    print("Konut tipi abone yoktur. ")
else:
    print("Konut tipi abone sayısı , yüzdesi ve aylık ortalama su tüketim miktarı : ",konut_tipi_toplam_hane_sayısı," %",format(konut_tipi_toplam_hane_sayısı*100/toplam_abone_sayisi,".2f"),format(konut_hane_basına_dusen_su_mıktarı,".2f")) # aylık olarak toplam suyu hesapladık yukarıda hepsinde.
if isyeri_abone_sayisi == 0:
    print("işyeri tipi abone yoktur .")
else:
    print("İşyeri tipi abone sayısı , yüzdesi ve aylık ortalama su tüketim miktarı : ", isyeri_abone_sayisi," %",format(isyeri_abone_sayisi * 100 / toplam_abone_sayisi,".2f"), format(isyeri_tipi_kullanılan_toplam_su,".2f"))
if resmi_daire_abone_sayisi == 0:
    print("Resmi daire abone tipi yoktur . ")
else:
    print("Resmi daire tipi abone sayısı , yüzdesi ve aylık ortalama su tüketim miktarı : ", resmi_daire_abone_sayisi," %",format(resmi_daire_abone_sayisi * 100 / toplam_abone_sayisi,".2f"), format(resmi_daire_tipi_kullanılan_toplam_su,".2f"))

if organize_sanayi_abone_sayisi == 0:
    print("Organize sanayi abone tipi yoktur . ")
else:
    print("Organize sanayi tipi abone sayısı , yüzdesi ve aylık ortalama su tüketim miktarı : ", organize_sanayi_abone_sayisi," % ",format(organize_sanayi_abone_sayisi * 100 / toplam_abone_sayisi,".2f"), format(organize_sanayi_tipi_kullanılan_toplam_su,".2f"))

if iths_abone_sayisi == 0:
    print("İlçe Tarımsal ve Hayvan Sulama abone tipi yoktur . ")
else:
    print("İlçe Tarımsal ve Hayvan Sulama abone tipi abone sayısı , yüzdesi ve aylık ortalama su tüketim miktarı : ", iths_abone_sayisi,format(iths_abone_sayisi * 100 / toplam_abone_sayisi,".2f"), format(iths_tipi_kullanılan_toplam_su,".2f"))

print("Konut abone tipinde 1. kademede olan hane sayısı , konut abone tipindeki haneler içindeki yüzdesi ve aylık oralama su tüketim miktarı : ",konut_birinci_kademede_hane_sayisi,format(konut_birinci_kademede_hane_sayisi/konut_tipi_toplam_hane_sayısı*100,".2f"),format(konut_birinci_kademede_su_harcama/konut_birinci_kademede_hane_sayisi,".2f"))
print("Konut abone tipinde 2. kademede olan hane sayısı , konut abone tipindeki haneler içindeki yüzdesi ve aylık oralama su tüketim miktarı : ",konut_ikinci_kademede_hane_sayisi,format(konut_ikinci_kademede_hane_sayisi/konut_tipi_toplam_hane_sayısı*100,".2f"),format(konut_ikinci_kademede_su_harcama/konut_ikinci_kademede_hane_sayisi,".2f"))
print("Konut abone tipinde 3. kademede olan hane sayısı , konut abone tipindeki haneler içindeki yüzdesi ve aylık oralama su tüketim miktarı : ",konut_ucuncu_kademede_hane_sayisi, format(konut_ucuncu_kademede_hane_sayisi / konut_tipi_toplam_hane_sayısı * 100,".2f"),format(konut_ucuncu_kademede_su_harcama/konut_ucuncu_kademede_hane_sayisi,".2f"))
print("Aylık su tüketim miktarı 50 tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı ve ilçe tarımsal ve hayvan sulama tipi aboneler içindeki yüzdesi : ",arti_elli_ton_iths,format(arti_elli_ton_iths*100/iths_abone_sayisi,".2f"))
print("Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı : ",arti_yuz_ton_abone_veya_arti_500_tl)
print("Şehit, gazi veya devlet sporcusu olan konut tipi abonelerin (hanelerin) sayısı ve konut tipi aboneler (haneler) içindeki yüzdesi : ",konuttaki_toplam_diger_oncelikli,format(konuttaki_toplam_diger_oncelikli*100/konut_tipi_toplam_hane_sayısı,".2f"))
print("Engelli olan konut tipi abonelerin (hanelerin) sayısı ve konut tipi aboneler (haneler) içindeki yüzdesi : ",konuttaki_toplam_engelli_oncelikli,format(konuttaki_toplam_engelli_oncelikli*100/konut_tipi_toplam_hane_sayısı,".2f"))
print("Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone no’su ve aylık su tüketim miktarı : ",max_resmi_daire_abone_no,format(max_resmi_daire,".2f"))
print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone no’su, abone tipi adı, aylık su tüketim miktarı ve ödediği aylık su tüketim ücreti : ",max_aylık_su_ucreti_abone_no,max_aylık_su_ucretinin_tipi,format(max_aylık_su_ucretinin_su_tuketimi,".2f"),format(max_aylık_su_ucret,".2f"))
print("Konut abone tipi aylık toplam su tüketim miktarı, Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(konut_tipi_kullanılan_toplam_su,".2f"),format(konut_tipi_kullanılan_toplam_su*100/bornova_aylık_su_tuketimi,".2f"))
print("İşyeri abone tipi aylık toplam su tüketim miktarı, Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(isyeri_tipi_kullanılan_toplam_su,".2f"), format(isyeri_tipi_kullanılan_toplam_su * 100 / bornova_aylık_su_tuketimi,".2f"))
print("Resmi daire abone tipi aylık toplam su tüketim miktarı, Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(resmi_daire_tipi_kullanılan_toplam_su,".2f"), format(resmi_daire_tipi_kullanılan_toplam_su * 100 / bornova_aylık_su_tuketimi,".2f"))
print("Organize sanayi abone tipi aylık toplam su tüketim miktarı, Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(organize_sanayi_tipi_kullanılan_toplam_su,".2f"), format(organize_sanayi_tipi_kullanılan_toplam_su * 100 / bornova_aylık_su_tuketimi,".2f"))
print("İlçe Tarımsal ve Hayvan Sulama abone tipi aylık toplam su tüketim miktarı, Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(iths_tipi_kullanılan_toplam_su,".2f"), format(iths_tipi_kullanılan_toplam_su * 100 / bornova_aylık_su_tuketimi,".2f"))
print("Bornova aylık su tüketim miktarı : ",format(bornova_aylık_su_tuketimi,".2f"))
print("Konut tipi abone aylık toplam su tüketim ücreti : ",format(konut_tipi_sadece_su_ucreti,".2f"))
print("İşyeri tipi abone aylık toplam su tüketim ücreti : ",format(isyeri_tipi_sadece_su_ucreti,".2f"))
print("Resmi daire tipi abone aylık toplam su tüketim ücreti : ", format(resmi_daire_tipi_sadece_su_ucreti,"2f"))
print("Organize sanayi tipi abone aylık toplam su tüketim ücreti : ", format(organize_sanayi_tipi_sadece_su_ucreti,".2f"))
print("İlçe Tarımsal ve Hayvan Sulama  tipi abone aylık toplam su tüketim ücreti : ", format(iths_tipi_sadece_su_ücreti,".2f"))
toplam_aylık_su_ucreti = konut_tipi_sadece_su_ucreti+isyeri_tipi_sadece_su_ucreti+resmi_daire_tipi_sadece_su_ucreti+organize_sanayi_tipi_sadece_su_ucreti+iths_tipi_sadece_su_ücreti
print("Tüm abonelerden elde edilen aylık toplam su tüketim ücreti : ",format(toplam_aylık_su_ucreti,".2f"))
print("İlgili dönemde su faturalarından İZSU’nun elde ettiği gelir tutarı : ",format(izsu_toplam_payı,".2f"))
print("İlgili dönemde su faturalarından İlçe belediye’nin elde ettiği gelir tutarı : ", format(ilcenin_toplam_payı,".2f"))
print("İlgili dönemde su faturalarından Büyükşehir Belediye'nin elde ettiği gelir tutarı : ", format(buyuksehir_belediyenin_toplam_payı,".2f"))
print("İlgili dönemde su faturalarından devletin elde ettiği gelir tutarı : ", format(devletin_toplam_payı,".2f"))