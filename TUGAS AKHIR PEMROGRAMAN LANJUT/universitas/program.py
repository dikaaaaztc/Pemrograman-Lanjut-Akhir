class Program:
    def __init__(self, id_program, nama_program):
        self.id_program = id_program
        self.nama_program = nama_program

    def info_program(self):
        return f"{self.nama_program} (ID: {self.id_program})"

class ProgramS1(Program):
    def __init__(self, id_program, nama_program, durasi):
        super().__init__(id_program, nama_program)
        self.durasi = durasi

    def info_program(self):
        info_dasar = super().info_program()
        return f"{info_dasar}, Durasi: {self.durasi} tahun"

class ProgramS2(Program):
    def __init__(self, id_program, nama_program, durasi, bidang_riset):
        super().__init__(id_program, nama_program)
        self.durasi = durasi
        self.bidang_riset = bidang_riset

    def info_program(self):
        info_dasar = super().info_program()
        return f"{info_dasar}, Durasi: {self.durasi} tahun, Bidang Riset: {self.bidang_riset}"
