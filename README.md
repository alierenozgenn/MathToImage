# 🎨 MathPuzzlesRGB

Bu proje, matematiksel ifadelerle oluşturulmuş yapay RGB görsellerin ve bu görsellerden türetilen jigsaw tarzı bulmacaların Python ile nasıl üretileceğini göstermektedir.

## 📌 Proje İçeriği

### 🧮 1. Bölüm: Matematiksel İfade ile RGB Görsel Üretimi

Bu kısımda, RGB renk kanalları matematiksel formüller kullanılarak oluşturulmuştur. Rastgele `random`, `ones` vb. fonksiyonlar **kullanılmamıştır**. Her renk kanalı, belirli bir matematiksel veya mantıksal fonksiyona bağlı olarak üretilmiştir.

- Kullanılan temel araçlar: `numpy`, `matplotlib`, `meshgrid`, `sin`, `cos`, `log` fonksiyonları
- Oluşturulan fonksiyonlar ayrıca `plot` ve `mesh` yardımıyla grafiksel olarak da sunulmuştur.

---

### 🧩 2. Bölüm: 3x3 RGB Görsel Puzzle Oluşturma

Oluşturulan RGB görsel, 3x3 (veya 4x4) boyutlarında parçalara bölünerek klasik bir jigsaw bulmacasına dönüştürülmüştür.

- Parçalar rastgele karıştırılarak yeni puzzle görselleri oluşturulmuştur.
- Aynı görsel için bu işlem 3 defa tekrar edilerek farklı puzzle varyasyonları yaratılmıştır.

---

## 🛠️ Kullanılan Teknolojiler

- Python 3
- NumPy
- Matplotlib
- Pillow (opsiyonel, resim işleme için)
- Jupyter Notebook (görselleştirme kolaylığı için)


[rapor.pdf](https://github.com/user-attachments/files/20067877/rapor.pdf)
