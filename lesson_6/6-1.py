from time import sleep

class TrafficLight:
    # атрибуты класса
    __color = 'Цвет'

    # методы класса
    def running(self):
        while True:

            def red(text):
                print("\r \033[31m {}".format(text), end="")
            red('Светофор горит красным')
            sleep(7)

            def yellow(text):
                print("\r \033[33m {}".format(text), end="")
            yellow('Светофор горит желтым ')
            sleep(2)

            def green(text):
                print("\r \033[32m {}".format(text), end="")
            green('Светофор горит зеленым')
            sleep(7)

            yellow('Светофор горит желтым ')
            sleep(2)

trlight = TrafficLight()
trlight.running()
