# Runbook: <Pipeline or system name>

## Summary
<What this runbook covers and when to use it>

## Contacts and escalation
| Role | Name / group | When to contact |
|---|---|---|
| Primary on-call | TBD: confirm with owner | First response |
| Escalation | TBD: confirm with owner | If unresolved after <time> |

## Health checks
- How to confirm it is healthy: <query, dashboard or job status>
- Expected run time: <duration>
- Expected output: <row counts, freshness target>

## Common failures
### <Failure name, e.g. "Source file missing">
- **Symptoms:** <alert text or log message>
- **Likely cause:** <cause>
- **Fix:**
  1. <step>
  2. <step>
- **Verify:** <how to confirm it's fixed>

### <Next failure>
...

## Rerun and backfill
- Rerun a failed run: <command or UI steps>
- Backfill a date range: <steps, parameters>
- Safe to rerun? <yes / no, and why>

## Rollback
<How to undo a bad load, such as time travel, restore or reload steps>

## Data impact
- Affected downstream tables or reports: <list>
- Who to notify: <teams>

## Maintenance
- Routine tasks: <cleanup, rotation of credentials, scheduled maintenance>

## Source files
<List of files this document was derived from>