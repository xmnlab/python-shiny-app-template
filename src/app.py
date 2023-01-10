from shiny import App, render, ui

import numpy as np
import matplotlib.pyplot as plt



app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.panel_main(
        ui.output_plot("plot"),

    ),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"
        
    @output
    @render.plot(alt="Gráfica")
    def plot():
        ts=[-20, 0 ]
        hs=[23,23]

        t1=np.linspace(0, 20, 50)

        T1=(input.n()-23)*(1-np.exp(-t1/15))+23
        t2=np.linspace(20,60,100)
        T2=(input.n()-23)*(-np.exp(-t2/15)+np.exp(-(t2-20)/15))+23

        ta=[-20, 0,0, 20,20, 60]
        Ta=[23,23,80,80,23,23]

        fig, ax = plt.subplots()
        font = {'family': 'serif',
                'color': '#4a4a4a',
                'weight': 'bold',
                'size': 12,
                }
 
        ax.plot(ts, hs, zorder=3, linewidth=2, color='#1f77b4')
        ax.plot(t1, T1, zorder=3, linewidth=2, color='#1f77b4')
        ax.plot(t2, T2, zorder=3, linewidth=2, color='#1f77b4')
        
        ax.set_xlabel("x", labelpad=10, fontdict=font)
        ax.set_ylabel("y", labelpad=10, fontdict=font)
        
        fig.set_tight_layout(tight=True)
        ax.grid()
        
        fig.set_figwidth(8)
        fig.set_figheight(11)
        ax.set_ylim(0, 85)
        return fig
        
app = App(app_ui, server)




