"""
names = ['Bruno', 'Joao', 'Bernado', 'Barbara', 'Brian']

for name in names: 
    if name.lower().startswith('b'):
        print(name)
"""

names = [
    'Bruno', 
    'Joao', 
    'Bernado', 
    'Barbara', 
    'Brian'
]
print("Estilo funcional")
print(*list(filter(lambda text: text[0].lower() == 'b', names)), sep="\n")
print()

print("Estilo precedural")

     
def starts_with_b(text):
    """Return bool if text starts with b"""
    return text[0].lower() == 'b'
    #return text.startswith(('b', 'B'))


filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
