#!/usr/bin/env python3
"""
Generate charts visualizing legal AI adoption data using Altair.

This script creates three charts:
1. AI Adoption Rates by Firm Size
2. AI Adoption by Practice Area - Individual vs. Firm Level
3. Concerns Slowing AI Adoption

The charts use the Solarized color palette for consistent styling with the presentation.
"""

import pandas as pd
import altair as alt
import os

# Ensure the output directory exists
os.makedirs('../img', exist_ok=True)

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

# Create a custom theme
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

# Register the theme
alt.themes.register('solarized', solarized_theme)
alt.themes.enable('solarized')

# =====================================================================
# Chart 1: AI Adoption Rates by Firm Size
# =====================================================================

# Create DataFrame for firm size adoption
firm_size_data = pd.DataFrame({
    'Firm Size': ['51+ Lawyers', '50 or Fewer Lawyers'],
    'Adoption Rate': [39, 20]
})

chart1 = alt.Chart(firm_size_data).mark_bar().encode(
    x=alt.X('Firm Size:N', title=None),
    y=alt.Y('Adoption Rate:Q', title='Adoption Rate (%)', scale=alt.Scale(domain=[0, 50])),
    color=alt.Color('Firm Size:N', scale=alt.Scale(range=[COLORS['blue'], COLORS['cyan']]), legend=None),
    tooltip=['Firm Size', 'Adoption Rate']
).properties(
    title='AI Adoption Rates by Firm Size',
    width=500,
    height=350
)

# Add text labels on top of bars
text1 = chart1.mark_text(
    align='center',
    baseline='bottom',
    dy=-10,
    fontSize=14,
    color=COLORS['base3']
).encode(
    text=alt.Text('Adoption Rate:Q', format='.0f')
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

chart2 = alt.Chart(practice_area_melted).mark_bar().encode(
    x=alt.X('Practice Area:N', title=None, sort=sorted_areas),
    y=alt.Y('Adoption Rate:Q', title='Adoption Rate (%)', scale=alt.Scale(domain=[0, 50])),
    color=alt.Color('Adoption Type:N', 
                   scale=alt.Scale(domain=['Individual Practitioners', 'Firm Level'],
                                 range=[COLORS['yellow'], COLORS['orange']]),
                   legend=alt.Legend(title="Adoption Level")),
    tooltip=['Practice Area', 'Adoption Type', 'Adoption Rate']
).properties(
    title='AI Adoption by Practice Area: Individual vs. Firm Level',
    width=600,
    height=350
)

# Add text labels on top of bars
text2 = chart2.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontSize=11,
    color=COLORS['base3']
).encode(
    text=alt.Text('Adoption Rate:Q', format='.0f')
)

chart2_final = (chart2 + text2).configure_title(
    fontSize=20,
    fontWeight='bold',
    color=COLORS['base2'],
    anchor='middle'
)

# Save chart
chart2_final.save('img/legal_ai_adoption_by_practice_area.html')

# =====================================================================
# Chart 3: Concerns Slowing AI Adoption
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
concerns_data = concerns_data.sort_values('Percentage', ascending=True)

# Color mapping for categories
category_colors = {
    'Trust': COLORS['red'],
    'Ethical': COLORS['magenta'],
    'Maturity': COLORS['violet'],
    'Legal': COLORS['blue'],
    'Financial': COLORS['cyan']
}

# Create a horizontal bar chart
chart3 = alt.Chart(concerns_data).mark_bar().encode(
    y=alt.Y('Concern:N', title=None, sort='-x'),
    x=alt.X('Percentage:Q', title='Percentage (%)', scale=alt.Scale(domain=[0, 50])),
    color=alt.Color('Category:N', 
                   scale=alt.Scale(domain=list(category_colors.keys()),
                                 range=list(category_colors.values())),
                   legend=alt.Legend(title="Concern Category")),
    tooltip=['Concern', 'Percentage', 'Category']
).properties(
    title='Concerns Slowing AI Adoption in Legal Practices',
    width=600,
    height=300
)

# Add text labels at the end of bars
text3 = chart3.mark_text(
    align='left',
    baseline='middle',
    dx=3,
    fontSize=12,
    color=COLORS['base3']
).encode(
    text=alt.Text('Percentage:Q', format='.0f')
)

chart3_final = (chart3 + text3).configure_title(
    fontSize=20,
    fontWeight='bold',
    color=COLORS['base2'],
    anchor='middle'
)

# Save chart
chart3_final.save('img/legal_ai_adoption_concerns.html')

print("Charts generated and saved to the 'img' directory.")