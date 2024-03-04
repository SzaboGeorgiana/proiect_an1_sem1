from domain.validators import StValidator,PbValidator, NValidator
from repository.st_repo import InMemoryRepository
from  repository.pb_repo import InMemoryRepository1
from repository.nota_repo import InMemoryRepository2
from controller.service import Service
from ui.console import Console

repo = InMemoryRepository()
val = StValidator()
srv = Service(repo, val)

val1 = PbValidator()
repo1=InMemoryRepository1()
srv1 = Service(repo1, val1)

val2=NValidator()
repo2=InMemoryRepository2()
srv2=Service(repo2,val2)

ui = Console(srv,srv1,srv2)
ui.meniu()