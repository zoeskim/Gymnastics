""" Functions to construct all data visualizations. These include All-Around, individual event, and team highest scoring data. """
import math
from os import path
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
import numpy as np
import plotly.graph_objects as go
from gym.gym import import_data, get_duplicates_for_top_team_table, flatten


# import dictionary mapping athletes to colors
_, name_color, _ = import_data(return_dicts=True)


def patch_hatch(h):
    """ Create patch filled with given hatch pattern for legends. """
    return mpatches.Patch(hatch=h, edgecolor='black', facecolor='white')


def patch_color(c):
    """ Create patch filled with given color for legends. """
    return mpatches.Patch(color=c)


def athlete_legend(colors, names):
    """ Create a standalone legend for the univeral athlete color-coding. """
    _, ax = plt.subplots()
    handles = [patch_color(colors[i]) for i in range(len(colors))]
    legend = plt.legend(handles, names, title='Athlete Color Dictionary', ncol=4, fontsize=20, loc=8, bbox_to_anchor=[-0.3,-0.1], frameon=False)
    legend.get_title().set_position((-10, 40))
    legend.get_title().set_size(25)
    ax.axis('off')

    # save if not already generated/to regenerate
    if not path.exists(r'./gym/figures/Athlete Legend'):
        plt.savefig(r'./gym/figures/Athlete Legend')


def AA_slope_plot(names, colors, AA_day1, AA_day2, n=10):
    """ Create slope plot of top n top average all-arounders to show trends in performance across the days. """
    fig, ax = plt.subplots()

    # loop through top n all around athletes
    for i, name in enumerate(names[:n]):
        # plot points with scores on day 1 and day 2, slope between points
        plt.plot([0, 1], [AA_day1[i], AA_day2[i]], label=name, c=colors[i], marker='o', markersize=5)
    fig.legend(loc='right', bbox_to_anchor=(0.75, 0.25, 0.5, 0.5))
    ax.set_title(f'Top {n} (Average) AAers Day-by-Day Score Breakdown')
    ax.set_xticks([0,1])
    ax.set_xticklabels(['Day 1', 'Day 2'])

    # save if not already generated/to regenerate
    if not path.exists(f'./gym/figures/AA/Top {n} Average AA Performances Across Days'):
        plt.savefig(f'./gym/figures/AA/Top {n} Average AA Performances Across Days')


def AA_avg_bar_chart(AA, n=10):
    """ Create bar plot of the top n average All Around scores,
    color-coded by universal athlete colors and hatch-coded by event."""
    _, ax = plt.subplots(figsize=(10,10))
    # create temporary dataframe of top n entries sorted by average AA performance
    sort_AA = AA.sort_values(by='AA_avg', ascending=False)[:n]

    # create stacked bar chart with hatches differentiating event
    ax.bar(range(n), sort_AA['Vault_avg'], edgecolor='black', hatch='/', color=sort_AA['Color'].values)
    ax.bar(range(n), sort_AA['Bars_avg'], bottom=sort_AA['Vault_avg'], edgecolor='black', hatch='o', color=sort_AA['Color'].values)
    ax.bar(range(n), sort_AA['Beam_avg'], bottom=(sort_AA['Vault_avg']+sort_AA['Bars_avg']), edgecolor='black', hatch='+', color=sort_AA['Color'].values)
    ax.bar(range(n), sort_AA['Floor_avg'], bottom=(sort_AA['Vault_avg']+sort_AA['Bars_avg']+sort_AA['Beam_avg']), edgecolor='black', hatch='*', color=sort_AA['Color'].values)
    # set chart features (labels, title)
    ax.set_xticks(range(n))
    ax.set_xticklabels(sort_AA['Name'].values, rotation=90)
    ax.set_title(f'Top {n} Average AA Performances')
    # create data labels for the bars (top score or distance from top score)
    ax.bar_label(ax.containers[-1], fmt=lambda x: '{:.3f}'.format(x if x == round(AA['AA_avg'].max(), 3) else x-AA['AA_avg'].max()))

    # create legend
    hatch = ['/', 'o', '+', '*']
    handles = [patch_hatch(hatch[i]) for i in range(len(hatch))]
    ax.legend(handles=handles, labels=['Vault', 'Bars', 'Beam', 'Floor'], fontsize='25', loc='right', bbox_to_anchor=[1.35,0.4])

    # save if not already generated/to regenerate
    if not path.exists(f'./gym/figures/AA/Top {n} Average AA Performances'):
        plt.savefig(f'./gym/figures/AA/Top {n} Average AA Performances')


def AA_by_day_bar_chart(AA, n=10):
    """ Create bar plots of the top n All Arounders for each night of competition,
    color-coded by universal athlete colors and hatch-coded by event."""
    fig = plt.figure(figsize=(20, 10))
    # create gridspec to make two larger columns for plots, one smaller for legend
    gs = fig.add_gridspec(nrows=1, ncols=3, width_ratios=[3, 3, 1])

    # loop across both days
    for i in range(2):
        # create temporary dataframe OF top n entries sorted by that day's AA performance
        sort_AA = AA.sort_values(by=f'AA_day{i+1}', ascending=False)[:n]

        # create stacked bar chart with hatches differentiating event
        ax = fig.add_subplot(gs[:, i]) # set axis
        ax.bar(range(n), sort_AA[f'Vault_day{i+1}'], edgecolor='black', hatch='/', color=sort_AA['Color'].values)
        ax.bar(range(n), sort_AA[f'Bars_day{i+1}'], bottom=sort_AA[f'Vault_day{i+1}'], edgecolor='black', hatch='o', color=sort_AA['Color'].values)
        ax.bar(range(n), sort_AA[f'Beam_day{i+1}'], bottom=(sort_AA[f'Vault_day{i+1}']+sort_AA[f'Bars_day{i+1}']), edgecolor='black', hatch='+', color=sort_AA['Color'].values)
        ax.bar(range(n), sort_AA[f'Floor_day{i+1}'], bottom=(sort_AA[f'Vault_day{i+1}']+sort_AA[f'Bars_day{i+1}']+sort_AA[f'Beam_day{i+1}']), edgecolor='black', hatch='*', color=sort_AA['Color'].values)
        # set chart features (labels, title)
        ax.set_xticks(range(n))
        ax.set_xticklabels(sort_AA['Name'].values, rotation=90)
        ax.set_title(f'Day {i+1}: Top {n} AA Performances')
        # create data labels for the bars (top score or distance from top score)
        ax.bar_label(ax.containers[-1], fmt=lambda x: '{:.3f}'.format(x if x == AA[f'AA_day{i+1}'].max() else x-AA[f'AA_day{i+1}'].max()))

    # create legend
    ax = fig.add_subplot(gs[-1, -1]) # set axis
    hatch = ['/', 'o', '+', '*']
    handles = [patch_hatch(hatch[i]) for i in range(len(hatch))]
    ax.legend(handles=handles, labels=['Vault', 'Bars', 'Beam', 'Floor'], fontsize='25', loc='center', bbox_to_anchor=[0.3,0.5])
    ax.axis('off')

    # save if not already generated/to regenerate
    if not path.exists(f'./gym/figures/AA/Top {n} AA Performances by Day'):
        plt.savefig(f'./gym/figures/AA/Top {n} AA Performances by Day')


def event_by_day_bar_chart(AA, event, n=10):
    """ Create bar plots of the top n event scores for each night of competition,
    color-coded by universal athlete colors."""
    _, ax = plt.subplots(1,2,figsize=(20, 10))

    # loop across both days
    for i in range(2):
        event_day = f'{event}_day{i+1}'
        # create bar chart of top n event scores coded by athlete color
        bar_container = ax[i].bar(range(n), height=AA.sort_values(by=event_day, ascending=False)[event_day][:n].values, color=AA.sort_values(by=event_day, ascending=False)['Color'][:n].values, edgecolor='black')
        # create data labels for the bars (top score or distance from top score)
        ax[i].bar_label(bar_container, fmt=lambda x: '{:.3f}'.format(x if x == AA[event_day].max() else x-AA[event_day].max()))
        # set chart features (labels, title)
        ax[i].set_xticks(range(n))
        ax[i].set_xticklabels(AA.sort_values(by=event_day, ascending=False)['Name'][:n].values, rotation=90)
        ax[i].set_title(f'Day {i+1}: Top {n} {event} Performances')
        ax[i].set_ylim([12,16])

    # save if not already generated/to regenerate
    if not path.exists(f'./gym/figures/{event}/Top {n} {event} Performances Across Days'):
        plt.savefig(f'./gym/figures/{event}/Top {n} {event} Performances Across Days')


def event_avg_bar_chart(AA, event, n=10):
    """ Create bar plot of the top n average event scores,
    color-coded by universal athlete colors. """
    _, ax = plt.subplots(figsize=(8, 6))
    # create temporary dataframe of top n average event scores
    event_by_average = AA.sort_values(by=f'{event}_avg', ascending=False)[:n]

    # create bar chart of top n event scores coded by athlete color
    ax.bar(range(n), height=event_by_average[f'{event}_avg'].values, color=event_by_average['Color'].values, edgecolor='black')

    # create error bars displaying minimum and maximum scores
    for i, p in enumerate(ax.patches):
        x = p.get_x()  # get the bottom left x corner of the bar
        w = p.get_width()  # get width of bar
        min_y = event_by_average[[f'{event}_day1', f'{event}_day2']].iloc[i].min()
        max_y = event_by_average[[f'{event}_day1', f'{event}_day2']].iloc[i].max()
        plt.vlines(x+w/2, min_y, max_y, color='k')

    # set chart features (axes, labels, title)
    ax.set_xticks(range(n))
    ax.set_xticklabels(event_by_average['Name'].values, rotation=90)
    ax.set_title(f'Top {n} Average {event} Performances')
    ax.set_ylim([12,16])

    # save if not already generated/to regenerate
    if not path.exists(f'./gym/figures/{event}/Top {n} Average {event} Performances'):
        plt.savefig(f'./gym/figures/{event}/Top {n} Average {event} Performances')

def team_scores_bar_chart(team_data, occ, n=10):
    """ Create bar plot of the top n team scores of all possible team iterations for occasion specified,
    color-coded by universal athlete colors and hatch-coded by event. """
    fig, axs = plt.subplots(figsize=(20, 10), nrows=1, ncols=2, width_ratios=[3,1])

    team_data.set_index('Team ID', inplace=True)
    # calculate team score for each team and add to df
    team_data['Team Score'] = np.repeat(team_data.groupby(team_data.index)['Score'].sum().values, 12)
    max_score = team_data['Team Score'].max()
    # sort values by descending team score while preserving index
    team_data = team_data.sort_values(by = ['Team Score', 'Team ID'], ascending = [False, True])
    # get team ID's ordered by score
    ordered_team_ids = team_data.groupby('Team ID')['Score'].sum().sort_values(ascending=False).index.values
    top_team_ids = ordered_team_ids[:n]
    # keep only top scoring teams to reduce computation time
    team_data = team_data.loc[top_team_ids]

    # create stacked bar chart with total team scores (colors differentiating athletes, hatches differentiating events)
    height = np.zeros(n)
    hatch = ['/', 'o', '+', '*']
    ax = fig.add_subplot(axs[0])
    # iterate through each event
    for i, event in enumerate(['Vault', 'Bars', 'Beam', 'Floor']):
      # iterate through top 3 scoring athletes on given team and event
        for ii in range(1,4):
            x_up = team_data[(team_data['Event'] == event) & (team_data['Score_Rank'] == ii)]
            athletes = x_up['Name']
            # check color dictionary to get colors to color code by athlete
            colors = []
            for _, athlete in enumerate(athletes):
                colors.append(name_color[athlete])
            ax.bar(range(n), height=x_up['Score'].values, bottom=height, hatch=hatch[i], color=colors, edgecolor='black')
            height = np.add(height, x_up['Score'].values)

    # set chart features (data labels, tick leabels, title)
    ax.bar_label(ax.containers[-1], fmt=lambda x: '{:.2f}'.format(x if round(x,3) == max_score else x-max_score), fontsize=15)
    ax.set_xticks(range(n), labels=top_team_ids)
    ax.set_xticklabels(top_team_ids)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(f'{occ} Highest Scoring Teams', fontsize=20)

    # create legend with athlete colors and event hatches
    ax = fig.add_subplot(axs[1]) # set axis
    athletes = team_data['Name'].unique()
    unique_colors = [name_color[athlete] for athlete in athletes]
    handles = [patch_hatch(hatch[i]) for i in range(len(hatch))] + [patch_color(unique_colors[i]) for i in range(len(unique_colors))]
    labels = ['Vault', 'Bars', 'Beam', 'Floor'] + team_data['Name'].unique().tolist()
    ax.legend(handles=handles, labels=labels, fontsize='25', loc='center', bbox_to_anchor=[0.3,0.5], frameon=False)
    plt.axis('off')

    # save if not already generated/to regenerate
    if not path.exists(f'./gym/figures/Team/{occ} Top {n} Team Scores'):
        plt.savefig(f'./gym/figures/Team/{occ} Top {n} Team Scores')

    return top_team_ids


def build_top_team_table(top_team_ids, removed_teams, team_df, occ, annotations_y=0):
    """ Build a table of Team IDs with corresponding athlete names to accompany team scores bar chart. """
    # get exceptions to note (cases where one team member could be swapped for other athletes)
    duplicate_team_ids, team_constants, team_variables = get_duplicates_for_top_team_table(top_team_ids, removed_teams, team_df)
    # create option for annotations to note exceptions
    flags = ['*', '**', '***', '****']
    annotations = ''
    chart = team_df[team_df['Team ID'].isin(top_team_ids)].set_index('Team ID').copy()
    # loop through exceptions and note all athletes who could be substituted for the same team score
    if duplicate_team_ids:
        annotations += 'Could be any of: <br>'
        for i, team_id in enumerate(duplicate_team_ids):
            name_test = flatten(chart[~chart.isin(team_constants[i])].loc[team_id].drop('Team Score', axis=1).values)
            variable_name = [ele for ele in name_test if str(ele) != 'nan']
            variable_column = chart.loc[team_id].columns[chart.isin(variable_name).any()].values
            chart.at[team_id[0], f'{variable_column[0]}'] = variable_name[0] + flags[i]
            annotations += f'{flags[i]} '
            # start new line every 7 athletes
            for ii in range(math.floor(len(team_variables[i]) / 7)):
                annotations += ', '.join(team_variables[i][ii*7:ii*7+7])
                annotations += ', <br>'
            annotations += ', '.join(team_variables[i][ii*7+7:]) + '<br>'
    chart.reset_index(inplace=True)

    # create table
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(chart.columns), line_color='white', fill_color='black', font=dict(color='white', size=16), height=40), 
    cells=dict(values=chart.transpose().values.tolist(), line_color='black',  fill_color='white', font_size=14, height=30))],
    layout=go.Layout(height=825, 
                     annotations=[go.layout.Annotation(showarrow=False, text=annotations, font_size=14, align='left', xanchor='left', x=0, yanchor='bottom', y=annotations_y)]))

    # save if not already generated/to regenerate
    n = len(top_team_ids)
    if not path.exists(f'./gym/figures/Team/{occ} Top {n} Team Members'):
        fig.write_image(f'./gym/figures/Team/{occ} Top {n} Team Members.png')

    fig.show()
