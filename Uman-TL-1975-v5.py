import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as it

#Constants
eps0=8.854e-12
mu0=4*(math.pi)*1e-7
H=4e3 #meters
D=1e3#meters
v=8e7 #m/s
c=1/math.sqrt(mu0*eps0) #m/s

R_max=math.sqrt(H**2+D**2)
print('R_max',R_max)
dt=0.1e-6
dz=1

#arrays
t=np.arange(0,25e-6,dt)
z=np.arange(0,H,dz)

Nt=len(t)
Nz=len(z)

I=np.zeros(Nt) #channel-base
index=1e-6/dt
I[0:index+1]=(10e3/1e-6)*t[0:index+1]
I[index+1:]=-(10e3/24e-6)*t[index+1:]+(10e3+10e3/24) 

max_delayz=H/v;
max_delayD=R_max/c
N_delay=int((max_delayz+max_delayD)/dt)
print('N_delay',N_delay)
print('Nt',Nt)

Iz=np.zeros((Nz, Nt + N_delay)) #new time array to account for delays
#I_rad=np.zeros((Nt + N_delay)) #new time array to account for delays
print('Iz',Iz.shape)

R=np.zeros(Nz)
theta=np.zeros(Nz)
i=np.arange(0,Nz,1)
R=np.sqrt(i*dz**2+D**2)
theta=np.arcsin(D/R) #rad

for i in range(0,Nz):
    Iz[i,(i*((dz/v)/dt)+R[i]/c/dt):(i*((dz/v)/dt)+R[i]/c/dt+Nt)]=I #2-D array
#    I_rad[(i*((dz/v)/dt)+D/c/dt):(i*((dz/v)/dt)+D/c/dt+Nt)]=I #2-D array

tf=(Nt+N_delay+1)*dt
tz=np.arange(0,tf-dt,dt)
print('tz',tz.shape)
print('dt',dt)

plt.plot(tz*1e6,Iz[0,:],tz*1e6,Iz[-1,:])
plt.legend(['channel-base','4km'])
plt.xlabel('Time ($\mu$s)')
plt.xlim([0,tz[-1]*1e6])
plt.ylabel('Current Amplitude (A)')
plt.show()

#plt.plot(tz*1e6,-mu0*v*I_rad/(math.pi*2*D))
#plt.show()

#dI/dt
dI=np.gradient(I)

dIz=np.zeros((Nz, Nt + N_delay)) #new time array to account for delays

for i in range(0,Nz):
    dIz[i,(i*((dz/v)/dt)+R[i]/c/dt):(i*((dz/v)/dt)+R[i]/c/dt+Nt)]=dI #2-D array
    
#plt.plot(tz*1e6,dIz[0,:],tz*1e6,dIz[-1,:])
#plt.legend(['channel-base','4km'])
#plt.xlabel('Time ($\mu$s)')
#plt.xlim([0,tz[-1]*1e6])
#plt.ylabel('dI/dt')
#plt.show()   
    
Ntz=len(tz)
E_ind=np.zeros((Nt + N_delay))
B_phi=np.zeros((Nt + N_delay))
E_rad=np.zeros((Nt + N_delay))
E_elec=np.zeros((Nt + N_delay))
E_elec2=np.zeros((Nz))
E_elec_total=np.zeros((Nz, Nt + N_delay))
E_elec_zconstant=np.zeros((Nz, Nt + N_delay))

E1=np.zeros(Nz)
E2=np.zeros(Nz)
E3=np.zeros(Nz)
E4=np.zeros(Nz)
B1=np.zeros(Nz)
B2=np.zeros(Nz)

print('dIz',dIz[:,100].shape)
#
#it.quad
for i in range(0,Ntz): #for each time t, integrate over z
    B1=((np.sin(theta))*Iz[:,i])/(R**2)    
    B1[i]=(mu0/(2*math.pi))*it.simps(B1,dx=dz)
    
    B2=((np.sin(theta))*dIz[:,i])/(c*R) 
    B2[i]=(mu0/(2*math.pi))*it.simps(B2,dx=dz)
    B_phi[i]=B1[i]+B2[i]
    
    E1=(2-3*((np.sin(theta))**2))*Iz[:,i]/(c*R*R)
    E_ind[i]=(1/(2*eps0*math.pi))*it.simps(E1,dx=dz)
    
    E2=(((np.sin(theta))**2)*dIz[:,i])/(c*c*R)       
    E_rad[i]=-(1/(2*eps0*math.pi))*it.simps(E2,dx=dz)
        
    E3=Iz[:,i]*(2-3*((np.sin(theta))**2))/(R**3)
    E_elec[i]=it.simps(E3,dx=dz)
    
#    print(E_elec.shape, i)
   
#    for j in range (0,Nz):
#        for t0 in range (0,tz):
#            E_elec2[j,t0]=(1/(2*eps0*math.pi))*it.simps(E_elec[j,0:t0],dx=dt)
#            E_elec_total[t0]=E_elec2[j,t0]
#    E4=(2-3*((np.sin(theta))**2))/(R**3)
#    E_elec_total[:,i]=(1/(2*eps0*math.pi))*it.simps(E4,dx=dz)*it.simps(E3,dx=dt) 
#        
##        for j in range(0,Nz):
##            print('stuck',i,j)
##            E4=(2-3*((np.sin(theta))**2))/(R*R*R)
##            E_elec_total[j,i]=(1/(2*eps0*math.pi))*it.simps(E4,dx=dz)   
#        
print('Ntz',Ntz)
print('tz',tz.shape)
print('E_ind',E_ind.shape)
print('B_phi',B_phi.shape)

plt.figure(1)
plt.subplot(221)
plt.plot(tz*1e6,B_phi*1e7)
plt.ylabel("Magnetic Flux Amplitude($Wb/m^2$)")
plt.title(r"$B_\Phi*10^7$ at D=%d km"%(D/1000))

plt.subplot(222)
plt.plot(tz*1e6,-E_ind)
plt.ylabel("Induction Component of E-Field ($V/m$)")
plt.title(r"$E_{ind}$ at D=%d km"%(D/1000))

plt.subplot(223)
plt.plot(tz*1e6,-E_rad)
plt.ylabel("Radiation Component of E-Field ($V/m$)")
plt.title(r"$E_{rad}$ at D=%d km"%(D/1000))

plt.subplot(224)
plt.plot(tz*1e6,-E_elec)
plt.ylabel("Electrostatic Component of E-Field ($V/m$)")
plt.title(r"$E_{elec}$ at D=%d km"%(D/1000))
plt.show()

#plt.figure(2)
#plt.subplot(211)
#plt.plot(tz*1e6,B_phi)
#
#plt.subplot(212)
#plt.plot(tz*1e6,-(E_elec+E_rad+E_ind))
plt.show()