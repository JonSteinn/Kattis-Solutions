jumps = [2, 4, 5, 7, 9, 11, 12]
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
scales = {notes[i]: {notes[(i + j) % len(notes)] for j in jumps} for i in range(len(notes))}
input()  # dump
_set = set(input().split())
out = " ".join(filter(lambda z: _set.issubset(scales[z]), notes))
print(out if len(out) > 0 else 'none')