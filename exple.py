from Module import Module
import math

PER_CONST = pow(10,-6)
diction = {
"TR": Module('Transducer',1000*PER_CONST, 100),

"P_S" : Module("Power Supply",20*PER_CONST, 100),

"H_E" : Module("Heat Exchanger", 20*PER_CONST, 100),

"T_R_S" :Module("Transmitter/Receiver Switch", 6*PER_CONST, 100),

"P_A" : Module("Power Amplifier", 120*PER_CONST, 100),

"PRE_A" : Module("Pre Amplifier", 32*PER_CONST, 100),

"F_P" : Module("Front-end Processor", 400*PER_CONST, 100),

"S_C" : Module("System Controller", 10*PER_CONST, 100),

"SDLC" : Module("SDLC Bus", 15*PER_CONST, 100),

"S_P" : Module("Signal Procesor", 450*PER_CONST, 100),

"D_P" : Module("Display_ Processor", 150*PER_CONST, 100),

"D_M" :Module("Display Monitor", 50*PER_CONST, 100),

"A_P" : Module("Audio Processor", 20*PER_CONST, 100)
}



def show_Modules(diction:dict):
    print("-----------------|-----------------------------------\n")
    print("Module Name      | Reliability\n")
    print("-----------------|-----------------------------------\n")
    for kev in diction:
        print(str(kev) + "               |"+ str(diction[kev].rel)+"\n")
        print("-----------------|-----------------------------------\n")


##############"registering module"##############
# done = False
# while not done:
#     name = input("Enter the moudle name")
#     print(''' 
#         Select info you would want to give for your module
#         1. Reliability
#         2. failure rate and operational time
#         ''')
#     val = int(input())
#     if val == 1:
#         rel = float(input("Enter the reliabilty:\n"))
#         m1 = Module(name, rel)
#     elif val == 2:
#         f_rate = float(input("Enter your failure rate:\n"))
#         op_time = float(input("Enter your operational time:\n"))
#         m1 = Module(name, f_rate*math.pow(10,-6), op_time)
    
#     diction[name] = m1
    
#     cnt = input("Do you want to register a new module?(y/n)\n")
#     if cnt in ['n','N']:
#         done = True
        
print("The Following are your modules:\n")
print(diction)
show_Modules(diction)

n_blocks = int(input("How many block can you partition your system into?\n"))
block_modules = {}

i = 1
done = False
while(i < n_blocks+1):
        
    
    name = "block"+ str(i)
    str_ = "enter your expression for block-"+ str(i)
    exp = input(str_)
   
    block_modules[name] = eval(exp, diction)

    i= i + 1
    
show_Modules(block_modules)

exp = input("enter your expression for the system\n")
    
print("This is your expression"+ exp)

ans = eval(exp, block_modules)

print(ans)

    

    
    


