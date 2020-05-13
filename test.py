#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Documentation
=========
Bla Bla Bla
"""

from datetime import datetime


def main():
    """ Function main """
    print(whythis.__doc__)


def whythis():
    """Hi!
    Aim for cities of all sizes to give everyone a fair go!
    """


def bat_decorator(self):
    """ add a garden """

    def garden(self, authorization, num_build):
        """ the green garden """
        # do something
        print("Le jardin est en plus")
        return num_build

    return garden


class Batiment(object):
    """
    class Batiment
    batiment générique
    """

    company = ["Bouyges", "Lafarge", "Vinci"]
    finition = {"luxe": 200, "standart": 125, "free": 0}

    def __init__(self):
        self.build = False

        self.builder = 0
        debut_chantier = datetime.now()
        date_debut = debut_chantier.strftime("%d-%m-%Y")
        print("The start of construction date : " + date_debut + "\n")

    def __str__(self):
        pass

    @bat_decorator
    def set_build(self, authorization, num_build):
        """
        setup build authorization true/false """

        self.build = authorization
        self.builder = num_build
        if self.build:
            print("The gardener does his garden in the garden on the top roof!")

            print("numero constructeur " + str(self.builder))

    def get_build(self):
        """
        return authorization value """

        print("Une contruction " + Batiment.company[self.builder])
        return None


if __name__ == "__main__":
    main()
    cite = []
    bt1 = Batiment()
    bt1.set_build(True, 2)
    bt1.get_build()
    cite.append(bt1)
