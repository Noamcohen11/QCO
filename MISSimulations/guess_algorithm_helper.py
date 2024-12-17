import matplotlib.pyplot as plt

def timeEvoPlot(taulist, Omega, Delta):
    plt.figure(figsize=(10, 6))

    # Plotting the time evolution of Ω(t) and Δ(t)
    plt.plot(taulist, Omega(taulist), 
            label='Ω(t)', color='blue', linewidth=2, linestyle='-', marker='o', markersize=5)
    plt.plot(taulist, Delta(taulist), 
            label='Δ(t)', color='red', linewidth=2, linestyle='--', marker='s', markersize=5)

    # Adding enhancements to the plot
    plt.legend(loc='upper right', fontsize=12)
    plt.xlabel('Time (s)', fontsize=14)
    plt.ylabel('Amplitude (MHz)', fontsize=14)
    plt.title('Time Evolution of Rabi Frequency and Detuning', fontsize=16)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add a horizontal line at y=0

    # Show the plot
    plt.tight_layout()
    plt.show()


def plot_setup(ax, x, lst, coeffs, label_prefix):
    """
    Helper function to set up the plot.

    Parameters:
    ax (matplotlib.axes.Axes): The axes to plot on.
    x (array): X positions for the bar graph.
    lst (list): List of state combinations.
    coeffs (list): Coefficients to plot.
    label_prefix (str): Prefix for the legend label.
    """
    ax.bar(x, coeffs, width=0.2, alpha=0.7, label=f'{label_prefix} Probability')
    ax.set_xticks(x)
    ax.set_xticklabels(lst, fontsize=12, rotation=90)
    ax.yaxis.set_tick_params(labelsize=12)  # Set y-tick label size
    ax.set_ylabel('Probability', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(axis='y')  # Enable grid on the y-axis