length = float(raw_input("What is the length of the room in feet? "))
width = float(raw_input("What is the width of the room in feet? "))

area = length * width
area_m_2 = area * 0.09290304

print "You entered dimensions of {} feet by {} feet".format(length, width)
print """The area is
{} square feet
{} square meters""".format(area, area_m_2)

