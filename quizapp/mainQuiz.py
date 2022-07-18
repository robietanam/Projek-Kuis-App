import json
import pos
import os
from posixpath import abspath

#jalur = '/'.join(str(abspath('quizapp')).split('\\'))
jalur = '.'


def MainQuiz(username):
    os.system('clear')
    onlyfiles = os.listdir(jalur+ '/soal')
    while True :
        print('Soal yang tersedia')
        print('| %-2s | %-6s | %-20s | %-6s |'%('No','Tipe','Nama soal','Jumlah'))
        counter_index = 0
        for i in onlyfiles:
            counter_index += 1
            jumalah = len(pos.loadData(i,folder='soal'))
            splitter = i.split('_')
            try :
                print('| %-2s | %-6s | %-20s | %-6s |'%(counter_index,splitter[1][:-5],splitter[0],jumalah))
            except IndexError:
                print('Belum ada soal')
                break
        print('Masukkan n untuk keluar')
        index = input('Pilih no soal : ')
        if index == 'n':
            break
        try : 
            quiz = pos.loadData(f'{onlyfiles[int(index)-1]}',folder='soal')
            tipe = onlyfiles[int(index)-1][-9:]
            namasoal = onlyfiles[int(index)-1][:-5]
        except IndexError:
            print('Belum ada soal')
            break
        
        counter_soal = 0
        score_quiz = 0
        score_ujian = 0
        for soal in quiz :
            counter_soal += 1
            print(f"{counter_soal}.) {soal['soal']}")
            if 'a' in soal.keys():
                print(f"A. {soal['a']}")
                print(f"B. {soal['b']}")
                print(f"C. {soal['c']}")
                print(f"D. {soal['d']}")
                while True :
                    jawab = input('Jawaban : ')
                    if ' '.join(jawab.lower().split()) in ['a','b','c','d'] and jawab.isalpha():
                        break
            else :
                jawab = input('Jawaban anda : ')
            if ' '.join(jawab.lower().split()) == soal['jawaban']:
                if tipe == 'quiz.json':
                    print('Benar , poin bertambah : ', soal['score'])
                    score_quiz += soal['score']
                else :
                    print('Jawaban anda benar')
                    score_ujian += 1
            else :
                print('Jawaban anda salah')
        print(score_ujian)
        if tipe == 'quiz.json':
            print('Score anda adalah : ',score_quiz)
            users = pos.loadData('user.json',folder='user_data')
            for user in users:
                if user['username'] == username:
                    if f'Score_({namasoal})' in user.keys():
                        user[f'Last_Score_({namasoal})'] = score_quiz
                    user[f'Score_({namasoal})'] = score_quiz
            pos.simpanData('user.json',folder='user_data',data=users)
        else : 
            print(score_ujian)
            print('Nilai anda adalah %.2d'%(((score_ujian/jumalah) * 100 )))
        main_lagi = input('Apakah ingin bermain lagi?(y/n) : ')
        if not main_lagi == 'y' :
            break
        