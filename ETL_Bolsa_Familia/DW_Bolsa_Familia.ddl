-- Gerado por Oracle SQL Developer Data Modeler 18.4.0.339.1536
--   em:        2019-04-10 20:20:09 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



CREATE TABLE dm_local (
    id_local   INTEGER NOT NULL,
    nm_local   VARCHAR2(40),
    uf         VARCHAR2(2),
    regiao     VARCHAR2(10)
);

ALTER TABLE dm_local ADD CONSTRAINT dm_local_pk PRIMARY KEY ( id_local );

CREATE TABLE dm_tempo (
    anomes      INTEGER NOT NULL,
    semestre    INTEGER,
    trimestre   INTEGER,
    bimestre    INTEGER
);

ALTER TABLE dm_tempo ADD CONSTRAINT dm_tempo_pk PRIMARY KEY ( anomes );

CREATE TABLE ft_dados (
    id_local           INTEGER NOT NULL,
    id_tempo           INTEGER NOT NULL,
    qnt_beneficiados   INTEGER,
    valor              INTEGER
);

ALTER TABLE ft_dados
    ADD CONSTRAINT ft_dados_dm_local_fk FOREIGN KEY ( id_local )
        REFERENCES dm_local ( id_local );

ALTER TABLE ft_dados
    ADD CONSTRAINT ft_dados_dm_tempo_fk FOREIGN KEY ( id_tempo )
        REFERENCES dm_tempo ( anomes );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             3
-- CREATE INDEX                             0
-- ALTER TABLE                              4
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
