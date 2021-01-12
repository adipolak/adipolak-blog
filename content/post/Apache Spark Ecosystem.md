---
title: Apache Spark Ecosystem Jan 2021 Highlights
author: "Adi Polak"
description: "Ever growing Open Source Ecosystem"
tags: ["open-source", "apache spark", "koalas","pandas","delta lake","ray","ray on spark","analytic zoo"]
date: "2021-01-12"
draft: false
---

If you've been reading here for a while, you know that I'm a big fan of Apache Spark and have been using it for more than 8 years.\
Apache Spark is continually growing. It started as part of the Hadoop family,\
but with [the slow death of hadoop](https://medium.com/@acmurthy/hadoop-is-dead-long-live-hadoop-f22069b264ac) and the fast growth of Kubernetes, many new tools and connectors have emerged.

Let's take a look at them:

## **Ray:**
<img class="responsive" src=" https://github.com/ray-project/ray/raw/master/doc/source/images/ray_header_logo.png" alt="drawing">


 Ray is an open source, python based framework for building distributed applications.
 Their main audience is ML developers and Data Scientists who would like to accelerate their machine learning workloads using distributed computing.
Ray was open sourced by UC Berkly [RISELab](https://rise.cs.berkeley.edu/), the same lab who created the [AMPLab](https://amplab.cs.berkeley.edu/) project, where Apache Spark was created.
BTW, if you are curious, their next big 5 years project is all about **Real-time Intelligence with Secure Explainable decision**.
<br></br>


 <span style="background-color: #FFFF00"> RayOnSpark </span> is a feature that was recently added to [Analytic Zoo](https://github.com/intel-analytics/analytics-zoo), end to end data analytics + AI open sourced platform, that helps you unified multiple analytics workload like recommendation, time series, computer vision, nlp and more into one platform running on Spark, Yarn or K8S.
 <br></br>

<span style="background-color: #DCDCDC"> "RayOnSpark allows users to directly run Ray programs on Apache Hadoop*/YARN, so that users can easily try various emerging AI applications on their existing Big Data clusters in a distributed fashion. Instead of running big data applications and AI applications on two separate systems, which often introduces expensive data transfer and long end-to-end learning latency, RayOnSpark allows Ray applications to seamlessly integrate into Apache Spark* data processing pipeline and directly run on in-memory Spark RDDs or DataFrames." Jason Dai. </span>



<img class="responsive" src="https://miro.medium.com/max/728/1*Jv085PlSKouE9RRuvFNlDQ.png" alt="drawing">

To learn more about Ray and RayOnSpark, checkout [Jason Dai article from RISELab publication](https://medium.com/riselab/rayonspark-running-emerging-ai-applications-on-big-data-clusters-with-ray-and-analytics-zoo-923e0136ed6a).

-------------------------------
<br></br>
<br></br>

## **Koalas:**
<img  style="width:auto;max-width:350px; height: auto;" src="https://raw.githubusercontent.com/databricks/koalas/master/icons/koalas-logo.png" alt="drawing"> 
<br></br>
 <span style="background-color: #FFFF00"> Koalas </span> is Pandas scalable Sibling:

From the [Pandas](https://pandas.pydata.org/docs/) docs: _"pandas is an open source, BSD-licensed library providing high-performance,
 easy-to-use data structures and data analysis tools for the Python programming language."_

From the [Koalas](https://koalas.readthedocs.io/en/latest/) docs: _"The Koalas project makes data scientists more productive when interacting with big data,
 by implementing the pandas DataFrame API on top of Apache Spark."_


If you are familiar with exploring and running analytics on data with _panads_,\
 _Koalas_ provides a similar API for running the same analytics on Apache Spark DataFrames.\
 Which makes it easier for Pandas user to run their workloads at scale.\
When using it, notice the different versions of Koalas, many new versions are NOT available with Spark 2.4 and require Spark 3.0 cluster.

Koalas is built with an internal frame to hold indexes and information on top of Spark DataFrame.

<img  style="width:auto;max-width:650px; height: auto;" src="https://i.ytimg.com/vi/NpAMbzerAp0/maxresdefault.jpg" alt="drawing">
 <br></br>
 
To learn more about it, checkout [Tim Hunter talk on Koalas](https://databricks.com/session_eu19/koalas-pandas-on-apache-spark) from Spark Summit 2019.

-------------------------------
<br></br>
<br></br>

## **Delta Lake:**
<img  style="width:auto;max-width:350px; height: auto;" src="https://camo.githubusercontent.com/5535944a613e60c9be4d3a96e3d9bd34e5aba5cddc1aa6c6153123a958698289/68747470733a2f2f646f63732e64656c74612e696f2f6c61746573742f5f7374617469632f64656c74612d6c616b652d77686974652e706e67" alt="drawing"> 



[Delta Lake](https://delta.io/) is nothing new with the Spark ecosystem, but still many confuse Delta Lake to be a ... DataBase! (DB) well.. delta lake is NOT a database.
Detla Lake is an open source storage layer that brings ACID (atomicity, consistency,
 isolation, and durability) transactions to Apache Spark and Big data workloads but is not a DB! Just like [Azure Blog storage](https://docs.microsoft.com/en-us/learn/paths/store-data-in-azure/?WT.mc_id=blog-00000-adpolak) and [AWS S3](https://aws.amazon.com/s3/) are not acting as databases, they are defined as storage.\
Delta helps with ACID that is hard to achieve and a great pain point with distributed storage.
It provides scalable metadata handling on the data itself.  
When combined with Spark this is highly useful due to the nature of Spark SQL engine
the catalyst which uses this metadata to better plan and executed big data queries.

There is also data versioning through snapshot of the storage named Time Travel feature.
I recommend being mindful with using this feature as saving snapshots and later using them might create an overhead to the size and compute of your data.

If you are curious to learn more about it, read [here](https://databricks.com/blog/2020/06/18/time-traveling-with-delta-lake-a-retrospective-of-the-last-year.html).

-------------------------------

## That's it.

I hope you enjoyed reading this short recap on open sources for January 2021.\
If you are interested in learning more and getting updates, follow [Adi Polak on Twitter.](https://twitter.com/AdiPolak).