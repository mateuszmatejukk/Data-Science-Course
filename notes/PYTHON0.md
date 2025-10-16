## Wskazówki dla PyCharm - skróty i narzędzia

* **Scratch file (pliki robocze):** Jeśli chcesz szybko wypróbować jakiś fragment kodu lub zrobić notatkę, a nie chcesz tworzyć nowego pliku w projekcie, użyj funkcji Scratch File. Tworzy ona tymczasowy plik poza strukturą projektu (nie będzie dodany do Gita). W PyCharm skrót to 
`Ctrl + Alt + Shift + Insert`

* **Formatowanie i czyszczenie kodu przy commicie:** PyCharm ma opcje automatycznych akcji przed commitem. W oknie Commit możesz zaznaczyć m.in.: Reformat code, Rearrange code, Optimize imports, Perform code cleanup.

-Reformat code – zastosuje autoformatowanie zgodnie ze stylem kodu projektu (np. PEP8 dla Pythona)

-Rearrange code – ewentualnie przeorganizuje kod (zgodnie z regułami, np. kolejność metod, sortowanie atrybutów klas jeśli skonfigurowane)

-Optimize imports – usunie nieużywane importy, posortuje i pogrupuje importy w pliku

-Code cleanup – wykona zdefiniowane inspekcje i szybkie poprawki na kodzie (np. usunie zbędne spacje, poprawi drobne problemy zgodnie z profilem inspekcji)

* **Ręczne reformatowanie kodu:** W dowolnym momencie możesz sformatować aktualnie otwarty plik kodu skrótem *Ctrl + Alt + L* (Windows/Linux) lub *⌥⌘L (macOS)*

* **Komentowanie i odkomentowanie kodu:** Aby szybko zakomentować jedną lub wiele linii kodu, zaznacz je i użyj Ctrl + /).git add Ten skrót przełącza komentowanie – jeśli linie nie były komentowane, doda # na początku, a jeśli były – usunie go

**Polecenia systemowe w terminalu:**

* dir to komenda wyświetlająca zawartość katalogu w Windows (w PowerShell i Cmd).

* ls (list) to odpowiednik na Mac/Linux (oraz w PowerShell również działa alias ls).
Obie służą do wypisania plików i folderów. Możesz użyć ich zamiennie w zależności od shell.

 * **Jupyter Lab Skróty**
    
    - `B` to create new block of code Below current block
    - `A` to do the same Above current block
    - `D+D` to delete block of code
    - `Ctr+Enter` to Run selected cell
    - `Shift+Enter` to Run selected cell
    - `Ctrl+/` to comment line of code
    - `C` to copy selected block of code
    - `V` to paste copied block of code
    - `X` to cut selected block of code
    - `Z` to undo last action
    - `Y` to change block of code to code block
    - `M` to change block of code to markdown block
    - `Shift+M` to merge selected blocks of code
    - `Shift+Arrow Up` to select multiple blocks of code
    - `Ctrl+S` to save notebook

  **Podstawowe typy danych w Pythonie:** 
  
Wbudowane typy proste w Pythonie to:

* **int** – liczby całkowite (np. 1, 42, -7).

* **float** – liczby zmiennoprzecinkowe (np. 3.14, -0.001).

* **bool** – wartości logiczne: True lub False (w rzeczywistości to podtyp int, gdzie True=1, False=0, ale logicznie traktujemy je osobno)

* **str** – łańcuchy znaków (tekst) ujęte w cudzysłowy, np. "hello world"

* **NoneType** – specjalny typ reprezentowany przez singleton None, oznaczający brak wartości.

* **complex** – liczby zespolone (rzadziej używane, postaci np. 3+5j).

* **bytes/bytearray** – typy binarne do przechowywania sekwencji bajtów.

Poza tym mamy typy złożone jak list (lista), tuple (krotka), dict (słownik), set (zbiór) – one jednak są strukturami danych przechowującymi powyższe typy podstawowe lub inne obiekty.