from domain.entities import st

class InMemoryRepository:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de studenti (i.e. sa ofere un depozit persistent pentru obiecte
        de tip st)
    """
    def __init__(self):
        # st - multimea de studenti pe care o gestionam
        # vs. [st1, st2]
        self.__st = []


    def store(self, stud):
        """
        Adauga un student in lista
        :param stud: studentul care se adauga
        :type stud: st
        :return: -; lista de studenti se modifica prin adaugarea studentului dat
        :rtype:
        """
        self.__st.append(stud)

    def get_all_stud(self):
        """
        Returneaza o lista cu toti studentii
        :rtype: list of objects de tip st
        """
        return self.__st

    '''def __delete_by_criteria(self, cautare_id):
        """
        sterge studentii dupa un criteriu dat
        :param filter_fct:  functia(criteriul dupa care se sterg, in cazul de fata id ul)
        :type function
        :return: nr de seriale sterse
        """
        nr_st=len(self)
        self.__st=[st for st in self.__st if not cautare_id(st)]
        return nr_st-len(self)
'''
    def delete_by_id(self, id):
        """
        Sterge student dupa id
        :param id: id-ul dat
        :type id: str
        :return: studentul sters
        :rtype: st
        :raises: ValueError daca id-ul nu exista
        """
        stud = self.cautare_id(id)
        if stud is None:
            raise ValueError('Nu exista serial cu acest id.')

        self.__st.remove(stud)
        return stud

    def cautare_id(self,id):
        """
        cauta serialul cu id ul dat
        :param id: id ul studentului
        :type :str
        :return: studentul cu id ul dat, None daca nu exista
        """
        stud_list=self.__st
        for st in stud_list:
            if st.getID()==id:
                return st
        return None

    def update_st(self,id,mod_st):
        """
        modifica serialul cu id ul dat
        :param id: id ul studentului
        :type :str
        :param mod_st: studentul cu noile date
        :type: st
        :return: studentul modificat
        """
        stud = self.cautare_id(id)
        if stud is None:
            raise ValueError('Nu exista serial cu acest id.')
        #stud
       # vechi_st=self.__st[stud]
        #self.__st[stud]=mod_st
        stud_list = self.__st
        for st in stud_list:
            if st.getID() == id:
                st.setnume(mod_st.getnume())
                st.setgrup(mod_st.getgrup())
        return mod_st

    def size(self):
        """
        Returneaza numarul de studenti din multime
        :return: numar studenti existente
        :rtype:int
        """
        return len(self.__st)

def setup_test_repo():
    stud1=st('1234', 'Ana', 12)
    stud2=st('1235', 'Alin', 12)
    stud3=st('1236', 'Andrei', 13)
    stud4=st('1237', 'Alisa', 14)
    stud5=st('1238', 'Denisa', 13)
    stud6=st('1239', 'Daniel', 13)
    stud7=st('1240', 'Carmen', 12)
    stud8=st('1241', 'Diana', 12)

    test_repo=InMemoryRepository()
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
    assert(test_repo1.size()==8)
    s=st('1211', 'Carla', 12)
    test_repo1.store(s)
    assert(test_repo1.size()==9)

def test_get_all_stud():
    test_repo1 = setup_test_repo()
    crt_s = test_repo1.get_all_stud()
    assert (type(crt_s) == list)
    assert (len(crt_s) == 8)

    test_repo1.delete_by_id('1234')
    test_repo1.delete_by_id('1238')

    crt_ss = test_repo1.get_all_stud()
    assert (len(crt_ss) == 6)

    test_repo1.store(st('1211', 'Carla', 12))
    assert(test_repo1.size()==7)

    assert (test_repo1.get_all_stud()[-1].getnume() == 'Carla')
    assert (test_repo1.get_all_stud()[-1].getID() == '1211')

    test_repo1.update_st('1211', st('1211', 'Mara', 12))

    assert (test_repo1.get_all_stud()[-1].getnume() == 'Mara')

def test_update():
    test_repo1 = setup_test_repo()
    s = st('1234', 'Carla', 12)
    modified_s = test_repo1.update_st('1234', s)
    assert (modified_s.getID() == '1234')
    assert (modified_s.getnume() == 'Carla')
    assert (modified_s.getgrup() == 12)

    try:
        test_repo1.update_st('12345', st('1234', 'Kim', 8873))
        assert False
    except ValueError:
        assert True
def test_delete():
    test_repo1 = setup_test_repo()
    s = st('1234', 'Carla', 12)

    deleted_show = test_repo1.delete_by_id('1234')
    assert (deleted_show.getnume() == 'Ana')
    assert (test_repo1.size() == 7)
    try:
        test_repo1.delete_by_id('wrongid')
        assert False
    except ValueError:
        assert True


def test_find():
    test_repo = setup_test_repo()

    p = test_repo.cautare_id('1234')
    assert (p.getID() == '1234')
    assert (p.getnume() == 'Ana')
    assert (p.getgrup() == 12)

    p1 = test_repo.cautare_id('1888')
    assert (p1 is None)

test_store()
test_get_all_stud()
test_update()
test_delete()
test_find()