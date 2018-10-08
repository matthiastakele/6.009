out = []
x = quiz.Pond()
x.add_fish((1, 0), SpottedBass(923, 16, 176))
x.add_fish((3, 2), LargemouthBass(525, 83, 227))
x.add_fish((3, 2), SpottedBass(957, 4, 430))
x.add_fish((1, 1), SpottedBass(111, 41, 283))
x.add_fish((3, 2), BlackBass(397, 56, 261))
x.add_fish((0, 3), BlackBass(773, 63, 91))
x.add_fish((2, 1), Catfish(978, 22, 458))
x.add_fish((3, 0), BubbleBass(919, 44, 57))
x.add_fish((3, 2), LargemouthBass(855, 57, 365))
x.add_fish((2, 2), BlackBass(790, 51, 80))
x.add_fish((3, 3), SpottedBass(945, 2, 176))
x.add_fish((1, 3), SmallmouthBass(545, 59, 102))
x.add_fish((2, 0), SmallmouthBass(508, 83, 280))
x.add_fish((2, 1), SpottedBass(141, 81, 413))
x.add_fish((3, 2), LargemouthBass(226, 58, 108))
x.add_fish((1, 0), SmallmouthBass(385, 61, 369))
x.add_fish((2, 0), BubbleBass(842, 4, 324))
x.add_fish((0, 2), StripedBass(454, 18, 358))
x.add_fish((0, 2), SpottedBass(223, 1, 372))
x.add_fish((0, 1), LargemouthBass(355, 53, 177))
x.add_fish((1, 0), SmallmouthBass(83, 54, 251))
x.add_fish((3, 3), BubbleBass(792, 47, 491))
x.add_fish((0, 2), Catfish(873, 92, 407))
x.add_fish((0, 1), StripedBass(907, 78, 430))
x.add_fish((3, 1), TemperateBass(924, 63, 252))
x.add_fish((0, 2), Catfish(185, 33, 224))
x.add_fish((3, 1), BlackBass(241, 91, 121))
x.add_fish((3, 0), BubbleBass(998, 24, 342))
x.add_fish((2, 2), TemperateBass(205, 21, 338))
x.add_fish((1, 3), BlackBass(24, 71, 76))
x.add_fish((3, 1), SpottedBass(535, 11, 420))
x.add_fish((0, 3), BlackBass(396, 42, 204))
x.add_fish((3, 0), Catfish(979, 60, 382))
x.add_fish((2, 2), Catfish(141, 3, 106))
x.add_fish((3, 2), SpottedBass(861, 71, 52))
x.add_fish((2, 2), SmallmouthBass(391, 40, 419))
x.add_fish((1, 3), SmallmouthBass(374, 51, 474))
x.add_fish((0, 2), BlackBass(725, 54, 280))
x.add_fish((1, 2), SmallmouthBass(136, 60, 361))
x.add_fish((1, 0), StripedBass(26, 3, 254))
x.add_fish((1, 0), BubbleBass(315, 2, 424))
x.add_fish((0, 0), BlackBass(689, 28, 195))
x.add_fish((2, 0), Catfish(284, 89, 123))
x.add_fish((2, 1), SpottedBass(373, 73, 260))
x.add_fish((3, 3), TemperateBass(786, 61, 445))
x.add_fish((0, 0), BlackBass(344, 73, 404))
x.add_fish((2, 3), StripedBass(534, 2, 234))
out.append(x.catch_fish((4, 4), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 4), 'crawfish'))
out.append(x.weight_caught())
x.wait(7)
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 4), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 1), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 0), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 0), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 2), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 3), 'frog'))
out.append(x.weight_caught())
x.add_fish((1, 1), SmallmouthBass(693, 40, 339))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 1), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 3), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'spinner'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 0), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 0), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 2), 'worm'))
out.append(x.weight_caught())
x.wait(10)
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 3), 'frog'))
out.append(x.weight_caught())
x.wait(8)
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 0), 'insect'))
out.append(x.weight_caught())
x.add_fish((3, 0), StripedBass(946, 41, 379))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 0), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 1), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 4), 'insect'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 3), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 1), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 3), 'crawfish'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 0), 'stinky cheese'))
out.append(x.weight_caught())
x.add_fish((2, 1), TemperateBass(372, 27, 299))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 3), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 2), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 2), 'spinner'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 1), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 4), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 4), 'insect'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 3), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 4), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 0), 'insect'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 2), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 1), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 4), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 4), 'eel'))
out.append(x.weight_caught())
x.wait(6)
out.append(x.weight_caught())
out.append(x.catch_fish((0, 2), 'crawfish'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 2), 'crawfish'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 0), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 4), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 2), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 0), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 0), 'spinner'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 3), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 3), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 3), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 0), 'spinner'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 3), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 4), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 3), 'crawfish'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 3), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 1), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 0), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 4), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 0), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'insect'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 4), 'insect'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 2), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 3), 'spinner'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 0), 'eel'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 4), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 4), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 3), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 1), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'insect'))
out.append(x.weight_caught())
x.wait(1)
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 0), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 0), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 4), 'crawfish'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'insect'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 1), 'spinner'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 4), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 3), 'worm'))
out.append(x.weight_caught())
x.wait(6)
out.append(x.weight_caught())
x.wait(1)
out.append(x.weight_caught())
out.append(x.catch_fish((1, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'spinner'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 0), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 1), 'insect'))
out.append(x.weight_caught())
x.wait(3)
out.append(x.weight_caught())
out.append(x.catch_fish((2, 3), 'insect'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 3), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 4), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 1), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 2), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 0), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 3), 'krabby patty'))
out.append(x.weight_caught())
x.add_fish((0, 3), LargemouthBass(38, 21, 417))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 0), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 0), 'crankbait'))
out.append(x.weight_caught())
x.wait(8)
out.append(x.weight_caught())
x.add_fish((2, 0), TemperateBass(155, 54, 425))
out.append(x.weight_caught())
x.add_fish((1, 3), Catfish(649, 68, 361))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 0), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'worm'))
out.append(x.weight_caught())
x.add_fish((1, 1), LargemouthBass(484, 96, 406))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 0), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 0), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 0), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 0), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 1), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 0), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 4), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 0), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 0), 'crawfish'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 1), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 0), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 3), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 2), 'stinky cheese'))
out.append(x.weight_caught())
x.add_fish((1, 3), SpottedBass(565, 7, 237))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 0), 'insect'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 2), 'spinner'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 1), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 0), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 0), 'stinky cheese'))
out.append(x.weight_caught())
out.append(x.catch_fish((3, 2), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 2), 'krabby patty'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 4), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((4, 0), 'crawfish'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 2), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((1, 3), 'crankbait'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 3), 'frog'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'crawfish'))
out.append(x.weight_caught())
out.append(x.catch_fish((2, 1), 'spinner'))
out.append(x.weight_caught())
x.wait(10)
out.append(x.weight_caught())
out.append(x.catch_fish((1, 4), 'worm'))
out.append(x.weight_caught())
out.append(x.catch_fish((0, 0), 'crankbait'))
out.append(x.weight_caught())