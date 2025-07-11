# Set an interactive backend
matplotlib.use('TkAgg')

def buffon_matches(L, d):

    num_lines = 6
    num_matches = 1000

    
    # Counters
    matches_crossed = 0
    matches_thrown = 0

    plt.ion()  # Enable interactive mode
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a single figure and axis

    # Generating Lines
    for i in range(num_lines):
        ax.axhline(i * d, color='black', linewidth=1)
    
    # x and y limits of the plot
    ax.set_xlim(0, d * 2)
    ax.set_ylim(-L, (num_lines - 1) * d + L)
    
    # Text box for counters and current pi_estimate
    stats_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, 
                         fontsize=12, verticalalignment='top', 
                         bbox=dict(facecolor='white', alpha=0.8))
    
    # Randomly Generating Position Of Matches(x,y,theta)
    for _ in range(num_matches):
        x = np.random.uniform(0, d * 2)
        y = np.random.uniform(0, (num_lines - 1) * d)
        theta = np.random.uniform(0, 2 * np.pi)

        x1 = x - (L / 2) * np.cos(theta)
        y1 = y - (L / 2) * np.sin(theta)
        x2 = x + (L / 2) * np.cos(theta)
        y2 = y + (L / 2) * np.sin(theta)
        
        # Checking if a matchestick crosses a line
        cross = False
        for i in range(num_lines):
            temp = i * d
            if (y1 < temp < y2) or (y2 < temp < y1):
                cross = True
                break

        color = 'red' if cross else 'blue'
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=1)
        
        matches_thrown += 1
        if cross:
            matches_crossed += 1

        # Estimating pi(pi_estimate) for two cases L<d and L>=d 
        if matches_crossed > 0:
            if L < d:
                pi_estimate = (2 * L * matches_thrown) / (matches_crossed * d)
            else:
                denominator = matches_crossed - matches_thrown
                if denominator != 0:
                    term = (2 / d) * (L - np.sqrt(L ** 2 - d ** 2) - d * np.arcsin(d / L))
                    pi_estimate = (matches_thrown / denominator) * term
                else:
                    pi_estimate = 0
        else:
            pi_estimate = 0

        # Update stats text
        stats_text.set_text(f'Matches thrown: {matches_thrown}\nMatches crossed: {matches_crossed}\nπ estimate: {pi_estimate:.4f}')
        
        # Refresh the plot
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.0001)

    plt.ioff()
    plt.show()
    print(f"Matches thrown: {matches_thrown}, Matches crossed: {matches_crossed}, π estimate: {pi_estimate:.4f}")

buffon_matches(L=2, d=3)
