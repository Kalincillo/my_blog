#include <regx52.h>
void retardo_ms(unsigned int msegs), sensor();

unsigned int distancia = 0, cuenta = 0, cuenta_baja = 0, cuenta_alta = 0;
#define tx_der P1_0
#define motor0 P1_1
#define motor1 P1_2
#define motor2 P1_3
#define motor3 P1_4
#define A5 P2_4
#define A6 P2_3
#define A7 P2_2
#define A8 P2_1
#define A9 P2_0

void main() // Función principal
{
    tx_der = 0;
    TMOD = 0x01; // Timer0 en modo 1, sin intervención externa
    TR0 = 1;     // Habilita Timer0
    while (1)
    {
        sensor();
        if (distancia <= 210 && distancia >= 191)
        {
            A9 = 0;
            A8 = 0;
            A7 = 0;
            A6 = 0;
            A5 = 0;
        }
        else if (distancia <= 190 && distancia >= 171)
        {
            A9 = 0;
            A8 = 0;
            A7 = 0;
            A6 = 1;
            A5 = 0;
        }
        else if (distancia <= 170 && distancia >= 151)
        {
            A9 = 0;
            A8 = 0;
            A7 = 1;
            A6 = 0;
            A5 = 0;
        }
        else if (distancia <= 150 && distancia >= 131)
        {
            A9 = 0;
            A8 = 0;
            A7 = 1;
            A6 = 1;
            A5 = 0;
        }
        else if (distancia <= 130 && distancia >= 111)
        {
            A9 = 0;
            A8 = 1;
            A7 = 0;
            A6 = 0;
            A5 = 0;
        }
        else if (distancia <= 110 && distancia >= 91)
        {
            A9 = 0;
            A8 = 1;
            A7 = 0;
            A6 = 1;
            A5 = 0;
        }
        else if (distancia <= 90 && distancia >= 71)
        {
            A9 = 0;
            A8 = 1;
            A7 = 1;
            A6 = 0;
            A5 = 0;
        }
        else if (distancia <= 70 && distancia >= 51)
        {
            A9 = 0;
            A8 = 1;
            A7 = 1;
            A6 = 1;
            A5 = 0;
        }
        else if (distancia <= 50 && distancia >= 31)
        {
            A9 = 1;
            A8 = 0;
            A7 = 0;
            A6 = 0;
            A5 = 0;
        }

        else if (distancia <= 30 && distancia >= 11)
        {
            A9 = 1;
            A8 = 0;
            A7 = 0;
            A6 = 1;
            A5 = 0;
        }
        else if (distancia <= 10)
        {
            A9 = 0;
            A8 = 0;
            A7 = 0;
            A6 = 0;
            A5 = 1;
        }
        else if (distancia > 211)
        {
            A9 = 0;
            A8 = 0;
            A7 = 1;
            A6 = 0;
            A5 = 1;
        }
        if (distancia <= 200 && distancia >= 187)
        {
            motor0 = 0;
            motor1 = 0;
            motor2 = 0;
            motor3 = 1;
        }
        else if (distancia <= 186 && distancia >= 175)

        {
            motor0 = 0;
            motor1 = 0;
            motor2 = 1;
            motor3 = 0;
        }
        else if (distancia <= 174 && distancia >= 162)
        {
            motor0 = 0;
            motor1 = 0;
            motor2 = 1;
            motor3 = 1;
        }
        else if (distancia <= 161 && distancia >= 150)

        {
            motor0 = 0;
            motor1 = 1;
            motor2 = 0;
            motor3 = 0;
        }
        else if (distancia <= 149 && distancia >= 136)

        {
            motor0 = 0;
            motor1 = 1;
            motor2 = 0;
            motor3 = 1;
        }
        else if (distancia <= 135 && distancia >= 122)

        {
            motor0 = 0;
            motor1 = 1;
            motor2 = 1;
            motor3 = 0;
        }
        else if (distancia <= 121 && distancia >= 109)
        {
            motor0 = 0;
            motor1 = 1;
            motor2 = 1;
            motor3 = 1;
        }
        else if (distancia <= 108 && distancia >= 95)

        {
            motor0 = 1;
            motor1 = 0;
            motor2 = 0;
            motor3 = 0;
        }
        else if (distancia <= 94 && distancia >= 83)

        {
            motor0 = 1;
            motor1 = 0;
            motor2 = 0;
            motor3 = 1;
        }
        else if (distancia <= 82 && distancia >= 70)

        {
            motor0 = 1;
            motor1 = 0;
            motor2 = 1;
            motor3 = 0;
        }
        else if (distancia <= 69 && distancia >= 56)
        {
            motor0 = 1;
            motor1 = 0;
            motor2 = 1;
            motor3 = 1;
        }
        else if (distancia <= 55 && distancia >= 43)

        {
            motor0 = 1;
            motor1 = 1;
            motor2 = 0;
            motor3 = 0;
        }
        else if (distancia <= 42 && distancia >= 30)

        {
            motor0 = 1;
            motor1 = 1;
            motor2 = 0;
            motor3 = 1;
        }
        else if (distancia <= 29 && distancia >= 16)

        {
            motor0 = 1;
            motor1 = 1;
            motor2 = 1;
            motor3 = 0;
        }
        else if (distancia <= 15)
        {
            motor0 = 1;
            motor1 = 1;
            motor2 = 1;
            motor3 = 1;
        }
        else if (distancia > 200)

        {
            motor0 = 0;
            motor1 = 0;
            motor2 = 0;
            motor3 = 0;
        }
    }
}

void sensor()
{
    tx_der = 1;
    TL0 = 0;
    TH0 = 0;
    while (TL0 < 20)
        ;
    tx_der = 0;
    while (tx_der == 0)
        ;
    TL0 = 0;
    TH0 = 0;
    while (tx_der == 1)
        ;
    cuenta_baja = TL0;
    cuenta_alta = TH0;
    cuenta = cuenta_alta << 8;
    cuenta = cuenta | cuenta_baja;
    distancia = cuenta / 58;
}

