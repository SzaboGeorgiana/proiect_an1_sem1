from domain.entities import st, pb, nota
from domain.validators import StValidator, PbValidator, NValidator
from repository.st_repo import InMemoryRepository
from repository.pb_repo import InMemoryRepository1
from repository.nota_repo import InMemoryRepository2

class Service:
    """
        GRASP Controller (Curs 6)
        Responsabil de efectuarea operatiilor cerute de utilizator
        Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
        (i.e. declansare actiune: utilizator -> ui-> obiect tip service in ui -> service -> service coordoneaza operatiile
        folosind alte obiecte (e.g. repo, validator) pentru a realiza efectiv operatia)
        """
    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam studentii
        :type repo: InMemoryRepository
        :param validator: validator pentru verificarea datelor ce apartin de studenti
        :type validator: StValidator, PbValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_st(self, ID, nume, grup):
        '''
        creaza un nou student cu ID, nume, grup
        :param ID: ID ul
        :type ID: str
        :param nume: numele studentului
        :type nume: str
        :param grup: grupa din care face parte
        :type grup: int
        '''
        s = st(ID, nume, grup)
        self.__validator.validate(s)
        self.__repo.store(s)
        return s

    def add_pb(self,nr_pb,descriere,deadline):
        '''
        creaza o problema cu nr_pb,descriere,deadline
        :param nr_pb: numarul problemei
        :type nr_pb: int
        :param descriere: descrierea problemei
        :type descriere: str
        :param deadline: data pana la care trebuie facuta tema
        :type deadline: str
        '''
        p=pb(nr_pb,descriere,deadline)
        self.__validator.validate1(p)
        self.__repo.store(p)
        return p

    def del_st(self, id):
        """
        sterge studentul cu id ul citit de la tastatura
        :param id: id ul studentului
        :type: str
        :return: studentul sters
        """
        return self.__repo.delete_by_id(id)

    def cauta_st(self,id):
        """
               cauta studentul cu id ul citit de la tastatura
               :param id: id ul studentului
               :type: str
               :return: studentul cautat
               """
        return self.__repo.cautare_id(id)

    def get_all_stud(self):
        """
        Returneaza o lista cu toti studentii
        :return: lista de studenti
        :rtype: list of objects de tip st
        """
        return self.__repo.get_all_stud()

    def del_pb(self, id):
        """
               sterge problema cu numarul citit de la tastatura
               :param id: numarul prob
               :type: int
               :return: problema stearsa
               """
        return self.__repo.delete_by_id(id)

    def cauta_pb(self, id):
        """
               cauta problema cu numarul citit de la tastatura
               :param id: numarul prob
               :type: int
               :return: problema cautata
               """
        return self.__repo.cautare_id(id)

    def get_all_prob(self):
        """
        Returneaza o lista cu toate problemele
        :return: lista de probleme
        :rtype: list of objects de tip pb
        """
        return self.__repo.get_all_pb()

    def mod_st(self,id,nume,grup):
        '''
                modifica datele studentului cu id ul dat
                :param id: ID ul
                :type id: str
                :param nume: numele studentului
                :type nume: str
                :param grup: grupa din care face parte
                :type grup: int
                '''
        s=st(id,nume,grup)

        self.__validator.validate(s)
        return self.__repo.update_st(id,s)


    def mod_pb(self,nr_pb,descriere,deadline):
        '''
        modifica datele problemei cu numarul dat
        :param nr_pb: numarul problemei
        :type nr_pb: int
        :param descriere: descrierea problemei
        :type descriere: str
        :param deadline: data pana la care trebuie facuta tema
        :type deadline: str
        '''
        p=pb(nr_pb,descriere,deadline)

        self.__validator.validate1(p)
        return self.__repo.update_pb(nr_pb,p)

    def add_nota(self, ID, nta, pb):
        '''
        creaza o noua nota cu ID, nota, pb
        :param ID: ID ul
        :type ID: str
        :param nota: nota studentului
        :type nota: float
        :param pb: problema pe care a primit studentul nota
        :type pb: int
        '''
        s = nota(pb, nta, ID)
        self.__validator.validate2(s)
        self.__repo.store(s)
        return s

    def get_all_n(self):
        """
        Returneaza o lista cu toate notele
        :return: lista de note
        :rtype: list of objects de tip nota
        """
        return self.__repo.get_all_n()

    def cauta_idii_pb(self,nr):
        """
        Returneaza o lista cu toate notele
        :return: lista de note
        :rtype: list of objects de tip nota
        """
        return self.__repo.cautare_iduri_pb(nr)

    def cauta_idii_st(self,nr):
        """
        Returneaza o lista cu toate notele
        :return: lista de note
        :rtype: list of objects de tip nota
        """
        return self.__repo.cautare_iduri_st(nr)

    def med(self,nr):
        """
        Returneaza un numar
        :return: media notelor
        :rtype:float
        """
        return self.__repo.media(nr)


def test_add_show():
        repo = InMemoryRepository()
        validator = StValidator()
        test_srv = Service(repo, validator)

        added_show = test_srv.add_st('6767', 'Ana', 12)
        assert (added_show.getID()=='6767')
        assert (added_show.getnume()=='Ana')
        l=test_srv.get_all_stud()
        assert (len(l) == 1)
        try:
            added_show = test_srv.add_st('6767', 'Ana', 120)
            assert False
        except ValueError:
            assert True
test_add_show()


def test_add_prob():
    repo = InMemoryRepository1()
    validator = PbValidator()
    test_srv = Service(repo, validator)
    added = test_srv.add_pb(6, 'Acuma', '12.10')
    assert (added.getnr_pb() == 6)
    assert (added.getdeadline() == '12.10')
    l = test_srv.get_all_prob()
    assert (len(l) == 1)
    try:
        added = test_srv.add_pb(6, 'Acuma', '12.100')
        assert False
    except ValueError:
        assert True

test_add_prob()


def test_add_n():
        repo = InMemoryRepository2()
        validator = NValidator()
        test_srv = Service(repo, validator)

        added_show = test_srv.add_nota('6767', 6.7, 12)
        assert (added_show.getid_st()=='6767')
        assert (added_show.getnota()==6.7)
        l=test_srv.get_all_n()
        assert (len(l) == 1)
        try:
            added_show = test_srv.add_nota('6767', 80, 20)
            assert False
        except ValueError:
            assert True
test_add_n()

def test_del_st():
    repo = InMemoryRepository()
    validator = StValidator()
    test_srv = Service(repo, validator)

    test_srv.add_st('6767', 'Ana', 12)
    del_s=test_srv.del_st('6767')

    assert (del_s.getID() == '6767')
    assert (del_s.getnume() == 'Ana')
    l = test_srv.get_all_stud()
    assert (len(l) == 0)

    try:
        test_srv.del_st('2223')
        assert False
    except ValueError:
        assert True

def test_del_pb():
    repo = InMemoryRepository1()
    validator = PbValidator()
    test_srv = Service(repo, validator)

    test_srv.add_pb(6, 'Acuma', '12.10')
    del_pb=test_srv.del_pb(6)
    assert (del_pb.getnr_pb() == 6)
    assert (del_pb.getdeadline() == '12.10')
    l = test_srv.get_all_prob()
    assert (len(l) == 0)
    try:
        test_srv.del_pb(8)
        assert False
    except ValueError:
        assert True

def test_cauta_st():
    repo = InMemoryRepository()
    validator = StValidator()
    test_srv = Service(repo, validator)

    test_srv.add_st('6767', 'Ana', 12)
    find = test_srv.cauta_st('6767')
    assert (find.getID() == '6767')
    assert (find.getnume() == 'Ana')
    assert (find.getgrup() == 12)

def test_cauta_pb():
    repo = InMemoryRepository1()
    validator = PbValidator()
    test_srv = Service(repo, validator)

    test_srv.add_pb(6, 'Acuma', '17.11')
    find = test_srv.cauta_pb(6)

    assert (find.getnr_pb() == 6)
    assert (find.getdeadline() == '17.11')
    assert (find.getdescriere() == 'Acuma')

def test_cauta_idii_pb():
    repo = InMemoryRepository2()
    validator = NValidator()
    test_srv = Service(repo, validator)

    test_srv.add_nota('6767', 6.7, 12)
    find=test_srv.cauta_idii_pb(12)
    assert (len(find)==2)

    assert (find[1]["id_st"] == '6767')
    assert (find[1]["nr_pb"] == 12)
    assert (find[1]["nota"] == 6.7)

test_cauta_idii_pb()

def test_med():
    repo = InMemoryRepository2()
    validator = NValidator()
    test_srv = Service(repo, validator)

    test_srv.add_nota('6767', 6.7, 12)
    test_srv.add_nota('6767', 7.7, 13)
    test_srv.add_nota('6767', 8.7, 14)
    test_srv.add_nota('6767', 9.7, 15)
    test_srv.add_nota('6767', 2.7, 16)

    m=test_srv.med('6767')
#    print(m)
    assert (m==7.1)
    m = test_srv.med('6677')
    assert (m==None)

test_med()

def test_modifica_st():
    repo = InMemoryRepository()
    validator = StValidator()
    test_srv = Service(repo, validator)

    test_srv.add_st('6767', 'Ana', 12)
    mod_s=test_srv.mod_st('6767', 'Alina', 15)
    assert (mod_s.getID() == '6767')
    assert (mod_s.getnume() == 'Alina')
    assert (mod_s.getgrup() == 15)

    try:
        test_srv.mod_st('invalid', 'Ana', 120)
        assert False
    except ValueError:
        assert True

def test_modifica_pb():
    repo = InMemoryRepository1()
    validator = PbValidator()
    test_srv = Service(repo, validator)

    test_srv.add_pb(6, 'Acuma', '12.10')
    mod_p=test_srv.mod_pb(6, 'nu Acuma', '17.11')

    assert (mod_p.getnr_pb() == 6)
    assert (mod_p.getdeadline() == '17.11')
    assert (mod_p.getdescriere() == 'nu Acuma')

    try:
        test_srv.mod_pb(9, 'Acuma', '12.10')
        assert False
    except ValueError:
        assert True

test_del_st()
test_del_pb()
test_cauta_st()
test_cauta_pb()
test_modifica_st()
test_modifica_pb()
