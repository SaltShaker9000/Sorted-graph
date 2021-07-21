import pygame
import time
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
light_grey = (125, 125, 125)
dark_grey = (25, 25, 25)
ran_quicksort = False
clock = pygame.time.Clock()
my_values = []

my_item_idex0 = False
my_item_idex1 = False
my_item_idex2 = False
my_item_idex3 = False
my_item_idex4 = False
my_item_idex5 = False
my_item_idex6 = False
my_item_idex7 = False
my_item_idex8 = False
my_item_idex9 = False
my_item_idex10 = False
my_item_idex11 = False
my_item_idex12 = False
my_item_idex13 = False
my_item_idex14 = False
my_item_idex15 = False

while True:
    try:
        my_input = round(float(input("Enter your values(0, 100), Enter 101 to continue: ")), 1)

    except ValueError:
        continue

    else:
        if my_input > 100:
            break

        else:
            my_values.append(my_input)



class Sorting:
    def __init__(self, values):
        self.values = values
        self.lenValues = len(self.values)

        self.width = 900
        self.height = 500

        self.display = pygame.display.set_mode((self.width, self.height))
        self.marking_font = pygame.font.SysFont("ubuntu", 10)
        self.main_font = pygame.font.SysFont("ubuntu", 20)

        # filling white and drawing the bottom rect
        self.display.fill(white)
        pygame.draw.rect(self.display, black, [0, 450, self.width, 2])

        # Bar 25
        pygame.draw.rect(self.display, black, [0, 337, self.width, 1])
        number25 = self.marking_font.render("25", True, black)
        self.display.blit(number25, [1, 336])

        # Bar 50
        pygame.draw.rect(self.display, black, [0, 225, self.width, 1])
        number50 = self.marking_font.render("50", True, black)
        self.display.blit(number50, [1, 224])

        # Bar 75
        pygame.draw.rect(self.display, black, [0, 112, self.width, 1])
        number75 = self.marking_font.render("75", True, black)
        self.display.blit(number75, [1, 111])

        # Bar 100
        pygame.draw.rect(self.display, black, [0, 0, self.width, 1])
        number100 = self.marking_font.render("100", True, black)
        self.display.blit(number100, [1, 1])

        # pygame.draw.rect(self.display, black, [25, 337, 10, (450 - 337)])
        pygame.display.update()

    def quicksort(self):
        global ran_quicksort
        global my_item_idex0
        global my_item_idex1
        global my_item_idex2
        global my_item_idex3
        global my_item_idex4
        global my_item_idex5
        global my_item_idex6
        global my_item_idex7
        global my_item_idex8
        global my_item_idex9
        global my_item_idex10
        global my_item_idex11
        global my_item_idex12
        global my_item_idex13
        global my_item_idex14
        global my_item_idex15

        def quicksort(list):
            if len(list) < 2:
                return list

            else:
                pivot = list[0]

                high = [i for i in list[1:] if i > pivot]

                low = [i for i in list[1:] if i <= pivot]

                return quicksort(low) + [pivot] + quicksort(high)


        def bar1():
            pygame.draw.rect(self.display, black, [25, round(450 - (quicksort(self.values)[0] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[0] * 4.5)))])
            number1 = self.main_font.render(str(quicksort(self.values)[0]), True, black)
            self.display.blit(number1, [(((875 - (self.lenValues * 2)) / self.lenValues) + 25) / 2, 460])

        def bar2():
            pygame.draw.rect(self.display, black, [((875 - (self.lenValues * 2)) / self.lenValues) + 28, round(450 - (quicksort(self.values)[1] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[1] * 4.5)))])
            number2 = self.main_font.render(str(quicksort(self.values)[1]), True, black)
            self.display.blit(number2, [((((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30) / 1.5, 460])

        def bar3():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30, round(450 - (quicksort(self.values)[2] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[2] * 4.5)))])
            number3 = self.main_font.render(str(quicksort(self.values)[2]), True, black)
            self.display.blit(number3, [((((875 - (self.lenValues * 2)) / self.lenValues) * 3) + 30) / 1.25, 460])

        def bar4():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32, round(450 - (quicksort(self.values)[3] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[3] * 4.5)))])
            number4 = self.main_font.render(str(quicksort(self.values)[3]), True, black)
            self.display.blit(number4, [((((875 - (self.lenValues * 2)) / self.lenValues) * 4) + 30) / 1.2, 460])

        def bar5():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34, round(450 - (quicksort(self.values)[4] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[4] * 4.5)))])
            number5 = self.main_font.render(str(quicksort(self.values)[4]), True, black)
            self.display.blit(number5, [((((875 - (self.lenValues * 2)) / self.lenValues) * 5) + 34) / 1.17, 460])

        def bar6():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36, round(450 - (quicksort(self.values)[5] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[5] * 4.5)))])
            number6 = self.main_font.render(str(quicksort(self.values)[5]), True, black)
            self.display.blit(number6, [((((875 - (self.lenValues * 2)) / self.lenValues) * 6) + 36) / 1.1, 460])

        def bar7():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38, round(450 - (quicksort(self.values)[6] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[6] * 4.5)))])
            number7 = self.main_font.render(str(quicksort(self.values)[6]), True, black)
            self.display.blit(number7, [((((875 - (self.lenValues * 2)) / self.lenValues) * 7) + 38) / 1.1, 460])

        def bar8():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40, round(450 - (quicksort(self.values)[7] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[7] * 4.5)))])
            number8 = self.main_font.render(str(quicksort(self.values)[7]), True, black)
            self.display.blit(number8, [((((875 - (self.lenValues * 2)) / self.lenValues) * 8) + 40) / 1.09, 460])

        def bar9():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42, round(450 - (quicksort(self.values)[8] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[8] * 4.5)))])
            number9 = self.main_font.render(str(quicksort(self.values)[8]), True, black)
            self.display.blit(number9, [((((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 42) / 1.08, 460])

        def bar10():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 9) +  44, round(450 - (quicksort(self.values)[9] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[9] * 4.5)))])
            number10 = self.main_font.render(str(quicksort(self.values)[9]), True, black)
            self.display.blit(number10, [((((875 - (self.lenValues * 2)) / self.lenValues) * 10) + 44) / 1.075, 460])

        def bar11():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 10) +  46, round(450 - (quicksort(self.values)[10] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[10] * 4.5)))])
            number11 = self.main_font.render(str(quicksort(self.values)[10]), True, black)
            self.display.blit(number11, [((((875 - (self.lenValues * 2)) / self.lenValues) * 11) + 46) / 1.070, 460])

        def bar12():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 11) +  48, round(450 - (quicksort(self.values)[11] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[11] * 4.5)))])
            number12 = self.main_font.render(str(quicksort(self.values)[11]), True, black)
            self.display.blit(number12, [((((875 - (self.lenValues * 2)) / self.lenValues) * 12) + 28) / 1.045, 460])

        def bar13():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 12) + 50, round(450 - (quicksort(self.values)[12] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[12] * 4.5)))])
            number13 = self.main_font.render(str(quicksort(self.values)[12]), True, black)
            self.display.blit(number13, [((((875 - (self.lenValues * 2)) / self.lenValues) * 13) + 50) / 1.060, 460])

        def bar14():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 13) +  52, round(450 - (quicksort(self.values)[13] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[13] * 4.5)))])
            number14 = self.main_font.render(str(quicksort(self.values)[13]), True, black)
            self.display.blit(number14, [((((875 - (self.lenValues * 2)) / self.lenValues) * 14) + 52) / 1.05, 460])

        def bar15():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 14) +  54, round(450 - (quicksort(self.values)[14] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[14] * 4.5)))])
            number15 = self.main_font.render(str(quicksort(self.values)[14]), True, black)
            self.display.blit(number15, [((((875 - (self.lenValues * 2)) / self.lenValues) * 15) + 54) / 1.050, 460])

        def bar16():
            pygame.draw.rect(self.display, black, [(((875 - (self.lenValues * 2)) / self.lenValues) * 15) +  56, round(450 - (quicksort(self.values)[15] * 4.5)), ((875 - (self.lenValues * 2)) / self.lenValues), round(450 - (450 - (quicksort(self.values)[15] * 4.5)))])
            number16 = self.main_font.render(str(quicksort(self.values)[15]), True, black)
            self.display.blit(number16, [((((875 - (self.lenValues * 2)) / self.lenValues) * 16) + 56) / 1.049, 460])




        if self.lenValues == 1:
            bar1()


        elif self.lenValues == 2:
            bar1()
            bar2()


            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2


            pygame.draw.polygon(self.display, green, [[point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point2_x, point2_y]])

        elif self.lenValues == 3:
            bar1()
            bar2()
            bar3()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [[point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2], [point3_x, point3_y], [point2_x, point2_y]])

        elif self.lenValues == 4:
            bar1()
            bar2()
            bar3()
            bar4()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)
            pygame.draw.polygon(self.display, green, [[point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]])

        elif self.lenValues == 5:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [[point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2],[point5_x, point5_y2], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]])

        elif self.lenValues == 6:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()



            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2],
            [point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 7:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2],
            [point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 8:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2],
            [point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 9:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()
            bar9()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            point9_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42
            point9_y = round(450 - (quicksort(self.values)[8] * 4.5))
            point9_y2 = (round(450 - (quicksort(self.values)[8] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2], [point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2], [point9_x, point9_y2],
            [point9_x, point9_y] ,[point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 10:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()
            bar9()
            bar10()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            point9_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42
            point9_y = round(450 - (quicksort(self.values)[8] * 4.5))
            point9_y2 = (round(450 - (quicksort(self.values)[8] * 4.5))) + 2

            point10_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 44
            point10_y = round(450 - (quicksort(self.values)[9] * 4.5))
            point10_y2 = (round(450 - (quicksort(self.values)[9] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2], [point9_x, point9_y2], [point10_x, point10_y2],
            [point10_x, point10_y] ,[point9_x, point9_y] ,[point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 11:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()
            bar9()
            bar10()
            bar11()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            point9_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42
            point9_y = round(450 - (quicksort(self.values)[8] * 4.5))
            point9_y2 = (round(450 - (quicksort(self.values)[8] * 4.5))) + 2

            point10_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 44
            point10_y = round(450 - (quicksort(self.values)[9] * 4.5))
            point10_y2 = (round(450 - (quicksort(self.values)[9] * 4.5))) + 2

            point11_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 10) +  46
            point11_y = round(450 - (quicksort(self.values)[10] * 4.5))
            point11_y2 = (round(450 - (quicksort(self.values)[10] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2], [point9_x, point9_y2], [point10_x, point10_y2], [point11_x, point11_y2],
            [point11_x, point11_y] ,[point10_x, point10_y] ,[point9_x, point9_y] ,[point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 12:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()
            bar9()
            bar10()
            bar11()
            bar12()


            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            point9_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42
            point9_y = round(450 - (quicksort(self.values)[8] * 4.5))
            point9_y2 = (round(450 - (quicksort(self.values)[8] * 4.5))) + 2

            point10_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 44
            point10_y = round(450 - (quicksort(self.values)[9] * 4.5))
            point10_y2 = (round(450 - (quicksort(self.values)[9] * 4.5))) + 2

            point11_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 10) +  46
            point11_y = round(450 - (quicksort(self.values)[10] * 4.5))
            point11_y2 = (round(450 - (quicksort(self.values)[10] * 4.5))) + 2

            point12_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 11) +  48
            point12_y =  round(450 - (quicksort(self.values)[11] * 4.5))
            point12_y2 = (round(450 - (quicksort(self.values)[11] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2], [point9_x, point9_y2], [point10_x, point10_y2], [point11_x, point11_y2], [point12_x, point12_y2],
            [point12_x, point12_y], [point11_x, point11_y] ,[point10_x, point10_y] ,[point9_x, point9_y] ,[point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 13:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()
            bar9()
            bar10()
            bar11()
            bar12()
            bar13()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            point9_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42
            point9_y = round(450 - (quicksort(self.values)[8] * 4.5))
            point9_y2 = (round(450 - (quicksort(self.values)[8] * 4.5))) + 2

            point10_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 44
            point10_y = round(450 - (quicksort(self.values)[9] * 4.5))
            point10_y2 = (round(450 - (quicksort(self.values)[9] * 4.5))) + 2

            point11_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 10) +  46
            point11_y = round(450 - (quicksort(self.values)[10] * 4.5))
            point11_y2 = (round(450 - (quicksort(self.values)[10] * 4.5))) + 2

            point12_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 11) +  48
            point12_y =  round(450 - (quicksort(self.values)[11] * 4.5))
            point12_y2 = (round(450 - (quicksort(self.values)[11] * 4.5))) + 2

            point13_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 12) +  50
            point13_y = round(450 - (quicksort(self.values)[12] * 4.5))
            point13_y2 = (round(450 - (quicksort(self.values)[12] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2], [point9_x, point9_y2], [point10_x, point10_y2], [point11_x, point11_y2], [point12_x, point12_y2], [point13_x, point13_y2],
            [point13_x, point13_y] ,[point12_x, point12_y], [point11_x, point11_y] ,[point10_x, point10_y] ,[point9_x, point9_y] ,[point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 14:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()
            bar9()
            bar10()
            bar11()
            bar12()
            bar13()
            bar14()


            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            point9_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42
            point9_y = round(450 - (quicksort(self.values)[8] * 4.5))
            point9_y2 = (round(450 - (quicksort(self.values)[8] * 4.5))) + 2

            point10_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 44
            point10_y = round(450 - (quicksort(self.values)[9] * 4.5))
            point10_y2 = (round(450 - (quicksort(self.values)[9] * 4.5))) + 2

            point11_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 10) +  46
            point11_y = round(450 - (quicksort(self.values)[10] * 4.5))
            point11_y2 = (round(450 - (quicksort(self.values)[10] * 4.5))) + 2

            point12_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 11) +  48
            point12_y =  round(450 - (quicksort(self.values)[11] * 4.5))
            point12_y2 = (round(450 - (quicksort(self.values)[11] * 4.5))) + 2

            point13_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 12) +  50
            point13_y = round(450 - (quicksort(self.values)[12] * 4.5))
            point13_y2 = (round(450 - (quicksort(self.values)[12] * 4.5))) + 2

            point14_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 13) +  52
            point14_y = round(450 - (quicksort(self.values)[13] * 4.5))
            point14_y2 = (round(450 - (quicksort(self.values)[13] * 4.5))) + 2

            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2], [point9_x, point9_y2], [point10_x, point10_y2], [point11_x, point11_y2], [point12_x, point12_y2], [point13_x, point13_y2], [point14_x, point14_y2],
            [point14_x, point14_y], [point13_x, point13_y] ,[point12_x, point12_y], [point11_x, point11_y] ,[point10_x, point10_y] ,[point9_x, point9_y] ,[point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 15:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()
            bar9()
            bar10()
            bar11()
            bar12()
            bar13()
            bar14()
            bar15()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            point9_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42
            point9_y = round(450 - (quicksort(self.values)[8] * 4.5))
            point9_y2 = (round(450 - (quicksort(self.values)[8] * 4.5))) + 2

            point10_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 44
            point10_y = round(450 - (quicksort(self.values)[9] * 4.5))
            point10_y2 = (round(450 - (quicksort(self.values)[9] * 4.5))) + 2

            point11_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 10) +  46
            point11_y = round(450 - (quicksort(self.values)[10] * 4.5))
            point11_y2 = (round(450 - (quicksort(self.values)[10] * 4.5))) + 2

            point12_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 11) +  48
            point12_y =  round(450 - (quicksort(self.values)[11] * 4.5))
            point12_y2 = (round(450 - (quicksort(self.values)[11] * 4.5))) + 2

            point13_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 12) +  50
            point13_y = round(450 - (quicksort(self.values)[12] * 4.5))
            point13_y2 = (round(450 - (quicksort(self.values)[12] * 4.5))) + 2

            point14_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 13) +  52
            point14_y = round(450 - (quicksort(self.values)[13] * 4.5))
            point14_y2 = (round(450 - (quicksort(self.values)[13] * 4.5))) + 2

            point15_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 14) +  54
            point15_y = round(450 - (quicksort(self.values)[14] * 4.5))
            point15_y2 = (round(450 - (quicksort(self.values)[14] * 4.5))) + 2


            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2], [point9_x, point9_y2], [point10_x, point10_y2], [point11_x, point11_y2], [point12_x, point12_y2], [point13_x, point13_y2], [point14_x, point14_y2], [point15_x, point15_y2],
            [point15_x, point15_y], [point14_x, point14_y], [point13_x, point13_y] ,[point12_x, point12_y], [point11_x, point11_y] ,[point10_x, point10_y] ,[point9_x, point9_y] ,[point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])

        elif self.lenValues == 16:
            bar1()
            bar2()
            bar3()
            bar4()
            bar5()
            bar6()
            bar7()
            bar8()
            bar9()
            bar10()
            bar11()
            bar12()
            bar13()
            bar14()
            bar15()
            bar16()

            point1_x = 25
            point1_y = round(450 - (quicksort(self.values)[0] * 4.5))
            point1_y2 = (round(450 - (quicksort(self.values)[0] * 4.5))) + 2

            point2_x = ((875 - (self.lenValues * 2)) / self.lenValues) + 28
            point2_y = round(450 - (quicksort(self.values)[1] * 4.5))
            point2_y2 = (round(450 - (quicksort(self.values)[1] * 4.5))) + 2

            point3_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 30
            point3_y = round(450 - (quicksort(self.values)[2] * 4.5))
            point3_y2 = (round(450 - (quicksort(self.values)[2] * 4.5))) + 2

            point4_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 3) +  32
            point4_y = round(450 - (quicksort(self.values)[3] * 4.5))
            point4_y2 = (round(450 - (quicksort(self.values)[3] * 4.5)) + 2)

            point5_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 4) +  34
            point5_y = round(450 - (quicksort(self.values)[4] * 4.5))
            point5_y2 = (round(450 - (quicksort(self.values)[4] * 4.5))) + 2

            point6_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 5) +  36
            point6_y = round(450 - (quicksort(self.values)[5] * 4.5))
            point6_y2 = (round(450 - (quicksort(self.values)[5] * 4.5))) + 2

            point7_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 6) +  38
            point7_y = round(450 - (quicksort(self.values)[6] * 4.5))
            point7_y2 = (round(450 - (quicksort(self.values)[6] * 4.5))) + 2

            point8_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 7) +  40
            point8_y  = round(450 - (quicksort(self.values)[7] * 4.5))
            point8_y2 = (round(450 - (quicksort(self.values)[7] * 4.5))) + 2

            point9_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 8) +  42
            point9_y = round(450 - (quicksort(self.values)[8] * 4.5))
            point9_y2 = (round(450 - (quicksort(self.values)[8] * 4.5))) + 2

            point10_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 44
            point10_y = round(450 - (quicksort(self.values)[9] * 4.5))
            point10_y2 = (round(450 - (quicksort(self.values)[9] * 4.5))) + 2

            point11_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 10) +  46
            point11_y = round(450 - (quicksort(self.values)[10] * 4.5))
            point11_y2 = (round(450 - (quicksort(self.values)[10] * 4.5))) + 2

            point12_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 11) +  48
            point12_y =  round(450 - (quicksort(self.values)[11] * 4.5))
            point12_y2 = (round(450 - (quicksort(self.values)[11] * 4.5))) + 2

            point13_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 12) +  50
            point13_y = round(450 - (quicksort(self.values)[12] * 4.5))
            point13_y2 = (round(450 - (quicksort(self.values)[12] * 4.5))) + 2

            point14_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 13) +  52
            point14_y = round(450 - (quicksort(self.values)[13] * 4.5))
            point14_y2 = (round(450 - (quicksort(self.values)[13] * 4.5))) + 2

            point15_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 14) +  54
            point15_y = round(450 - (quicksort(self.values)[14] * 4.5))
            point15_y2 = (round(450 - (quicksort(self.values)[14] * 4.5))) + 2

            point16_x = (((875 - (self.lenValues * 2)) / self.lenValues) * 15) +  56
            point16_y = round(450 - (quicksort(self.values)[15] * 4.5))
            point16_2y = (round(450 - (quicksort(self.values)[15] * 4.5))) + 2


            pygame.draw.polygon(self.display, green, [
            [point1_x, point1_y], [point1_x, point1_y2], [point2_x, point2_y2], [point3_x, point3_y2],[point4_x, point4_y2], [point5_x, point5_y2], [point6_x, point6_y2], [point7_x, point7_y2], [point8_x, point8_y2], [point9_x, point9_y2], [point10_x, point10_y2], [point11_x, point11_y2], [point12_x, point12_y2], [point13_x, point13_y2], [point14_x, point14_y2], [point15_x, point15_y2], [point16_x, point16_2y],
            [point16_x, point16_y], [point15_x, point15_y], [point14_x, point14_y], [point13_x, point13_y] ,[point12_x, point12_y], [point11_x, point11_y] ,[point10_x, point10_y] ,[point9_x, point9_y] ,[point8_x, point8_y] ,[point7_x, point7_y] ,[point6_x, point6_y], [point5_x, point5_y] , [point4_x, point4_y], [point3_x, point3_y], [point2_x, point2_y]
            ])


        number1_pos = (((875 - (self.lenValues * 2)) / self.lenValues) + 25) / 2
        number2_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 2) + 28) / 1.5
        number3_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 3) + 30) / 1.25
        number4_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 4) + 32) / 1.2
        number5_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 5) + 34) / 1.17
        number6_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 6) + 36) / 1.12
        number7_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 7) + 38) / 1.1
        number8_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 8) + 40) / 1.09
        number9_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 9) + 42) / 1.07
        number10_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 10) + 44) / 1.075
        number11_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 11) + 46) / 1.070
        number12_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 12) + 28) / 1.045
        number13_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 13) + 50) / 1.060
        number14_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 14) + 52) / 1.05
        number15_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 15) + 54) / 1.05
        number16_pos = ((((875 - (self.lenValues * 2)) / self.lenValues) * 16) + 56) / 1.049

        if my_item_idex0 == True:
            pygame.draw.rect(self.display, red, [number1_pos + 2, 490, 10, 10])

        elif my_item_idex1 == True:
            pygame.draw.rect(self.display, red, [number2_pos + 2, 490, 10, 10])

        elif my_item_idex2 == True:
            pygame.draw.rect(self.display, red, [number3_pos + 2, 490, 10, 10])

        elif my_item_idex3 == True:
            pygame.draw.rect(self.display, red, [number4_pos + 2, 490, 10, 10])

        elif my_item_idex4 == True:
            pygame.draw.rect(self.display, red, [number5_pos + 2, 490, 10, 10])

        elif my_item_idex5 == True:
            pygame.draw.rect(self.display, red, [number6_pos + 2, 490, 10, 10])

        elif my_item_idex6 == True:
            pygame.draw.rect(self.display, red, [number7_pos + 2, 490, 10, 10])

        elif my_item_idex7 == True:
            pygame.draw.rect(self.display, red, [number8_pos + 2, 490, 10, 10])

        elif my_item_idex8 == True:
            pygame.draw.rect(self.display, red, [number9_pos + 2, 490, 10, 10])

        elif my_item_idex9 == True:
            pygame.draw.rect(self.display, red, [number10_pos + 2, 490, 10, 10])

        elif my_item_idex10 == True:
            pygame.draw.rect(self.display, red, [number11_pos + 2, 490, 10, 10])

        elif my_item_idex11 == True:
            pygame.draw.rect(self.display, red, [number12_pos + 2, 490, 10, 10])

        elif my_item_idex12 == True:
            pygame.draw.rect(self.display, red, [number13_pos + 2, 490, 10, 10])

        elif my_item_idex13 == True:
            pygame.draw.rect(self.display, red, [number14_pos + 2, 490, 10, 10])

        elif my_item_idex14 == True:
            pygame.draw.rect(self.display, red, [number15_pos + 2, 490, 10, 10])

        elif my_item_idex15 == True:
            pygame.draw.rect(self.display, red, [number16_pos + 2, 490, 10, 10])



        pygame.display.update()
        time.sleep(0.1)

        def binarysearch(list, item):
            low = 0
            high = len(list) - 1

            while low <= high:
                mid = (low + high) // 2
                guess = list[mid]

                if guess == item:
                    return mid

                if guess > item:
                    high = mid - 1

                else:
                    low = mid + 1

            return None

        while True:
            try:
                my_item = float(input("Enter the item you want to find: "))

            except ValueError:
                continue

            else:
                my_item_idex = binarysearch(quicksort(self.values), my_item)
                if my_item_idex == None:
                    print("Not found")
                    continue
                else:
                    break

            finally:
                my_item_idex0 = False
                my_item_idex1 = False
                my_item_idex2 = False
                my_item_idex3 = False
                my_item_idex4 = False
                my_item_idex5 = False
                my_item_idex6 = False
                my_item_idex7 = False
                my_item_idex8 = False
                my_item_idex9 = False
                my_item_idex10 = False
                my_item_idex11 = False
                my_item_idex12 = False
                my_item_idex13 = False
                my_item_idex14 = False
                my_item_idex15 = False



        if my_item_idex == 0:
            my_item_idex0 = True

        elif my_item_idex == 1:
            my_item_idex1 = True

        elif my_item_idex == 2:
            my_item_idex2 = True

        elif my_item_idex == 3:
            my_item_idex3 = True

        elif my_item_idex == 4:
            my_item_idex4 = True

        elif my_item_idex == 5:
            my_item_idex5 = True

        elif my_item_idex == 6:
            my_item_idex6 = True

        elif my_item_idex == 7:
            my_item_idex7 = True

        elif my_item_idex == 8:
            my_item_idex8 = True

        elif my_item_idex == 9:
            my_item_idex9 = True

        elif my_item_idex == 10:
            my_item_idex10 = True

        elif my_item_idex == 11:
            my_item_idex11 = True

        elif my_item_idex == 12:
            my_item_idex12 = True

        elif my_item_idex == 13:
            my_item_idex13 = True

        elif my_item_idex == 14:
            my_item_idex14 = True

        elif my_item_idex == 15:
            my_item_idex15 = True



        pygame.display.update()
        time.sleep(0.1)


while True:
    runing = Sorting(my_values)
    runing.quicksort()
