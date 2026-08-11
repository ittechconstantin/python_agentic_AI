-- =============================================================
-- SQL - TEORIE, PAS CU PAS  (sesiunea 26)
-- =============================================================
-- Acesta e primul tau contact cu SQL. Fisierul e RULABIL: deschide-l
-- in DataGrip (vezi 26.sql_mysql_datagrip.md) si ruleaza-l bucata cu
-- bucata, cu Ctrl+Enter (Cmd+Enter pe Mac) pe fiecare comanda -  nu
-- tot fisierul dintr-o data, ca sa vezi rezultatul fiecarui pas.
--
-- CE E SQL, pe scurt (detalii in 26.sql_mysql_datagrip.md):
--   SQL (Structured Query Language) e limbajul prin care VORBESTI cu
--   o baza de date relationala: ii ceri sa creeze tabele, sa
--   adauge/citeasca/modifice/stearga date. Nu e un limbaj de
--   PROGRAMARE ca Python (nu ai if/for in SQL standard) - e un
--   limbaj de CERERI (queries): descrii CE vrei, nu CUM sa faca.
--
-- Construim, PAS CU PAS, o mini baza de date pentru un magazin
-- online: utilizatori, produse, comenzi.
-- =============================================================


-- #############################################################
-- PARTEA 0 - BAZA DE DATE (schema)
-- #############################################################

-- O baza de date (DATABASE, sau SCHEMA - in MySQL sunt sinonime) e
-- un "dulap" separat, cu propriul lui set de tabele. Pe acelasi
-- server MySQL poti avea mai multe baze de date, complet izolate
-- una de alta (o baza pentru cursul asta, alta pentru alt proiect).

-- Stergem baza de date daca exista deja (ca sa pornim curat) si o
-- recream. ATENTIE: DROP DATABASE sterge ABSOLUT TOT ce e in ea -
-- toate tabelele, toate randurile. Il folosim aici doar pentru ca
-- e un fisier de exercitiu, pe care vrem sa-l putem rula de mai
-- multe ori de la zero.

DROP DATABASE IF EXISTS CURS;
CREATE database curs;


-- USE = "de acum inainte, toate comenzile de mai jos se aplica pe
-- ACEASTA baza de date". Fara USE, ar trebui sa scrii `curs.useri`
-- in loc de `useri` la fiecare comanda.
USE curs;


-- #############################################################
-- PARTEA 1 - CREATE TABLE  (creezi o tabela)
-- #############################################################

-- O TABELA e ca o foaie de Excel foarte stricta: are COLOANE fixe,
-- fiecare cu un TIP de data declarat dinainte (nu poti pune text
-- intr-o coloana declarata pentru numere). Fiecare RAND e o
-- inregistrare (un user, un produs...).

CREATE TABLE useri(
    id       INT AUTO_INCREMENT PRIMARY KEY,
    nume     VARCHAR(50) NOT NULL,
    email    VARCHAR(100) NOT NULL UNIQUE,
    varsta   INT,
    creat_la DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Sa desfacem, linie cu linie, ce inseamna fiecare bucata:
--
--   id INT AUTO_INCREMENT PRIMARY KEY
--     - INT            -> coloana tine numere intregi
--     - PRIMARY KEY    -> aceasta coloana IDENTIFICA UNIC fiecare
--                         rand (doua randuri NU pot avea acelasi id;
--                         orice tabela ar trebui sa aiba una)
--     - AUTO_INCREMENT -> MySQL genereaza singur urmatorul numar
--                         (1, 2, 3...) - NU dai tu valoarea la INSERT
--
--   nume VARCHAR(50) NOT NULL
--     - VARCHAR(50)    -> text de pana la 50 de caractere
--     - NOT NULL       -> randul NU poate fi salvat fara o valoare aici
--                         (nu poti lasa numele necompletat)
--
--   email VARCHAR(100) NOT NULL UNIQUE
--     - UNIQUE         ->  doua randuri nu pot avea ACELASI email;
--                         daca incerci, MySQL respinge al doilea INSERT
--
--   varsta INT
--     - fara NOT NULL  -> aici e OK sa lipseasca (poate fi necunoscuta)
--
--   creat_la DATETIME DEFAULT CURRENT_TIMESTAMP
--     - DATETIME               -> data + ora
--     - DEFAULT CURRENT_TIMESTAMP -> daca nu specifici tu o valoare,
--                                    MySQL pune singur data/ora curenta

-- Tipuri de date pe care le vei intalni des:
--   INT / BIGINT     - numere intregi (id, cantitate, varsta)
--   DECIMAL(10,2)    - zecimale EXACTE - pentru PRETURI (10 cifre in
--                      total, 2 dupa virgula). Nu folosi FLOAT pentru
--                      bani - FLOAT rotunjeste aproximativ.
--   VARCHAR(N)       - text scurt, pana la N caractere
--   TEXT             - text lung (descrieri)
--   DATE             - doar data:  2026-05-10
--   DATETIME         - data + ora
--   BOOLEAN          - adevarat/fals

-- Ca sa VEZI structura unei tabele deja create (coloane, tipuri, chei):


-- #############################################################
-- PARTEA 2 - INSERT  (adaugi randuri)
-- #############################################################

-- Un singur rand: specifici in ce COLOANE bagi date, apoi VALUES cu
-- valorile, in ACEEASI ordine. `id` si `creat_la` lipsesc - MySQL le
-- completeaza singur (AUTO_INCREMENT, respectiv DEFAULT).

INSERT INTO useri (nume, email, varsta)
VALUES ('George Popescu', 'george@gmail.com', 29);



-- Mai multe randuri, intr-un singur INSERT (mai eficient decat unul
-- cate unul):

INSERT INTO useri (nume, email, varsta) VALUES
          ('Horia Popescu', 'horia@gmail.com', 29),
          ('Gica Popescu', 'gica@gmail.com', 29),
          ('Florin Popescu', 'florin@gmail.com', 29),
          ('Alex Popescu', 'alex@gmail.com', 29);



-- Ce se intampla daca incalci o regula? MySQL REFUZA randul si arunca
-- o eroare - exact ca `raise` din Python (sesiunea 13): o problema nu
-- trece neobservata.
--   INSERT INTO useri (nume, email) VALUES ('Test', 'ana@example.com');
--   -> Error: Duplicate entry 'ana@example.com' for key 'useri.email'
--   (pentru ca 'ana@example.com' e deja folosit, iar email e UNIQUE)


-- #############################################################
-- PARTEA 3 - SELECT  (citesti date - cea mai folosita comanda)
-- #############################################################

-- SELECT * inseamna "toate coloanele". FROM spune din ce tabela.
SELECT * FROM useri;

-- De obicei nu vrei TOATE coloanele - alegi doar ce te intereseaza:

SELECT nume, email FROM useri;

-- WHERE filtreaza randurile - la fel ca un `if` care decide ce
-- randuri raman. Doar cele pentru care conditia e ADEVARATA apar.

SELECT * FROM useri WHERE varsta = 28;

-- Operatori de comparatie: =   !=   >   <   >=   <=
SELECT nume, varsta FROM useri WHERE varsta >= 29;

-- Combini conditii cu AND (toate trebuie sa fie adevarate) si
-- OR (cel putin una trebuie sa fie adevarata):
SELECT nume, varsta FROM useri WHERE varsta >= 29 AND varsta <=35;

-- BETWEEN e o scurtatura pentru "intre X si Y, inclusiv":

SELECT nume, varsta FROM useri WHERE varsta BETWEEN 25 AND 35;

-- IN verifica daca valoarea e UNA DINTR-O LISTA - scurtatura pentru
-- mai multe OR-uri legate de aceeasi coloana:

SELECT nume, varsta FROM useri WHERE nume IN ('Ana Popescu', 'Gica Popescu');

-- IS NULL / IS NOT NULL - verifici daca o coloana NU are valoare.
-- Atentie: NU folosesti `= NULL` (nu functioneaza in SQL), ci IS NULL.

SELECT nume FROM useri WHERE varsta IS NULL;


-- #############################################################
-- PARTEA 4 - ORDER BY  (sortare)
-- #############################################################

-- Fara ORDER BY, MySQL NU garanteaza nicio ordine anume a randurilor.
-- ORDER BY coloana ASC  = crescator (implicit, poti omite ASC)
-- ORDER BY coloana DESC = descrescator

SELECT nume, varsta FROM useri ORDER BY varsta ASC;
SELECT nume, varsta FROM useri ORDER BY varsta DESC;

-- Poti sorta dupa mai multe coloane - a doua decide doar cand prima
-- e egala la mai multe randuri (ca o "sortare de rezerva"):

SELECT nume, varsta FROM useri  ORDER BY  varsta DESC, nume ASC;

-- LIMIT taie rezultatul la primele N randuri - util cu ORDER BY,
-- pentru "Top N":

SELECT * FROM useri ORDER BY varsta ASC LIMIT 2;

-- #############################################################
-- PARTEA 5 - LIKE  (cauti text dupa un TIPAR, nu exact)
-- #############################################################

-- WHERE nume = 'Ana' cauta un text EXACT. LIKE cauta un TIPAR
-- (pattern), folosind doua simboluri speciale:
--   %  -> "orice, oricat de lung (inclusiv nimic)"
--   _  -> "exact UN caracter, oricare ar fi el"

-- Toti userii al caror nume CONTINE "Popescu", oriunde in text:

SELECT * FROM useri WHERE nume LIKE '%Popescu%';

-- Toti userii al caror nume INCEPE cu "Ana":

SELECT * FROM useri WHERE nume LIKE 'Ana%';

-- Toti userii al caror email SE TERMINA cu "example.com":

SELECT * FROM useri WHERE email LIKE '%example.com';

-- `_` inlocuieste exact UN caracter - util cand stii lungimea sau
-- pozitia, dar nu litera exacta. Ex: nume care au "a" pe pozitia 2:

SELECT nume FROM useri WHERE nume  LIKE '_l%';

-- NOT LIKE = inversul - randurile care NU se potrivesc tiparului:

SELECT * FROM useri WHERE nume NOT LIKE '%Popescu%';


-- #############################################################
-- PARTEA 6 - UPDATE  (modifici randuri existente)
-- #############################################################

-- SET spune ce coloane se schimba si cu ce valori; WHERE spune CARE
-- randuri sunt afectate.
UPDATE useri SET varsta = 20 WHERE nume='Ana Popescu';

-- Verificam ca s-a schimbat:
SELECT * FROM useri WHERE nume = 'Ana Popescu';
-- ATENTIE MAXIMA: UPDATE fara WHERE modifica TOATE randurile din
-- tabela, nu doar unul. Nu exista "undo" automat in SQL simplu - o
-- data rulat, e rulat. Exemplu PERICULOS (NU il rula - e comentat
-- intentionat):
--   UPDATE useri SET varsta = 0;
--   -- asta ar pune varsta 0 la TOTI userii, nu doar la unul!
-- Regula de aur: scrii INTAI un SELECT cu acelasi WHERE, verifici ca
-- randurile afectate sunt cele corecte, ABIA APOI transformi in
-- UPDATE / DELETE.


-- #############################################################
-- PARTEA 7 - DELETE  (stergi randuri)
-- #############################################################

-- Mai intai adaugam un rand "de test", ca sa avem ce sterge fara sa
-- afectam datele reale de mai jos:

-- INSERAM DATE....

-- DELETE FROM tabela WHERE conditie -> sterge DOAR randurile care se
-- potrivesc conditiei.

DELETE FROM useri WHERE nume = 'Ana Popescu';

-- Acelasi pericol ca la UPDATE: DELETE FROM useri; (fara WHERE) ar
-- sterge TOATE randurile din tabela. La fel, verifica intai cu
-- SELECT + acelasi WHERE.


-- #############################################################
-- PARTEA 8 - FOREIGN KEY (FK)  -  legaturi intre tabele
-- #############################################################

-- DE CE nu punem TOTUL intr-un singur tabel urias (user + produsele
-- lui cumparate + preturile, toate pe acelasi rand)? Pentru ca ar
-- trebui sa REPETI aceleasi date iar si iar: numele lui Ana ar aparea
-- de 10 ori daca a facut 10 comenzi, iar daca ii schimbi emailul,
-- trebuie sa-l corectezi in 10 locuri - usor de gresit, usor sa ramana
-- inconsistent. Solutia: date separate, in tabele separate, LEGATE
-- printr-un ID.
--
-- Gandeste-te la o legatura ca la o trimitere: "acest rand din
-- comenzi apartine userului cu id=3" - nu mai copiezi tot userul,
-- doar tii minte NUMARUL lui.

-- Mai intai, o a doua tabela simpla, fara legaturi inca:
CREATE TABLE produse (
                         id   INT AUTO_INCREMENT PRIMARY KEY,
                         nume VARCHAR(100) NOT NULL,
                         pret DECIMAL(10,2) NOT NULL,
                         stoc INT NOT NULL DEFAULT 0
);

INSERT INTO produse (nume, pret, stoc) VALUES
                                           ('Laptop',    4500.00, 10),
                                           ('Mouse',       79.00, 50),
                                           ('Tastatura',  199.00, 25),
                                           ('Monitor',   1200.00,  7),
                                           ('Casti',      350.00, 30);

-- Acum tabela COMENZI, care are nevoie sa "stie" la care user si la
-- care produs se refera fiecare comanda. `user_id` si `produs_id` sunt
-- FOREIGN KEY (FK) - fiecare arata spre `id`-ul (PRIMARY KEY) dintr-o
-- alta tabela.

CREATE TABLE comenzi(
        id        INT AUTO_INCREMENT PRIMARY KEY,
        user_id   INT NOT NULL,
        produs_id INT NOT NULL,
        cantitate INT NOT NULL,

        FOREIGN KEY (user_id) REFERENCES useri(id),
        FOREIGN KEY (produs_id) REFERENCES produse(id)

);


-- Ce castigi cu FOREIGN KEY: MySQL VERIFICA singur legatura. Nu poti
-- insera o comanda cu un user_id care NU EXISTA in useri - exemplu
-- PERICULOS/GRESIT (NU il rula - e comentat intentionat):
--   INSERT INTO comenzi (user_id, produs_id, cantitate) VALUES (999, 1, 1);
--   -> Error: Cannot add or update a child row: a foreign key
--      constraint fails  (nu exista niciun user cu id=999)
-- Asta e "integritate referentiala": FK-ul te protejeaza de date
-- "orfane", care trimit spre ceva ce nu exista.

INSERT INTO comenzi (user_id, produs_id, cantitate) VALUES
                        (2, 1, 2),   -- Ana a comandat 2 Laptop-uri
                        (2, 2, 1),   -- Ana a comandat 1 Mouse
                        (2, 3, 3),   -- Horia a comandat 3 Tastaturi
                        (3, 4, 1),   -- George a comandat 1 Monitor
                        (4, 2, 5);   -- Maria a comandat 5 Mouse-uri

-- FK-ul te protejeaza si invers: nu poti sterge un user care ARE
-- comenzi, ca sa nu ramana comenzi "orfane" (fara user):
--   DELETE FROM useri WHERE nume = 'Ana Popescu';
--   -> Error: Cannot delete or update a parent row: a foreign key
--      constraint fails  (Ana are comenzi in tabela comenzi)
-- Ca sa poti sterge userul, trebuie sa stergi INTAI comenzile lui.


-- #############################################################
-- PARTEA 9 - JOIN  (combini date din mai multe tabele)
-- #############################################################

-- Problema: tabela comenzi are doar NUMERE (user_id=1, produs_id=1),
-- nu nume. Daca vrei un raport CITIBIL ("Ana a comandat Laptop"), ai
-- nevoie sa "lipesti" comenzi cu useri si cu produse, folosind exact
-- legaturile FK -> PK create mai sus. Asta face JOIN.
--
-- INNER JOIN (varianta cea mai comuna, de obicei scrisa doar JOIN):
-- pastreaza DOAR randurile unde legatura chiar exista de-o parte si
-- de alta (aici, mereu - toate comenzile au un user si un produs
-- valide, datorita FK).

SELECT u.nume, p.nume, c.cantitate
FROM comenzi c
JOIN useri u ON u.id = c.user_id
JOIN produse p ON p.id = c.produs_id;


-- Cum se citeste:
--   FROM comenzi c        -> pornim din comenzi, ii spunem alias `c`
--                             (o prescurtare, ca sa nu rescriem
--                             "comenzi." de fiecare data)
--   JOIN useri u ON ...   -> lipim si tabela useri (alias `u`); ON
--                             spune REGULA de potrivire: randul din
--                             useri unde u.id = c.user_id
--   JOIN produse p ON ... -> la fel, lipim si produse (alias `p`)
--   SELECT u.nume, ...    -> alegem ce coloane afisam, din ORICE
--                             tabela lipita; `p.nume AS produs` ii
--                             pune eticheta "produs" in rezultat, ca
--                             sa nu se confunde cu u.nume

-- JOIN se combina normal cu WHERE, ORDER BY - vin DUPA toate JOIN-urile:
SELECT u.nume, p.nume, c.cantitate
FROM comenzi c
         JOIN useri u ON u.id = c.user_id
         JOIN produse p ON p.id = c.produs_id
ORDER BY u.nume;

-- Nota: exista si LEFT JOIN, care pastreaza si randurile FARA
-- potrivire (ex: userii care N-AU nicio comanda inca) - il vei
-- intalni mai des cand faci rapoarte/statistici (GROUP BY),
-- in exercitii si in sesiunile urmatoare.


-- =============================================================
-- DE RETINUT
-- =============================================================
-- - CREATE DATABASE / USE  -> alegi in ce "baza de date" lucrezi
-- - CREATE TABLE           -> defineste coloane + tipuri + reguli
--   (PRIMARY KEY, NOT NULL, UNIQUE, DEFAULT, AUTO_INCREMENT)
-- - INSERT INTO ... VALUES -> adaugi randuri
-- - SELECT ... FROM ... WHERE -> citesti si filtrezi
-- - ORDER BY ... ASC/DESC  -> sortezi;  LIMIT  -> tai la N randuri
-- - LIKE '%text%'          -> cauti dupa TIPAR, nu exact (% = orice,
--   _ = un caracter)
-- - UPDATE ... SET ... WHERE  -> modifici; FARA WHERE = TOT tabelul!
-- - DELETE FROM ... WHERE     -> stergi;  FARA WHERE = TOT tabelul!
-- - FOREIGN KEY (FK)       -> leaga un rand de PK-ul din alta tabela,
--   si IMPIEDICA date orfane (referinte catre ceva inexistent)
-- - JOIN ... ON            -> combina randuri din mai multe tabele
--   acolo unde FK = PK
--
-- Regula de aur, de tinut minte din prima zi: inainte de UPDATE sau
-- DELETE, ruleaza ACELASI WHERE intr-un SELECT si verifica randurile
-- afectate. Abia apoi transformi in UPDATE/DELETE.
--
-- Mai mult: 26.1.exercise.sql
-- =============================================================