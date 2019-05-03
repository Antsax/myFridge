## User-storyt

- As a **student** I would like a **recipe generating functionality** so that I can **manage my fridge**

- As a **fruitarian** I would like **to be able to declare the product type** so that I can **control my diet** without any problems

- As a **programmer** I would like a **safe logging system**

- As a **beer enthusiast** I would like to **generate recepies for people**

- As a **food critic** I would like to able to **products**

## SQL-kyselyt 

 - Käyttäjän rekisteröityminen:
 `INSERT INTO User (name, username, password) VALUES ('name', 'username', 'password')`

  - Käyttäjä voi luoda tuotteen:
  `INSERT INTO Item (name, vegan, account_id) VALUES ('name', 'vegan', 'account_id')`

  - Käyttäjä voi tarkastella tuotteita:
  `SELECT * FROM Item`

  - Käyttäjä voi poistaa tuotteen:
  `DELETE FROM Item WHERE item_id = 'item_id'`

  - Käyttäjä voi tehdä tuotteesta vegaanisen:
  `UPDATE Item SET vegan = 'True'`

  - Käyttäjä voi luoda reseptin:
  `INSERT INTO Recipe (name, instructions, diet, timeInMinutes) VALUES ('name', 'instructions', 'diet', 'timeInMinutes')`

  - Käyttäjä voi tarkastella reseptejä:
  `SELECT * FROM Recipe`

  - Käyttäjä voi poistaa reseptin:
  `DELETE FROM Recipe WHERE recipe_id = 'recipe_id'`

  - Käyttäjä voi luoda tuotteelle arvostelun:
  `INSERT INTO Review (title, rating, comment, item_id) VALUES ('title', 'rating', 'comment', 'item_id')`

  - Käyttäjä voi tarkastella tuotteen arvostelun:
  `SELECT * FROM Review WHERE item_id = 'item_id' AND item_name = 'item_name')`