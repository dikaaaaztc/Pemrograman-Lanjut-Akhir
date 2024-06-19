from abc import ABC, abstractmethod

class Orang(ABC):
    @abstractmethod
    def info(self):
        pass

class Mahasiswa(Orang):
    def __init__(self, nama, umur, program):
        self.nama = nama
        self.umur = umur
        self.program = program

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Program: {self.program.info_program()}"

    def daftar_kursus(self, kursus):
        print(f"{self.nama} telah mendaftar di kursus {kursus}.")

class MahasiswaS2(Mahasiswa):
    def __init__(self, nama, umur, program, judul_tesis):
        super().__init__(nama, umur, program)
        self.judul_tesis = judul_tesis

    def info(self):
        info_dasar = super().info()
        return f"{info_dasar}, Judul Tesis: {self.judul_tesis}"
