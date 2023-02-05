from tkinter import *

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
        