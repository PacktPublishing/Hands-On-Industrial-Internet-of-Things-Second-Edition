# neo4j asset registry

Structure of the project:
* 📁 src : python code of neo4j client
* docker-compose.yml : docker compose file to start neo4j server

## 🎮 How To

Create assets:

    CREATE  (CT001:Pump {name:'CT001', alias:'Pump-SN-993416776', model:'standard'}),
            (Train1:Section {name:'Production Train 1'}),
            (SydneyPlant:Plant {name:'Plant of ACME in Sydney'}),
            (ACME:Company {name:'ACME International'}),

            (CT001)-[:BELONGING_OF {roles:['Part of']}]->(Train1), 
            (Train1)-[:BELONGING_OF {roles:['Part of']}]->(SydneyPlant), 
            (SydneyPlant)-[:BELONGING_OF {roles:['Managed by']}]->(ACME),

            (TEMP01:Measure {name:'CT001.TEMPERATURE01', alias:'TEMP01', type:'TEMPERATURE', uom:'DEG'}),
            (FLOW01:Measure {name:'CT001.FLOW01', alias:'FLOW01',type:'FLOW', uom:'sm3/sec'}),
            (CPU:Measure {name:'CT001.CPU', alias:'CPU',type:'cpu', uom:'perc', topic:'sensors/edge1/cpu/0',analytic:'ruledag', threshold:'99'}),

            (TEMP01)-[:MEASURE_OF]->(CT001),
            (FLOW01)-[:MEASURE_OF]->(CT001),
            (CPU)-[:MEASURE_OF]->(CT001)

a simple query
        MATCH (M:Measure {topic:"sensors/edge1/cpu/0"})-[BELONGING_OF]->(A) RETURN M.name, M.analytic, A.name