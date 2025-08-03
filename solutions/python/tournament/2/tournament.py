def tally(rows):
    from collections import defaultdict

    # Structure: team name → [MP, W, D, L, P]
    stats = defaultdict(lambda: [0, 0, 0, 0, 0])

    outcomes = {
        "win":  (1, 3, 0),
        "loss": (0, 0, 1),
        "draw": (0, 1, 0),
    }

    for row in rows:
        if not row.strip():
            continue
        team1, team2, result = row.split(";")

        stats[team1][0] += 1  # MP
        stats[team2][0] += 1

        if result == "win":
            stats[team1][1] += 1  # W
            stats[team1][4] += 3  # P
            stats[team2][3] += 1  # L
        elif result == "loss":
            stats[team2][1] += 1
            stats[team2][4] += 3
            stats[team1][3] += 1
        elif result == "draw":
            stats[team1][2] += 1  # D
            stats[team2][2] += 1
            stats[team1][4] += 1
            stats[team2][4] += 1

    # Sort by points descending, then name
    sorted_teams = sorted(stats.items(), key=lambda t: (-t[1][4], t[0]))

    header = "Team                           | MP |  W |  D |  L |  P"
    lines = [header]
    for team, (mp, w, d, l, p) in sorted_teams:
        lines.append(f"{team:<31}| {mp:>2} | {w:>2} | {d:>2} | {l:>2} | {p:>2}")

    return lines
