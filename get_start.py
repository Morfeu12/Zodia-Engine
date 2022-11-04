# Importar a classe "Main" no projeto
from bin.main import Main

# Criar uma váriavel que passe as dimensões da tela e o título.
game = Main(1280, 720, "Hello world!")

# Usar a função "draw" para carregar e desenhar na tela.
campo = game.draw("assets/field.png", 0,0)
p1 = game.draw("assets/p1.png", 50,300)
p2 = game.draw("assets/p2.png", 1150,550)

# Usar a função "update" atualizar os frames do game.
game.update()