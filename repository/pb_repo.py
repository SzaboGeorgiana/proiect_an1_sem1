from domain.entities import pb


class InMemoryRepository1:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de seriale (i.e. sa ofere un depozit persistent pentru obiecte
        de tip serial)

        Detaliere: seminar 7
    """
    def __init__(self):
        # shows - multimea de seriale pe care o gestionam
        # poate fi si dictionar, este la latitudinea noastra cum stocam datele
        # e.g. stocare in dict cu un camp in plus id_serial (dar se poate lua titlu ca si cheie
        # de ex, daca am sti ca e unic):
        # {idSerial1: Serial1, idSerial2: Serial2}
        # vs. [serial1, serial2]
        self.__pb = []


    def store(self, pb):
        """
        Adauga o problema in lista
        :param pb: problema care se adauga
        :type pb: pb
        :return: -; lista de probleme se modifica
        :rtype:
        """
        self.__pb.append(pb)


    def get_all_pb(self):
        """
        Returneaza o lista cu toate problemele existente
        :rtype: list of objects de tip Serial
        """
        return self.__pb

    def delete_by_id(self, id):
            """
            Sterge problema dupa id
            :param id: id-ul dat
            :type id: str
            :return: studentul sters
            :rtype: st
            :raises: ValueError daca id-ul nu exista
            """
            stud = self.cautare_id(id)
            if stud is None:
                raise ValueError('Nu exista problema cu acest id.')

            self.__pb.remove(stud)
            return stud

    def cautare_id(self, id):
            """
            cauta problema cu id ul dat
            :param id: id ul studentului
            :type: str
            :return: problema cu id ul dat, None daca nu exista
            """
            stud_list = self.__pb
            for st in stud_list:
                if st.getnr_pb() == id:
                    return st
            return None

    def update_pb(self,nr,mod_pb):
        """
        modifica problema cu nr dat
        :param nr: nr prob
        :type :int
        :param mod_pb: problema cu noile date
        :type: pb
        :return: problema modificata
        """
        stud = self.cautare_id(nr)
        if stud is None:
            raise ValueError('Nu exista problema cu nr dat.')
        #stud
       # vechi_st=self.__st[stud]
        #self.__st[stud]=mod_st
        stud_list = self.__pb
        for st in stud_list:
            if st.getnr_pb() == nr:
                st.setdescriere(mod_pb.getdescriere())
                st.setdeadline(mod_pb.getdeadline())
        return mod_pb

    def size(self):
        """
        Returneaza numarul de probleme din multime
        :return: numar probleme existente
        :rtype:int
        """
        return len(self.__pb)


def setup_test_repo():
    stud1 = pb(34, 'Suma numere', '12.02')
    stud2 = pb(35, 'Diferenta numere', '12.03')
    stud3 = pb(36, 'produs numere', '13.11')
    stud4 = pb(17, 'a la puterea b', '14.10')
    stud5 = pb(18, 'impartire cu rest', '13.11')
    stud6 = pb(19, 'impartire a doua numere', '13.03')
    stud7 = pb(40, 'adunare fractii', '12.12')
    stud8 = pb(12, 'comparare fractii', '12.02')

    test_repo = InMemoryRepository1()
    test_repo.store(stud1)
    test_repo.store(stud2)
    test_repo.store(stud3)
    test_repo.store(stud4)
    test_repo.store(stud5)
    test_repo.store(stud6)
    test_repo.store(stud7)
    test_repo.store(stud8)
    return test_repo


def test_store():
    test_repo1 = setup_test_repo()
    assert (test_repo1.size() == 8)
    s = pb(89, 'comparare functii', '12.02')
    test_repo1.store(s)
    assert (test_repo1.size() == 9)

def test_get_all_pb():
    test_repo1 = setup_test_repo()
    crt_s = test_repo1.get_all_pb()
    assert (type(crt_s) == list)
    assert (len(crt_s) == 8)

    test_repo1.delete_by_id(18)
    test_repo1.delete_by_id(19)

    crt_ss = test_repo1.get_all_pb()
    assert (len(crt_ss) == 6)

    test_repo1.store(pb(89, 'comparare functii', '12.02'))
    assert (test_repo1.size() == 7)

    assert (test_repo1.get_all_pb()[-1].getdescriere() == 'comparare functii')
    assert (test_repo1.get_all_pb()[-1].getdeadline() == '12.02')
    test_repo1.update_pb(89, pb(89, 'numarare functii', '22.02'))

    assert (test_repo1.size() == 7)
   # assert (test_repo1.get_all_pb()[-1].getdescriere == 'numarare functii')
    #assert (test_repo1.get_all_pb()[-1].getdeadline == '22.02')

def test_update():
    test_repo1 = setup_test_repo()
    s = pb(19, 'comparare functii', '12.02')
    modified_s = test_repo1.update_pb(19, s)
    assert (modified_s.getnr_pb() == 19)
    assert (modified_s.getdescriere() == 'comparare functii')
    assert (modified_s.getdeadline() == '12.02')

    try:
        test_repo1.update_pb(875, pb(19, 'functii', '12.02'))
        assert False
    except ValueError:
        assert True

def test_delete():
    test_repo1 = setup_test_repo()
    s = pb(19, 'comparare functii', '12.02')

    deleted_show = test_repo1.delete_by_id(19)
    assert (deleted_show.getdescriere() == 'impartire a doua numere')
    assert (test_repo1.size() == 7)
    try:
        test_repo1.delete_by_id(8765)
        assert False
    except ValueError:
        assert True

def test_find():
    test_repo = setup_test_repo()

    p = test_repo.cautare_id(36)
    assert (p.getnr_pb() ==36)
    assert (p.getdescriere() == 'produs numere')
    assert (p.getdeadline() == '13.11')

    p1 = test_repo.cautare_id(66)
    assert (p1 is None)

test_store()
test_get_all_pb()
test_update()
test_delete()
test_find()