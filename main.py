import os
import requests
from datetime import datetime
import subprocess
import colorama
from colorama import Fore, Style

# Inisialisasi colorama untuk reset otomatis
colorama.init(autoreset=True)

# Warna untuk output
hitam = Fore.LIGHTBLACK_EX
hijau = Fore.LIGHTGREEN_EX
putih = Fore.LIGHTWHITE_EX
kuning = Fore.LIGHTYELLOW_EX
biru = Fore.LIGHTBLUE_EX
merah = Fore.LIGHTRED_EX
reset = Style.RESET_ALL
ungu = Fore.LIGHTMAGENTA_EX
muda = Fore.LIGHTCYAN_EX
line = putih + "~" * 50

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_console()

def print_welcome_message():
    print(
    f"""
{putih}╔══════════════════════════════════════════════════════════════╗
{putih}║                                                              ║
{putih}║   ██████╗  ██████╗ ███╗   ██╗███████╗    ██╗                 ║
{putih}║   ██╔══██╗██╔═══██╗████╗  ██║██╔════╝   ██╔╝                 ║
{putih}║   ██║  ██║██║   ██║██╔██╗ ██║███████╗  ██╔╝                  ║
{putih}║   ██║  ██║██║   ██║██║╚██╗██║╚════██║ ██╔╝                   ║
{putih}║   ██████╔╝╚██████╔╝██║ ╚████║███████║██╔╝██╗                 ║
{putih}║   ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝ ╚═╝                 ║
{putih}║                                                              ║
{putih}║   ███████╗███╗   ███╗███████╗██╗  ██╗██╗   ██╗██████╗        ║
{putih}║   ██╔════╝████╗ ████║██╔════╝██║  ██║██║   ██║██╔══██╗       ║
{putih}║   ███████╗██╔████╔██║███████╗███████║██║   ██║██████╔╝       ║
{putih}║   ╚════██║██║╚██╔╝██║╚════██║██╔══██║██║   ██║██╔══██╗       ║
{putih}║   ███████║██║ ╚═╝ ██║███████║██║  ██║╚██████╔╝██████╔╝       ║
{putih}║   ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝        ║
{putih}║                                                              ║
{putih}╚══════════════════════════════════════════════════════════════╝
          """
    )

# Panggil fungsi untuk menampilkan welcome message
print_welcome_message()

    
def input_nama_dan_api_key():
    nama = input("Masukkan Nama Anda: ")
    api_key = input("Masukkan API Key Anda: ")

    with open("nama.txt", "w") as nama_file:
        nama_file.write(nama)

    with open("key.txt", "w") as key_file:
        key_file.write(api_key)

def get_ip_address():
    # Ganti dengan logika untuk mendapatkan alamat IP pengguna
    return "192.168.0.1"

def get_sms_hub_info(api_key):
    url = f"https://smshub.org/stubs/handler_api.php?api_key={api_key}&action=getBalance"
    response = requests.get(url)
    if response.status_code == 200:
        info = response.text
        info = info.replace("ACCESS_BALANCE:", "")  # Menghapus "ACCESS_BALANCE:"
        return info
    else:
        return "Gagal mendapatkan informasi SMSHub."
    
def buka_file_otp_smshub_py():
    try:
        subprocess.run(["python", "telegram.py"])
    except Exception as e:
        print(f"Error: {e}")

def buka_file_list_country_py():
    try:
        subprocess.run(["python", "countrylist.py"])
    except Exception as e:
        print(f"Error: {e}")

def tampilkan_dashboard():
    with open("nama.txt", "r") as nama_file:
        nama = nama_file.read()

    api_key = ""
    with open("key.txt", "r") as key_file:
        api_key = key_file.read()

    ip_address = get_ip_address()
    tanggal_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sms_hub_info = get_sms_hub_info(api_key)

    grey = "\033[1;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[1;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    white = "\033[0;37m"

    print(f"Selamat datang, {yellow}{nama}!{white}")
    print(f"IP Address   : {ip_address}")
    print(f"Tanggal      : {tanggal_sekarang}")
    print(f"{yellow}SMSHub Balance {sms_hub_info} Rub{white}")

    print("\nMenu:")
    print("1. Get OTP SMSHub")
    print("2. Get List Country")
    print("3. Keluar")

    while True:
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            buka_file_otp_smshub_py()
            pass
        elif pilihan == "2":
            buka_file_list_country_py()
            pass
        elif pilihan == "3":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

if __name__ == "__main__":
    if not os.path.exists("nama.txt") or not os.path.exists("key.txt"):
        input_nama_dan_api_key()

    tampilkan_dashboard()
