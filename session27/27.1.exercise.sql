-- =============================================================
-- EXERCITII SQL (sesiunea 26)  -  useri / produse / comenzi
-- =============================================================
-- Cum lucrezi:
--   1. Ruleaza intai sectiunea "PREGATIRE" de mai jos (Ctrl+Shift+Enter
--      sau ruleaza tot fisierul pana acolo), ca sa ai date CURATE
--      (aceleasi la fiecare rulare).
--   2. Rezolva pe rand exercitiile: scrie query-ul tau sub linia
--      "-- ZONA TA DE LUCRU" si ruleaza-l cu Ctrl+Enter.
--   3. Compara rezultatul cu "REZULTAT ASTEPTAT".
--   4. Solutiile sunt la finalul fisierului (comentate), pentru verificare.
--
-- Dificultate crescatoare:
--   EX 1-5  (usor)  - CREATE/INSERT, SELECT+LIKE, WHERE+ORDER BY,
--                      ORDER BY+LIMIT, WHERE+IN
--   EX 6-10 (mediu) - UPDATE, INSERT+DELETE, JOIN, JOIN+LIKE, FOREIGN KEY
--
-- Teoria completa, comentata: 26.teorie.sql
-- =============================================================


-- #############################################################
-- PREGATIRE - date curate (ruleaza o data, la inceput)
-- #############################################################
DROP DATABASE IF EXISTS curs;
CREATE DATABASE curs;
USE curs;

CREATE TABLE useri (
                       id     INT AUTO_INCREMENT PRIMARY KEY,
                       nume   VARCHAR(50) NOT NULL,
                       email  VARCHAR(100) NOT NULL UNIQUE,
                       varsta INT
);
CREATE TABLE produse (
                         id   INT AUTO_INCREMENT PRIMARY KEY,
                         nume VARCHAR(100) NOT NULL,
                         pret DECIMAL(10,2) NOT NULL,
                         stoc INT NOT NULL DEFAULT 0
);
CREATE TABLE comenzi (
                         id        INT AUTO_INCREMENT PRIMARY KEY,
                         user_id   INT NOT NULL,
                         produs_id INT NOT NULL,
                         cantitate INT NOT NULL,
                         FOREIGN KEY (user_id)   REFERENCES useri(id),
                         FOREIGN KEY (produs_id) REFERENCES produse(id)
);

INSERT INTO useri (nume, email, varsta) VALUES
                                            ('Ana Popescu',   'ana@example.com',    28),
                                            ('Horia Ionescu', 'horia@example.com',  30),
                                            ('George Pop',    'george@example.com', 40),
                                            ('Maria Vasile',  'maria@example.com',  25),
                                            ('Vlad Popescu',  'vlad@example.com',   35);

INSERT INTO produse (nume, pret, stoc) VALUES
                                           ('Laptop',    4500.00, 10),
                                           ('Mouse',       79.00, 50),
                                           ('Tastatura',  199.00, 25),
                                           ('Monitor',   1200.00,  7),
                                           ('Casti',      350.00, 30);

INSERT INTO comenzi (user_id, produs_id, cantitate) VALUES
                                                        (1, 1, 2),
                                                        (1, 2, 1),
                                                        (2, 3, 3),
                                                        (3, 4, 1),
                                                        (4, 2, 5),
                                                        (5, 5, 2),
                                                        (1, 5, 1);


-- #############################################################
-- EXERCITIUL 1  -  CREATE TABLE + INSERT   (usor)
-- #############################################################
-- CONTEXT:
--   Magazinul vrea sa organizeze produsele pe categorii, incepand
--   cu o tabela simpla, separata, pentru numele categoriilor.
--
-- CE AI DE FACUT:
--   Creeaza o tabela  categorii  cu doua coloane:
--     - id    -> numar intreg, creste singur, cheie primara
--     - nume  -> text de maxim 50 caractere, obligatoriu, unic
--   Apoi insereaza 3 categorii:  'Electronice', 'Accesorii', 'Birou'.
--
-- CERINTE:
--   - foloseste  CREATE TABLE  cu  AUTO_INCREMENT PRIMARY KEY  pentru id
--   - foloseste  NOT NULL UNIQUE  pentru nume
--   - un singur  INSERT  cu toate cele 3 randuri
--
-- REZULTAT ASTEPTAT ( SELECT * FROM categorii; -> 3 randuri):
--   id | nume
--   ---+------------
--   1  | Electronice
--   2  | Accesorii
--   3  | Birou

-- ZONA TA DE LUCRU:

CREATE TABLE categorii(
    id   INT AUTO_INCREMENT PRIMARY KEY,
    nume VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO categorii (nume) VALUES ('Electronice'), ('Accesorii'), ('Birou');


-- #############################################################
-- EXERCITIUL 2  -  SELECT + WHERE + LIKE   (usor)
-- #############################################################
-- CONTEXT:
--   Cineva de la depozit isi aminteste doar ca numele produsului
--   cautat incepe cu litera "M" si vrea o lista rapida, de la ieftin
--   la scump.
--
-- CE AI DE FACUT:
--   Afiseaza  nume  si  pret  pentru produsele al caror nume INCEPE
--   cu litera "M", ordonate CRESCATOR dupa pret.
--
-- CERINTE:
--   - foloseste  WHERE nume LIKE 'M%'
--   - foloseste  ORDER BY pret ASC  (sau doar  ORDER BY pret)
--
-- REZULTAT ASTEPTAT (2 randuri):
--   nume    | pret
--   --------+--------
--   Mouse   |   79.00
--   Monitor | 1200.00

-- ZONA TA DE LUCRU:

SELECT nume FROM categorii WHERE nume LIKE 'M%', ORDER BY pret ASC

-- #############################################################
-- EXERCITIUL 3  -  SELECT + WHERE + ORDER BY   (usor)
-- #############################################################
-- CONTEXT:
--   Echipa de marketing vrea o lista cu userii de varsta "medie", ca sa
--   le trimita o campanie.
--
-- CE AI DE FACUT:
--   Afiseaza  nume  si  varsta  pentru userii cu varsta INTRE 28 si 35
--   (inclusiv), ordonati DESCRESCATOR dupa varsta.
--
-- CERINTE:
--   - foloseste  WHERE ... BETWEEN 28 AND 35  (sau  >= 28 AND <= 35)
--   - foloseste  ORDER BY varsta DESC
--
-- REZULTAT ASTEPTAT (3 randuri):
--   nume            | varsta
--   ----------------+-------
--   Vlad Popescu    | 35
--   Horia Ionescu   | 30
--   Ana Popescu     | 28

-- ZONA TA DE LUCRU:



-- #############################################################
-- EXERCITIUL 4  -  ORDER BY + LIMIT   (usor)
-- #############################################################
-- CONTEXT:
--   Managementul vrea un raport rapid cu cele mai scumpe produse din
--   catalog, ca sa decida ce pune in vitrina principala.
--
-- CE AI DE FACUT:
--   Afiseaza  nume  si  pret  pentru cele mai SCUMPE 3 produse,
--   ordonate descrescator dupa pret.
--
-- CERINTE:
--   - foloseste  ORDER BY pret DESC
--   - foloseste  LIMIT 3
--
-- REZULTAT ASTEPTAT (3 randuri):
--   nume    | pret
--   --------+--------
--   Laptop  | 4500.00
--   Monitor | 1200.00
--   Casti   |  350.00

-- ZONA TA DE LUCRU:



-- #############################################################
-- EXERCITIUL 5  -  SELECT + WHERE + IN   (usor)
-- #############################################################
-- CONTEXT:
--   Suportul vrea datele pentru 3 useri anume, identificati dupa nume,
--   fara sa scrie 3 conditii separate legate cu OR.
--
-- CE AI DE FACUT:
--   Afiseaza  nume  si  email  pentru userii cu numele  'Ana Popescu',
--   'George Pop'  sau  'Vlad Popescu', ordonati alfabetic dupa nume.
--
-- CERINTE:
--   - foloseste  WHERE nume IN ('Ana Popescu', 'George Pop', 'Vlad Popescu')
--   - foloseste  ORDER BY nume
--
-- REZULTAT ASTEPTAT (3 randuri):
--   nume          | email
--   --------------+---------------------
--   Ana Popescu   | ana@example.com
--   George Pop    | george@example.com
--   Vlad Popescu  | vlad@example.com

-- ZONA TA DE LUCRU:



-- #############################################################
-- EXERCITIUL 6  -  UPDATE   (mediu)
-- #############################################################
-- CONTEXT:
--   S-au vandut 5 bucati de Mouse in ultima ora (in afara comenzilor
--   deja inregistrate) - stocul trebuie scazut corespunzator.
--
-- CE AI DE FACUT:
--   Scade stocul produsului "Mouse" cu 5 bucati (stocul actual e 50,
--   deci ar trebui sa ramana 45). NU pune direct valoarea 45 "de mana"
--   - scade-o din valoarea curenta.
--
-- CERINTE:
--   - foloseste  UPDATE produse SET stoc = stoc - 5 WHERE ...
--   - WHERE-ul trebuie sa vizeze DOAR produsul "Mouse"
--
-- REZULTAT ASTEPTAT ( SELECT nume, stoc FROM produse WHERE nume = 'Mouse'; ):
--   nume  | stoc
--   ------+-----
--   Mouse | 45

-- ZONA TA DE LUCRU:



-- #############################################################
-- EXERCITIUL 7  -  INSERT + DELETE   (mediu)
-- #############################################################
-- CONTEXT:
--   Cineva a adaugat din greseala un produs test, la un pret absurd,
--   care nu are inca nicio comanda - trebuie sters complet.
--
-- CE AI DE FACUT:
--   a) Insereaza produsul  ('Produs Test', 9999.99, 1)  in  produse.
--   b) Verifica ca a fost adaugat (SELECT).
--   c) Sterge-l din nou, cautandu-l dupa nume.
--   d) Verifica ca a disparut (SELECT).
--
-- CERINTE:
--   - foloseste  INSERT INTO produse (...) VALUES (...)
--   - foloseste  DELETE FROM produse WHERE nume = 'Produs Test'
--   - NU sterge dupa `id` fix - foloseste WHERE nume = ... (asa merge
--     oricate randuri ar mai fi in tabela)
--
-- REZULTAT ASTEPTAT, la final ( SELECT COUNT(*) FROM produse WHERE nume = 'Produs Test'; ):
--   COUNT(*)
--   --------
--   0

-- ZONA TA DE LUCRU:



-- #############################################################
-- EXERCITIUL 8  -  JOIN + WHERE   (mediu)
-- #############################################################
-- CONTEXT:
--   Depozitul vrea sa vada comenzile "in cantitate mare", cu numele
--   userului si al produsului (nu doar id-urile).
--
-- CE AI DE FACUT:
--   Afiseaza  numele userului,  numele produsului  si  cantitatea  pentru
--   comenzile cu  cantitate >= 2. Ordoneaza dupa numele userului.
--
-- CERINTE:
--   - porneste din  comenzi  si fa  JOIN  cu  useri  si cu  produse
--   - leaga:  useri.id = comenzi.user_id   si   produse.id = comenzi.produs_id
--   - filtreaza cu  WHERE c.cantitate >= 2
--   - ORDER BY dupa numele userului
--
-- REZULTAT ASTEPTAT (4 randuri):
--   nume            | produs     | cantitate
--   ----------------+------------+----------
--   Ana Popescu     | Laptop     | 2
--   Horia Ionescu   | Tastatura  | 3
--   Maria Vasile    | Mouse      | 5
--   Vlad Popescu    | Casti      | 2

-- ZONA TA DE LUCRU:



-- #############################################################
-- EXERCITIUL 9  -  JOIN + WHERE + LIKE   (mediu)
-- #############################################################
-- CONTEXT:
--   Depozitul vrea, de data asta, doar comenzile care contin produse
--   al caror nume are litera "o" in el (Laptop, Mouse, Monitor...).
--
-- CE AI DE FACUT:
--   Afiseaza  numele userului,  numele produsului  si  cantitatea,
--   pentru comenzile unde produsul comandat are litera "o" in nume.
--   Ordoneaza dupa numele userului, apoi dupa numele produsului.
--
-- CERINTE:
--   - JOIN intre  comenzi, useri  si  produse  (ca la exercitiul 8)
--   - filtreaza cu  WHERE p.nume LIKE '%o%'
--   - ORDER BY u.nume, p.nume
--
-- REZULTAT ASTEPTAT (4 randuri):
--   nume            | produs   | cantitate
--   ----------------+----------+----------
--   Ana Popescu     | Laptop   | 2
--   Ana Popescu     | Mouse    | 1
--   George Pop      | Monitor  | 1
--   Maria Vasile    | Mouse    | 5

-- ZONA TA DE LUCRU:



-- #############################################################
-- EXERCITIUL 10  -  FOREIGN KEY - eroare si reparare   (mediu)
-- #############################################################
-- CONTEXT:
--   Un coleg a incercat sa introduca manual o comanda si a gresit
--   user_id-ul. Vrem sa intelegem ce ne protejeaza FK-ul si cum
--   reparam situatia.
--
-- CE AI DE FACUT:
--   a) Ruleaza exact asta si citeste mesajul de eroare primit:
--        INSERT INTO comenzi (user_id, produs_id, cantitate) VALUES (999, 1, 1);
--   b) Scrie, intr-un comentariu, DE CE a aparut eroarea (ce regula,
--      din care tabela, a fost incalcata).
--   c) Insereaza comanda CORECT, de data asta pentru userul cu id 2
--      (Horia Ionescu), pentru produsul cu id 1 (Laptop), cantitate 1.
--   d) Verifica cu un SELECT ca userul 2 are acum DOUA comenzi.
--
-- CERINTE:
--   - la pasul (a), foloseste EXACT comanda de mai sus (o sa dea eroare -
--     e intentionat, nu e o greseala a ta)
--   - la pasul (c), foloseste  INSERT INTO comenzi (user_id, produs_id, cantitate)
--     VALUES (2, 1, 1);
--
-- REZULTAT ASTEPTAT:
--   - pasul (a): eroare de tipul "Cannot add or update a child row: a
--     foreign key constraint fails" (user_id 999 nu exista in useri)
--   - pasul (d), din  SELECT * FROM comenzi WHERE user_id = 2;  ->
--     2 randuri (comanda veche cu produs_id 3, plus cea noua cu produs_id 1)

-- ZONA TA DE LUCRU: