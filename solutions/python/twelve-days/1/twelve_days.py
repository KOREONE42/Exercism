def recite(start_verse, end_verse):
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]

    verses = []
    for day in range(start_verse, end_verse + 1):
        verse = f"On the {ordinals[day - 1]} day of Christmas my true love gave to me: "
        day_gifts = []

        for i in range(day - 1, -1, -1):
            gift = gifts[i]
            if i == 0 and day != 1:
                gift = "and " + gift
            day_gifts.append(gift)

        verse += ", ".join(day_gifts)
        verses.append(verse)

    return verses