from rich import print
import time
class Livro:
    
    def __init__(self, titulo, paginas):
        
        self.titulo = titulo
        self.paginasTotal = paginas
        self.pagina_atual = 1
        
    def __str__(self):
        return f'Você acabou de abrir o livro "{self.titulo}" que contém {self.paginasTotal} paginas no total. Você agora está na pagina {self.pagina_atual}.'
    
    def avancar_paginas(self, quantidade=1):
        cont = 0
        for pag in range(0, quantidade, 1):
            if not self.fim_livro():
                self.pagina_atual += 1
                print(f"Pag{self.pagina_atual} -> ", end='')
                time.sleep(0.35)
                cont += 1
        print(f"Você avançou {cont} páginas e agora está na pagina {self.pagina_atual}.")
        if self.fim_livro():
            print(f"[red]Você chegou ao final do livro {self.titulo}.[/]")
            print(f"Você chegou ao final do livro, mas as {self.titulo} não tem um fim, pois não há limites nos motivos para amar a Yasmin. Te amo amor!")
                
    def fim_livro(self) -> bool:
        return True if self.pagina_atual >= self.paginasTotal else False
        
        
            
l1 = Livro("Razões para amar a Yas", 30)
print(l1)
l1.avancar_paginas(10)
l1.avancar_paginas(15)
l1.avancar_paginas(40)