# Aplikasi Quiz

from posixpath import abspath
import mainQuiz
import buatQuiz
import pos
import os
import time
#jalur = '/'.join(str(abspath('quizapp')).split('\\'))
jalur = '.'

def welcome():
    os.system('clear')
    print("Selamat datang diaplikasi quiz kami")
    while True :
        menu_login = input("Silahkan pilih menu disamping 1.Login 2.Sign Up 3.Exit: ")
        if menu_login == "1":
            login()
        elif menu_login == "2":
            sign_up()
        elif menu_login == '3':
            exit()
        else : 
            print("Silahkan pilih menu diatas")
    
def login():
    os.system('clear')
    global username
    global pwd
    print("Login")
    username = input("Silahkan masukkan username anda : ")
    pwd = input("Silahkan masukkan password anda : ")
    datauser = pos.loadData('user.json',folder='user_data')
    for user in datauser :
        if ' '.join(username.lower().split()) == user['username'] :
            if ' '.join(pwd.lower().split()) == user['password'] :
                menu_utama()
            else : 
                print("Password salah")
    print("Password atau username salah")

def sign_up():
    os.system('clear')
    datauser = pos.loadData('user.json',folder='user_data')
    print("Sign up")
    username = input("Username : ")
    pwd = input("Password : ")
    datauser.append({'username':' '.join(username.lower().split()),'password':' '.join(pwd.lower().split())})
    pos.simpanData(PATH='user.json' ,data = datauser,folder='user_data')
    
    print("Data sudah terinput")

def profile(username,pwd):
    os.system('clear')
    datauser = pos.loadData('user.json',folder='user_data')
    pwd = input("Silahkan masukkan password anda : ")
    for user in datauser :
        if username == user['username'] :
            if pwd == user['password'] :
                print('Edit Profile')
                while True:
                    print('1.Edit nama 2.Edit pass 3.Simpan 4.Keluar')
                    choice = input()
                    if choice == '1':
                        username = input("Masukkan nama baru : ")
                    elif choice == '2':
                        pwd == input('Masukkan pass baru : ')
                    elif choice == '3' :
                        user['username'] = username
                        user['password'] = pwd
                        pos.simpanData(PATH='user.json' ,data = datauser,folder='user_data')
                    elif choice == '4' :
                        break  
    os.system('clear')                    
def updateRanking():
    datauser = pos.loadData('user.json',folder='user_data')
    filles = os.listdir(jalur + '/' + 'soal') 
    index = 0
    for i in filles :
        nilai = []
        for j in datauser:
            if f"Score_({i[:-5]})" in j:
                nilai.append({'score': j[f'Score_({i[:-5]})'],'username':j['username'],})
        pos.simpanData(f'Rank_{i[:-5]}.json',nilai,folder='ranking',mode = True)
def lihatRanking(username):
    os.system('clear')
    soal = os.listdir(jalur + '/soal')
    print('Ranking hanya dilihat dari score pertama anda')
    index = 0
    print('%-2s %-20s '% ('no','Nama soal'))
    for i in soal :
        print('%-2s %-20s '% (index + 1,i[:-5]))
        index += 1
    while True:
        try :
            index = input('Pilih index : ')
            if index.lower() == 'n':
                break
            rank = pos.loadData(f'Rank_{soal[int(index)-1]}',folder='ranking')
            break
        except :
            print('Pilih dari index')

    count = 0
    for i in rank:
        print("%-3s %-20s"%(count + 1,i['username']))
        if i['username'] == username :
            index = count
        count += 1
    print('Ranking anda : ',index)



def menu_utama():
    os.system('clear')
    print("Selamat datang di aplikasi kami, ",username)
    while True:
        print("1.Bermain 2.Buat dan Edit Soal 3.Profile 4.Ranking 5.Exit")
        pilih = input()
        if pilih == '1':
            mainQuiz.MainQuiz(username)
        elif pilih  == '2':
            buatQuiz.menuEditdanBuat()
        elif pilih == '3' :
            profile(username,pwd)
        elif pilih == '4' :
            updateRanking()
            lihatRanking(username)
        elif pilih == '5':
            exit()
    os.system('clear')
welcome()


