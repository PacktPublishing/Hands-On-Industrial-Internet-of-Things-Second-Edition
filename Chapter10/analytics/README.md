

## Synapse Analytic

Create key

     CREATE CREDENTIAL [iiotbook2]
     WITH IDENTITY = 'SHARED ACCESS SIGNATURE', SECRET = '<your cosmos db key>'

and then

    SELECT JSON_VALUE(Body, '$.temperature') AS temperature
    FROM OPENROWSET(​PROVIDER = 'CosmosDB',
                    CONNECTION = 'Account=iiotbook2;Database=iiotdata',
                    OBJECT = 'iiotdata-container',
                    SERVER_CREDENTIAL = 'iiotbook2'
    ) AS [iiotdata-container]
    WHERE CAST(JSON_VALUE(Body, '$.temperature') AS float) >19