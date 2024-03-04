class st:
    no_instances=0
    def __init__(self, ID,nume,grup):
        '''
        creaza un nou student cu ID, nume, grup
        :param ID: ID ul
        :type ID: str
        :param nume: numele studentului
        :type nume: str
        :param grup: grupa din care face parte
        :type grup: int
        '''
        self.__ID=ID
        self.__nume=nume
        self.__grup=grup
        st.no_instances+=1

    def getID(self):
        return self.__ID

    def getnume(self):
        return self.__nume

    def getgrup(self):
        return self.__grup

    def setID(self, value):
        self.__ID= value

    def setgrup(self, value):
        self.__grup = value

    def setnume(self, value):
        self.__nume = value

    def __eq__(self, other):
        if self.__ID == other.getID():
            return True
        return False

    def __str__(self):
        return "ID student: " + self.__ID + '; Nume: ' + self.__nume + '; Grup: ' +str(self.__grup)

    @staticmethod
    def getNumberObjects():
        return st.no_instances


def test_create_st():
        stud = st('6767', 'Ana', 12)
        assert (stud.getID() == '6767')
        assert (stud.getnume() == 'Ana')
        assert (stud.getgrup() == 12)

        stud.setID('6666')
        stud.setnume('Alina')
        stud.setgrup(13)

        assert (stud.getID() == '6666')
        assert (stud.getnume() == 'Alina')
        assert (stud.getgrup() == 13)


def test_equals_st():
        stud1 = st('6767', 'Ana', 12)
        stud2 = st('6767', 'Ana', 12)


        assert (stud2 == stud1)

        stud3 = st('6766', 'Ana', 12)
        assert (stud2 != stud3)


class pb:
    no_instances1=0
    def __init__(self, nr_pb,descriere,deadline):
        '''
        creaza o problema cu nr_pb,descriere,deadline
        :param nr_pb: numarul problemei
        :type nr_pb: int
        :param descriere: descrierea problemei
        :type descriere: str
        :param deadline: data pana la care trebuie facuta tema
        :type deadline: str
        '''
        self.__nr_pb = nr_pb
        self.__descriere = descriere
        self.__deadline = deadline
        st.no_instances+=1

    def getnr_pb(self):
        return self.__nr_pb

    def getdescriere(self):
        return self.__descriere

    def getdeadline(self):
        return self.__deadline

    def setnr_pb(self, value):
        self.__nr_pb= value

    def setdeadline(self, value):
        self.__deadline = value

    def setdescriere(self, value):
        self.__descriere = value

    def __eq__(self, other):
        if self.__nr_pb == other.getnr_pb() :
            return True
        return False

    def __str__(self):
        return "Numar laborator/numar problema: " + str(self.__nr_pb) + '; descriere: ' + self.__descriere + '; deadline: ' +self.__deadline

    @staticmethod
    def getNumberObjects1():
        return pb.no_instances1


def test_create_pb():
        stud =pb(1, 'nu stiu', '21.10')
        assert (stud.getnr_pb() == 1)
        assert (stud.getdescriere() == 'nu stiu')
        assert (stud.getdeadline() =='21.10')

        stud.setnr_pb(6)
        stud.setdescriere('Acum stiu')
        stud.setdeadline('13.10')

        assert (stud.getnr_pb() == 6)
        assert (stud.getdescriere() == 'Acum stiu')
        assert (stud.getdeadline() == '13.10')


def test_equals_pb():
        pb1 = pb(6, 'Acuma', '12.10')
        pb2 = pb(6, 'Acuma', '12.10')


        assert (pb2 == pb1)

        pb3 = pb(7, 'Acuma', '12.10')
        assert (pb3 != pb1)



class nota:
    def __init__(self,nrpb, nota,id_st):
        '''
        creaza o nota a studentului cu id-ul id_st la problema cu numarul nr_pb
        :param nrpb: numarul problemei
        :type nrpb: int
        :param nota: nota a studentului cu id-ul id_st la problema cu numarul nr_pb
        :type nota: float
        :param id_st: id-ul studentului
        :type id_st: str
        '''
        self.__nrpb = nrpb
        self.__nota = nota
        self.__id_st= id_st
        st.no_instances+=1

    def getnrpb(self):
        return self.__nrpb

    def getnota(self):
        return self.__nota

    def getid_st(self):
        return self.__id_st

    def setnrpb(self, value):
        self.__nrpb= value

    def setid_st(self, value):
        self.__id_st = value

    def setnota(self, value):
        self.__nota = value

    def __eq__(self, other):
        if self.__nrpb == other.getnrpb() and self.__id_st==other.getid_st() :
            return True
        return False

    def __str__(self):
        return "Numar laborator/numar problema: " + str(self.__nrpb) + '; nota: ' + str(self.__nota) + '; studentul: ' +self.__id_st

    @staticmethod
    def getNumberObjects2():
        return nota.no_instances2



def test_create_nota():
    stud = nota(1, 8, '2110')
    assert (stud.getnrpb() == 1)
    assert (stud.getnota() == 8)
    assert (stud.getid_st() == '2110')

    stud.setnrpb(6)
    stud.setnota(8.5)
    stud.setid_st('1310')

    assert (stud.getnrpb() == 6)
    assert (stud.getnota() == 8.5)
    assert (stud.getid_st() == '1310')


def test_equals_nota():
    pb1 = pb(6, 7, '1210')
    pb2 = pb(6, 9, '1210')

    assert (pb2 == pb1)

    pb3 = pb(7, 7, '1210')
    assert (pb3 != pb1)


test_create_pb()
test_equals_pb()
test_create_st()
test_equals_st()
test_create_nota()
test_equals_nota()


