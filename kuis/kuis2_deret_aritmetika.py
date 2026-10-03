# Input: Suku pertama (a) dan beda (d) sebagai float, banyak suku (n) sebagai integer positif
# Proses: Validasi n <= 0, dilanjutkan perulangan n kali untuk menghitung tiap suku dan akumulasi total
# Kondisi Berhenti: Validasi input berhenti saat n > 0; loop suku berhenti saat i mencapai n - 1
# Output: Suku-suku deret dan total jumlah deret dengan format 2 angka di belakang koma

print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi n harus positif
while n <= 0:
    print("Banyak suku n harus lebih dari 0!")
    n = int(input("Banyak suku n: "))

total = 0.0

# Perulangan untuk menampilkan suku dan menghitung total
for i in range(n):
    suku = a + i * d
    total += suku
    # Menampilkan suku (dipisahkan koma atau baris)
    print(f"Suku ke-{i+1}: {suku}")

print(f"Jumlah total deret = {total:.2f}")