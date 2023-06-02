import re

methodINSERT = {
    'ing' : 'INGRESO',
    'gas' : 'GASTO'
}

methodsUSER = {
         'USER' : 'ST',
         'ID' : 'id',
         'ing': methodINSERT
         ,'search': 'SEARCH'
          }



def formatDate(fecha):
    fechaFormat = str(fecha).split()[::-1]
    newformat = fechaFormat[2:]
    hourfreve = newformat[0:2][::-1]
    horaHM = hourfreve[0] + hourfreve[1]
    horaf = horaHM.replace(',',':')[0:-1]
    fechaArray = newformat[2:7]
    newfecha = fechaArray[0] + fechaArray[1] + fechaArray[2]
    fecha = (newfecha.replace(",","/"))[0:-1]
    fechaYhora = fecha +' '+ horaf
    return fechaYhora

def recogDate(fecha):
    reg = re.compile("[0-9]+,\s[0-9]+,\s[0-9]+,\s[0-9]+,\s[0-9]+,\s[0-9]+,\s[0-9]+")
    Date = str(fecha)
    result = reg.findall(Date)
    fechaT = formatDate(result[0])
    return fechaT


