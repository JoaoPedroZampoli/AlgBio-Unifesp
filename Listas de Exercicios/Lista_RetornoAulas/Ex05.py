#Sala = {"Nome do Aluno":"Nota"}
Sala = {
    "João": 10,
    "Daniel": 6,
    "Maria": 9,
    "Ana": 8,
    "Pedro": 4,
    "Laura": 2,
}

def media(Sala):
    media = 0
    for aluno in Sala:
        media += Sala[aluno]
    return media/len(Sala)

print(media(Sala))