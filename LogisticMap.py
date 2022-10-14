import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image


#### SEE: https://www.johndcook.com/blog/2020/01/19/cobweb-plots/
#### Plota o diagrama "cobweb"
# f = função
# x0 = ponto inicial
# N = núm. de iterações
def cobweb(f, x0, N, a=0, b=1):
        # plot the function being iterated
        t = np.linspace(a, b, 200)
        fig = plt.figure(figsize=(4,4))
        X=[]
        X.append(x0)
        #
        plt.axes().set_aspect(1)
        plt.plot(t, f(t), 'k')
        # plot the dotted line y = x
        plt.plot(t, t, "k:")
        # plot the INITIAL point (x0, f(x0)) => black
        plt.plot(x0, 0, 'k.')
        plt.plot( [x0,x0],[0,f(x0)], 'g')
        # plot the iterates
        x, y = x0, f(x0)
        for _ in range(N):
            fy = f(y)
            X.append(fy)
            plt.plot([x, y], [y,  y], 'g', linewidth=1)
            plt.plot([y, y], [y, fy], 'g', linewidth=1)
            x, y = y, fy
        plt.xlabel(r'$x_n$')
        plt.ylabel(r'$x_{n+1}$')
        plt.tight_layout()
        fig.savefig("figure1.png")
        image = Image.open('figure1.png')
        st.image(image)
        #st.pyplot(plt)
        return X

# Plota a Evolução temporal:
def Evolucao(X):
    n = len(X)
    T = np.arange(n)
    ini = 0 if n<=90 else -90
    ymin, ymax = np.min(X[ini:])-0.2, np.max(X[ini:])+0.2
    ymin = 0 if ymin<0 else ymin
    ymax = 1 if ymax>1 else ymax
    fig2 = plt.figure(figsize=(5,4))
    plt.plot(T[ini:], X[ini:], 'k.-')
    plt.xlabel(r'$n$')
    plt.ylabel(r'$x_n$')
    plt.ylim(ymin,ymax)
    plt.tight_layout()
    fig2.savefig("figure2.png")
    image2 = Image.open('figure2.png')
    st.image(image2)    

################################    
# Função principal da aplicação
def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(page_title = 'Mapa Logístico', \
        layout="wide",
        initial_sidebar_state='expanded'
    )
    # Na barra lateral:
    st.sidebar.write('## Mapa Logístico : ')
    st.sidebar.latex(r''' x_{n+1} = r . x_n . (1-x_n) ''')
    st.sidebar.markdown("---")
    #
    st.sidebar.markdown("## Controles:")
    r  = st.sidebar.slider('Valor de r :', min_value=0.0, max_value=4.0, step=0.001, value=3.8)
    x0 = st.sidebar.slider('Valor de x0 :', min_value=0.0, max_value=0.999, step=0.001, value=0.25)
    N = st.sidebar.slider('Núm. máximo de iterações :', min_value=5, max_value=2000, step=1, value=90)
    #
    # Colunas:
    col1, col2, col3 = st.columns([4,1,4])
    
    with col1:
        st.write('#### Mapa de 1o. retorno:')
        X = cobweb( lambda x: r * x * (1 - x) , x0, N)
    
    with col2:
        st.write(" . ")
        st.write(" . ")
        st.write("Valores:")
        st.write("     r = ", r)
        st.write("    x0 = ", x0)
    
    with col3:
        st.write("#### Evolução temporal:")
        Evolucao(X)
    
##########################################################
if __name__ == '__main__':
	main()
