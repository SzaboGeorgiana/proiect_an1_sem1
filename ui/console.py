
from domain.entities import st, pb

'''
P2. Gestiune laboratoare studenți
Scrieți o aplicație pentru gestiunea notelor și a problemelor de laborator pentru o disciplină.
Aplicația gestionează:
 studenți: <studentID>,<nume>,<grup>
 problemă laborator: <număr laborator_număr problemă>,<descriere>, <deadline>
Creați o aplicație care permite:
 gestiunea listei de studenți și probleme de laborator.
 adaugă, șterge, modifică, lista de studenți, listă de probleme
 căutare student, căutare problemă
 Asignare laborator/Notare laborator
 Creare statistici:
 lista de studenți și notele lor la o problema de laborator dat, ordonat: alfabetic după nume,
după notă.
 Toți studenții cu media notelor de laborator mai mic decât 5. (nume student și notă)
+toate notele unui student dat ordonate crescator si media as generala.
'''


class Console:

    def __init__(self, srv, srv1,srv2):
        """
        Initializeaza consola
        :type srv: service
        """
        self.__srv = srv
        self.__srv1 = srv1
        self.__srv2 = srv2

    def __print_all_stud(self):
        """
        Afiseaza toti studentii
        """
        st_list = self.__srv.get_all_stud()
        if len(st_list) == 0:
            print('Nu exista studenti in lista.')
        else:
            print('Lista de studenti este:')
            for st in st_list:
                # print(show)
                print(
                    "ID student: " + st.getID() + '; Nume: ' + st.getnume()+ '; Grup: ' +str(st.getgrup()))

    def __print_all_pb(self):
        """
        Afiseaza toate problemele
        """
        st_list = self.__srv1.get_all_prob()
        if len(st_list) == 0:
            print('Nu exista probleme in lista.')
        else:
            print('Lista de probleme este:')
            print(st_list)
            for pb in st_list:
                # print(show)
                print(
                    "Numar problema: " + str(pb.getnr_pb())+ '; Descriere: ' + pb.getdescriere()+ '; Deadline: ' +str(pb.getdeadline()))


    def __print_all_note(self):
        """
        Afiseaza toate notele
        """
        st_list = self.__srv2.get_all_n()
        if len(st_list) == 0:
            print('Nu exista note in lista.')
        else:
            print('Lista de note este:')
            for st in st_list:
                # print(show)
                print(
                    "ID student: " + st.getid_st() + '; Nota: ' + str(st.getnota())+ '; Numarul problemei: ' +str(st.getnrpb()))

    def __generate_st(self):
        self.__srv.add_st('1234', 'Ana', 12)
        self.__srv.add_st('1235', 'Alin', 12)
        self.__srv.add_st('1236', 'Andrei', 13)
        self.__srv.add_st('1237', 'Alisa', 14)
        self.__srv.add_st('1238', 'Denisa', 13)
        self.__srv.add_st('1239', 'Daniel', 13)
        self.__srv.add_st('1240', 'Carmen', 12)
        self.__srv.add_st('1241', 'Diana', 12)

    def __generate_pb(self):
        self.__srv1.add_pb(34, 'Suma numere', '12.02')
        self.__srv1.add_pb(35, 'Diferenta numere', '12.03')
        self.__srv1.add_pb(36, 'produs numere', '13.11')
        self.__srv1.add_pb(17, 'a la puterea b', '14.10')
        self.__srv1.add_pb(18, 'impartire cu rest', '13.11')
        self.__srv1.add_pb(19, 'impartire a doua numere', '13.03')
        self.__srv1.add_pb(40, 'adunare fractii', '12.12')
        self.__srv1.add_pb(12, 'comparare fractii', '12.02')

    def __generate_note(self):
        self.__srv2.add_nota('1234',7.1,34)
        self.__srv2.add_nota('1234', 2.4, 36)
        self.__srv2.add_nota('1234', 6.5, 18)
        self.__srv2.add_nota('1234',1.3,19)

        self.__srv2.add_nota('1235',7.6,35)
        self.__srv2.add_nota('1235',7.5,40)

        self.__srv2.add_nota('1236',10,17)

        self.__srv2.add_nota('1237',9.5,18)
        self.__srv2.add_nota('1237',9.1,35)
        self.__srv2.add_nota('1237',9.2,36)
        self.__srv2.add_nota('1237',1.2,40)
        self.__srv2.add_nota('1237',1.7,12)

        self.__srv2.add_nota('1238',3.3,18)
        self.__srv2.add_nota('1238',1.3,17)
        self.__srv2.add_nota('1238',1.2,40)

        self.__srv2.add_nota('1239',2.4,17)
        self.__srv2.add_nota('1239',8.4,18)

        self.__srv2.add_nota('1240',7.3,19)
        self.__srv2.add_nota('1240',1.2,40)

        self.__srv2.add_nota('1241',8.5,36)
        self.__srv2.add_nota('1241',1.7,12)

    def __add_st(self):
        """
        Adauga un student cu datele citite de la tastatura
        """
        ID = input("ID ul studentului:")
        nume = input("Numele studentului:")
        try:
            grup = int(input("Grupa studentului:"))
        except ValueError:
            print('Grupa trebuie sa fie un numar.')
            return
        stud=self.__srv.cauta_st(ID)
        if stud is None:
            try:
                added_st= self.__srv.add_st(ID, nume, grup)
                print('studentul ' + added_st.getnume() + ' (' + str(
                    added_st.getID()) + ') a fost adaugat cu succes.')
            except ValueError as ve:
                    print(str(ve))
        else:
            print("exista deja un sutdent cu acest ID")

    def __add_pb(self):
        """
        Adauga o problema cu datele citite de la tastatura
        """
        try:
            nr_pb = int(input("Numarul problemei:"))
        except ValueError:
            print('Trebuie sa fie un numar.')
            return
        descriere = input("descrieti problema:")
        deadline = input("problema trebuie executata pana in data de:")
        pbr=self.__srv1.cauta_pb(nr_pb)
        if pbr is None:
            try:

                added_pb = self.__srv1.add_pb(nr_pb,descriere,deadline)
                print('problema: ' + str(added_pb.getnr_pb()) + ' (' +
                    added_pb.getdescriere() + ') a fost adaugat cu succes.')

            except ValueError as ve:
                    print(str(ve))
        else:
            print("exista deja o problema cu acest numar")


    def __del_st(self):
        id=input("id ul studentului: ")
        try:
            deleted=self.__srv.del_st(id)
            print('Studentul '+deleted.getnume()+' ('+deleted.getID()+') a fost sters.')
        except ValueError as ve:
            print(str(ve))

    def __cauta_st(self):
        id = input("id ul studentului: ")
        st=self.__srv.cauta_st(id)
        if st is None:
            print('Nu exista student cu acest id.')
        else:
            print( "ID student: " + st.getID() + '; Nume: ' + st.getnume()+ '; Grup: ' +str(st.getgrup()))

    def __del_pb(self):#pune try
        try:
            nr = int(input("Numarul problemei:"))
        except ValueError:
            print('Trebuie sa fie un numar intreg.')
            return
        try:
            deleted=self.__srv1.del_pb(nr)
            print('Problema '+str(deleted.getnr_pb())+' ('+deleted.getdescriere()+') a fost stearsa.')
        except ValueError as ve:
            print(str(ve))

    def __cauta_pb(self):
        try:
            nr = int(input("Numarul problemei:"))
        except ValueError:
            print('Trebuie sa fie un numar intreg.')
            return
        pb=self.__srv1.cauta_pb(nr)
        if pb is None:
            print('Nu exista problema cu acest id.')
        else:
            print( "Numar problema: " + str(pb.getnr_pb()) + '; Descriere: ' + pb.getdescriere()+ '; Deadline: ' +str(pb.getdeadline()))

    def __modif_st(self):
        id = input("id ul studentului: ")
        st = self.__srv.cauta_st(id)
        if st is None:
            print('Nu exista student cu acest id.')
        else:
            print("ID student: " + st.getID() + '; Nume: ' + st.getnume() + '; Grup: ' + str(st.getgrup()))
            nume = input("Numele nou al studentului:")
            try:
                grup = int(input("Grupa studentului:"))
            except ValueError:
                print('Grupa trebuie sa fie un numar.')
                return
            try:
                mod_st = self.__srv.mod_st(id, nume, grup)
                print('studentul ' + mod_st.getnume() + ' (' + str(
                    mod_st.getID()) + ') a fost modificat cu succes.')
            except ValueError as ve:
                print(str(ve))

    def __modif_pb(self):
        try:
            nr = int(input("Numarul problemei:"))
        except ValueError:
            print('Trebuie sa fie un numar intreg.')
            return
        pb=self.__srv1.cauta_pb(nr)
        if pb is None:
            print('Nu exista problema cu acest id.')
        else:
            print( "Numar problema: " + str(pb.getnr_pb()) + '; Descriere: ' + pb.getdescriere()+ '; Deadline: ' +str(pb.getdeadline()))
            descriere = input("descrieti problema:")
            deadline = input("problema trebuie executata pana in data de:")
            try:
                added_pb = self.__srv1.mod_pb(nr, descriere, deadline)
                print('problema: ' + str(added_pb.getnr_pb()) + ' (' +
                      added_pb.getdescriere() + ') a fost modificata cu succes.')

            except ValueError as ve:
                print(str(ve))

    def __add_nota(self):
        """
                Adauga o nota cu datele citite de la tastatura
        """
        ID = input("ID ul studentului:")

        try:
            nota = float(input("Nota studentului:"))
            nr_pb = int(input("Numarul problemei:"))
        except ValueError:
            print('Grupa trebuie sa fie un numar.')
            return

        st = self.__srv.cauta_st(ID)
        if st is None:
            print('Nu exista studentul.')
        else:
            pb=self.__srv1.cauta_pb(nr_pb)
            if pb is None:
                print('Nu exista problema cu nr dat.')
            else:
                l=self.__srv2.get_all_n()
                for n in l:
                    if n.getnrpb()==nr_pb and n.getid_st()==ID:
                        print('La laboratorul ', nr_pb, ' studentul ', ID, ' are deja nota.' )
                        return
                try:
                    added_n = self.__srv2.add_nota(ID, nota, nr_pb)
                    print('Nota ' + str(added_n.getnota()) +' a studentului ' + added_n.getid_st() +  ' a fost adaugata cu succes.')
                except ValueError as ve:
                    print(str(ve))
#STATISTICI
    def ord_alfabetic_lab(self):
        try:
            nr = int(input("Numarul problemei:"))
        except ValueError:
            print('Trebuie sa fie un numar intreg.')
            return
        pb=self.__srv1.cauta_pb(nr)
        if pb is None:
            print('Nu exista problema cu acest id.')
        else:
            l = self.__srv2.cauta_idii_pb(nr)
            if l is None:
                print("nu exista note la acest laborator")
            else:
                for i, k in enumerate(l):
                    if i != 0:
                        for j, w in enumerate(l):
                            if j != 0:
                                st1 = self.__srv.cauta_st(k['id_st'])
                                st2 = self.__srv.cauta_st(w['id_st'])
                                if st1.getnume() < st2.getnume():
                                    aux = k['nota']
                                    k['nota'] = w['nota']
                                    w['nota'] = aux

                                    aux = k['id_st']
                                    k['id_st'] = w['id_st']
                                    w['id_st'] = aux
                print('La laboratorul ', nr, ' s-au obtinut in ordine alfabetica dupa nume notele: ')
                for i, k in enumerate(l):
                    if i != 0:
                        st = self.__srv.cauta_st(k['id_st'])
                        print(st.getnume(), '(', st.getID(), '):', k['nota'])

    def ord_nota_lab(self):
        try:
            nr = int(input("Numarul problemei:"))
        except ValueError:
            print('Trebuie sa fie un numar intreg.')
            return
        pb=self.__srv1.cauta_pb(nr)
        if pb is None:
            print('Nu exista problema cu acest id.')
        else:
            l=self.__srv2.cauta_idii_pb(nr)
            if l is None:
                print("nu exista note la acest laborator")
            else:
                for i, k in enumerate(l):
                    if i != 0:
                        for j, w in enumerate(l):
                            if j != 0:
                                if w['nota']>k['nota']:
                                    aux=k['nota']
                                    k['nota']=w['nota']
                                    w['nota']=aux

                                    aux = k['id_st']
                                    k['id_st'] = w['id_st']
                                    w['id_st'] = aux
                print('La laboratorul ',nr,' s-au obtinut in ordine crescatoare notele: ')
                for i, k in enumerate(l):
                    if i != 0:
                        st = self.__srv.cauta_st(k['id_st'])
                        print(st.getnume(),'(',st.getID(),'):', k['nota'])

    def st_cu_media(self):
        st=self.__srv.get_all_stud()
        ok=1
        for stud in st:
                m = self.__srv2.med(stud.getID())
                if m is not None:
                    if m < 5:
                        print(stud.getnume(), '(', stud.getID(), '):', m)
                        ok=0
        if ok==1:
            print('nu exista studenti cu media sub 5.')


    def ord_nota_stud(self):
        ID = input("ID ul studentului:")
        stud = self.__srv.cauta_st(ID)
        if stud is None:
            print('Nu exista student cu acest id.')
        else:
            l = self.__srv2.cauta_idii_st(ID)
            if l is None:
                print("Acest student nu are note la acest laborator")
            else:
                #print(l)
                for i, k in enumerate(l):
                    if i != 0:
                        for j, w in enumerate(l):
                            if j != 0:
                                '''st1 = self.__srv.cauta_st(k['id_st'])
                                st2 = self.__srv.cauta_st(w['id_st'])'''
                                if k['nota'] < w['nota']:
                                    aux = k['nota']
                                    k['nota'] = w['nota']
                                    w['nota'] = aux

                                    aux = k['id_st']
                                    k['id_st'] = w['id_st']
                                    w['id_st'] = aux

                print('Studentul ', stud.getnume(),'din grupa', stud.getgrup(), ' a obtinut in ordine crescatoare notele: ')
                for i, k in enumerate(l):
                    if i != 0:
                        print('problema: ',k['nr_pb'], '         nota: ', k['nota'])
                m = self.__srv2.med(stud.getID())
                print('media sa generala este: ', m)



    def meniu(self):
            while True:
                print('Comenzi disponibile: ')
                print('generate_st, generate_pb, generate_note, ')
                print('add_st,    add_pb,')
                print('delete_st, delete_pb,')
                print('cauta_st,cauta_pb')
                print('modif_st,   modif_pb,  ')
                print('asignare_lab, ord_alfabetic_lab,   ord_nota_lab,')#statistici
                print('ord_nota_stud,  st_cu_media,   ')#statistici
                print('show_all_stud,  show_all_prob, show_all_note, exit')
                cmd = input('Optiunea dumneavoastra este:')
                cmd = cmd.lower().strip()
                if cmd == 'add_st':
                    self.__add_st()
                elif cmd == 'add_pb':
                    self.__add_pb()
                elif cmd == 'delete_st':
                    self.__del_st()
                elif cmd == 'delete_pb':
                    self.__del_pb()
                elif cmd == 'cauta_st':
                    self.__cauta_st()
                elif cmd == 'cauta_pb':
                    self.__cauta_pb()
                elif cmd == 'modif_st':
                    self.__modif_st()
                elif cmd == 'modif_pb':
                    self.__modif_pb()
                elif cmd == 'asignare_lab':
                    self.__add_nota()
                elif cmd == 'ord_alfabetic_lab':
                    self.ord_alfabetic_lab()
                elif cmd == 'ord_nota_lab':
                    self.ord_nota_lab()
                elif cmd == 'st_cu_media':
                    self.st_cu_media()
                elif cmd == 'show_all_stud':
                    self.__print_all_stud()
                elif cmd == 'show_all_prob':
                    self.__print_all_pb()
                elif cmd == 'show_all_note':
                    self.__print_all_note()
                elif cmd=='generate_st':
                    self.__generate_st()
                elif cmd == 'generate_pb':
                    self.__generate_pb()
                elif cmd == 'generate_note':
                    self.__generate_note()
                elif cmd =='ord_nota_stud':
                    self.ord_nota_stud()
                elif cmd == 'exit':
                    print("Total number of objects created (including tests):", st.getNumberObjects())
                    return
                else:
                    print('Comanda invalida.')

'''pe saptamana viitoare
repo pt fiecare entitate(3 repo) si lucram cu fisiere
testele le punem in white box(pe caxuri teste) si black box(pe conditii teste)'''