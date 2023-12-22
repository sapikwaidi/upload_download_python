import sys
from ftplib import FTP

class Utama():
    def __init__(self):
        alamat = input("Masukan alamat: ")
        login = input("Masukan login: ")
        pwd = input("Masukan password: ")
        
        self.ftp = FTP(alamat)
        self.ftp.login(user=login, passwd = pwd)
        self.daftarfiles = []
        self.tampilMenu()
        
    
    def tampilMenu(self):
        print("Pilih menu: ")
        print("1) Daftar file dan direktory")
        print("2) Download file")
        print("3) Upload file")
        print("4) keluar")
        
        pilih = input("Anda memilih: ")
        if pilih == "1":
            self.isiDirektory()
        elif pilih == "2":
            nf = input("Nama file yang akan didownload: ")
            self.downloadFiles(nf)
        elif pilih == "3":
            nf = input("Nama file yang akan di upload: ")
            self.uploadFile(nf)
        else:
            self.ftp.quit()    
            
    def isiDirektory(self):
        self.ftp.dir(self.daftarfiles.append)
        for df in self.daftarfiles:
            print(df)
            
        self.daftarfiles = []
        self.tampilMenu()
        
    def downloadFiles(self, nf):
        
        with open(nf, "w", encoding="utf-8") as local_file:
            
            resp = self.ftp.retrlines("RETR "+nf, local_file.write)
            input("stop")
            if resp.startswith("226"):
                print("Download selesai")
            else:
                print("Download error")
        self.tampilMenu()
        
    def uploadFiles(self, nf):
        with open(nf, "rd") as local_file:
            self.ftp.storlines("STOR "+nf, local_file)
        self.tampilMenu()
        
if __name__ == "__main__":
    Utama()
    sys.exit()