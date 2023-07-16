from Module import Module
import math

PER_CONST = pow(10,-6)
TR= Module('Transducer',1000*PER_CONST, 100)

P_S = Module("Power Supply",20*PER_CONST, 100)

H_E = Module("Heat Exchanger", 20*PER_CONST, 100)

T_R_S = Module("Transmitter/Receiver Switch", 6*PER_CONST, 100)

P_A = Module("Power Amplifier", 120*PER_CONST, 100)

PRE_A = Module("Pre Amplifier", 32*PER_CONST, 100)

F_P = Module("Front-end Processor", 400*PER_CONST, 100)

S_C = Module("System Controller", 10*PER_CONST, 100)

SDLC = Module("SDLC Bus", 15*PER_CONST, 100)

S_P = Module("Signal Procesor", 450*PER_CONST, 100)

D_P = Module("Display_ Processor", 150*PER_CONST, 100)

D_M = Module("Display Monitor", 50*PER_CONST, 100)

A_P = Module("Audio Processor", 20*PER_CONST, 100)



New_sys = TR * P_S * H_E * T_R_S * P_A * PRE_A * F_P * (S_C | S_C) * (SDLC | SDLC) * S_P * ((D_P * (D_M | D_M)) | (D_P * (D_M | D_M)) ) * A_P

print(New_sys)
