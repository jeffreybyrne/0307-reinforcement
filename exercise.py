seat = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, "Tama"],
  ["Smokey", "Toast", "Pacha", "Mau"]
]


def empty_seats(seat_array):
    for num in range(0, len(seat_array)):
        for num2 in range(0, len(seat_array[num])):
            if seat_array[num][num2] is None:
                print("Row {} seat {} is empty. Do you want to sit there? (y/n)".format(num+1, num2+1))
                resp = input()
                if resp == 'y':
                    print("What is your name?")
                    name = input()
                    seat_array[num][num2] = name
                    return ''


empty_seats(seat)
# empty_seats(seat)
print(seat)
