
.. blogpost::
    :title: Pourquoi pandas et numpy, pourquoi pas seulement pandas (2A) ?
    :keywords: machine learning, pandas, numpy, matplotlib
    :date: 2017-09-19
    :categories: machine learning

    Voici quelques questions abord�es durant la premi�re s�ance.
    L'instruction :epkg:`pandas:read_csv` n'a pas toujours fonctionn�.
    Deux principales raisons � cela, la premi�re � cause du **chemin**.
    Un chemin peut �tre absolu, il commence par ``c:\`` ou ``\`` sous Windows
    ou ``/`` sous Linux, ou relatif, il commence par un nom.
    Le chemin absolu ne pose pas de difficult� en :epkg:`Python` sauf dans
    quelques cas o� le chemin est un chemin r�seau (commen�ant par ``\\``).
    Par d�faut, :epkg:`Python` cherche les donn�es � partir de l'emplacement
    du programme si le chemin est relatif. Cet emplacement est aussi l'emplacement
    courant pour le programme. Il suffit de placer les fichiers dans ce r�petoire
    pour n'utiliser que le nom du fichier. On l'obtient en ex�cutant :

    .. runpython::
        :showcode:

        import os
        print(os.getcwd())

    Il est possivble de v�rifier le contenu d'un r�pertoire, en particulier
    du r�pertoire courent avec :

    .. runpython::
        :showcode:

        import os
        for name in os.listdir("."):
            print(name)

    La seconde raison est l'**encoding**. Les caract�res chinois n�cessitent
    un encodage particulier car il faut plusieurs octets pour coder un des nombreux
    caract�res. Il n'existe pas une seule fa�on d'associer un caract�re chinois mais
    la fa�on commune est `utf-8 <https://en.wikipedia.org/wiki/UTF-8>`_ qui est le
    standard du web. Il faut s'assurer que le code utilis�e pour cr�er le fichier de donn�es
    est le m�me que celui utilis� pour relire :

    ::

        import pandas
        df = pandas.read_csv("...", encoding="...")

    Autre question, pourquoi `numpy <http://www.numpy.org/>`_ alors que
    `pandas <http://pandas.pydata.org/>`_ fait d�j� tout. La r�ponse tient
    dans l'image qui suit :

    .. image:: images/ml_simple
        :width: 500

    `pandas <http://pandas.pydata.org/>`_ sert � pr�parer les donn�es, � transformer
    tout ce qui n'est pas num�rique en nombres r�elles, � enrichir les donn�es
    en fusionnant avec d'autres bases. Une fois que cela est fait, on peut convertir
    toutes les donn�es au format num�rique, en matrice pour simplfiier car les algorihmes
    num�riques utilisant principalement cela. Des nombres r�els sous forme de matrices,
    c'est ce que manipulent tous les algorithmes de machine learning.
    `matplotlib <https://matplotlib.org/>`_ conclue le processus en donnant les
    moyens de repr�senter le r�sultat de l'exp�rience.

    Pour ceux qui ont commenc� la comp�tition, les liens vers les donn�es
    sont cass�s et seront r�par�s d�s la publication de cet article. Un data leakage
    ou exp�rience surprenante avec la derni�re variable de la base qui contient
    le nombre de valeurs non nulles parmi les colonnes dont le nom se termine pas
    ``100g``. La prise en compte de cette variable semble influencer beaucoup
    la pr�diction.
