# Databricks notebook source
# MAGIC %python
# MAGIC ## set path to source file in storage, staging
# MAGIC path = 'abfss://stg@alpbpocdapstawedal.dfs.core.windows.net/hh/mes/operations_hist.parquet' 
# MAGIC ##path = 'abfss://stg@alpbproddapstadal.dfs.core.windows.net/grv/dwh/norf/fp_fehlerbeobachtungen.parquet'
# MAGIC 
# MAGIC ## create temporary view on source file
# MAGIC sqlContext.read.parquet(path).createOrReplaceTempView('raw_hh_mes_operations_hist')

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC ## Transform to pandas
# MAGIC df=sqlContext.sql('select op_hist_id from raw_hh_mes_operations_hist').toPandas()

# COMMAND ----------

# MAGIC %python
# MAGIC import pandas as pd
# MAGIC print(df.iloc[1:20,:])