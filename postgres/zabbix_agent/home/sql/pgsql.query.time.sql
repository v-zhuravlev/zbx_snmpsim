WITH T AS
    (SELECT db.datname,
            coalesce(T.etime_query, 0) etime_query,
            coalesce(T.etime_tx, 0) etime_tx,
            coalesce(T.etime_maintenance, 0) etime_maintenance,
            coalesce(T.itime_query, 0) itime_query,
            coalesce(T.itime_tx, 0) itime_tx,
            coalesce(T.itime_maintenance, 0) itime_maintenance
    FROM pg_database db NATURAL
    LEFT JOIN (
        SELECT datname,
            extract(epoch FROM now())::integer ts,
            coalesce(max(extract('epoch' FROM (clock_timestamp() - query_start) * 1000) * (state NOT IN ('idle', 'idle in transaction', 'idle in transaction (aborted)') AND query !~* E'^(\s*(--[^\\n]*\\n|/\\*.*\\*/|\\n))*(autovacuum|VACUUM|ANALYZE|REINDEX|CLUSTER|CREATE|ALTER|TRUNCATE|DROP)')::integer), 0) etime_query,
            coalesce(max(extract('epoch' FROM (clock_timestamp() - query_start) * 1000) * (state NOT IN ('idle') AND query !~* E'^(\\s*(--[^\\n]*\\n|/\\*.*\\*/|\\n))*(autovacuum|VACUUM|ANALYZE|REINDEX|CLUSTER|CREATE|ALTER|TRUNCATE|DROP)')::integer), 0) etime_tx,
            coalesce(max(extract('epoch' FROM (clock_timestamp() - query_start) * 1000) * (state NOT IN ('idle') AND query ~* E'^(\\s*(--[^\\n]*\\n|/\\*.*\\*/|\\n))*(autovacuum|VACUUM|ANALYZE|REINDEX|CLUSTER|CREATE|ALTER|TRUNCATE|DROP)')::integer), 0) etime_maintenance,
            coalesce(sum(extract('epoch' FROM (clock_timestamp() - query_start) * 1000) * (state NOT IN ('idle', 'idle in transaction', 'idle in transaction (aborted)') AND query !~* E'^(\\s*(--[^\\n]*\\n|/\\*.*\\*/|\\n))*(autovacuum|VACUUM|ANALYZE|REINDEX|CLUSTER|CREATE|ALTER|TRUNCATE|DROP)')::integer), 0) itime_query,
            coalesce(sum(extract('epoch' FROM (clock_timestamp() - query_start) * 1000) * (state NOT IN ('idle') AND query !~* E'^(\\s*(--[^\\n]*\\n|/\\*.*\\*/|\\n))*(autovacuum|VACUUM|ANALYZE|REINDEX|CLUSTER|CREATE|ALTER|TRUNCATE|DROP)')::integer), 0) itime_tx,
            coalesce(sum(extract('epoch' FROM (clock_timestamp() - query_start) * 1000) * (state NOT IN ('idle') AND query ~* E'^(\\s*(--[^\\n]*\\n|/\\*.*\\*/|\\n))*(autovacuum|VACUUM|ANALYZE|REINDEX|CLUSTER|CREATE|ALTER|TRUNCATE|DROP)')::integer), 0) itime_maintenance
        FROM pg_stat_activity
        WHERE pid <> pg_backend_pid()
        GROUP BY 1) T
    WHERE NOT db.datistemplate )
SELECT json_object_agg(datname, row_to_json(T))
FROM T