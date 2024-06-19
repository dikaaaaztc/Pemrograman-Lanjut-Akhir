from universitas.mahasiswa import Mahasiswa, MahasiswaS2
from universitas.program import ProgramS1, ProgramS2

def buat_program():
    tipe_program = input("Masukkan tipe program (S1/S2): ").strip().upper()
    id_program = int(input("Masukkan ID program: ").strip())
    nama_program = input("Masukkan nama program: ").strip()
    durasi = int(input("Masukkan durasi program (tahun): ").strip())
    
    if tipe_program == "S1":
        return ProgramS1(id_program, nama_program, durasi)
    elif tipe_program == "S2":
        bidang_riset = input("Masukkan bidang riset: ").strip()
        return ProgramS2(id_program, nama_program, durasi, bidang_riset)
    else:
        print("Tipe program tidak valid.")
        return None

def buat_mahasiswa(program):
    nama = input("Masukkan nama mahasiswa: ").strip()
    umur = int(input("Masukkan umur mahasiswa: ").strip())
    tingkat_pendidikan = input("Masukkan tingkat pendidikan (S1/S2): ").strip().upper()

    if tingkat_pendidikan == "S1":
        return Mahasiswa(nama, umur, program)
    elif tingkat_pendidikan == "S2":
        judul_tesis = input("Masukkan judul tesis: ").strip()
        return MahasiswaS2(nama, umur, program, judul_tesis)
    else:
        print("Tingkat pendidikan tidak valid.")
        return None

def main():
    program = None
    while not program:
        program = buat_program()

    mahasiswa = None
    while not mahasiswa:
        mahasiswa = buat_mahasiswa(program)

    print(mahasiswa.info())
    kursus = input("Masukkan nama kursus yang ingin didaftarkan: ").strip()
    mahasiswa.daftar_kursus(kursus)

if __name__ == "__main__":
    main()
