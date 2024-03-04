from domain.entities import nota
#from repository.pb_repo import InMemoryRepository1
#from repository.st_repo import InMemoryRepository

class InMemoryRepository2:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de note (i.e. sa ofere un depozit persistent pentru obiecte
        de tip nota)

        Detaliere: seminar 7
    """
    def __init__(self):
        self.__nota = []


    def store(self, nota):
        """
        Adauga o nota in lista
        :param nota: nota care se adauga
        :type nota: nota
        :return: -; lista de note se modifica
        :rtype:
        """
        self.__nota.append(nota)


    def get_all_n(self):
        """
        Returneaza o lista cu toate notele existente
        :rtype: list of objects de tip nota
        """
        return self.__nota

    def cautare_iduri_pb(self, id):
            """
            cauta problema cu id ul dat
            :param id: id ul problemei
            :type: int
            :return: dictionar cu probleme cu id ul dat, None daca nu exista
            """
            l=[{}]
            n_list = self.__nota
            for n in n_list:
                if n.getnrpb() == id:
                    p={'nota': n.getnota(),'nr_pb': n.getnrpb(),'id_st': n.getid_st()}
                    l.append(p)
            if len(l)>1:
                    return l
            return None

    def cautare_iduri_st(self, id):
            """
            cauta studentntii cu id ul in lista notelor
            :param id: id ul studentului
            :type: str
            :return: dictionar cu studentii cu id ul dat, None daca nu exista
            """
            l=[{}]
            n_list = self.__nota
            for n in n_list:
                if n.getid_st() == id:
                    p={'nota': n.getnota(),'nr_pb': n.getnrpb(),'id_st': n.getid_st()}
                    l.append(p)
            if len(l)>1:
                    return l
            return None

    def media(self,id):
        '''
        calculeaza si returneaza mediile la laboratoare a tuturor studentilor
        :param id: id ul studentului
        :type: str
        :return: media
        :type: float
        '''
        l = self.cautare_iduri_st(id)
        if l is None:
            return None
        medie = 0
        for i, k in enumerate(l):
            if i != 0:
                medie = medie + k["nota"]
        medie = medie / (len(l) - 1)
        return medie

    def size(self):
        """
        Returneaza numarul de note din multime
        :return: numar note existente
        :rtype:int
        """
        return len(self.__nota)


def setup_test_repo():
    stud1 = nota(34, 6.7, '1202')
    stud2 = nota(35, 7.8, '1203')
    stud3 = nota(36,  6.8, '1311')
    stud4 = nota(18, 3.5, '1410')
    stud5 = nota(18,1.2, '1311')
    stud6 = nota(19, 10, '1303')
    stud7 = nota(35, 8, '1212')
    stud8 = nota(35,3.4, '1202')

    test_repo = InMemoryRepository2()
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
    s = nota(89, 3.4 , '1202')
    test_repo1.store(s)
    assert (test_repo1.size() == 9)

test_store()


def test_get_all_pb():
    test_repo1 = setup_test_repo()
    crt_s = test_repo1.get_all_n()
    assert (type(crt_s) == list)
    assert (len(crt_s) == 8)


    test_repo1.store(nota(89, 3.4, '1202'))
    assert (test_repo1.size() == 9)

    assert (test_repo1.get_all_n()[-1].getnota() == 3.4)
    assert (test_repo1.get_all_n()[-1].getid_st() == '1202')

test_get_all_pb()

def test_cautare_iduri_pb():
    test_repo1 = setup_test_repo()
    crt_s = test_repo1.cautare_iduri_pb(35)
    assert (len(crt_s)==4)
    crt_s=test_repo1.cautare_iduri_pb(3)
    assert (crt_s==None)

test_cautare_iduri_pb()

def test_cautare_iduri_st():
    test_repo1 = setup_test_repo()
    crt_s = test_repo1.cautare_iduri_st('1202')
    assert (len(crt_s) == 3)
    crt_s = test_repo1.cautare_iduri_pb('1233')
    assert (crt_s == None)

test_cautare_iduri_st()

def test_med():
    test_repo1 = setup_test_repo()
    m = test_repo1.media('1202')
    #print(m)
    assert(m==5.05)
    crt_s = test_repo1.media('1233')
    assert (crt_s == None)

test_med()