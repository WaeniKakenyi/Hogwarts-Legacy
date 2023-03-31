SELECT "Hogwarts Legacy".names, "Hogwarts Legacy".categories, "Hogwarts Legacy".sub_categories, "Hogwarts Legacy".subject, "students".species, "students".gender
FROM "Hogwarts Legacy"
INNER JOIN "students" ON "Hogwarts Legacy".names = "students".name
UNION
SELECT "Hogwarts Legacy".names, "Hogwarts Legacy".categories, "Hogwarts Legacy".sub_categories, "Hogwarts Legacy".subject, "gang members".species, "gang members".gender
FROM "Hogwarts Legacy"
INNER JOIN "gang members" ON "Hogwarts Legacy".names = "gang members".name
UNION
SELECT "Hogwarts Legacy".names, "Hogwarts Legacy".categories, "Hogwarts Legacy".sub_categories, "Hogwarts Legacy".subject, "other_characters".species, "other_characters".gender
FROM "Hogwarts Legacy"
INNER JOIN "other_characters" ON "Hogwarts Legacy".names = "other_characters".name
UNION
SELECT "Hogwarts Legacy".names, "Hogwarts Legacy".categories, "Hogwarts Legacy".sub_categories, "Hogwarts Legacy".subject, "gang members".species, "gang members".gender
FROM "Hogwarts Legacy"
INNER JOIN "gang members" ON "Hogwarts Legacy".names = "gang members".name
UNION
SELECT "Hogwarts Legacy".names, "Hogwarts Legacy".categories, "Hogwarts Legacy".sub_categories, "Hogwarts Legacy".subject, "staff".species, "staff".gender
FROM "Hogwarts Legacy"
INNER JOIN "staff" ON "Hogwarts Legacy".names = "staff".name
UNION
SELECT "Hogwarts Legacy".names, "Hogwarts Legacy".categories, "Hogwarts Legacy".sub_categories, "Hogwarts Legacy".subject, "villagers".species, "villagers".gender
FROM "Hogwarts Legacy"
INNER JOIN "villagers" ON "Hogwarts Legacy".names = "villagers".name
UNION
SELECT "Hogwarts Legacy".names, "Hogwarts Legacy".categories, "Hogwarts Legacy".sub_categories, "Hogwarts Legacy".subject, "wizards".species, "wizards".gender
FROM "Hogwarts Legacy"
INNER JOIN "wizards" ON "Hogwarts Legacy".names = "wizards".name
