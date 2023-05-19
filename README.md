# uni-se-prj
A project for a software engineering "group" project class from semester 6.

## Technologies used
* **Vue.js 3** (front-end JS framework)
* **Axios** (HTTP client)
* **npm** + **Vite** (for running frontend)
* **FastAPI** (Python API framework)
* **Pydantic** (API data validation)
* **SQLAlchemy 2.0** (ORM)
* **Alembic** (database migration tool)
* **Uvicorn** (for running backend)
* **SQLite 3** (database engine)
* **tclsh/ActiveTcl** (app running scripts)
* *~~Docker, something to run Docker~~ <- only if I'll feel like it and have time*

## Requirements (🇵🇱) / Wymagania
English translation is located below the Polish requirement list.

###### 🅵🅱✅❎

### Wymagania niefunkcjonalne

1. ✅Frontend napisany w frameworku Vue.js 3.
2. ✅Obsługa zapytań HTTP w frontendzie za pomocą biblioteki Axios.
3. ✅Backend napisany Pythonie z frameworkiem FastAPI.
4. ✅Walidacja danych w backendzie za pomocą biblioteki Pydantic.
5. ✅Mapowanie obiektowo-relacyjne (Object-Relational Mapping; ORM) za pomocą biblioteki SQLAlchemy 2.0.
6. ✅Dane użytkownika są przechowywane w bazie danych z silnikiem SQLite 3.
7. ✅Komunikacja między backendem a bazą danych za pomocą narzędzia migracji bazy danych Alembic.
8. ✅Aplikacja webowa przyjmuje postać Single-Page Application (SPA).
9. Strona internetowa aplikacji ładuje się w przeglądarce opartej na technologii Chromium nie dłużej niż 3 sekundy.10. 🅵✅Strona jest podzielona na "kontenery" kalendarza, paska nawigacyjnego oraz bocznej sekcji pomocniczej.

### Wymagania funkcjonalne

1. 🅱❎Użytkownik musi założyć konto w bazie danych w celu korzystania z funkcjonalności kalendarza.
~~2. 🅵✅Strona jest podzielona na "kontenery" kalendarza, paska nawigacyjnego oraz bocznej sekcji pomocniczej.~~
3. 🅵✅Główny kalendarz jest podzielony na 7 dni wybranego tygodnia z etykietami godzin oraz dni tygodnia.
4. Miniaturowy kalendarz wyświetlający jedynie dni, miesiąc i rok oraz etykiety dni tygodnia.
5. Możliwość dodania różnych form zadań i przypomnień.
6. Możliwość usunięcia oraz modyfikacji wybranego zadania lub przypomnienia.
7. Użytkownik może nadać zadaniu lub przypomnieniu tytuł, godzinę rozpoczęcia i zakończenia, opcjonalny styl (np. kolor lub motyw do wybrania) oraz opcjonalny krótki opis/dodatkowe dane.
8. Zadania dłuższe niż 2 dni są wyświetlane poza 7-dniowym kalendarzem.
9. Przypomnienia zajmują ściśle ograniczoną ilość miejsca na 7-dniowym kalendarzu.
10. Aplikacja wyświetla jedynie tyle danych w komponencie ile się zmieści.
11. Komponent zadania można kliknąć aby wyświetlić w oddzielnym panelu całość danych zawieranych przez zadanie.
12. Zadania można łączyć w grupy zadań.
13. Można wyświetlić listę zadań i grup zadań w oddzielnej stronie wewnątrz aplikacji.
14. Można podświetlić lub wyświetlić/ukryć zadania z wybranej grupy zadań.
15. Zadaniom można nadawać priorytety, które są wykorzystywane przez aplikację do sugerowania lub podkreślania istotności wybranych zadań.
16. 🅱❎Logowanie użytkownika odbywa się za pomocą JSON Web Token-a.

## Harmonogram/Schedule

##### **Legenda/legend:**
**`F5`** = **F**unctional requirement 5. (wymaganie funkcjonalne 5.).

**`NF7`** = **N**on-**F**unctional requirement 7. (wymaganie niefunkcjonalne 7.).

**`FE.F5`** = **F**ront-**E**nd side of functional requirement 5. (wymaganie funkcjonalne frontendu 5.).

**`BE.F6`** = **B**ack-**E**nd side of functional requirement 6. (wymaganie funkcjonalne backendu 6.).

**`FEBE.F13`** = **F**ront-**E**nd & **B**ack-**E**nd side of functional requirement 13. (wymaganie funkcjonalne 13. dla frontendu i backendu).

| Data/Date | Zajęcia/Class | ToDo by EOC[^1] |
| --- | --- | --- |
| `13/04/2023` | ***I***st | General project documentation |
| `12/05/2023` | ***II***nd | Prepare **`NF1`**, **`NF2`**, **`NF3`**, **`NF4`**, **`NF5`**, **`NF6`**, **`NF7`**; implement **`NF8`** |
| `19/05/2023` | ***III***rd | Implement **`NF2`**, **`FE.F3`**, **`FE.F4`**, **`FEBE.F5`**, **`FEBE.F6`**, **`FE.F7`**, **`FE.F9`** |d
| `26/05/2023` | ***IV***th | Implement **`FE.F8`**, **`FE.F10`**, **`FE.F11`**, **`FEBE.F12`**, **`FE.F14`**, **`FEBE.F15`** |
| `30/05/2023` | ***V***th | Implement **`FE.F13`**, **`FEBE.F15`**; begin impementing **`FEBE.F13`**, **`FEBE.F16`** |
| `02/06/2023` | ***VI***th | Implement **`FEBE.F13`**, **`FEBE.F16`** |
| `16/06/2023` | ***VII***th | Testing |
| `21/06/2023` | ***VIII***th | Project presentation |

[^1]: To do by the **E**nd **O**f a **C**lass (do zakończenia pod koniec danych zajęć).

## Database model



## Requirements
### Non-functional requirements

1. Translation WIP

### Functional requirements

* Translation WIP

## Project members

**Chief Technology Officer**: me

**Project Manager**: me

**Software Analyst**: me

**Frontend Engineer**: me

**Backend Engineer**: me

**Quality Assurance Engineer**: me

**UI/UX Designer**: me

**Graphic Design "Artist"**: me

**Cafe Barista**: me

**Scrum/Agile Master**: we don't need this guy.
