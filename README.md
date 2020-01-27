Aplikacja okienkowa do wizualizacji wyników sieci neuronowej
======
### 1. Cel modułu.
Stworzony graficzny interfejs pozwała na szybką zmianę parametrów, uczenie oraz wizualizację wyników przez zaimplementowaną sieć neuronową. Zaletą modułu jest to, że w dość łatwy sposób można zamienić użyty w danej implementacji typ sieci neuronowej na inny, a następnie na bieżąco wizualizować wyniki zmieniając parametry tylko w jednym pliku XML.
### 2. Opis interfesju graficznego.
Aplikacja okienkowa jest zaimplementowana za pomocą modułu GTK ([więcej o GTK](https://www.gtk.org/)). 
Interfejs zawiera:
- przycisk **File**:
    - **Load Xml Files** - do importowania pliku XML/ParametersNN.xml z parametrami sieci neuronowej i do utworzenia datasetu;
    - **Exports Parameters** - do eksportowania bieżących parametrów sieci neuronowej do pliku txt.
    - **Clear Chart** - do wyczyszczenia bieżących wykresów z okna do wizualizacji wyników.
- główne okno programu:
    - okno do wizualizacji wyników;
    - **Train** - do wytrenowania sieci po zaimportowaniu parametrów z pliku; XML/ParametersNN.xml, a następnie do naniesienia na wykres danych testowych;
    - **Predict** - do nanoszenia wyników zwróconych przez sieć neuronową na wykres;
    - **Stop** - resetuje zaimportowane parametry.


![atl text](https://i.imgur.com/jnUSEWh.png "Rys. 1. Interfejs graficzny.")

![atl text](https://i.imgur.com/YHasoMn.png "Rys. 2. Interfejs graficzny.")

### 3. Opis zaimplementowanej sieci neuronowej.
- Zaimplementowana sieć jest prostą implementacją problemu regresji. 
- Sieć jest perceptronem z jedną warstwą ukrytą. 
- Na wejście są podawane zaszumione wartości X dla jednej z 3. funkcji trygonometrycznych: Sin, Cos lub Tan. Na wyjście - odpowiednio wartości Y.
- Jako zbiór testowy można użyć tę samą (lub inną funkcję trygonometryczną) bez szumu - w ten spób można sprawdzić, czy udało się sieci rozpoznać w zaszumionych danych wykorzystaną funkcję.
- Warstwa wejściowa i wyjściowa jest liniowa i przyjmuje po 1. wartości.
- Użytkownik decyduje o ilości neuronów w ukrytej warstwie oraz o funkcji aktywacji (są 3 do wyboru).
- Sieć zaimplementowano za pomocą biblioteki PyTorch ([oficjalna strona modułu PyTorch](https://pytorch.org/)).

### 4. Instrukcja instalacji. 
0. Zalecana wersja Python to 3.6.
1. Najpierw nałeży zainstałować PyGObject: [link do tutoriala](https://pygobject.readthedocs.io/en/latest/getting_started.html).
2. Utworzyć witrualne środowisko: [link do tutoriala](https://python101.readthedocs.io/pl/latest/env/tools.html).
3. Zainstalować używane moduły w projekcie: `$ pip3 install -r requirements.txt`

### 5. Demo użycia.
1. Użytkownik podaje parametry do pliku .xml w folderze `XML/ParametersNN.xml`
    - Parametry do *NeuralNetwork*:
        - **n_hidden_neurons** - ilość neuronów w warstwie ukrytej, typu `int`.
        - **fun_activation** - funkcja aktywacji, tylko jedna z: `Sigmoid, Tanh, ReLU`.
    - Parametry do *Dataset*:
        - **train_size** - rozmiar zbioru uczącego. Ilość punktów, która będzie wygenerowana losowo do zbioru uczącego. Typ `int`.
        - **x_train_scale_0, x_train_scale_1, x_train_scale_2** - człony przez które zostanie przeliczony *x_train* w celu przeskalowania według wzoru: `x_train = x_train * x_train_scale_0 + x_train_scale_1 - x_train_scale_2`.
        - **y_train_type** - typ funkcji trygonometrycznej zbioru treningowego, do wyboru: `Sin, Cos, Tan`. Następnie do tych wartości automatycznie zostanie dodany odpowiedni szum (w celu zwiększenia trudności rozpoznania funkcji przez sieć neuronową).
        - **test_size** - rozmiar zbioru testowego. Ilość punktów, która będzie wygenerowana do zbioru testowego (bez dodawania szumu). Typ `int`.
        - **y_test_type** - typ funkcji trygonometrycznej zbioru testowego, do wyboru: `Sin, Cos, Tan`.
2. Laduje powyższy XML za pomocą przycisku `File -> Load Xml File`.
3. Uczy sieć i wyświetla zbior testowy na wykresie, przycisk `Train`.
4. Wykorzystuje wytrenowaną sieć do prognozowania i wyrysowuje uzyskane wyniki na wykresie, przycisk `Predict`.
5. Zapisuje użyte parametry do pliku, przycisk `File -> Export Parameters`.
6. Przyciskiem `Stop` resetuje wykresy i sieć.
7. Powtarza czynności z punktów 1-6 dla innych interesujących parametrów.

### 6. Inspiracje
1. https://github.com/SlinkoIgor/Neural_Networks_and_CV, inspiracja do wykorzystanego problemu, który rozwiązuje w danym modułu sieć neuronowa.

