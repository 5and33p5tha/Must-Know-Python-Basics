# Polymorphism means many forms.
# it is almost like inheritance BUT SAME METHOD MAY NOT BE SUITABLE FOR ALL SCENARIO
# HENCE WE OVERRIDE THE METHODS TO SUIT OUR NEEDS AND MATCH THE SCENARIO. THIS IS POLYMORPHISM

class Bird:
    def intro(self):
        print("Many birds in the sky")

    def fly(self):
        print("Most fly but some cannot")

        # OVERRIDE WITH INHERITANCE


class Pigeon(Bird):  # Pigeon (Birds) signifies that this code is inheritance
    # AS IT IS INHERITANCE, WE CAN USE THE INTRO OF PARENT CLASS AS WELL

    # here, this will override the METHOD FLY of bird
    def fly(self):
        print("Pigeons can fly")

    # OVERRIDE WITHOUT INHERITANCE
   # class Pigeon():
    # here this will override the method fly()
    # def fly(self):
        #print("Pigeons can fly")

    # Now FOR ANother INHERITED CLASS


class Penguin(Bird):
    # This will override the method fly
    def fly(self):
        print("Penguins can't fly")


obj_bird = Bird()
obj_bird.intro()
obj_bird.fly()

obj_pgn = Pigeon()
obj_pgn.intro()  # THIS IS ONLY POSSIBLE VIA INHERITANCE AS WE HAVE NOT DESCRIBED  INTRO IN PENGUIN BUT STILL USE IT
obj_pgn.fly()

obj_penguin = Penguin()
obj_penguin.fly()


# FROM DAY 14_B WE HAD SQL
