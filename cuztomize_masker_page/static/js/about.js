function getSelectValue()
        {
            var selectedValue = document.getElementById("model").value;
            document.getElementById("image").src = "/static/images/"+selectedValue+".jpeg";
            if (selectedValue == "SURGICAL"){
                document.getElementById("description").innerHTML = "Masker bedah atau bisa disebut sebagai masker medis yang biasanya berwarna hijau atau biru. Masker jenis ini mampu menahan droplet sekitar 80-90 persen. Masker ini hanya bisa digunakan satu kali pakai dalam waktu 4 jam pemakaian. Masker ini terutama wajib digunakan oleh pasien sakit dan petugas kesehatan yang tidak menangani pasien COVID-19 secara langsung. Petugas yang menangani pasien COVID-19 secara langsung wajib mengenakan masker N-95 dan APD level 3";
                
            } else if (selectedValue == "SPONGE"){
                document.getElementById("description").innerHTML = "Familiar dengan masker dengan tipe seperti ini? Kalau kamu suka dengan K-pop Idol, ini adalah masker yang sering dipakai oleh mereka, biasanya untuk menyamar. Nggak sedikit orang yang menjual masker berbahan spons seperti ini di tengah adanya wabah korona ini. Tapi tahu nggak, masker ini nggak didesain untuk menangkal virus, tapi untuk fashion! Masker ini nggak mampu melindungi diri kita dari virus maupun debu. Hanya mampu menahan bakteri maupun pollen sebanyak 5%.";
                
            } else if (selectedValue == "PITTA"){
                document.getElementById("description").innerHTML = "Masker Pitta Mask, yang sering dikenal sebagai 'masker K-Pop' karena masker ini banyak digunakan oleh para selebriti dari Korea Selatan. Masker ini terbuat dari bahan nano fiber elastis sehingga produk ini mampu melekat sesuai dengan bentuk wajah. Masker ini terdiri dari 1 lapisan yang bisa menahan serbuk sari dan debu. Berbeda dari masker medis, masker ini bisa digunakan kembali dengan mencucinya jika ingin dipakai lagi. Berikut review maskernya.";
                
            } else if (selectedValue == "CLOTH"){
                document.getElementById("description").innerHTML = "Sering melihat masker-masker beredar yang berbahan kain? Produk ini sebetulnya didesain untuk membuat kita tetap hangat, bukan untuk menahan virus. Mirip dengan Sponge Mask, masker ini nggak mampu menahan virus dan debu. Tapi, mampu menahan bakteri maupun pollen sebanyak 50%. Masker ini sebetulnya masih boleh digunakan oleh kamu yang sehat tapi ada urusan di luar rumah. Tapi, jangan lupa untuk mencuci masker setiap kali setelah pemakaian, dan perhatikan cara melepasnya supaya bagian luar masker nggak terkena wajah kamu.";

            }
        }