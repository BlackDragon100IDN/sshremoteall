1️⃣ DESKRIPSI
SSH REMOTE adalah tool berbasis Python (CLI) untuk:
•	Scan IP address dalam jaringan aktif
•	Deteksi host yang membuka port SSH (22)
•	Menampilkan daftar IP + info SSH banner
•	Memilih host dari list
•	Login SSH manual
•	Otomatis masuk mode root (sudo)
•	Menggunakan terminal interaktif
Tool ini khusus kompatibel dengan Windows.
________________________________________
2️⃣ PERSYARATAN SISTEM
💻 Sistem Operasi
•	Windows 10 / 11
•	CMD atau PowerShell
🌐 Jaringan
•	Terhubung ke LAN / WiFi
•	Target device berada di subnet yang sama
•	SSH aktif di target (port 22 terbuka)
🔐 Target Device
•	Linux server / router / mini PC
•	User memiliki akses sudo
________________________________________
3️⃣ INSTALL PYTHON (DARI NOL)
🔹 Langkah 1 — Download Python
1.	Buka browser
2.	Kunjungi:
👉 https://www.python.org/downloads/
3.	Download Python 3.10+ (64-bit)
________________________________________
🔹 Langkah 2 — Install Python
1.	Jalankan installer
2.	WAJIB centang:
3.	☑ Add Python to PATH
4.	Klik Install Now
5.	Tunggu sampai selesai
________________________________________
🔹 Langkah 3 — Cek Instalasi
Buka CMD, lalu ketik:
python --version
Jika muncul:
Python 3.x.x
✅ Python berhasil terinstall
________________________________________
4️⃣ BUAT FOLDER PROJECT
Contoh:
C:
mkdir ssh
cd ssh
________________________________________
5️⃣ INSTALL DEPENDENCY PYTHON
Jalankan perintah ini:
pip install paramiko colorama netifaces
📦 Fungsi Library
Library	Fungsi
paramiko	SSH client
netifaces	Deteksi network aktif
colorama	Warna CLI
socket	Scan port
threading	Scan cepat
________________________________________
6️⃣ BUAT FILE SCRIPT
1.	Di folder C:\ssh
2.	Buat file:
scan_ssh_remote.py
3.	Copy FULL CODE SSH REMOTE (versi terakhir)
4.	Simpan
________________________________________
7️⃣ STRUKTUR FILE
C:\ssh
 ├─ scan_ssh_remote.py
________________________________________
8️⃣ MENJALANKAN SCRIPT
▶️ Jalankan dari CMD
cd C:\ssh
python scan_ssh_remote.py
________________________________________
9️⃣ ALUR KERJA SCRIPT
🔹 1. Tampilan Awal
SSH REMOTE TOOL
Author: Strom81
________________________________________
🔹 2. Scan Jaringan
•	Otomatis mendeteksi subnet:
192.168.2.0/24
•	Scan semua IP
•	Deteksi port 22
________________________________________
🔹 3. Daftar Host
NO  IP ADDRESS        SSH INFO
1   192.168.2.1       Dropbear_2020.81
2   192.168.2.20      OpenSSH_8.2p1 Ubuntu
________________________________________
🔹 4. Pilih Host
Pilih nomor host: 2
________________________________________
🔹 5. Login SSH
Username : user
Password : ****
________________________________________
🔹 6. Auto Root
Script otomatis menjalankan:
sudo -i
________________________________________
🔹 7. Terminal Aktif
Langsung masuk:
root@192.168.2.20#
Gunakan seperti SSH normal:
ls
cd /etc
systemctl status ssh
________________________________________
🔹 8. Keluar
Ketik:
exit
________________________________________
🔟 TROUBLESHOOTING
❌ Python tidak dikenali
Solusi:
•	Reinstall Python
•	Pastikan Add Python to PATH dicentang
________________________________________
❌ SSH tidak terdeteksi
Penyebab:
•	SSH belum aktif di target
•	Firewall blok port 22
•	IP beda subnet
________________________________________
❌ Authentication failed
Penyebab:
•	Username/password salah
•	User tidak punya akses SSH
________________________________________
❌ Tidak jadi root
Penyebab:
•	User bukan sudoer
•	sudo password berbeda
•	sudo butuh TTY
Solusi:
•	Login sebagai root langsung
•	Atau modifikasi script ke su -
________________________________________
1️⃣1️⃣ KEAMANAN
⚠️ Gunakan hanya untuk jaringan milik sendiri
⚠️ Jangan scan jaringan tanpa izin
⚠️ Password diketik manual (tidak disimpan)
________________________________________
1️⃣2️⃣ PENGEMBANGAN LANJUT
Fitur yang bisa ditambahkan:
•	SSH key login
•	Label device otomatis
•	Simpan host favorit
•	UI panah ↑ ↓
•	Multi subnet scan
________________________________________
1️⃣3️⃣ PENUTUP
Tool ini dibuat untuk:
•	Admin jaringan
•	IoT & server monitoring
•	Remote device cepat
•	Debug device Linux

![Uploading image.png…]()
