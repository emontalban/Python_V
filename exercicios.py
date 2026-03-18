lenguajes =['Go', 'Java', 'Ruby', 'Python', 'Swift', 'PHP']
for lenguaje in lenguajes:
    if lenguaje == "Python":
        print(f"{lenguaje} fue encontrado en la posición {lenguajes.index(lenguaje)}")
        break
    print(lenguaje)
