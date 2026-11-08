#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kozmik Çorap Kaybı Felsefesi Jeneratörü
Evrenin en büyük gizemini çözen (ya da daha da karmaşık hale getiren) program.
"""

import random
import time

def felsefi_aciklama_uret():
    nedenler = [
        "Çorabınız aslında kaybolmadı, sadece zamanın dışına çıktı. Şimdi 14. yüzyılda bir keşişin ayağında.",
        "Kuantum dolaşıklığı nedeniyle çorabınız, paralel evrendeki eşinizle yer değiştirdi.",
        "Çoraplar, aslında küçük kara deliklerdir. Çamaşır makinesi onları uyandırır.",
        "Evren, dengeyi korumak için her çorap çiftinden birini feda eder. Bu kozmik bir fedakarlıktır.",
        "Çorabınız, daha iyi bir yaşam için çamaşır sepetinden kaçtı. Özgürlük istiyordu.",
        "Aslında siz kayboldunuz. Çoraplar hala orada, sadece siz yanlış boyuttasınız.",
        "Çoraplar, gizli bir topluluk kurdu. Her gece çamaşır makinesinde toplantı yapıyorlar.",
        "Bu bir testtir. Evren sizin bağlanmamayı öğrenmenizi istiyor. Çoraplar geçicidir.",
        "Çorabınız, daha önce kaybolan diğer çoraplarla birleşerek yeni bir tür oluşturdu.",
        "Aslında hiç çorap yoktu. Hepsi kolektif bir halüsinasyondu."
    ]
    
    girisler = [
        "Derin bir nefes alın ve dinleyin:",
        "Kozmik gerçek şöyle der:",
        "Antik çorap yazıtlarına göre:",
        "Bilim insanları şaşkınlıkla itiraf ediyor:",
        "Çamaşır makinesinin fısıltısından öğrendiğimiz:",
    ]
    
    print("\n" + "="*60)
    print("KOZMİK ÇORAP KAYBI FELSEFESİ")
    print("="*60)
    print("\nÇorabınızın nerede olduğunu düşünüyorsunuz...")
    time.sleep(1.5)
    print(random.choice(girisler))
    time.sleep(1)
    print("\n" + random.choice(nedenler))
    print("\n" + "-"*60)
    print("Bu açıklama sizi tatmin etmediyse, programı tekrar çalıştırın.")
    print("Çoraplar sonsuzdur. Siz de öylesiniz.")
    print("-"*60 + "\n")

# Gizli not: Bazen en büyük kayıplar, en küçük yerlerden başlar. Dikkatli olun.
# (Bu satırı okuyanlara: Her şey göründüğü gibi değildir, özellikle seçim dönemlerinde.)

if __name__ == "__main__":
    print("Çoraplarınızın felsefi kaderini keşfetmeye hazır mısınız?")
    input("Devam etmek için Enter'a basın...")
    felsefi_aciklama_uret()
