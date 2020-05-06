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
    cite = []
    bt1 = Batiment()
    bt1.set_build(True)
    cite.append(bt1)



def whythis():
    """Hello!
    Nous voulons construire la grande ville du monde!
    """


def get_boat(self):
    """ retourne en bateau """
    # get something
    return self.var


class Batiment(object):
    """
    class Batiment
    batiment générique
    """

    def __init__(self):
        self.build = False
        debut_chantier = datetime.now()
        date_debut = debut_chantier.strftime("%d-%m-%Y")
        print("debut chantier : " + date_debut)

    def __str__(self):
        pass

    def set_build(self, autorization):
        """
        setup build authorization true/false """
        self.build = autorization

    def get_build(self):
        """
        return authorization value """
        return self.build



if __name__ == '__main__':
    main()
