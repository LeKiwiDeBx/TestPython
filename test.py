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
    # do something
    def garden(self, authorization):
        """ the green garden """

        if authorization:
            print("The gardener does his garden in the garden on the top roof!")
        return None
    return garden


class Batiment(object):
    """
    class Batiment
    batiment générique
    """

    def __init__(self):
        self.build = False
        debut_chantier = datetime.now()
        date_debut = debut_chantier.strftime("%d-%m-%Y")
        print("The start of construction date : " + date_debut + "\n")

    def __str__(self):
        pass

    @bat_decorator
    def set_build(self, autorization):
        """
        setup build authorization true/false """
        self.build = autorization

    def get_build(self):
        """
        return authorization value """
        self.owner = ["Bouyges", "Lafarge", "Vinci"]
        print("Une contruction " + self.owner[2])
        return self.build


if __name__ == '__main__':
    main()
    cite = []
    bt1 = Batiment()
    bt1.set_build(True)
    bt1.get_build()
    cite.append(bt1)
