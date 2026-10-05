# Project 14: AI in Sports

title = "AI in Sports"

# 1. DATA
players = {
    "Virat": [82, 45, 96, 71],
    "Rohit": [65, 88, 72, 91],
    "Rahul": [55, 76, 68, 84],
    "Surya": [91, 63, 79, 86],
    "Hardik": [48, 70, 81, 60]
}

# 2. FUNCTION to calculate player statistics
def player_stats(scores):
    total = sum(scores)
    average = total / len(scores)
    best = max(scores)

    return total, average, best


# 3. Find Player of the Series
totals = {}

for player, scores in players.items():
    total, average, best = player_stats(scores)
    totals[player] = total

player_of_series = max(totals, key=totals.get)

# 4. Create leaderboard rows
rows = ""

for player, scores in players.items():
    total, average, best = player_stats(scores)

    if player == player_of_series:
        highlight = "winner"
    else:
        highlight = ""

    rows += f"""
    <tr class="{highlight}">
        <td>{player}</td>
        <td>{scores[0]}</td>
        <td>{scores[1]}</td>
        <td>{scores[2]}</td>
        <td>{scores[3]}</td>
        <td>{total}</td>
        <td>{average:.2f}</td>
        <td>{best}</td>
    </tr>
    """

# 5. HTML TEMPLATE
html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>

    <style>
        body {{
            font-family: Arial;
            margin: 40px;
            background: #f4f8fb;
        }}

        h1 {{
            color: #1F3A5F;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
        }}

        th, td {{
            padding: 12px;
            border: 1px solid #ddd;
            text-align: center;
        }}

        th {{
            background: #2A9D8F;
            color: white;
        }}

        .winner {{
            background: #fff3b0;
            font-weight: bold;
        }}

        .note {{
            margin-top: 20px;
            padding: 15px;
            background: white;
            border-left: 5px solid #2A9D8F;
        }}
    </style>
</head>

<body>

    <h1>{title}</h1>

    <h2>Player of the Series: {player_of_series}</h2>

    <table>
        <tr>
            <th>Player</th>
            <th>Match 1</th>
            <th>Match 2</th>
            <th>Match 3</th>
            <th>Match 4</th>
            <th>Total</th>
            <th>Average</th>
            <th>Best Match</th>
        </tr>

        {rows}

    </table>

    <div class="note">
        <b>AI in Performance Analytics:</b>
        AI can analyse player performance, identify patterns,
        monitor workload and help teams develop better match strategies.
    </div>

</body>
</html>"""

# 6. SAVE FILE
with open("index.html", "w") as f:
    f.write(html)

print("Webpage created: index.html")
