import os
import subprocess
import colorama
from colorama import Fore, Style

# Inisialisasi Colorama
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
# Definisikan warna LIGHT yang akan digunakan
warna_list = [
    Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
]

data_tabel = [
    ["0 Russia", "1 Ukraine", "2 Kazakhstan", "3 China"],
    ["4 Philippines", "5 Myanmar", "6 Indonesia", "7 Malaysia"],
    ["8 Kenya", "9 Tanzania", "10 Vietnam", "11 Kyrgyzstan"],
    ["12 Usa", "13 Israel", "14 Hongkong", "15 Poland"],
    ["16 England", "17 Madagascar", "18 Dcongo", "19 Nigeria"],
    ["20 Macao", "21 Egypt", "22 India", "23 Ireland"],
    ["24 Cambodia", "25 Laos", "26 Haiti", "27 Ivory"],
    ["28 Gambia", "29 Serbia", "30 Yemen", "31 Southafrica"],
    ["32 Romania", "33 Colombia", "34 Estonia", "35 Azerbaijan"],
    ["36 Canada", "37 Morocco", "38 Ghana", "39 Argentina"],
    ["40 Uzbekistan", "41 Cameroon", "42 Chad", "43 Germany"],
    ["44 Lithuania", "45 Croatia", "46 Sweden", "47 Iraq"],
    ["48 Netherlands", "49 Latvia", "50 Austria", "51 Belarus"],
    ["52 Thailand", "53 Saudiarabia", "54 Mexico", "55 Taiwan"],
    ["56 Spain", "57 Iran", "58 Algeria", "59 Slovenia"],
    ["60 Bangladesh", "61 Senegal", "62 Turkey", "63 Czech"],
    ["64 Srilanka", "65 Peru", "66 Pakistan", "67 Newzealand"],
    ["68 Guinea", "69 Mali", "70 Venezuela", "71 Ethiopia"],
    ["72 Mongolia", "73 Brazil", "74 Afghanistan", "75 Uganda"],
    ["76 Angola", "77 Cyprus", "78 France", "79 Papua"],
    ["80 Mozambique", "81 Nepal", "82 Belgium", "83 Bulgaria"],
    ["84 Hungary", "85 Moldova", "86 Italy", "87 Paraguay"],
    ["88 Honduras", "89 Tunisia", "90 Nicaragua", "91 Timorleste"],
    ["92 Bolivia", "93 Costarica", "94 Guatemala", "95 Uae"],
    ["96 Zimbabwe", "97 Puertorico", "98 Sudan", "99 Togo"],
    ["100 Kuwait", "101 Salvador", "102 Libyan", "103 Jamaica"],
    ["104 Trinidad", "105 Ecuador", "106 Swaziland", "107 Oman"],
    ["108 Bosnia", "109 Dominican", "110 Syrian", "111 Qatar"],
    ["112 Panama", "113 Cuba", "114 Mauritania", "115 Sierraleone"],
    ["116 Jordan", "117 Portugal", "118 Barbados", "119 Burundi"],
    ["120 Benin", "121 Brunei", "122 Bahamas", "123 Botswana"],
    ["124 Belize", "125 Caf", "126 Dominica", "127 Grenada"],
    ["128 Georgia", "129 Greece", "130 Guineabissau", "131 Guyana"],
    ["132 Iceland", "133 Comoros", "134 Saintkitts", "135 Liberia"],
    ["136 Lesotho", "137 Malawi", "138 Namibia", "139 Niger"],
    ["140 Rwanda", "141 Slovakia", "142 Suriname", "143 Tajikistan"],
    ["144 Monaco", "145 Bahrain", "146 Reunion", "147 Zambia"],
    ["148 Armenia", "149 Somalia", "150 Congo", "151 Chile"],
    ["152 Burkinafaso", "153 Lebanon", "154 Gabon", "155 Albania"],
    ["156 Uruguay", "157 Mauritius", "158 Bhutan", "159 Maldives"],
    ["160 Guadeloupe", "161 Turkmenistan", "162 Frenchguiana", "163 Finland"],
    ["164 Saintlucia", "165 Luxembourg", "166 Saintvincentgrenadines", "167 Equatorialguinea"],
    ["168 Djibouti", "169 Antiguabarbuda", "170 Caymanislands", "171 Montenegro"],
    ["172 Denmark", "173 Switzerland", "174 Norway", "175 Australia"],
    ["176 Eritrea", "177 Southsudan", "178 Saotomeandprincipe", "179 Aruba"],
    ["180 Montserrat", "181 Anguilla", "182 Northmacedonia", "183 Seychelles"],
    ["184 Newcaledonia", "185 Capeverde", "186 Usaphysical", "187 Fiji"],
    ["188 Singapore", "189 Gibraltar"]
]

# Print header
print(f"""\n {merah}{'Negara 1':<25} {hijau}{'Negara 2':<25} {kuning}{'Negara 3':<25} {biru}{'Negara 4':<25}
          """
     ) 
# Print data rows
# Print data rows dengan warna berbeda
for row in data_tabel:
    for i in range(len(row)):
        # Pilih warna dari daftar warna LIGHT secara berulang
        warna = warna_list[i % len(warna_list)]
        print(f"{warna}{row[i]:<25}", end=" ")
    print()  # Baris baru setelah setiap baris data

def buka_file_main():
    file_path = 'main.py'  # Ganti dengan path file main.py jika perlu
    if os.path.exists(file_path):
        # Bersihkan layar sebelum menjalankan perintah
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        
        # Jalankan file main.py
        subprocess.run(f'python {file_path}', shell=True)
    else:
        print(f"File {file_path} tidak ditemukan")

if __name__ == '__main__':
    print(Fore.LIGHTCYAN_EX+"\nGANTI NEGARA DI LINE 24 country_code =")
    print(Fore.LIGHTMAGENTA_EX+"GANTI MAPPING DI LINE 108 country_mapping =")
    print("Tekan Enter untuk kembali ke Menu")
    input()  # Menunggu sampai Enter ditekan
    buka_file_main()
