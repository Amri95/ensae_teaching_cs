# coding: latin-1
import string


class SecondeInserstion (AttributeError):
    "insertion d'un mot d�j� ins�r�"


class NoeudTri:

    def __init__(self, s):
        self.mot = s

    # la cr�ation d'un nouveau noeud a �t� plac�e dans une m�thode
    def nouveau_noeud(self, s):
        return self.__class__(s)
        # return NoeudTri (s)

    def __str__(self):
        s = ""
        if "avant" in self.__dict__:
            s += self.avant.__str__()
        s += self.mot + "\n"
        if "apres" in self.__dict__:
            s += self.apres.__str__()
        return s

    def insere(self, s):
        c = cmp(s, self.mot)
        if c == -1:
            if "avant" in self.__dict__:
                self.avant.insere(s)  # d�l�gation
            else:
                self.avant = self.nouveau_noeud(s)         # cr�ation
        elif c == 1:
            if "apres" in self.__dict__:
                self.apres.insere(s)  # d�l�gation
            else:
                self.apres = self.nouveau_noeud(s)           # cr�ation
        else:
            raise SecondeInsertion("mot: '{}'".format(s))


lw = ["un", "deux", "unite", "dizaine", "exception", "dire",
      "programme", "abc", "xyz", "opera", "quel"]

racine = None
for mot in lw:
    if racine is None:
        # premier cas : aucun mot --> on cr�e le premier noeud
        racine = NoeudTri(mot)
    else:
        # second cas : il y a d�j� un mot, on ajoute le mot suivant
        # � l'arbre
        racine.insere(mot)

print(racine)
