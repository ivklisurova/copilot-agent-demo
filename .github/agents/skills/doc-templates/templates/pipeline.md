# <Pipeline name>

## Purpose
<One or two sentences: what business need this pipeline serves>

## Overview
| Item | Value |
|---|---|
| Type | <batch / streaming / ELT / ingestion> |
| Orchestrator | <Airflow / ADF / Databricks Workflows / Snowflake Tasks> |
| Schedule | <cron or trigger, with timezone> |
| Owner | TBD: confirm with owner |
| Environment(s) | <dev / test / prod> |

## Sources and targets
| Direction | System | Object | Format |
|---|---|---|---|
| Source | <system> | <table / file / topic> | <format> |
| Target | <system> | <table> | <format> |

## Data flow
```mermaid
flowchart LR
```

## Steps
1. <Step name>: <what it does, with file or job reference>
2. ...

## Load pattern
- Mode: <incremental / full / merge>
- Watermark or key: <column>
- Idempotent: <yes / no, and why>

## Dependencies
- Upstream: <pipelines or datasets this needs>
- Downstream: <consumers>

## Data quality checks
| Check | Where | Action on failure |
|---|---|---|

## Sensitive data
- PII columns: <list, or "none found">
- Masking / access controls: <what is applied>
- Retention: TBD: confirm with owner

## Configuration and secrets
- Config location: <file or parameter store>
- Secrets: <where they are stored, never the values>

## Monitoring and alerts
- Alerts sent to: <channel or group>
- Key metrics: <runtime, row counts, freshness>

## Source files
<List of files this document was derived from>