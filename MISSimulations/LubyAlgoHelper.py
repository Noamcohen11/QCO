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