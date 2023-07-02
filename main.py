#André Felipe Pereira Guimarães
#LAB 07
#Equipe NECAS

#Rodar na mesma pasta do design_tools e aux_tools

import design_tools as dt
import aux_tools as at
import numpy as np
import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
    
    #Pegando dados da aeronave e atualizando as dimensões
    current_aircraft = dt.default_aircraft()
    dim = dt.geometry(current_aircraft)
    current_aircraft['dimensions'].update(dim)

    #current_aircraft['dimensions']['fus']['Swet'] = aero['Swet_f']

    #Caso de testes
   
    gravity = 9.81
    W0_guess = 43090*gravity
    T0_guess = 125600
    
    altitude_cruise = 11000
    Mach_cruise = 0.77
    range_cruise = 2390000.000000000

    altitude_altcruise = 4572
    Mach_altcruise = 0.4
    range_altcruise = 370000

    loiter_time = 2700
    
    altitude_takeoff = 0.0
    distance_takeoff = 1520.0
    TO_flap_def = 0.34906585039887
    TO_slat_def = 0

    altitude_landing = 0.0
    distance_landing = 1520.0
    LD_flap_def = 0.69813170079733
    LD_slat_def = 0
    MLW_frac = 0.84
    

    W0 , Wf , T0 , deltaS_wlan , SM_fwd , SM_aft , b_tank_b_w , frac_nlg_fwd , frac_nlg_aft , alpha_tipback , alpha_tailstrike, phi_overturn = dt.analyze ( current_aircraft, W0_guess , T0_guess , Mach_cruise , altitude_cruise , range_cruise , Mach_altcruise , range_altcruise , altitude_altcruise ,
             loiter_time , altitude_takeoff , distance_takeoff , TO_flap_def , TO_slat_def ,altitude_landing , distance_landing , LD_flap_def , LD_slat_def, MLW_frac )
    
    Teste = [current_aircraft['geo_param']['wing']['sweep']*180/np.pi, SM_fwd, SM_aft]
    #Exercício 01
    #A alteracao no CG de todo o resto foi feita dentro da pasta design tools, entao o mesmo codigo foi rodado duas vezes
    #Basta alterar no desgin tools para ter os dois graficos gerados

    sweeps = np.linspace(0,45)
    fwds = []
    afts = []
    fwd_limite = [0.30]*len(sweeps)
    aft_limite = [0.05]*len(sweeps)

    for sweep in sweeps:
       current_aircraft['geo_param']['wing']['sweep'] = sweep * np.pi/180
       _,_,_,_, SM_fwd,SM_aft,_,_,_,_,_,_ = dt.analyze ( current_aircraft, W0_guess , T0_guess , Mach_cruise , altitude_cruise , range_cruise , Mach_altcruise , range_altcruise , altitude_altcruise ,
             loiter_time , altitude_takeoff , distance_takeoff , TO_flap_def , TO_slat_def ,altitude_landing , distance_landing , LD_flap_def , LD_slat_def, MLW_frac )
       fwds.append(SM_fwd)
       afts.append(SM_aft)
   
    plt.figure()
    plt.plot(fwds, sweeps, label='SM_fwd', color = 'red', linewidth = 1.5)
    plt.plot(afts, sweeps, label = 'SM_aft', color = 'blue', linewidth = 1.5)
    plt.plot(fwd_limite, sweeps, label = 'SM_fwd_limit_max', linestyle='--', color='red')
    plt.plot(aft_limite, sweeps, label = 'SM_aft_limit_min', linestyle='--', color='blue')
    plt.scatter( Teste[1], Teste[0], label = 'SM_fwd_teste', color = 'red')
    plt.scatter( Teste[2], Teste[0], label = 'SM_aft_teste', color = 'blue')
    plt.title('Sweep x Margem estatica')
    plt.xlabel('SM')
    plt.ylabel('Sweep(degree)')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig("Sweep_SM_cor.png")
   
    


    


    