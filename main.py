import os, random, time

from bus import Bus

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

equipo1 = 'JUNIOR'
equipo2 = 'SANTA FE'

def main():
    bus_1 = Bus()
    bus_2 = Bus()
    print('¡¡CARRERA DE BUSES!!')
    print(f'{equipo1} VS {equipo2}')

    time.sleep(1)
    while True:
        limpiar_consola()
        Bus.dibujar_inicio_pista()
        bus_1.dibujar_bus(random.randint(1, 2), f'{equipo1}')
        Bus.dibujar_inicio_pista()
        bus_2.dibujar_bus(random.randint(1, 2), f'{equipo2}')
        Bus.dibujar_inicio_pista()

        if bus_1.posicion >= 100 or bus_2.posicion >= 100:
            if bus_1.posicion >= 100:
                print(f'¡¡¡{equipo1} GANA!!!')
            else:
                print(f'¡¡¡{equipo2} GANA!!!')
            time.sleep(2)
            break

        time.sleep(0.1)

main()

