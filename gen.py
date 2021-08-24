# coding: utf8
"""
Генератор сайта ПАК-Звезда

"""

import os
from os.path import join
from os.path import abspath
import re
SLIDES = [
    {
        "title" : "Скуд, Подмена данных",
        "cat" : "zavod",
        "full" : "кпп(скуд).png",
        "folder" : "кпп(скуд)"
    },
    {
        "title" : "Скуд, Автоматизация",
        "cat" : "zavod",
        "full" : "охранники(скуд).png",
        "folder" : "охрана"
    },
    {
        "title" : "Техпроцесс, Датчики состояния среды",
        "cat" : "zavod",
        "full" : "работник_месяца.png",
        "folder" : "работник_года"
    },
    {
        "title" : "Датчики состояния среды, Подмена данных",
        "cat" : "zavod",
        "full" : "первый_день.png",
        "folder" : "первый_день"
    },
    {
        "title" : "Сигнализация, Подмена данных",
        "cat" : "zavod",
        "full" : "пожар.png",
        "folder" : "пожар"
    },
    {
        "title" : "Электрокар",
        "cat" : "sklad",
        "full" : "погрузчик.png",
        "folder" : "погрузчик"
    },
    {
        "title" : "Счётчики",
        "cat" : "dom",
        "full" : "счётчики.png",
        "folder" : "счётчики"
    },
    {
        "title" : "Датчики температуры",
        "cat" : "dom",
        "full" : "датчики_температуры.png",
        "folder" : "датчики_температуры"
    },
    {
        "title" : "Кормилка, Подмена данных",
        "cat" : "dom",
        "full" : "кормилка.png",
        "folder" : "кормилка"
    },
    {
        "title" : "Получение доступа к устройству, DDoS",
        "cat" : "dom",
        "full" : "ддос.png",
        "folder" : "ддос"
    },
    {
        "title" : "Подмена данных",
        "cat" : "muzei",
        "full" : "музей.png",
        "folder" : "музей"
    },
    {
        "title" : "Удалённое управление, Подмена данных",
        "cat" : "auto",
        "full" : "автомобиль.png",
        "folder" : "автомобиль"
    },
    {
        "title" : "Светофор, Зелёная полоса, Подмена сигнала",
        "cat" : "gorod",
        "full" : "премьера(зеленая_полоса).png",
        "folder" : "зеленая_полоса_плохо"
    },
    {
        "title" : "Светофор, Зелёная полоса",
        "cat" : "gorod",
        "full" : "пожарные(зеленая_полоса).png",
        "folder" : "пожарные"
    },
    {
        "title" : "GPS-трэкинг, подмена сигнала",
        "cat" : "ferma",
        "full" : "корова.png",
        "folder" : "корова"
    },
    {
        "title" : "Подмена данных",
        "cat" : "implant",
        "full" : "кардиостимулятор.png",
        "folder" : "кардиостимулятор"
    }
]

CATS = {
    "zavod" : {"title" : "Умный завод", "label" : "warning"},
    "sklad" : {"title" : "Умный склад", "label" : "violet"},
    "dom" : {"title" : "Умный дом", "label" : "success"},
    "muzei" : {"title" : "Умный музей", "label" : "danger"},
    "auto" : {"title" : "Умный автомобиль", "label" : "light"},
    "gorod" : {"title" : "Умный город", "label" : "secondary"},
    "ferma" : {"title" : "Умная ферма", "label" : "blue"},
    "implant" : {"title" : "Умные импланты", "label" : "info"}
}

SITE_PATH="./"
FOLDER_PATH = "Ох уж этот ПАК Звезда/images/"
FIRST_IMG = "Cell-Row-0-Col-0.png"
FULL_PATH = "Ох уж этот ПАК Звезда/column1/"
SITE_DIR = "site"

def transliterate(text):
    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
    tr = {ord(a):ord(b) for a, b in zip(*symbols)}
    return text.translate(tr)

def genUrl(text):
    return transliterate(text).replace('(', '_').replace(')', '_').replace(' ', '_') \
    .replace(',', '').strip()
	
def CreateFile(url, txt):
    f = open( join( abspath(os.path.curdir), SITE_DIR, url+".html"), 'w', 
        encoding="utf-8")
    f.write(txt)
    f.close()
	
def getTmpl(f):
    return open( join( abspath(os.path.curdir), SITE_DIR, "tmpl_"+f+".html" ), 
        encoding="utf-8" ).read()

def genBuklets():
    tmpl = getTmpl("buklet")
    html = ""
    for slide in SLIDES:
        sl=tmpl.replace(r"%img%", SITE_PATH+FOLDER_PATH+slide["folder"]+"/"+FIRST_IMG)
        sl=sl.replace(r"%text%", slide["title"])
        sl=sl.replace(r"%cat%", CATS[slide["cat"]]["title"])
        sl=sl.replace(r"%label%", CATS[slide["cat"]]["label"])
        sl=sl.replace(r"%show_link%", "./"+genUrl(CATS[slide["cat"]]["title"]+"_"+slide["title"])
        +".html")
        sl=sl.replace(r"%download_link%", SITE_PATH+FOLDER_PATH+slide["folder"]+".zip")

        html+=sl

    return html

def genGroups():
    html=""
    for cat, data in CATS.items():

        hlinks = ""
        for slide in SLIDES:
            if slide['cat'] == cat:
                url = "./"+genUrl(CATS[slide["cat"]]["title"]+"_"+slide["title"])+".html"
                hlinks+='<a class="dropdown-item" href="'+url+'">'+slide['title']+'</a>'
        html+='''
    <div class="btn-group">
        <button type="button" class="btn btn-sm btn-'''+data['label']+''' dropdown-toggle" 
        data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            '''+data['title']+'''
        </button>
        <div class="dropdown-menu">
        '''+hlinks+'''
        </div>
    </div>
    '''
    return html

def genHF(type):
    html = getTmpl(type).replace(r"%header%", getTmpl("header"))
    html = html.replace(r"%footer%", getTmpl("footer"))
    html = html.replace(r"%groups%", genGroups())

    for ctype in ["index", "page"]:
        ht = ""
        k=1
        arr = re.split('\[\['+ctype+'|'+ctype+'\]\]', html)
        for h in arr:
            if k or ctype==type:
                ht += h.strip().rstrip()
            k=1-k

        html = ht
    return html

def generatePages():
    for slide in SLIDES:
        html = genHF("page")
        html = html.replace(r"%title%", slide["title"])
        html = html.replace(r"%h1%", slide["title"])
        html = html.replace(r"%image%", SITE_PATH+FULL_PATH+slide["full"])
        html = html.replace(r"%label%", CATS[slide["cat"]]["label"])
        html = html.replace(r"%cat%", CATS[slide["cat"]]["title"])
        html = html.replace(r"%download_link%", SITE_PATH+FOLDER_PATH+slide["folder"]+".zip")

        url = genUrl(CATS[slide["cat"]]["title"]+"_"+slide["title"])
        CreateFile(url, html)

def generateIndex(): 

    html = genHF("index")
    html = html.replace(r"%buklets%", genBuklets())
    CreateFile("index", html)


generateIndex()
generatePages()