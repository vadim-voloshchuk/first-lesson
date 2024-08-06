isneighbor = True
wall_width = 3

# if wall_width < 2 and isneighbor == False:
#     print("Ураааа, можно ломать стену.")
# elif wall_width < 2 and isneighbor == True:
#     print("Сосеееед домааааааа.")
# elif wall_width >= 2 and isneighbor == False:
#     print("Толстая стенааааа.")
# else:
#     print("Блин, не получится :(")

if wall_width < 2 and isneighbor == False:
    print("Ураааа, можно ломать стену.")
else:
    if wall_width >= 2:
        print("Толстая стенааааа.")
        
    if isneighbor == True:
        print("Сосеееед домааааааа.")

    print("Блин, не получится :(")