def tally(rows):
    from collections import defaultdict

    # Team statistics initialized to 0
    stats = defaultdict(lambda: {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})

    for row in rows:
        if not row.strip():
            continue  # Skip empty lines
        team1, team2, result = row.strip().split(";")

        # Always increment matches played
        stats[team1]["MP"] += 1
        stats[team2]["MP"] += 1

        # Process result
        if result == "win":
            stats[team1]["W"] += 1
            stats[team1]["P"] += 3
            stats[team2]["L"] += 1
        elif result == "loss":
            stats[team2]["W"] += 1
            stats[team2]["P"] += 3
            stats[team1]["L"] += 1
        elif result == "draw":
            stats[team1]["D"] += 1
            stats[team2]["D"] += 1
            stats[team1]["P"] += 1
            stats[team2]["P"] += 1

    # Sort by points descending, then team name ascending
    sorted_teams = sorted(stats.items(), key=lambda x: (-x[1]["P"], x[0]))

    # Header
    lines = ["Team                           | MP |  W |  D |  L |  P"]
    for team, s in sorted_teams:
        lines.append(f"{team:<31}| {s['MP']:>2} | {s['W']:>2} | {s['D']:>2} | {s['L']:>2} | {s['P']:>2}")

    return lines
