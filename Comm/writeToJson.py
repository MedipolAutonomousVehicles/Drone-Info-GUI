import json
from random import randint
import sys
from time import sleep
while True:
    try:
        datas = {"Takım Numarası": "", "GPS Saat": "", "GPS Dakika": "", "GPS Saniye": "", "GPS Salise": "",
                      "Server Saat": "", "Server Dakika": "", "Server Saniye": "", "Server Salise": "", "İHA Enlem": "",
                      "İHA Boylam": "", "İHA İrtifa": "", "Dikilme": "", "Yönelme": "", "Yatış": "", "Hız": "", "Pil": "",
                      "İHA Modu": "", "Kilitlenme Durumu": "", "Kilit Çerçevesi Merkezi X": "", "Kilit Çerçevesi Merkezi Y": "",
                      "Kilit Çerçevesi Genişliği": "", "Kilit Çerçevesi Yüksekliği": "", "Avcı Takım Numarası": "",
                      "Kilitlenme Numarası": "", "GPS Saat Kilitlenme Başlangıç": "", "GPS Dakika Kilitlenme Başlangıç": "",
                      "GPS Saniye Kilitlenme Başlangıç": "", "GPS Salise Kilitlenme Başlangıç": "",
                      "GPS Saat Kilitlenme Bitiş": "", "GPS Dakika Kilitlenme Bitiş": "", "GPS Saniye Kilitlenme Bitiş": "",
                      "GPS Salise Kilitlenme Bitiş": ""}


        for key,value in datas.items():
            newValue = randint(1, 1000)
            if not value == newValue:
                datas[key]=newValue

        with open("dataFile.json", 'w') as writeFile:
            json_string = json.dumps(datas, default=lambda o: o.__dict__, sort_keys=False, indent=2)
            writeFile.write(json_string)

        writeFile.close()
    except KeyboardInterrupt:
        sys.exit()
    sleep(1)
