---
title: Koalas, Panda's Scalable Sibling
author: "Adi Polak"
description: "Gental introduction to Koalas"
tags: ["beginners", "apache spark", "koalas","pandas","Kubernetes"]
date: "2021-01-10"
draft: true
---

## What is it all about?

From the [pandas](https://pandas.pydata.org/docs/) docs: _"pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language."_

From the [Koalas](https://koalas.readthedocs.io/en/latest/) docs: _"The Koalas project makes data scientists more productive when interacting with big data, by implementing the pandas DataFrame API on top of Apache Spark."_




First thing first,
## Setting up the environment
You can use any Apache Spark environment that suits you. I often work with Azure Databricks or Synapse as I know both well. \


With [Databricks](https://docs.microsoft.com/en-us/azure/databricks/languages/koalas?WT.mc_id=spark-12578-adpolak), Koalas is pre-installed in Runtime 7.1 and above. With Datrbirkcs Runtime below, checkup [this tutorial](https://docs.microsoft.com/en-us/azure/databricks/languages/koalas?WT.mc_id=spark-12578-adpolak). 

With [Synapse](https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-overview?WT.mc_id=spark-12578-adpolak), you need to provide a `.txt` configuration file that can be used with the command `pip freeze`. The file staractire looks like this:

```txt
{PyPI package name}=={desired version}
{PyPI second package name}=={desired version}
```
Let's see how to get it done:
## How to start Spark pool with Koalas with Synapse:

First, create your Spark pool.
From the Synapse Studio workspace nevigate to `manage` -> `Analytics pools` -> `Apache Spark pools` and click on `+ New` button.

A new UI will menu will pop on the right side of the screen enables you to add information such as size of cluster, auto-scale, name, number of nodes, etc. \
 On the additional setting you can config Spark version, and see the libraries versions that comes built in with the Synapse Spark pool. \
 Such as .NET for Apache Spark.\

👉 .Net for Apache Spark is a library that developed by Microsoft to enable .NET developers easy way to work with Spark.\
Read about it [here](https://docs.microsoft.com/en-us/dotnet/spark/what-is-apache-spark-dotnet?WT.mc_id=spark-12578-adpolak). 


<img class="responsive" src="/images/pandas-synapse-post/create-spark-pool.png" alt="drawing"> \

Right from the `Additional Settings` tab, you can add the `.txt` configuration file.

Create a text file, and copy this line into it:
```
pandas==1.2.0
```
You can upload it while creating the cluster, or add it to an existing cluster.

If you have an existing cluster, from the same `Apache Spark Pools` you can add a new packages. \
Clicking on the `...` 3 dots next to your cluster name will open a menu bar for you, inside there is a Packages option, click on it:

<img class="responsive" src="/images/pandas-synapse-post/manage-packaging-synapse-ui.png" alt="drawing"> \


It will prompt you to a right side bar where you can upload your text file.

<img class="responsive" src="/images/pandas-synapse-post/upload-config-file.png" alt="drawing"> \

Click the Upload button at the top and choose the file you would like to upload.\
Now a new Upload blue button will appear at the bottom, click this too.

The UI will show you the configuration file name and size, all you have to do is to click the blue Apply button at the buttom.\
<img style="width:150px; height: auto;" src="/images/pandas-synapse-post/apply.png"> \

That's it, all set to start coding!  


## Coding

Nevigate to `Develop` -> `+` buttong and create a new Notebook, for `Attach to` choose your spark pool.

We will write our code right here in the notebook so we can run it in an interactive manner and see the results of every operation live.

Setting and importing Koalas:

```python
import pandas as pd
import numpy as np
import databricks.koalas as ks
from pyspark.sql import SparkSession
```