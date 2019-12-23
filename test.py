from sweeps import Sweeps
import sweeps

# test base instance
s = sweeps.Sweeps()
print(s.key)

# test boi creation
r = s.createboi(7, 3, 1, 1)
print("boi")
print(r)

# test world map & sectors
sector = Sweeps.getsector(1, 1)
m = Sweeps.getworldmap()
print("map")
print(m)
print("sector")
print(sector)
