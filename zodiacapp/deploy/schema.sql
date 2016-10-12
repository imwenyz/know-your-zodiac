CREATE TABLE WestZodiac (
	`id`	INTEGER,
	`name`	VARCHAR(50) UNIQUE,
	`image`	VARCHAR(200),
	PRIMARY KEY(`id`)
);
INSERT INTO `WestZodiac` (id,name,image) VALUES (1,'capricorn','static/images/zodiac/w1_capricorn.jpg'),
 (2,'aquarius','static/images/zodiac/w2_aquarius.jpg'),
 (3,'pisces','static/images/zodiac/w3_pisces.jpg'),
 (4,'aries','static/images/zodiac/w4_aries.jpg'),
 (5,'taurus','static/images/zodiac/w5_taurus.jpg'),
 (6,'gemini','static/images/zodiac/w6_gemini.jpg'),
 (7,'cancer','static/images/zodiac/w7_cancer.jpg'),
 (8,'leo','static/images/zodiac/w8_leo.jpg'),
 (9,'virgo','static/images/zodiac/w9_virgo.jpg'),
 (10,'libra','static/images/zodiac/w10_libra.jpg'),
 (11,'scorpio','static/images/zodiac/w11_scorpio.jpg'),
 (12,'sagitarius','static/images/zodiac/w12_sagitarius.jpg');
CREATE TABLE EastZodiac (
	`id`	INTEGER,
	`name`	VARCHAR(50) UNIQUE,
	`image`	VARCHAR(200),
	PRIMARY KEY(`id`)
);
INSERT INTO `EastZodiac` (id,name,image) VALUES (1,'rat','static/images/zodiac/e1_rat.jpg'),
 (2,'ox','static/images/zodiac/e2_ox.jpg'),
 (3,'tiger','static/images/zodiac/e3_tiger.jpg'),
 (4,'rabbit','static/images/zodiac/e4_rabbit.jpg'),
 (5,'dragon','static/images/zodiac/e5_dragon.jpg'),
 (6,'snake','static/images/zodiac/e6_snake.jpg'),
 (7,'horse','static/images/zodiac/e7_horse.jpg'),
 (8,'goat','static/images/zodiac/e8_goat.jpg'),
 (9,'monkey','static/images/zodiac/e9_monkey.jpg'),
 (10,'rooster','static/images/zodiac/e10_rooster.jpg'),
 (11,'dog','static/images/zodiac/e11_dog.jpg'),
 (12,'pig','static/images/zodiac/e12_pig.jpg');
