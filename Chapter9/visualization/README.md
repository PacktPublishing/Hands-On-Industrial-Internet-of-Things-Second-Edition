# Visualization

## Grafana

Query:

    SELECT  time, CAST(Temperature AS DOUBLE) Temperature, CAST(CPU AS DOUBLE) CPU FROM $__database.$__table ORDER BY time DESC LIMIT 300