# quiz fungsi
#import main
import json
import os
import pos
from posixpath import abspath

quiz = []
ujian = []

#jalur =  '/'.join(str(abspath('quizapp')).split('\\'))
jalur = './soal'



def menuEditdanBuat():
    os.system('clear')
    print('1.Buat soal 2.Edit soal 3.Kembali')
    pilih = input()
    if pilih == '1':
        menuBuat()
    elif pilih == '2':
        quizEdit()
    else :
        pass
def menuBuat():
    os.system('clear')
    print('Silahkan pilih jenis quiz')
    jenis = input('1.Quiz 2.Ujian 3.Keluar')
    if jenis == '1':
        quizBuat('quiz')
    elif jenis == '2' :
        quizBuat('Ujian')

def soalBuat(LIST,tipe = 'quiz',tipe_soal = 'pilihan'):
    os.system('clear')
    global quiz
    counter = 0

    while True :
        print('1.Soal baru 2.Hapus Soal 3.Simpan soal 4.Keluar')
        lagi = input()

        if lagi == '1':
            print('Masukkan Pertanyaan : ')
            soal = input()
            if tipe_soal == 'pilihan':
                a = input('Pilihan a : ')
                b = input('Pilihan b : ')
                c = input('Pilihan c : ')
                d = input('Pilihan d : ')
            
            if tipe_soal == 'pilihan':
                while True :
                    jawaban = input('Jawaban : ')
                    if jawaban.lower() in ['a','b','c','d'] and jawaban.isalpha():
                        break
            else :
                jawaban = input('Jawaban : ')

            if tipe == 'quiz':
                try :
                    score = int(input('Score : '))
                except:
                    print('Score default 20')
                    score = 202
                if tipe_soal == 'pilihan':
                    LIST.append({'soal': soal , 'a' : a, 'b' : b, 'c' : c, 'd' : d,'jawaban':jawaban.lower(),'score':score})
                else :
                    LIST.append({'soal': soal ,'jawaban': jawaban.lower(),'score': score})
            else :
                if tipe_soal == 'pilihan':
                    LIST.append({'soal': soal , 'a' : a, 'b' : b, 'c' : c, 'd' : d,'jawaban':jawaban.lower()})
                else :
                    LIST.append({'soal': soal ,'jawaban': jawaban.lower()})
        elif lagi == '2':
            counter = 0
            print('%-2s %-15s'%('No','Soal'))
            try :
                for i in LIST:
                    counter += 1
                    print('%-2s %-15s'%(counter, i['soal'][0:10]+ '.....'))
                index = input('Pilih no soal yg ingin dihapus : ')
                yakin = input('Apakah anda yakin ?(y/n) ')
                if yakin == 'y':
                        LIST.pop(int(index) - 1)
                else :
                    pass
            except :
                print('Belum ada soal atau no soal anda salah')
                continue
        elif lagi == '3':
            simpanQuiz(LIST,namasoal,tipe)
            quiz = []
            break
        elif lagi == '4':
            break
    return LIST


def quizBuat(tipemu):
    os.system('clear')
    global namasoal
    global kesulitan
    kumpulan_soal = os.listdir(jalur)
    if tipemu == 'ujian':
        print('Buat Ujianmu')
    else :
        print('Buat quizmu')
    os.system('clear')
    while True :
        namasoal = input('Masukkan nama soal : ')
        if namasoal in kumpulan_soal:
            print('Nama soal tersebut sudah ada')
        elif ' ' in namasoal or '_' in namasoal:
            print('Nama Soal tidak boleh menggunakan spasi atau underscore')
        elif len(namasoal) > 18 :
            print('Nama soal terlalu panjang')
        else :
            break

    while True:
        print('1.Buat Soal 2.Keluar')
        pilih_1 = input()
        if pilih_1 == '1':
            print('1.Pilihan Ganda 2.Isian 3.Kembali')
            pilih = input()
            if pilih == '1':
                
                soalBuat(quiz,tipemu)
            elif pilih == '2':
                soalBuat(quiz,tipemu,tipe_soal='isian')
            elif pilih == '3':
                break
        elif pilih_1 == '2':
            break

def quizEdit():
    os.system('clear')
    onlyfiles = os.listdir(jalur)
    while True :
        print('| %-2s | %-6s | %-20s | %-6s |'%('No','Tipe','Nama soal','Jumlah'))
        counter_index = 0
        for i in onlyfiles:
            counter_index += 1
            jumalah = len(pos.loadData(i,folder='soal'))
            splitter = i.split('_')
            print('| %-2s | %-6s | %-20s | %-6s |'%(counter_index,splitter[1][:-5],splitter[0],jumalah))
        print('n untuk kembali')
        index = input('Pilih no quiz : ')
        if index == 'n':
            break
        elif not index.isnumeric():
            continue
        try : 
            quiz = pos.loadData(onlyfiles[int(index)-1],folder='soal')
            tipe = onlyfiles[int(index)-1][-9:]
            nama = onlyfiles[int(index)-1]
        except IndexError:
            print('Belum ada Soal')
            break
        counter_soal = 0
        while True :
            print('| %-2s | %-20s | %-20s |'%('No','Soal','jawaban'))
            for soal in quiz :
                counter_soal += 1
                print('| %-2s | %-20s | %-20s |'%(counter_soal,soal['soal'],soal['jawaban']))
                print('Masukkan n untuk kembali')
                no = input("Pilih no soal : ")
                counter_soal = 0
            if no == 'n':
                break
            elif not no.isnumeric():
                continue
            soal = quiz[int(no)-1]
            print('Soal : ',soal['soal'])
            if 'a' in soal.keys() :
                print('A.)' ,soal['a'])
                print('B.)' ,soal['b'])
                print('C.)' ,soal['c'])
                print('D.)' ,soal['d'])
            print('Jawaban : ',soal['jawaban'])
            edit = input('Apa yang ingin anda edit? ')
            if edit.lower() == 'soal' :
                soal_baru = input('Masukkan soal baru : ')
                soal['soal'] = soal_baru
            elif edit.lower() == 'a' :
                soal_baru = input('Masukkan pilihan baru : ')
                soal['a'] = soal_baru
            elif edit.lower() == 'b' :
                soal_baru = input('Masukkan pilihan baru : ')
                soal['b'] = soal_baru
            elif edit.lower() == 'c' :
                soal_baru = input('Masukkan pilihan baru : ')
                soal['c'] = soal_baru
            elif edit.lower() == 'd' :
                soal_baru = input('Masukkan pilihan baru : ')
                soal['d'] = soal_baru
            elif edit.lower() == 'jawaban' :
                soal_baru = input('Masukkan jawaban baru : ')
                soal['jawaban'] = soal_baru
    simpan = input('Simpan perubahan?(y/n) : ')
    if simpan == 'y':
        with open(jalur + '//' + nama ,'w+') as dataquiz:
            json_object = json.dumps(quiz, indent = 2)
            dataquiz.write(json_object)


def simpanQuiz(data,namasoal,tipe='quiz'):
    with open(jalur + '//' + f"{namasoal}_{tipe}.json",'w+') as dataquiz:
        json_object = json.dumps(data, indent = 2)
        dataquiz.write(json_object)
