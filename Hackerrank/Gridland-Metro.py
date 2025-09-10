n, m, k = (int(x) for x in input().split())def intersect(ab, xy):
if ab[0] <= xy[0] and ab[1] >= xy[0]:
return True
if ab[0] <= xy[1] and ab[1] >= xy[1]:
return True
return Falsedef superinterval(ab, xy):
return (min(ab[0], xy[0]), max(ab[1], xy[1]))tracks = dict()for i in range(k):
r, c1, c2 = (int(x) for x in input().split())
t = (c1, c2)
deletion = []
if r not in tracks:
tracks[r] = [t]
continue
for i, interval in enumerate(tracks[r]):
if intersect(interval, t):
t = superinterval(interval, t)
deletion.append(i)
for i in reversed(deletion):
del tracks[r][i]
tracks[r].append(t)
covered = 0
for row in tracks:
for track in tracks[row]:
covered += (track[1] - track[0] + 1)
print(n*m - covered)
