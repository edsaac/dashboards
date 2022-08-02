import streamlit as st
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import root
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

## Define the derivative system
def stream(Y,t,p):
    '''
    dY/dt = f(Y,t,p) where Y can have n-dimensions
    but only 2 here to get a phase diagram
    '''
    x,s = Y
    dxdt =  x*s/(p[0]+s) - p[1]*x - p[2]*x
    dsdt =  p[2]*(1-s) - p[3]*x*s/(p[0]+s)
    return [dxdt,dsdt]

def plotStream():

    ## Calculate vector field
    dx,ds = stream([x,s],None,parValues)
    
    ## Calculate trayectories given initial condition
    tray = odeint(stream,list(init.values()),time,args=(parValues,))

    ## Calculate steady-state
    sol = root(stream,[tray[-1,0],tray[-1,1]],args=(None,parValues))
    ssx,sss = sol.x

    kw_streams = {'density':2,'linewidth':1.5,'arrowsize':0.8,
              'arrowstyle':'->','color':'k','minlength':0.1}

    fig,ax = plt.subplots(figsize=[6,6])
    ax.set_aspect("equal")
    ax.streamplot(x,s,dx,ds,**kw_streams,zorder=2)
    ax.plot(tray.T[0],tray.T[1],lw=5,c='purple')
    ax.scatter([0,ssx],[1,sss],s=250,clip_on=False,ec='k',label="Steady-states",zorder=3)
    ax.scatter(tray[0,0],tray[0,1],s=250,marker='X',clip_on=False,ec='k',
               label=r"$(x_0,s_0)$",zorder=4,c='wheat')

    ax.grid(True,ls='dashed',lw=1,c=[0.5,0.5,0.5,0.5])
    ax.set_xlabel("$x$ [-]",)
    ax.set_ylabel("$s$ [-]")
    ax.set(xlim=[0,1],ylim=[0,1])
    ax.legend(loc='upper right',fontsize=10)
    
    return fig

def updatePVector(pars):   
    ndpr[0] = pars['Ks']/pars['S0']
    ndpr[1] = pars['b']/(pars['q'] * pars['Y'])
    ndpr[2] = pars['Q/V']/(pars['q'] * pars['Y'])
    ndpr[3] = 1.0

########################

st.title("Chemostat")
tabList = st.tabs(["Governing eq.", "Non-dimensionalization"])

with tabList[0]:
    st.latex(r'''
        \begin{equation}
            \begin{array}{rcl}
                \dfrac{dX}{dt} &=& Y\hat{q}X\dfrac{S}{K_S + S} - bX - \tfrac{Q}{V}X \\[1em]
                \dfrac{dS}{dt} &=& \tfrac{Q}{V}(S_\infty-S) - \hat{q}X\dfrac{S}{K_S + S}
            \end{array}
        \end{equation}''')

## Math variables
time = np.arange(0,50,0.5)
xlin = np.linspace(-0.1,1.1,61)
slin = np.linspace(-0.1,1.1,61)
x,s  = np.meshgrid(xlin,slin)

## This should be a dataclass
parKeys   = ['Y','q','Ks','b','Q/V','S0']
parLabels = [r'Y', r'\hat{q}', r'K_s', r'b', r'Q/V',    r'S^0']
parValues = [0.42, 10.0 ,20.0 ,0.15, 1000.0/2000.0 ,50.0 ]
parUnits  = ["mg(X)/mg(S)","mg(S)/mg(X)·d","mg(S)/L","1/d","1/d","mg(S)/L"]
parDescr  = ["Microbial yield ",
            "Max growth rate",
            "Half-saturation rate",
            "Die-off rate",
            "Dilution rate",
            "Substrate concentration"]

ndpr = [None] * 4

## Interactives
with st.expander("Modify parameters:",expanded=True):
    
    tabs = st.tabs(parKeys)
    for i,tab in enumerate(tabs):
        with tab:
            cols = st.columns(2)
            with cols[1]:
                parValues[i] = st.number_input(
                    parDescr[i] + " --- " + parUnits[i], 
                    None , None, parValues[i], 0.05,
                    key=f"p_{i}", format="%.2f")
            with cols[0]: st.latex(f"{parLabels[i]}")

    init = {'X':0.5,'S':0.5}

updatePVector({k:v for k,v in zip(parKeys,parValues)})

with st.container():
    st.pyplot(plotStream())
