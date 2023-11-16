DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS question;


CREATE TABLE question (
    id SERIAL PRIMARY KEY NOT NULL,
    category VARCHAR(1000) NOT NULL,
    type VARCHAR(1000) NOT NULL,
    difficulty VARCHAR(1000) NOT NULL,
    question VARCHAR(1000) NOT NULL,
    correct_answer VARCHAR(1000) NOT NULL,
    incorrect_answer_1 VARCHAR(1000) NOT NULL,
    incorrect_answer_2 VARCHAR(1000) NOT NULL,
    incorrect_answer_3 VARCHAR(1000) NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    score INTEGER
);

INSERT INTO question (id, category, type, difficulty, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3) VALUES
(1, 'Entertainment: Comics', 'multiple', 'hard', 'When Batman trolls the online chat rooms, what alias does he use?', 'JonDoe297', 'iAmBatman', 'BWayne13', 'BW1129');
