
-- Step 1: Identify all constraints and indexes
SELECT constraint_name, constraint_type 
FROM user_constraints 
WHERE table_name = 'YOUR_TABLE_NAME' AND 
      (column_name = 'YOUR_COLUMN_NAME' OR 
       constraint_type IN ('P', 'R', 'U'));

-- Step 2: Identify all indexes on the column
SELECT index_name 
FROM user_indexes 
WHERE table_name = 'YOUR_TABLE_NAME';


    jvmArgs = ['--add-opens', 'java.base/java.lang=ALL-UNNAMED',
               '--add-opens', 'java.base/java.util=ALL-UNNAMED',
               '--add-opens', 'java.base/java.util.concurrent=ALL-UNNAMED',
               '--add-opens', 'java.base/java.time=ALL-UNNAMED']
