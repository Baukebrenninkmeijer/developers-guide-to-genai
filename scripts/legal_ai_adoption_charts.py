#!/usr/bin/env python3
"""
Generate charts visualizing legal AI adoption data using Altair and Plotly.

This script creates three charts:
1. AI Adoption Rates by Firm Size (Altair)
2. AI Adoption by Practice Area - Individual vs. Firm Level (Altair - connected dots)
3. Concerns Slowing AI Adoption (Plotly - bar chart)

The charts use the Solarized color palette for consistent styling with the presentation.
"""

import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import os
from typing import Dict, Any

# Ensure the output directory exists
os.makedirs('img', exist_ok=True)

# Set Altair theme based on Solarized colors
# Colors from styles.scss
COLORS = {
    'base03': '#002b36',  # Dark background
    'base02': '#073642',  # Dark background highlights
    'base01': '#586e75',  # Comments/secondary content
    'base00': '#657b83',  # Body text
    'base0': '#839496',   # Body text
    'base1': '#93a1a1',   # Optional emphasized content
    'base2': '#eee8d5',   # Light background highlights
    'base3': '#fdf6e3',   # Light background
    'yellow': '#b58900',
    'orange': '#cb4b16',
    'red': '#dc322f',
    'magenta': '#d33682',
    'violet': '#6c71c4',
    'blue': '#268bd2',
    'cyan': '#2aa198',
    'green': '#859900'
}

# Create a custom theme using the new API according to the deprecation warning
# Using a simpler approach to avoid type errors
def solarized_theme():
    return {
        'config': {
            'background': COLORS['base03'],
            'title': {'color': COLORS['base2']},
            'axis': {
                'labelColor': COLORS['base2'],
                'titleColor': COLORS['base2'],
                'gridColor': COLORS['base01'],
                'domainColor': COLORS['base01']
            },
            'legend': {
                'labelColor': COLORS['base2'],
                'titleColor': COLORS['base2']
            },
            'text': {'color': COLORS['base2']}
        }
    }

alt.themes.register('solarized', solarized_theme)
alt.themes.enable('solarized')

# =====================================================================
# Chart 1: AI Adoption Rates by Firm Size
# =====================================================================

# Create DataFrame for firm size adoption with more detailed categories
# Use simplified labels (removed "lawyers")
firm_size_data = pd.DataFrame({
    'Firm Size': ['51+', '21-50', '6-20', '2-5', 'Solo'],
    'Adoption Rate': [39, 22, 19, 21, 21]
})

# Add percentage label column
firm_size_data['Percentage Label'] = firm_size_data['Adoption Rate'].astype(str) + '%'

# Sort from largest to smallest firm size
firm_size_data['Firm Size'] = pd.Categorical(
    firm_size_data['Firm Size'], 
    categories=['51+', '21-50', '6-20', '2-5', 'Solo']
)
firm_size_data = firm_size_data.sort_values('Firm Size', ascending=False)

# Create a color gradient for the bars, going from dark blue to cyan
color_scale = alt.Scale(
    domain=firm_size_data['Firm Size'].tolist(),
    range=[COLORS['blue'], '#1a9dba', COLORS['cyan'], '#7ecac0', '#afdecb']
)

chart1 = alt.Chart(firm_size_data).mark_bar().encode(
    x=alt.X('Firm Size:N', 
            title=None, 
            sort=None,  # Use the order from the dataframe
            axis=alt.Axis(
                labelAngle=0,  # Rotate labels 0 degrees
                labelFontSize=15  # Increase label font size by 50%
            )),
    y=alt.Y('Adoption Rate:Q', title='Adoption Rate (%)', scale=alt.Scale(domain=[0, 50])),
    color=alt.Color('Firm Size:N', scale=color_scale, legend=None),
    tooltip=['Firm Size', 'Adoption Rate']
).properties(
    title='AI Adoption Rates by Firm Size',
    width=600,
    height=350
)

# Add text labels on top of bars
text1 = chart1.mark_text(
    align='center',
    baseline='bottom',
    dy=-10,
    fontSize=21,  # Increase text size by 50% (from 14 to 21)
    color=COLORS['base3']
).encode(
    text='Percentage Label:N'
)

chart1_final = (chart1 + text1).configure_title(
    fontSize=20,
    fontWeight='bold',
    color=COLORS['base2'],
    anchor='middle'
)

# Save chart
chart1_final.save('img/legal_ai_adoption_by_firm_size.html')

# =====================================================================
# Chart 2: AI Adoption by Practice Area - Individual vs. Firm Level
# =====================================================================

# Create DataFrame for practice area adoption
practice_area_data = pd.DataFrame({
    'Practice Area': ['Immigration', 'Personal Injury', 'Civil Litigation', 
                     'Criminal Law', 'Family Law', 'Trusts and Estates'],
    'Individual Practitioners': [47, 37, 36, 28, 26, 25],
    'Firm Level': [17, 20, 27, 18, 20, 18]
})

# Reshape data for Altair
practice_area_melted = pd.melt(
    practice_area_data, 
    id_vars=['Practice Area'],
    value_vars=['Individual Practitioners', 'Firm Level'],
    var_name='Adoption Type',
    value_name='Adoption Rate'
)

# Sort practice areas by individual adoption rate
sorted_areas = practice_area_data.sort_values('Individual Practitioners', ascending=False)['Practice Area'].tolist()
practice_area_melted['Practice Area'] = pd.Categorical(
    practice_area_melted['Practice Area'], 
    categories=sorted_areas
)

# Create a connected dot plot instead of a bar chart
# First create the points
points = alt.Chart(practice_area_melted).mark_circle(size=100).encode(
    x=alt.X('Practice Area:N', title=None, sort=sorted_areas),
    y=alt.Y('Adoption Rate:Q', title='Adoption Rate (%)', scale=alt.Scale(domain=[0, 50])),
    color=alt.Color('Adoption Type:N', 
                   scale=alt.Scale(domain=['Individual Practitioners', 'Firm Level'],
                                 range=[COLORS['yellow'], COLORS['orange']]),
                   legend=alt.Legend(title="Adoption Level")),
    tooltip=['Practice Area', 'Adoption Type', 'Adoption Rate']
)

# Create lines to connect the dots for the same practice area
lines = alt.Chart(practice_area_data).transform_fold(
    ['Individual Practitioners', 'Firm Level'],
    as_=['Adoption Type', 'Adoption Rate']
).mark_line(color=COLORS['base01'], strokeDash=[3, 3]).encode(
    x=alt.X('Practice Area:N', sort=sorted_areas),
    y=alt.Y('Adoption Rate:Q'),
    detail='Practice Area:N'
)

# Add text labels for the points
text2 = points.mark_text(
    align='center',
    baseline='bottom',
    dy=-10,
    fontSize=11,
    color=COLORS['base3']
).encode(
    text=alt.Text('Adoption Rate:Q', format='.0f')
)

chart2 = (lines + points + text2).properties(
    title='AI Adoption by Practice Area: Individual vs. Firm Level',
    width=600,
    height=350
)

chart2_final = chart2.configure_title(
    fontSize=20,
    fontWeight='bold',
    color=COLORS['base2'],
    anchor='middle'
)

# Save chart
chart2_final.save('img/legal_ai_adoption_by_practice_area.html')

# =====================================================================
# Chart 3: Concerns Slowing AI Adoption - Plotly Bar Chart
# =====================================================================

# Create DataFrame for concerns
concerns_data = pd.DataFrame({
    'Concern': [
        'Lack of trust in results', 
        'Ethical issues', 
        'Desire for AI to mature', 
        'Privilege issues',
        'Cost concerns'
    ],
    'Percentage': [42, 42, 41, 36, 22],
    'Category': [
        'Trust', 
        'Ethical', 
        'Maturity', 
        'Legal', 
        'Financial'
    ]
})

# Sort concerns by percentage (descending)
concerns_data = concerns_data.sort_values('Percentage', ascending=False).reset_index(drop=True)

# Color mapping for categories
category_colors = {
    'Trust': COLORS['red'],
    'Ethical': COLORS['magenta'],
    'Maturity': COLORS['violet'],
    'Legal': COLORS['blue'],
    'Financial': COLORS['cyan']
}

# Create a horizontal bar chart using Plotly Graph Objects for more control
fig = go.Figure()

# Add each bar with explicit color based on its category
for i, row in concerns_data.iterrows():
    fig.add_trace(go.Bar(
        y=[row['Concern']],  # Must be a list for a single point
        x=[row['Percentage']],
        orientation='h',
        name=row['Category'],
        showlegend=False,
        marker_color=category_colors[row['Category']],
        text=f"{row['Percentage']}%",
        textposition='outside',
        hovertemplate=f"<b>{row['Concern']}</b><br>Percentage: {row['Percentage']}%<extra></extra>"
    ))

# Update the layout to match the Solarized theme
fig.update_layout(
    paper_bgcolor=COLORS['base03'],
    plot_bgcolor=COLORS['base03'],
    font_color=COLORS['base2'],
    title={
        'text': 'Concerns Slowing AI Adoption in Legal Practices',
        'font': {'size': 20},
        'x': 0.5  # Center the title
    },
    yaxis_title=None,
    xaxis_title='Percentage (%)',
    xaxis=dict(
        gridcolor=COLORS['base01'],
        range=[0, 50]  # Set x-axis range to 0-50 for consistency
    ),
    yaxis=dict(
        gridcolor=COLORS['base01']
    ),
    margin=dict(l=200, r=100, t=80, b=50),  # Add margin for long concern names
    barmode='group',
    height=500,
    width=800
)

# Save the chart
fig.write_html('img/legal_ai_adoption_concerns.html')

print("Charts generated and saved to the 'img' directory.")