import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Data from the table
years = [2018, 2022, 2024]
context_windows = [512, 4096, 2000000]
models = ['BERT + GPT-1', 'GPT-3.5 (Original ChatGPT)', 'Gemini 1.5 pro']

# Create figure with transparent background
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_alpha(0)  # Transparent figure background
ax.patch.set_alpha(0)   # Transparent axes background

# Create the line plot with logarithmic y-axis (due to the large range)
ax.semilogy(years, context_windows, marker='o', linestyle='-', linewidth=2.5, markersize=10, color='#eee8d5')

# Add data points with annotations
for i, (year, window, model) in enumerate(zip(years, context_windows, models)):
    ax.annotate(f'{model}\n{window:,} tokens', 
                xy=(year, window),
                xytext=(0, 15), 
                textcoords='offset points',
                ha='center',
                fontsize=9,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.7, edgecolor='none'))

# Add a styled title and labels
ax.set_title('Context Window Size Evolution (2018-2024)', fontsize=14, color='white', fontweight='bold')
ax.set_xlabel('Year', fontsize=12, color='white')
ax.set_ylabel('Context Window Size (tokens)', fontsize=12, color='white')

# Style the y-axis to show values in a more readable format
def format_fn(x, pos):
    if x < 1000:
        return str(int(x))
    elif x < 1000000:
        return f'{int(x/1000)}K'
    else:
        return f'{x/1000000:.1f}M'

ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_fn))

# Style the plot for better aesthetics
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='both', colors='white')

# Set the x-axis ticks to just the years we have data for
ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years])

# Add a grid for better readability (just horizontal lines since we have a logarithmic scale)
ax.grid(axis='y', linestyle='--', alpha=0.7, color='gray')

# Define the text position for growth annotation
text_position = (2021, 100000)

# Highlight the dramatic growth
growth_annotation = ax.annotate(f'3,788× growth\nin just 6 years', 
            xy=text_position,
            xytext=(0, 0),
            textcoords='offset points',
            fontsize=12,
            color='#2aa198',
            fontweight='bold')

# Get the bounding box of the text to position the arrow start
bbox = growth_annotation.get_window_extent(fig.canvas.get_renderer()).transformed(ax.transData.inverted())
text_bottom_center = (bbox.x0 + bbox.width/2, bbox.y0 + 100000)

# Add an arrow starting from the text position to the high point
ax.annotate('', 
            xy=(2024, 1900000),  # arrow end (pointing to the high point)
            xytext=text_bottom_center,  # arrow start (from text)
            arrowprops=dict(facecolor='#2aa198', width=2, headwidth=10, alpha=0.7))

# Save figure with transparent background
plt.tight_layout()
plt.savefig('img/context_window_growth.png', dpi=300, transparent=True) 