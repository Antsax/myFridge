# Jatkokehitysideoita

- Ulkoasua olisi voinut viilata
- Reseptejä olisi voinut arvostella
- Resepteihin olisi voinut listata tuotteet, mitä siihen tarvitaan ja niiden määrät
- Tuotteet olisi voinut sijoittaa omiin varastointipaikkoihin (esim. jääkaappi, pakastin, hylly)
- Reseptien tekijät olisi voinut esittää
- Vain reseptien lisääjä voi poistaa oman reseptin
- Validointia ja autorotisointia olis voinut viilata

## CREATE TABLE -lauseet

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_added DATETIME, 
	date_removed DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
```

```
CREATE TABLE recipe (
	id INTEGER NOT NULL, 
	date_added DATETIME, 
	date_removed DATETIME, 
	name VARCHAR(144) NOT NULL, 
	instructions VARCHAR NOT NULL, 
	diet VARCHAR(50), 
	"timeInMinutes" INTEGER, 
	PRIMARY KEY (id)
);
```

```
CREATE TABLE item (
	id INTEGER NOT NULL, 
	date_added DATETIME, 
	date_removed DATETIME, 
	name VARCHAR(144) NOT NULL, 
	vegan BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (vegan IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```

```
CREATE TABLE review (
	id INTEGER NOT NULL, 
	date_added DATETIME, 
	date_removed DATETIME, 
	title VARCHAR(144) NOT NULL, 
	rating INTEGER NOT NULL, 
	comment VARCHAR, 
	item_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(item_id) REFERENCES item (id)
);
```