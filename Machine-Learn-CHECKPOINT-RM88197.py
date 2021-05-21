from sklearn import tree
encoding = 'utf-8'
features = [[60, 100, 87], [62, 102, 85], [67, 110, 90], [72, 105, 86], [79, 112, 96], [83, 116, 99], [88, 119, 95],
            [90, 121, 97], [97, 124, 105], [99, 125, 104], [100, 141, 125], [108, 148, 132], [112, 155, 142],
            [113, 162, 144], [115, 170, 158], [117, 178, 165], [119, 183, 165], [122, 189, 173], [124, 124, 105],
            [125, 199, 190], [126, 205, 200], [132, 208, 202], [144, 215, 204], [147, 216, 210], [149, 220, 211],
            [150, 221, 213], [152, 230, 210], [155, 233, 217], [160, 237, 219], [173, 244, 224]]
labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
glicemia_jejum = float(input("Digite o valor da glicemia em mg/dL em jejum: "))
glicemia_pos = float(input("Digite o valor da glicemia em mg/dL em pós-sobrecarga: "))
glicemia_casual = float(input("Digite o valor da glicemia em mg/dL casual: "))
x = classif.predict([[glicemia_jejum, glicemia_pos, glicemia_casual]])
if x == 1:
    print("Glicemia normal")
elif x == 2:
    print("Glicemia diminuida")
else:
    print("Diabetes")
