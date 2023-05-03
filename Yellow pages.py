MasterList = [[1001,"Cuadrado","Jalan Juara Nomor 15","8374930",14412,"Turin"],
              [1002,"Dybala","Jl. Jalan No 21","847394067",71197,"Roma"],
              [1003,"Arteta","Jalan Emirates No 1","087647584927",48593,"London"],
              [1004,"Benzema","Jl. Bernabeu No 34","081441273846",39483,"Madrid"],
              [1005,"Ederson","Jl. Tengah No 31","0837389392",27117,"Manchester"]]

def menuUtama():
    while True :
        print('===================================================')
        print('List Menu : ')
        print('1. Menampilkan Data')
        print('2. Menambah Data')
        print('3. Menghapus Data')
        print('4. Update Data')
        print('5. Exit Program')
        print('===================================================')
        try:
            pilihanMenu = int(input('Masukkan menu yang diinginkan : '))

            if pilihanMenu == 1 :
                tampilData()
                apaSort()

            elif pilihanMenu == 2 :
                tambahData()

            elif pilihanMenu == 3 :
                hapusData()

            elif pilihanMenu == 4 :
                updateData()
            
            elif pilihanMenu == 5 :
                break

            else : 
                print("Input yang anda masukkan invalid")

        except:
            print("Input yang anda masukkan invalid")
    return pilihanMenu

def tampilData():
    print('===============================================================================================================')
    print('ID\tNama\t\tAlamat\t\t\t\t\tNo. Telepon\tKode Pos\tDomisili')
    for i in range (len(MasterList)):
        print (MasterList[i][0],end='\t')

        if len(MasterList[i][1]) <= 7 :
            print (MasterList[i][1],end='\t\t')
        else :
            print(MasterList[i][1],end='\t')

        if len(MasterList[i][2]) <= 15 :
            print (MasterList[i][2],end='\t\t\t\t')

        elif len(MasterList[i][2]) > 15 and len(MasterList[i][2]) <= 20:
            print (MasterList[i][2],end='\t\t\t')

        else :
            print(MasterList[i][2],end='\t\t')

        if len(MasterList[i][3]) <= 7 :
            print(MasterList[i][3],end='\t\t')
        else :
            print(MasterList[i][3],end='\t')

        print(MasterList[i][4],end='\t\t')
        print(MasterList[i][5])
    print('===============================================================================================================')
    return tampilData

def apaSort():
    apakahSort = str(input('Apakah anda ingin melakukan sort pada data ? (y/n) '))
    if apakahSort == 'y' or apakahSort == 'Y' :
        sortData()
    elif apakahSort == 'n' or apakahSort == 'N':
        pass
    else :
        print("Input yang anda masukkan invalid")
    
def sortData():
        
    while True : 
        # try : 
        #     apakahSort = str(input('Apakah anda ingin melihat data yang sudah di sort ? (y/n) '))
        #     if apakahSort == 'y' or apakahSort == 'Y' :
        print ("1.Sort Data Berdasarkan Nama")
        print ("2.Sort Data Berdasarkan Kota Domisili")
        print ("3.Back to Main Menu")
        while True : 
            try : 
                pilihanSort = int(input('Masukkan nomor yang anda inginkan : '))
                
                if pilihanSort == 1 :

                    sortedName = sorted(MasterList,key=lambda l:l[1])
                    print('=========================================================================================================')
                    print('ID\tNama\t\tAlamat\t\t\t\t\tNo. Telepon\tKode Pos\tDomisili')
                    for i in range (len(sortedName)):
                        print (sortedName[i][0],end='\t')

                        if len(sortedName[i][1]) < 7 :
                            print (sortedName[i][1],end='\t\t')
                        else :
                            print(sortedName[i][1],end='\t')

                        if len(sortedName[i][2]) <= 15 :
                            print (sortedName[i][2],end='\t\t\t\t')

                        elif len(sortedName[i][2]) > 15 and len(sortedName[i][2]) <= 20:
                            print (sortedName[i][2],end='\t\t\t')

                        else :
                            print(sortedName[i][2],end='\t\t')

                        if len(sortedName[i][3]) <= 8 :
                            print(sortedName[i][3],end='\t\t')
                        else :
                            print(sortedName[i][3],end='\t')

                        print(sortedName[i][4],end='\t\t')
                        print(sortedName[i][5])
                    print('=========================================================================================================')
                    break

                elif pilihanSort == 2 :
                    sortedDom = sorted(MasterList,key=lambda l:l[5])

                    print('=========================================================================================================')
                    print('ID\tNama\t\tAlamat\t\t\t\t\tNo. Telepon\tKode Pos\tDomisili')
                    for i in range (len(sortedDom)):
                        print (sortedDom[i][0],end='\t')

                        if len(sortedDom[i][1]) < 7 :
                            print (sortedDom[i][1],end='\t\t')
                        else :
                            print(sortedDom[i][1],end='\t')

                        if len(sortedDom[i][2]) <= 15 :
                            print (sortedDom[i][2],end='\t\t\t\t')

                        elif len(sortedDom[i][2]) > 15 and len(sortedDom[i][2]) <= 20:
                            print (sortedDom[i][2],end='\t\t\t')

                        else :
                            print(sortedDom[i][2],end='\t\t')

                        if len(sortedDom[i][3]) <= 8 :
                            print(sortedDom[i][3],end='\t\t')
                        else :
                            print(sortedDom[i][3],end='\t')

                        print(sortedDom[i][4],end='\t\t')
                        print(sortedDom[i][5])
                    print('=========================================================================================================')
                    break

                elif pilihanSort == 3 :
                    break
                    
                else:
                    print("Input yang anda masukkan invalid\n") 

            except : 
                print("Input yang anda masukkan invalid")          
            # except : 
            #     print("Input yang anda masukkan invalid") 
        break

def tambahData():
    simpanTambahan = []
    while True :
        input_namaOrang = input('Masukkan nama Orang : ')
        if input_namaOrang.isalpha() == True:
            break
        else:
            print('Nama hanya bisa berisi huruf')
            continue
    input_alamat = str(input(f'Masukkan alamat si {input_namaOrang} : '))
    while True:
        try:
            input_telepon = int(input(f'Masukkan nomor telepon si {input_namaOrang} : '))
            str_input_telepon = str(input_telepon)
            if len(str_input_telepon) <5 :
                print('Nomor telepon terlalu pendek')
                continue
            elif len(str_input_telepon) >15 :
                print('Nomor telepon terlalu panjang')
                continue
            else:
                break
        except:
            print('Nomor Telepon hanya bisa diisi dengan angka !')
    
    while True:
        try:
            input_kodepos = int(input(f'Masukkan kode pos si {input_namaOrang} : '))
            str_input_kodepos = str(input_kodepos)
            if len(str_input_kodepos) == 5 :
                break
            else :
                print('Kode pos harus 5 digit dan hanya angka !')
                continue
        except:
            print('Kode pos harus 5 digit dan hanya angka !')

    input_kota = str(input(f'Masukkan kota si {input_namaOrang} : '))

    while True:
        apakahSort = str(input(f'Apakah anda ingin menambahkan data si {input_namaOrang} (y/n): '))
        if apakahSort == 'y' or apakahSort == 'Y' :

            simpanTambahan.append(int(f'{MasterList[-1][0]+1}'))
            simpanTambahan.append(str(f'{input_namaOrang}'.capitalize()))
            simpanTambahan.append(str(f'{input_alamat}'.title()))
            simpanTambahan.append(str(f'{input_telepon}'))
            simpanTambahan.append(int(f'{input_kodepos}'))
            simpanTambahan.append(f'{input_kota}'.title())
            MasterList.append(simpanTambahan)
            print(f'Data Si {input_namaOrang} berhasil ditambahkan')
            tampilData()
    
        elif apakahSort == 'n' or apakahSort == 'N' :
            break
        break
    return tambahData

def hapusData():
    tampilData()
    while True:
        diHapus = int(input('Masukkan ID data yang ingin dihapus : '))
        for i in range (len(MasterList)):
            if i == (len(MasterList)-1) and diHapus != MasterList[i][0]:
                print(f"Data dengan ID {diHapus} tidak ditemukan")

            elif diHapus == MasterList[i][0] :
                while True:
                    apaHapus = str(input(f"Apakah anda ingin menghapus data dengan id {diHapus} (y/n)?"))
                    if apaHapus == 'y' or apaHapus == 'Y' :
                        del MasterList[i]
                        print(f'Data dengan ID {diHapus} berhasil dihapus')
                        break
                    elif apaHapus == 'n' or apaHapus == 'N' :
                        break
                    else : 
                        print('Input yang anda masukkan invalid')
                break    
        break
    return hapusData

def updateData():
    while True : 
        try:
            tampilData()
            diUpdate = int(input('Masukkan ID data yang ingin diupdate : '))
            for x in range (len(MasterList)):
                if x == (len(MasterList)-1) and diUpdate != MasterList[x][0]:
                    print(f"Data dengan ID {diUpdate} tidak ditemukan")

                elif diUpdate == MasterList[x][0]:
                    print("1.Nama\n2.Alamat\n3.Nomor Telepon\n4.Kode Pos\n5.Domisili\n6.Back to Main Menu")
                    mauUpdate = int(input('Masukkan bagian data yang ingin diupdate : '))

                    if mauUpdate == 1:
                        while True :
                            updateNama = str(input('Masukkan nama baru : '))
                            if updateNama.isalpha() == True:
                                break
                            else:
                                print('Nama hanya bisa berisi huruf')
                                continue
                        for i in range (len(MasterList)):
                            if MasterList[i][0] == diUpdate:
                                MasterList[i][1] = updateNama.capitalize()
                                print("Nama berhasil diupdate")
                                break

                    elif mauUpdate == 2:
                        updateAlamat = str(input('Masukkan alamat baru : '))
                        for i in range (len(MasterList)):
                            if MasterList[i][0] == diUpdate:
                                MasterList[i][2] = updateAlamat.title()
                                print("Alamat berhasil diupdate")
                                break

                    elif mauUpdate == 3:
                        while True:
                            try:
                                updateTelepon = int(input('Masukkan nomor telepon baru : '))
                                str_updateTelepon = str(updateTelepon)
                                if len(str_updateTelepon) <5 :
                                    print('Nomor telepon terlalu pendek')
                                    continue
                                elif len(str_updateTelepon) >15 :
                                    print('Nomor telepon terlalu panjang')
                                    continue
                                else:
                                    for i in range (len(MasterList)):
                                        if MasterList[i][0] == diUpdate:
                                            MasterList[i][3] = str_updateTelepon
                                            print("Nomor telepon berhasil diupdate")
                                            break
                                    break
                            except:
                                print('Nomor telepon harus angka')

                    elif mauUpdate == 4:
                        while True:
                            try:
                                updatePos = int(input('Masukkan kode pos baru : '))
                                str_updatePos = str(updatePos)

                                if len(str_updatePos) == 5 :
                                    for i in range (len(MasterList)):
                                        if MasterList[i][0] == diUpdate:
                                            MasterList[i][4] = str_updatePos
                                            print("Kode pos berhasil diupdate")
                                            break
                                    break
                                else :
                                    print('Kode pos harus 5 digit dan hanya angka !')

                            except:
                                print('Kode pos harus 5 digit dan hanya angka !')

                    elif mauUpdate == 5:
                        updateKota = str(input('Masukkan nama kota baru : '))
                        for i in range (len(MasterList)):
                            if MasterList[i][0] == diUpdate:
                                MasterList[i][5] = updateKota.title()
                                print("Nama kota berhasil diupdate")
                                break
                            break
                    
                    elif mauUpdate == 6 :
                        break
                else :
                    continue
                break
        except:
            print('Data tidak ditemukan atau input bukan angka')
        break
    return updateData

menuUtama()