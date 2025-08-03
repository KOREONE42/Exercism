class BowlingGame:
    """
    Class to keep track of a bowling game and compute the final score.
    """
    def __init__(self):
        self.frames = []
        self.done = False

    def roll(self, pins: int):
        if pins < 0 or pins > 10:
            raise ValueError("pins must have value between 0 and 10")
        if self.done:
            raise Exception("cannot roll after game is complete")

        num_frames = len(self.frames)

        # Frames 1-9 (first roll or second roll)
        if num_frames < 9:
            # Starting new frame
            if not self.frames or len(self.frames[-1]) == 2 or self.frames[-1][0] == 10:
                if pins == 10:
                    self.frames.append([10])
                else:
                    self.frames.append([pins])
            else:
                # Second roll of current frame
                first = self.frames[-1][0]
                if first + pins > 10:
                    raise ValueError("two rolls in a frame cannot score more than 10 points")
                self.frames[-1].append(pins)

        # Second roll of the 9th frame (when 9th first roll was not a strike)
        elif num_frames == 9 and len(self.frames[-1]) == 1 and self.frames[-1][0] != 10:
            first = self.frames[-1][0]
            if first + pins > 10:
                raise ValueError("two rolls in a frame cannot score more than 10 points")
            self.frames[-1].append(pins)

        # Tenth frame, first roll (after completing 9 frames)
        elif num_frames == 9:
            self.frames.append([pins])

        # Tenth frame, second or bonus rolls
        elif num_frames == 10:
            tenth = self.frames[9]
            # Second roll
            if len(tenth) == 1:
                first = tenth[0]
                if first != 10 and first + pins > 10:
                    raise ValueError("two rolls in a frame cannot score more than 10 points")
                tenth.append(pins)
                if first != 10 and first + pins < 10:
                    self.done = True
            # Bonus roll
            elif len(tenth) == 2:
                first, second = tenth
                if first == 10 or first + second == 10:
                    if first == 10:
                        max_pins = 10 if second == 10 else 10 - second
                    else:
                        max_pins = 10
                    if pins < 0 or pins > max_pins:
                        raise ValueError("invalid fill ball")
                    tenth.append(pins)
                    self.done = True
                else:
                    raise IndexError("cannot throw bonus with an open tenth frame")
            else:
                raise Exception("cannot roll after game is complete")
        else:
            raise Exception("cannot roll after game is complete")

    def score(self) -> int:
        if len(self.frames) < 10 or not self.done:
            raise Exception("cannot score until the end of the game")
        total = 0
        def next_rolls(idx, count):
            rolls = []
            for frame in self.frames[idx+1:]:
                for p in frame:
                    rolls.append(p)
                    if len(rolls) == count:
                        return rolls
            return rolls
        # Score frames 1-9
        for i in range(9):
            frame = self.frames[i]
            if frame[0] == 10:  # strike
                bonus = next_rolls(i, 2)
                if len(bonus) < 2:
                    raise Exception("insufficient bonus rolls for strike")
                total += 10 + sum(bonus)
            elif sum(frame) == 10:  # spare
                bonus = next_rolls(i, 1)
                if len(bonus) < 1:
                    raise Exception("insufficient bonus roll for spare")
                total += 10 + bonus[0]
            else:  # open frame
                total += sum(frame)
        # Tenth frame
        total += sum(self.frames[9])
        return total
