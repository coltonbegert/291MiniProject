--
-- File generated with SQLiteStudio v3.0.7 on Thu Oct 27 09:19:04 2016
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: staff
DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
    staff_id CHAR (5),
    role     CHAR (1),
    name     CHAR (15),
    login    CHAR (8),
    password CHAR (30),
    PRIMARY KEY (
        staff_id
    )
);



INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '1',
                      'D',
                      'Timothy Stevens',
                      'Doctor',
                      '2e81233d2741064532015b6c200bb5dba058a14b4ae4e3fc4c48a36b'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '2',
                      'D',
                      'Colt Barlow',
                      'Colt',
                      '6d5094db82a6425db1b7725c9b8e6c892797e67f3a39f365347ba937'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '3',
                      'D',
                      'Beck Spears',
                      'Beck',
                      '69051a0851ddabbb9a3321d190c7802df7ec9c810bbd10f859985668'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '4',
                      'D',
                      'Flavia Gaines',
                      'Flavia',
                      'd4f32c37817fe26d92a9b449823e441ceb7784bdc1b125395ebd94c9'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '5',
                      'D',
                      'Lavinia Gutierrez',
                      'Lavinia',
                      '548ea99af32ba2a0a9b1a4f6e099f94822144921abaa14a68824cce4'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '7',
                      'N',
                      'Ariel Dillon',
                      'Ariel',
                      'cf5b7c60dc4e0703c5c7bdb40a8392100f178f88c6cdf0557fb58277'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '8',
                      'N',
                      'Oren Witt',
                      'Nurse',
                      '99faea5cc78ce96c261d4b6cccbb10ea28df7da217dfbafe772b08c8'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '9',
                      'N',
                      'Adrian Andrews',
                      'Adrian',
                      '7cea0f70c11eff7458a3be58ad88daa0c071df152c5b05fc8211f6dd'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '10',
                      'N',
                      'Aphrodite Glass',
                      'Aphrodite',
                      '0b7b7edefe35b45dd5a327c0bc3599f5d7c1f8beb4efb06f72c995c5'
                  );

INSERT INTO staff (
                      staff_id,
                      role,
                      name,
                      login,
                      password
                  )
                  VALUES (
                      '11',
                      'A',
                      'Xavier Cunningham',
                      'Admin',
                      '2589b66a2e8652e06bffd9a0bc7491edda66716b411e77379627cc3a'
                  );


-- Table: inferredallergies
DROP TABLE IF EXISTS inferredallergies;

CREATE TABLE inferredallergies (
    alg       CHAR (15),
    canbe_alg CHAR (15),
    PRIMARY KEY (
        alg,
        canbe_alg
    ),
    FOREIGN KEY (
        alg
    )
    REFERENCES drugs,
    FOREIGN KEY (
        canbe_alg
    )
    REFERENCES drugs
);

INSERT INTO inferredallergies (
                                  alg,
                                  canbe_alg
                              )
                              VALUES (
                                  'Advil',
                                  'Adult Cold'
                              );

INSERT INTO inferredallergies (
                                  alg,
                                  canbe_alg
                              )
                              VALUES (
                                  'Aleve',
                                  'methylphenidate'
                              );

INSERT INTO inferredallergies (
                                  alg,
                                  canbe_alg
                              )
                              VALUES (
                                  'methylphenidate',
                                  'Advil'
                              );

INSERT INTO inferredallergies (
                                  alg,
                                  canbe_alg
                              )
                              VALUES (
                                  'methylphenidate',
                                  'niacinis'
                              );

INSERT INTO inferredallergies (
                                  alg,
                                  canbe_alg
                              )
                              VALUES (
                                  'niacinis',
                                  'Interferon-gamma'
                              );


-- Table: medications
DROP TABLE IF EXISTS medications;

CREATE TABLE medications (
    hcno      CHAR (5),
    chart_id  CHAR (5),
    staff_id  CHAR (5),
    mdate     DATE,
    start_med DATE,
    end_med   DATE,
    amount    INT,
    drug_name CHAR (15),
    PRIMARY KEY (
        hcno,
        chart_id,
        staff_id,
        mdate,
        drug_name
    ),
    FOREIGN KEY (
        hcno
    )
    REFERENCES patients (hcno),
    FOREIGN KEY (
        chart_id
    )
    REFERENCES charts,
    FOREIGN KEY (
        staff_id
    )
    REFERENCES staff,
    FOREIGN KEY (
        drug_name
    )
    REFERENCES drugs
);

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '37654',
                            '23',
                            '3',
                            '2014-04-03 08:04:08',
                            '2014-04-03 08:04:08',
                            '2014-04-13 08:04:08',
                            230,
                            'amphetamine'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '37654',
                            '3',
                            '4',
                            '2013-02-04 11:02:03',
                            '2013-02-04 11:02:03',
                            '2013-02-14 11:02:03',
                            30,
                            'Adult Cold'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '37654',
                            '33',
                            '5',
                            '2015-02-12 01:02:35',
                            '2015-02-12 01:02:35',
                            '2015-02-22 01:02:35',
                            330,
                            'Penicillin'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '50618',
                            '1',
                            '3',
                            '2013-01-08 07:01:54',
                            '2013-01-08 07:01:54',
                            '2013-01-18 07:01:54',
                            10,
                            'Interferon-gamma'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '50618',
                            '21',
                            '4',
                            '2014-01-23 01:01:25',
                            '2014-01-23 01:01:25',
                            '2014-02-02 01:01:25',
                            210,
                            'Advil'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '50618',
                            '31',
                            '5',
                            '2015-02-11 04:02:54',
                            '2015-02-11 04:02:54',
                            '2015-02-21 04:02:54',
                            310,
                            'Aleve'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '50618',
                            '36',
                            '1',
                            '2016-07-06 03:07:46',
                            '2016-07-06 03:07:46',
                            '2016-07-16 03:07:46',
                            360,
                            'niacinis'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '50618',
                            '39',
                            '2',
                            '2016-07-19 07:07:27',
                            '2016-07-19 07:07:27',
                            '2016-07-29 07:07:27',
                            390,
                            'methylphenidate'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '87230',
                            '2',
                            '1',
                            '2013-02-01 11:02:18',
                            '2013-02-01 11:02:18',
                            '2013-02-11 11:02:18',
                            20,
                            'amphetamine'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '87230',
                            '22',
                            '2',
                            '2014-03-24 01:03:00',
                            '2014-03-24 01:03:00',
                            '2014-04-03 01:03:00',
                            220,
                            'Adult Cold'
                        );

INSERT INTO medications (
                            hcno,
                            chart_id,
                            staff_id,
                            mdate,
                            start_med,
                            end_med,
                            amount,
                            drug_name
                        )
                        VALUES (
                            '87230',
                            '32',
                            '1',
                            '2015-02-11 11:02:24',
                            '2015-02-11 11:02:24',
                            '2015-02-21 11:02:24',
                            320,
                            'Penicillin'
                        );


-- Table: reportedallergies
DROP TABLE IF EXISTS reportedallergies;

CREATE TABLE reportedallergies (
    hcno      CHAR (5),
    drug_name CHAR (15),
    PRIMARY KEY (
        hcno,
        drug_name
    ),
    FOREIGN KEY (
        hcno
    )
    REFERENCES patients,
    FOREIGN KEY (
        drug_name
    )
    REFERENCES drugs
);

INSERT INTO reportedallergies (
                                  hcno,
                                  drug_name
                              )
                              VALUES (
                                  '37654',
                                  'methylphenidate'
                              );

INSERT INTO reportedallergies (
                                  hcno,
                                  drug_name
                              )
                              VALUES (
                                  '50618',
                                  'Advil'
                              );

INSERT INTO reportedallergies (
                                  hcno,
                                  drug_name
                              )
                              VALUES (
                                  '50618',
                                  'methylphenidate'
                              );

INSERT INTO reportedallergies (
                                  hcno,
                                  drug_name
                              )
                              VALUES (
                                  '87230',
                                  'Adult Cold'
                              );

INSERT INTO reportedallergies (
                                  hcno,
                                  drug_name
                              )
                              VALUES (
                                  '87230',
                                  'amphetamine'
                              );


-- Table: diagnoses
DROP TABLE IF EXISTS diagnoses;

CREATE TABLE diagnoses (
    hcno      CHAR (5),
    chart_id  CHAR (5),
    staff_id  CHAR (5),
    ddate     DATE,
    diagnosis CHAR (20),
    PRIMARY KEY (
        hcno,
        chart_id,
        staff_id,
        diagnosis,
        ddate
    ),
    FOREIGN KEY (
        hcno
    )
    REFERENCES patients (hcno),
    FOREIGN KEY (
        chart_id
    )
    REFERENCES charts,
    FOREIGN KEY (
        staff_id
    )
    REFERENCES staff
);

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '37654',
                          '23',
                          '3',
                          '2014-04-03 08:04:08',
                          'Melanoma'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '37654',
                          '3',
                          '4',
                          '2013-02-04 11:02:03',
                          'Menopause'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '37654',
                          '33',
                          '5',
                          '2015-02-12 01:02:35',
                          'Rheumatoid Arthritis'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '50618',
                          '1',
                          '3',
                          '2013-01-08 07:01:54',
                          'Appendicitis'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '50618',
                          '21',
                          '4',
                          '2014-01-23 01:01:25',
                          'Asthma in Children'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '50618',
                          '31',
                          '5',
                          '2015-02-11 04:02:54',
                          'Common Cold'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '50618',
                          '36',
                          '1',
                          '2016-07-06 03:07:46',
                          'Crohn''s Disease'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '50618',
                          '39',
                          '2',
                          '2016-07-19 07:07:27',
                          'Depression'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '87230',
                          '2',
                          '1',
                          '2013-02-01 11:02:18',
                          'Common Cold'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '87230',
                          '22',
                          '2',
                          '2014-03-24 01:03:00',
                          'Crohn''s Disease'
                      );

INSERT INTO diagnoses (
                          hcno,
                          chart_id,
                          staff_id,
                          ddate,
                          diagnosis
                      )
                      VALUES (
                          '87230',
                          '32',
                          '1',
                          '2015-02-11 11:02:24',
                          'Depression'
                      );


-- Table: symptoms
DROP TABLE IF EXISTS symptoms;

CREATE TABLE symptoms (
    hcno     CHAR (5),
    chart_id CHAR (5),
    staff_id CHAR (5),
    obs_date DATE,
    symptom  CHAR (15),
    PRIMARY KEY (
        hcno,
        chart_id,
        staff_id,
        symptom,
        obs_date
    ),
    FOREIGN KEY (
        hcno
    )
    REFERENCES patients (hcno),
    FOREIGN KEY (
        chart_id
    )
    REFERENCES charts,
    FOREIGN KEY (
        staff_id
    )
    REFERENCES staff
);

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '37654',
                         '23',
                         '4',
                         '2014-04-03 08:04:08',
                         'Back pain'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '37654',
                         '3',
                         '3',
                         '2013-02-04 11:02:03',
                         'Abdominal pain.'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '37654',
                         '33',
                         '5',
                         '2015-02-12 01:02:35',
                         'agnosia'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '50618',
                         '1',
                         '1',
                         '2013-01-08 07:01:54',
                         'Abdominal pain.'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '50618',
                         '21',
                         '9',
                         '2014-01-23 01:01:25',
                         'Abdominal pain.'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '50618',
                         '31',
                         '3',
                         '2015-02-11 04:02:54',
                         'Nauseated'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '50618',
                         '36',
                         '7',
                         '2016-07-06 03:07:46',
                         'headache'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '50618',
                         '39',
                         '8',
                         '2016-07-19 07:07:27',
                         'headache'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '87230',
                         '2',
                         '2',
                         '2013-02-01 11:02:18',
                         'Abdominal pain.'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '87230',
                         '22',
                         '10',
                         '2014-03-24 01:03:00',
                         'Abdominal pain.'
                     );

INSERT INTO symptoms (
                         hcno,
                         chart_id,
                         staff_id,
                         obs_date,
                         symptom
                     )
                     VALUES (
                         '87230',
                         '32',
                         '4',
                         '2015-02-11 11:02:24',
                         'Short of breath'
                     );


-- Table: dosage
DROP TABLE IF EXISTS dosage;

CREATE TABLE dosage (
    drug_name  CHAR (15),
    age_group  CHAR (5),
    sug_amount INT,
    PRIMARY KEY (
        drug_name,
        age_group
    ),
    FOREIGN KEY (
        drug_name
    )
    REFERENCES drugs
);

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Adult Cold',
                       '20-29',
                       250
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Adult Cold',
                       '60-69',
                       20
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Adult Cold',
                       '30-39',
                       200
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Adult Cold',
                       '40-49',
                       150
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Adult Cold',
                       '50-59',
                       50
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Adult Cold',
                       '40-59',
                       100
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Advil',
                       '20-29',
                       250
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Advil',
                       '60-69',
                       20
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Advil',
                       '30-39',
                       200
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Advil',
                       '40-49',
                       150
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Advil',
                       '50-59',
                       50
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Advil',
                       '40-59',
                       100
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Aleve',
                       '20-29',
                       250
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Aleve',
                       '60-69',
                       20
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Aleve',
                       '30-39',
                       200
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Aleve',
                       '40-49',
                       150
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Aleve',
                       '50-59',
                       50
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Aleve',
                       '40-59',
                       100
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Interferon-gamma',
                       '20-29',
                       250
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Interferon-gamma',
                       '60-69',
                       20
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Interferon-gamma',
                       '30-39',
                       200
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Interferon-gamma',
                       '40-49',
                       150
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Interferon-gamma',
                       '50-59',
                       50
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Interferon-gamma',
                       '40-59',
                       100
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Penicillin',
                       '20-29',
                       250
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Penicillin',
                       '60-69',
                       20
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Penicillin',
                       '30-39',
                       200
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Penicillin',
                       '40-49',
                       150
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Penicillin',
                       '50-59',
                       50
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'Penicillin',
                       '40-59',
                       100
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'amphetamine',
                       '20-29',
                       250
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'amphetamine',
                       '60-69',
                       20
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'amphetamine',
                       '30-39',
                       200
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'amphetamine',
                       '40-49',
                       150
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'amphetamine',
                       '50-59',
                       50
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'amphetamine',
                       '40-59',
                       100
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'methylphenidate',
                       '20-29',
                       250
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'methylphenidate',
                       '60-69',
                       20
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'methylphenidate',
                       '30-39',
                       200
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'methylphenidate',
                       '40-49',
                       150
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'methylphenidate',
                       '50-59',
                       50
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'methylphenidate',
                       '40-59',
                       100
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'niacinis',
                       '20-29',
                       250
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'niacinis',
                       '60-69',
                       20
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'niacinis',
                       '30-39',
                       200
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'niacinis',
                       '40-49',
                       150
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'niacinis',
                       '50-59',
                       50
                   );

INSERT INTO dosage (
                       drug_name,
                       age_group,
                       sug_amount
                   )
                   VALUES (
                       'niacinis',
                       '40-59',
                       100
                   );


-- Table: charts
DROP TABLE IF EXISTS charts;

CREATE TABLE charts (
    chart_id CHAR (5),
    hcno     CHAR (5),
    adate    DATE,
    edate    DATE,
    PRIMARY KEY (
        chart_id
    ),
    FOREIGN KEY (
        hcno
    )
    REFERENCES patients (hcno) 
);

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '1',
                       '50618',
                       '2013-01-08 07:01:54',
                       '2013-02-01 11:02:18'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '2',
                       '87230',
                       '2013-02-01 11:02:18',
                       '2013-02-04 11:02:03'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '3',
                       '37654',
                       '2013-02-04 11:02:03',
                       '2013-02-13 06:02:22'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '21',
                       '50618',
                       '2014-01-23 01:01:25',
                       '2014-03-24 01:03:00'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '22',
                       '87230',
                       '2014-03-24 01:03:00',
                       '2014-04-03 08:04:08'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '23',
                       '37654',
                       '2014-04-03 08:04:08',
                       '2014-04-21 04:04:51'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '31',
                       '50618',
                       '2015-02-11 04:02:54',
                       '2015-02-11 11:02:24'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '32',
                       '87230',
                       '2015-02-11 11:02:24',
                       '2015-02-12 01:02:35'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '33',
                       '37654',
                       '2015-02-12 01:02:35',
                       '2015-02-14 03:02:50'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '36',
                       '50618',
                       '2016-07-06 03:07:46',
                       '2016-07-06 12:07:27'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '37',
                       '87230',
                       '2016-07-06 12:07:27',
                       NULL
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '38',
                       '37654',
                       '2016-07-13 08:07:25',
                       NULL
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '39',
                       '50618',
                       '2016-07-19 07:07:27',
                       '2016-07-20 07:07:37'
                   );

INSERT INTO charts (
                       chart_id,
                       hcno,
                       adate,
                       edate
                   )
                   VALUES (
                       '40',
                       '50618',
                       '2016-07-20 07:07:37',
                       NULL
                   );


-- Table: patients
DROP TABLE IF EXISTS patients;

CREATE TABLE patients (
    hcno      CHAR (5),
    name      CHAR (15),
    age_group CHAR (5),
    address   CHAR (30),
    phone     CHAR (10),
    emg_phone CHAR (10),
    PRIMARY KEY (
        hcno
    )
);

INSERT INTO patients (
                         hcno,
                         name,
                         age_group,
                         address,
                         phone,
                         emg_phone
                     )
                     VALUES (
                         '50618',
                         'Quin Parker',
                         '20-29',
                         'Ap #841-2564 Quis, St.',
                         '1-599-610-7934',
                         '1-529-273-7818'
                     );

INSERT INTO patients (
                         hcno,
                         name,
                         age_group,
                         address,
                         phone,
                         emg_phone
                     )
                     VALUES (
                         '87230',
                         'Donna Levy',
                         '60-69',
                         '7127 Dolor. Rd.',
                         '1-331-290-2620',
                         '1-904-392-0322'
                     );

INSERT INTO patients (
                         hcno,
                         name,
                         age_group,
                         address,
                         phone,
                         emg_phone
                     )
                     VALUES (
                         '37654',
                         'Chastity Chaney',
                         '30-39',
                         '6624 In St.',
                         '1-430-548-7146',
                         '1-329-348-5252'
                     );


-- Table: drugs
DROP TABLE IF EXISTS drugs;

CREATE TABLE drugs (
    drug_name CHAR (15),
    category  CHAR (25),
    PRIMARY KEY (
        drug_name
    )
);

INSERT INTO drugs (
                      drug_name,
                      category
                  )
                  VALUES (
                      'Penicillin',
                      'Antibiotics'
                  );

INSERT INTO drugs (
                      drug_name,
                      category
                  )
                  VALUES (
                      'Interferon-gamma',
                      'Anti-Viral'
                  );

INSERT INTO drugs (
                      drug_name,
                      category
                  )
                  VALUES (
                      'Advil',
                      'anti-inflammatory'
                  );

INSERT INTO drugs (
                      drug_name,
                      category
                  )
                  VALUES (
                      'Aleve',
                      'anti-inflammatory'
                  );

INSERT INTO drugs (
                      drug_name,
                      category
                  )
                  VALUES (
                      'niacinis',
                      'Vitamin B'
                  );

INSERT INTO drugs (
                      drug_name,
                      category
                  )
                  VALUES (
                      'methylphenidate',
                      'Stimulants'
                  );

INSERT INTO drugs (
                      drug_name,
                      category
                  )
                  VALUES (
                      'amphetamine',
                      'Stimulants'
                  );

INSERT INTO drugs (
                      drug_name,
                      category
                  )
                  VALUES (
                      'Adult Cold',
                      'anti-inflammatory'
                  );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
