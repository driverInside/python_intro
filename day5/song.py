'''
+---------+
|  Song   |
+---------+
| lyrics  |
| title   |
| duration|
+---------+
| display |
| play    |
| get_dur |
+---------+
'''

class Song(object):
    def __init__(self, lyrics, title):
       self.lyrics = lyrics
       self.title = title
       self.duration = len(lyrics)

    def display(self):
        print(f"La canción {self.title} tiene una duración de {self.duration} min")    
    
    def play(self):
        for line in self.lyrics:
            print(f"{line}")
            
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
       
 
happy_bd = Song(["Estas son", "que cantaba ", "..."], "Las mañanitas")
happy_bd.display()
mi_vida = Song(["Que, al fin ", "Bueno ya conoces "], "Mi vida")
mi_vida.display()
cenit = Song(["Foo", "Bar", "fizz", "buzz"], "Cenit")
cenit.display()
lorem = Song(["Lo", "rem", "ipsum", "consectetur", "adipiscing"], "Lorem ipsum")
lorem.display()

happy_bd.play()
lorem.play()

print(f"{cenit.get_title()}")
cenit.set_title("Mar")
print(f"{cenit.get_title()}")
