import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)



def dec2bin(number):
    return [int(element) for element in bin(number)[2:].zfill(8)]

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= 3.3):
        print("Напряжение выходит за динамический диапазон ЦАП")
        print("Устанавливаем ноль В")
        return 0

    return int(voltage / 3.3 * 255)



dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setup(dac_bits, GPIO.OUT)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            output = dec2bin(number)
            GPIO.output([16, 20, 21, 25, 26, 17, 27, 22], output)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()