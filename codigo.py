from PyQt5 import  uic,QtWidgets
from __future__import divmod

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
        for i in [1, 2]:
        print i
    
def __new__(cls, original_value):
    object = unicode.new__(cls, original_value)
    object.original_value = original_value
    return object

    match = 10
    from re import
    print match
   
    if formulario.radioButton.isChecked() :
        print("Categoria Eletronicos selecionada")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Informatica selecionada")
    else :
        print("Categoria Alimentos selecionada")
        def date_master(user):
            

    print("Código:",linha1)
    print("Descricao:",linha2)
    print("Preco",linha3) 

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario2.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)