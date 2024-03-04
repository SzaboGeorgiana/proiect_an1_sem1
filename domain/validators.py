from domain.entities import st, pb, nota


class StValidator:
    def validate(self, stud):
        errors = []
        if len(stud.getID()) != 4:
            errors.append('ID ul trebuie sa contina exact 4 caractere.')
        if len(stud.getnume()) < 2:
            errors.append('Numele trebuie sa aiba minim 2 caractere. ')
        if stud.getgrup() >= 100:
            errors.append('Numarul grupei are maxim 2 cifre.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def test_validator(self):
        test_validator = StValidator()
        stud1 = st('6767', 'Ana', 12)
        test_validator.validate(stud1)
        stud2 = st('676', 'Ana', 12)
        try:
            test_validator.validate(stud2)
            assert False
        except ValueError:
            assert True

        stud3 = st('6767', 'a', 12)

        try:
            test_validator.validate(stud3)
            assert False
        except ValueError:
            assert True

class PbValidator:
    def validate1(self, stud):
        errors = []
        if len(str(stud.getnr_pb())) >99:
            errors.append('Numarul problemei are maxim 2 cifre.')
        if len(stud.getdescriere()) < 2:
            errors.append('descrierea trebuie sa aiba minim 2 caractere. ')
        x=stud.getdeadline().split('.')
        if int(x[0])>31 or int(x[1])>12:
            errors.append('data trebuie sa fie valida.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def test_validator(self):
        test_validator = PbValidator()
        pb1 = pb(6, 'Acuma', '12.10')
        test_validator.validate1(pb1)
        pb2 = pb(6, 'Acuma', '1210')
        try:
            test_validator.validate1(pb2)
            assert False
        except ValueError:
            assert True

        pb3 = pb(6, 'A', '12.10')

        try:
            test_validator.validate1(pb3)
            assert False
        except ValueError:
            assert True


class NValidator:
    def validate2(self, stud):
        errors = []
        if len(str(stud.getnrpb())) >99:
            errors.append('Numarul problemei are maxim 2 cifre.')
        if stud.getnota() <1 or stud.getnota()>10:
            errors.append('nota poate fi doar intre 1 si 10 ')
        if len(stud.getid_st()) != 4:
            errors.append('ID ul trebuie sa contina exact 4 caractere.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def test_validator(self):
        test_validator = NValidator()
        pb1 = nota(6, 7, '1210')
        test_validator.validate2(pb1)
        pb2 = nota(6, 19, '1210')
        try:
            test_validator.validate2(pb2)
            assert False
        except ValueError:
            assert True

        pb3 = nota(6, 7.5, '12110')

        try:
            test_validator.validate2(pb3)
            assert False
        except ValueError:
            assert True