# Instalando PyQt5:

-   pip install PyQt5


# Instalando PyQt5-tools:

-   pip install PyQt5-tools

Se usa o Spyder e der ruim nele:

-   pip install PyQt5==5.10.1


# Feito isso, agora é só clicar em windows e procurar designer
<a href=""><img src="find_designer.png" title="designer" alt="designer"></a>

<!-- [![designer](find_designer.png]() -->


# Agora crie uma janela com um botão:

    Arraste o botão para a janela

<a href=""><img src="pyqt_screen_1.png" title="pyqt_screen1" alt="pyqt_screen1"></a>

<!-- [![pyqt_screen1](pyqt_screen_1.png]() -->

    Salve o arquivo .ui


# Abrir o prompt de comando e localizar a pasta de Scripts do seu Python:

Para localizar, abra o python e execute:

    import os
    import sys
    print(os.path.dirname(sys.executable))

No meu caso, uso o anaconda. Então tenho como resultado:

    cd C:\Users\alca0\Anaconda3\Scripts

Dentro da pasta Scripts deve conter um arquivo chamado:
    
    pyuic5.exe
    
Ele é o responsável em converter o .ui do qtdesigner em .py

Então sempre que modificarmos alguma coisa no designer, teremos que usar o comando abaixo

# Copiar o .ui pelo qtdesigner e converter para .py

    pyuic5 -x "C:\Users\alca0\Documents\Python Scripts\teste.ui" -o C:\Users\alca0\Documents\Python Scripts\teste.py"


# Abrir teste.py no vscode e ser feliz

    Pode usar meu teste.py como exemplo, pois já adicionei uma função para o evento do botão
    
    Pode usar o teste.ui também para converter em .py
