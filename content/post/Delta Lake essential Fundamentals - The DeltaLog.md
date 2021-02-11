---
title: "Delta Lake essential Fundamentals: Part 2 - The DeltaLog"
author: "Adi Polak"
description: "Multi-part series that will take you from beginner to expert in Delta Lake"
tags: ["open-source", "apache spark", "delta lake","beginner", "DeltaLog"]
date: "2021-02-11"
draft: false
---


In the previous part, we discussed what [ACID transaction](https://blog.adipolak.com/post/delta-lake-essential-fundamentals) is and what it means in Delta Lake.<br>
In this part, you will understand how Delta Transaction Log, named DeltaLog, is achieving it.

## Transaction Log
A transaction log is a history of actions executed by a (TaDa 💡) database management system with the goal to guarantees [ACID properties](https://blog.adipolak.com/post/delta-lake-essential-fundamentals/) over a crash.

## DeltaLake transaction log - DetlaLog

DeltaLog is a transaction log directory which holds an **ordered** record of every transaction committed on a Delta Lake table since it was created.
The goal of DeltaLog is to be the **single** source of truth for readers who read from the same table at the same time. Readers have access to the **exact** same data.
Hence, all users view the same correct data at all times. It's achieved with deltalog tracking all the changes - read, delete, update, etc. that users make to the table.

DeltaLogs also contains statistics on the data; depending on the data, it can have min, max values, resulting in faster querying. It uses a simplified [push down mechanism](https://medium.com/microsoftazure/data-at-scale-learn-how-predicate-pushdown-will-save-you-money-7063b80878d7).

Here is a simplification of deltalog on the file systems from Databricks site:
<img class="responsive" src="/images/Detla/deltalake-deltalog.png" alt="drawing">

The Delta Log is a folder that consists of multiple JSON files until it reaches 10 files, and then it operates a checkpoint and compaction ( we will dive into it in upcoming chapters).


Here is an example of a Deltalog JSON file from the OSS test resources:
```json
{"remove":{"path":"part-00001-f1cb1cf9-7a73-439c-b0ea-dcba5c2280a6-c000.snappy.parquet","dataChange":true}}
{"remove":{"path":"part-00000-f4aeebd0-a689-4e1b-bc7a-bbb0ec59dce5-c000.snappy.parquet","dataChange":true}}
```

You can see that the operation was to remove path, and it results in dataChange true.

Here is a more complex JSON file:
```json
{"metaData":{"id":"2edf2c02-bb63-44e9-a84c-517fad0db296","format":{"provider":"parquet","options":{}},"schemaString":"{\"type\":\"struct\",\"fields\":[{\"name\":\"id\",\"type\":\"integer\",\"nullable\":true,\"metadata\":{}},{\"name\":\"value\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}}]}","partitionColumns":["id"],"configuration":{}}}
{"remove":{"path":"part-00001-6d252218-2632-416e-9e46-f32316ec314a-c000.snappy.parquet","dataChange":true}}
{"remove":{"path":"part-00000-348d7f43-38f6-4778-88c7-45f379471c49-c000.snappy.parquet","dataChange":true}}
{"add":{"path":"id=5/part-00000-f1e0b560-ca00-409e-a274-f1ab264bc412.c000.snappy.parquet","partitionValues":{"id":"5"},"size":362,"modificationTime":1501109076000,"dataChange":true}}
{"add":{"path":"id=6/part-00000-adb59f54-6b8f-4bfd-9915-ae26bd0f0e2c.c000.snappy.parquet","partitionValues":{"id":"6"},"size":362,"modificationTime":1501109076000,"dataChange":true}}
{"add":{"path":"id=4/part-00001-36c738bf-7836-479b-9cc1-7a4934207856.c000.snappy.parquet","partitionValues":{"id":"4"},"size":362,"modificationTime":1501109076000,"dataChange":true}}
```

Here we have the metadata object - it means that there has been an update to the table schema or that a new table created.
Later we see 2 _remove_ operations, followed by 3 _add_ operations. Inside there can be a "stat" field, which contains statistics about the data in the file itself, such as the number of records, minValues, maxValues, and other stats we would like to save on the data for when we want to query it; 

These JSON files might also contain operations such as - "STREAMING UPDATE", notebook- if the operation took place from a notebook, isolationLevel, etc.

This information is valuable for managing the table overall and helps delta to know exactly which files to read, hence avoiding full scanning of the storage as much as possible. 

DeltaTable is abstracted to be a result of a set of actions (deltalog).



## DeltaLog and Atomicity
From the [first part](https://blog.adipolak.com/post/delta-lake-essential-fundamentals), you already know that atomicity means that a transaction has happened or not. The DeltaLog consists of atomic operations; each line in the log (like the ones you see above) represents an action, an atomic unit; we also call them commits.
The transactions that take place on the data can be broken into multiple components in which each one individually represents a commit in the deltalog. Breaking complex operations into small transactions helps us with ensuring atomicity.



## DeltaLog and Isolation
Operations such as Update, Delete, Add can harm our isolation; hence when we want to guarantee isolation with DeltaTable, we enable readers to read from a table snapshot. For deletion operations, delta avoids deleting the files immediately; it will tag it as deleted file and remove it only when considered safe (similar to Cassandra delete operations with a tombstone).


Here in Delta 0.8.1 source code, you can see that they recommended delete operations retention to be at least 2 weeks and generally should be larger than the duration of a job.
This will impact your streaming operations because there will be a need to delete/vacuum the actual files at some point.
<img class="responsive" src="/images/Detla/delta-tombston-retention.png" alt="drawing">



## DeltaLog and Consistency
Delta Lake solves the problem of consistency by solving conflicts with an optimistic concurrency algorithm.
The class in charge of this algorithm is the OptimisticTransaction class. It achieves it by using [Java 8 ReentrantLock](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/locks/ReentrantLock.html) that is "owned" by DeltaLog instance.
Here is the code snippet:

<img class="responsive" src="/images/Detla/delta-log-optimistic-concurrency-algo.png" alt="drawing">

It actively uses the ReentrantLock lock in the OptimisticTransaction under `doCommitRetryIteratively` function.
The optimistic approach was chosen here because we tend to add more data in the big data world than update it.
It's less common to find and update a specific record unless there was some data corruption. It can be that investigations will lead to the conclusion that it's better to update than delete and re-write. But updating scenario is less common.

Here is the code for the optimistic algorithm:
<img class="responsive" src="/images/Detla/delta-log-OptimisticTransaction.png" alt="drawing">

It works like this:
In line 572, it records the attempted version as the commit version; as you can see, it's from type `var`,
`var` in Scala represents a mutable object, which means its value can change.
In line 575, it starts the `while(true)` loop and maintains an attemptNumber; if it's `==0`, it will try to commit; if it fails here, that means that a file with this `commitVersion` was already written into the system and it will throw an exception that is being caught online 592+593. From there, the algorithm is increasing the attemptNumber by 1.
Now, it won't go into the first if statement on line 577; it will go straights into the `else if` on line 579.
If the attemptNumber is bigger than what is configured, it will throw a `DeltaErrors.maxCommitRetriesExceededException` exception.
maxCommitRetriesExceededException exception will provide information about the commit version, the first commit version attempt, the number of attempts commits, and total time spent attempting this commit in ms.
Otherwise, it will try to record this updated with checkForConflict functionality in line 588.
Multiple scenarios can bring us to this state.

DeltaLake introduces a set of conflict exceptions to provide us with as much information as possible about the data and the conflicts:

<img class="responsive" src="/images/Detla/delte-concurrent-exceptions.png" alt="drawing">

Let's look at some of the scenarios:

### Two writers at the same time:
This is the case of two writers who appends data to the same table simultaneously, without reading anything. In this scenario, one writer will commit, and the second writer will read the first one's updates before adding its own updates. Suppose it was only appended operation, like a counter which both are executing. In that case, there is no need to redo all computation, and it will automatically commit; if that's not the case, writer number two will need to redo the computation given the new information from writer one.


### Delete and Read operation:
In a more complex scenario like this one, 
for concurrent Delete-Read, there is `ConcurentDeleteReadException`.
That means that there is a request to delete a file that at the same time was used for a read operation.

### Delete and Delete operation:
When two operations delete the same file, it might be due to a compaction mechanism or other operation.



## DeltaLog and Durability
Since all transactions made on a DeltaTable are being stored directly to disk/file system, durability is givin, since all the commits are being persistent to disk and if there is an event of system failure, we can restore them from the disk.
(Unless there is a true disaster like fire etc and damage to the actual disks holding the information).


------------------------------------------
For exploring and learning about delta, I do a deep dive into the open source itself, if you are interested in that, I captured it through videos, please let me know if that is useful for you.


# What's next?

Next we will see more examples, scenarios and use cases for DeltaLake! We will learn about the compaction mechanism, schema enforcement and how it can enforce exactly once operation.

As always, I would love to get your comments and feedback on [Adi Polak](https://twitter.com/intent/follow?original_referer=http%3A%2F%2Flocalhost%3A1313%2F&ref_src=twsrc%5Etfw&region=follow_link&screen_name=AdiPolak&tw_p=followbutton) 🐦.


{{< youtube id="i24ZA6mmvDI" >}}




