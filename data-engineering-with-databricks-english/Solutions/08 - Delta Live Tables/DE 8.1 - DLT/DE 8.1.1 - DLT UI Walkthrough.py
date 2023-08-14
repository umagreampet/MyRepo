# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md <i18n value="1fb32f72-2ccc-4206-98d9-907287fc3262"/>
# MAGIC
# MAGIC
# MAGIC # Using the Delta Live Tables UI
# MAGIC
# MAGIC This demo will explore the DLT UI. 
# MAGIC
# MAGIC
# MAGIC ## Learning Objectives
# MAGIC By the end of this lesson, you should be able to:
# MAGIC * Deploy a DLT pipeline
# MAGIC * Explore the resultant DAG
# MAGIC * Execute an update of the pipeline
# MAGIC * Look at metrics

# COMMAND ----------

# MAGIC %md <i18n value="c950ed75-9a93-4340-a82c-e00505222d15"/>
# MAGIC
# MAGIC
# MAGIC ## Run Setup
# MAGIC
# MAGIC The following cell is configured to reset this demo.

# COMMAND ----------

# MAGIC %run ../../Includes/Classroom-Setup-08.1.1

# COMMAND ----------

# MAGIC %md <i18n value="0a719ade-b4b5-49b5-89bf-8fc2b0b7d63c"/>
# MAGIC
# MAGIC
# MAGIC Execute the following cell to print out values that will be used during the following configuration steps.

# COMMAND ----------

DA.print_pipeline_config()

# COMMAND ----------

# MAGIC %md <i18n value="71b010a3-80be-4909-9b44-6f68029f16c0"/>
# MAGIC
# MAGIC
# MAGIC ## Create and Configure a Pipeline
# MAGIC
# MAGIC In this section you will create a pipeline using a notebook provided with the courseware. We'll explore the contents of the notebook in the following lesson.
# MAGIC
# MAGIC 1. Click the **Workflows** button on the sidebar.
# MAGIC 1. Select the **Delta Live Tables** tab.
# MAGIC 1. Click **Create Pipeline**.
# MAGIC 1. Leave **Product Edition** as **Advanced**.
# MAGIC 1. Fill in a **Pipeline Name** - because these names must be unique, we suggest using the **`Pipeline Name`** provided by the cell above.
# MAGIC 1. For **Notebook Libraries**, use the navigator to locate and select the notebook specified above.
# MAGIC    * Even though this document is a standard Databricks Notebook, the SQL syntax is specialized to DLT table declarations.
# MAGIC    * We will be exploring the syntax in the exercise that follows.
# MAGIC 1. Under **Configuration**, add two configuration parameters:
# MAGIC    * Click **Add configuration**, set the "key" to **spark.master** and the "value" to **local[\*]**.
# MAGIC    * Click **Add configuration**, set the "key" to **datasets_path** and the "value" to the value provided in the cell above.
# MAGIC 1. In the **Target** field, enter the database name provided in the cell above.<br/>
# MAGIC This should follow the pattern **`da_<name>_<hash>_dewd_dlt_demo_81`**
# MAGIC    * This field is optional; if not specified, then tables will not be registered to a metastore, but will still be available in the DBFS. Refer to the <a href="https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-user-guide.html#publish-tables" target="_blank">documentation</a> for more information on this option.
# MAGIC 1. In the **Storage location** field, enter the path provided in the cell above.
# MAGIC    * This optional field allows the user to specify a location to store logs, tables, and other information related to pipeline execution. 
# MAGIC    * If not specified, DLT will automatically generate a directory.
# MAGIC 1. For **Pipeline Mode**, select **Triggered**
# MAGIC    * This field specifies how the pipeline will be run.
# MAGIC    * **Triggered** pipelines run once and then shut down until the next manual or scheduled update.
# MAGIC    * **Continuous** pipelines run continuously, ingesting new data as it arrives. Choose the mode based on latency and cost requirements.
# MAGIC 1. For **Pipeline Mode**, select **Triggered**.
# MAGIC 1. Uncheck the **Enable autoscaling** box.
# MAGIC 1. Set the number of **`workers`** to **`0`** (zero).
# MAGIC    * Along with the **spark.master** config above, this will create a **Single Node** clusters.
# MAGIC 1. Enable **Photon Acceleration**.
# MAGIC
# MAGIC The fields **Enable autoscaling**, **Min Workers** and **Max Workers** control the worker configuration for the underlying cluster processing the pipeline. 
# MAGIC
# MAGIC Notice the DBU estimate provided, similar to that provided when configuring interactive clusters.
# MAGIC
# MAGIC Finally, click **Create**.

# COMMAND ----------

# ANSWER

# This function is provided for students who do not 
# want to work through the exercise of creating the pipeline.
DA.create_pipeline()

# COMMAND ----------

DA.validate_pipeline_config()

# COMMAND ----------

# MAGIC %md <i18n value="a7e4b2fc-83a1-4509-8269-9a4c5791de21"/>
# MAGIC
# MAGIC
# MAGIC ## Run a Pipeline
# MAGIC
# MAGIC With a pipeline created, you will now run the pipeline.
# MAGIC
# MAGIC 1. Select **Development** to run the pipeline in development mode. 
# MAGIC   * Development mode provides for more expeditious iterative development by reusing the cluster (as opposed to creating a new cluster for each run) and disabling retries so that you can readily identify and fix errors.
# MAGIC   * Refer to the <a href="https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-user-guide.html#optimize-execution" target="_blank">documentation</a> for more information on this feature.
# MAGIC 2. Click **Start**.
# MAGIC
# MAGIC The initial run will take several minutes while a cluster is provisioned. 
# MAGIC
# MAGIC Subsequent runs will be appreciably quicker.

# COMMAND ----------

# ANSWER

# This function is provided to start the pipeline and  
# block until it has completed, canceled or failed
DA.start_pipeline()

# COMMAND ----------

# MAGIC %md <i18n value="4b92f93e-7a7f-4169-a1d2-9df3ac440674"/>
# MAGIC
# MAGIC
# MAGIC ## Exploring the DAG
# MAGIC
# MAGIC As the pipeline completes, the execution flow is graphed. 
# MAGIC
# MAGIC Selecting the tables reviews the details.
# MAGIC
# MAGIC Select **sales_orders_cleaned**. Notice the results reported in the **Data Quality** section. Because this flow has data expectations declared, those metrics are tracked here. No records are dropped because the constraint is declared in a way that allows violating records to be included in the output. This will be covered in more details in the next exercise.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
