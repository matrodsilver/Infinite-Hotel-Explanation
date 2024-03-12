'''#•  simplified version for simplified view

 supose there's a hotel with infinite rooms,
 an infinite number of guests arrive,
 each guest is assigned with a name,
 each name is composed by only two different letters (either "A" or "b"),

 this is the representation that, even though both the hotel and the guests are infinite, there not are enough rooms'''

guestsList = []
outsiderGuest = ''

with open("./Projectz/InfiniteHotel/guestsList.txt", "r+") as guests:
  lineCol = 0

  for guest in guests.readlines():
    outsiderGuest += 'A' if guest[lineCol] == 'b' else 'b'
    lineCol += 1

  while len(outsiderGuest) < len(guest) - 1:  # -1 accounts for line break
    outsiderGuest += 'b'
    print('b added')

  outsiderGuest += '\n'

  guests.write(outsiderGuest)

# end="" because .txt already ends each line with line break
print("ex-Outsider:", outsiderGuest, end="")

# • each time a new guest arrives, he's added to the list, and another outsider guest is created
