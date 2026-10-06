from machine import Pin, PWM
from time import sleep

# Motor A / Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B / Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Set PWM frequency to 1000 Hz / Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

#Funktiot Focarin liikkeille
def eteenpain (aika =6, nopeus = 32767):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)


def kaanny(suunta, maara, nopeus =32767):
    if(suunta== "vasemmalle"):
        m1.value(1)
        m2.value(0)
        e1.duty_u16(nopeus)
        e2.duty_u16(nopeus)
        sleep(maara)
    else: #mennään oikealle
        m1.value(0)
        m2.value(1)
        e2.duty_u16(nopeus)
        e1.duty_u16(nopeus)
        sleep(maara)

def taaksepain(aika =6, nopeus =32767):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def pysayta():
    m1.value(0)
    m2.value(0)
    e1.duty_u16(0)
    e2.duty_u16(0)

#odottaa kymmenen sekunttia ennen liikkeelle lähtöä
sleep(10)

#haetaan liikkeet tiedostosta
with open ("sreitti.txt", "r") as tiedosto:
    sisalto = tiedosto.readlines()

for rivi in sisalto:
    osat = rivi.strip().split(",")
    komento = osat[0]

    if komento == "suoraan":
        aika = float(osat[1])
        eteenpain(aika=aika)

    elif komento == "kaanny":
        suunta = osat[1].strip()
        aika = float(osat[2])
        kaanny(suunta=suunta, maara=aika)


    elif komento == "taaksepain":
        aika = float(osat[1])
        taaksepain(aika=aika)

    elif komento == "pysayta":
        pysayta()




pysayta()