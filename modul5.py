from tkinter import *
from tkinter import messagebox as mb

datUser = 'admin'
datPassword = '12345'

class DemoLogin:
    def __init__(self, induk, judul):
        self.induk = induk

        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.induk.resizable(False, False)

        self.aturKomponen()

        self.entUser.focus_set()

    def aturKomponen(self):
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)

        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)

        Label(frData, text='Nama Pengguna:').grid(row=0, column=0, sticky=W)
        self.entUser = Entry(frData)
        self.entUser.grid(row=0, column=1)

        Label(frData, text='Password:').grid(row=1, column=0, sticky=W)
        self.entPass = Entry(frData, show='*')
        self.entPass.grid(row=1, column=1)

        self.cek = IntVar()

        self.cbShowPass = Checkbutton(frData, text='tampilkan password',
            variable=self.cek, command=self.lihatPassword)
        self.cbShowPass.grid(row=2, column=1, sticky=E)

        frTombol = Frame(frameUtama, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        self.btnLogin = Button(frTombol, text='Login', command=self.prosesLogin)
        self.btnLogin.pack(side=LEFT, fill=BOTH, expand=YES)

        self.btnBatal = Button(frTombol, text='Batal', command=self.Tutup)
        self.btnBatal.pack(side=LEFT, fill=BOTH, expand=YES)

    def prosesLogin(self, event=None):
        nmUser = self.entUser.get()
        passUser = self.entPass.get()

        if nmUser=='':
            mb.showwarning('Pesan Salah', 'Nama user tidak boleh kosong!',
parent=self.induk)
            self.entUser.focus_set()
        elif passUser=='':
            mb.showwarning('Pesan Salah', 'Password tidak boleh kosong!',
parent=self.induk)
            self.entPass.focus_set()
        elif (nmUser==datUser) and (passUser==datPassword):
            class ProgramPembayaran:
                def __init__(self, parent, title):
                    self.parent = parent

                    self.parent.title(title)
                    self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
                    self.aturKomponen()

                def aturKomponen(self):
                    mainFrame = Frame(self.parent, bd=10)
                    mainFrame.pack(fill=BOTH, expand=YES)

                    Label(mainFrame, text='Total Pembelian').grid(row=0, column=0,
                        sticky=W, padx=5, pady=5)
                    self.entPembelian = Entry(mainFrame)
                    self.entPembelian.grid(row=0, column=1, padx=5, pady=5)
                    self.btnHitung = Button(mainFrame, text='Hitung',
                        command=self.onHitung)
                    self.btnHitung.grid(row=0, column=2, padx=5, pady=5)

                    Label(mainFrame, text='Pajak (10%)').grid(row=1, column=0,
                        sticky=W, padx=5, pady=5)
                    self.entPajak = Entry(mainFrame)
                    self.entPajak.grid(row=1, column=1, padx=5, pady=5)

                    Label(mainFrame, text='Total Pembayaran').grid(row=2, column=0,
                        sticky=W, padx=5, pady=5)
                    self.entPembayaran = Entry(mainFrame)
                    self.entPembayaran.grid(row=2, column=1, padx=5, pady=5)

                def onHitung(self, event=None):
                    totalPembelian = int(self.entPembelian.get())
                    pajak = 0.1 * totalPembelian
                    totalPembayaran = 1.1 * totalPembelian

                    self.entPajak.delete(0, END)
                    self.entPembayaran.delete(0, END)

                    self.entPajak.insert(END, str(pajak))
                    self.entPembayaran.insert(END, str(totalPembayaran))

                def onKeluar(self, event=None):
                    self.parent.destroy()
            if __name__ == '__main__':
                root = Tk()

                aplikasi = ProgramPembayaran(root, "Program Pembayaran")

                root.mainloop()
        else:
            mb.showwarning('Pesan Salah', 'Nama Pengguna / Password Anda Salah',
parent=self.induk)
            self.Hapus()

    def lihatPassword(self, event=None):
        nilaiCek =  self.cek.get()

        if nilaiCek== 1:
            self.entPass['show'] = ''
        else:
            self.entPass['show'] = '*'

    def Tutup(self, event=None):
        self.induk.destroy()

    def Hapus(self, event=None):
        self.entUser.delete(0, END)
        self.entPass.delete(0, END)
        self.entUser.focus_set()

if __name__ == '__main__':
    root = Tk()

    app = DemoLogin(root, ":: Demo Login Password ::")

    root.mainloop()