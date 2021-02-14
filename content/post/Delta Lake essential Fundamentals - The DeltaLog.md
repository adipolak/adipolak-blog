---
title: "Delta Lake essential Fundamentals: Part 2 - The DeltaLog"
author: "Adi Polak"
description: "Multi-part series that will take you from beginner to expert in Delta Lake"
tags: ["open-source", "apache spark", "delta lake","beginner", "DeltaLog"]
date: "2021-02-11"
draft: false
---


In the previous part, we discussed what [ACID transaction](https://blog.adipolak.com/post/delta-lake-essential-fundamentals) is and what it means in Delta Lake.<br>
In this part, you will understand how Delta Transaction Log, named DeltaLog, is achieving ACID.

## Transaction Log
A transaction log is a history of actions executed by a (TaDa 💡) database management system with the goal to guarantees [ACID properties](https://blog.adipolak.com/post/delta-lake-essential-fundamentals/) over a crash.

## DeltaLake transaction log - DetlaLog

DeltaLog is a transaction log directory which holds an **ordered** record of every transaction committed on a Delta Lake table since it was created.
The goal of DeltaLog is to be the **single** source of truth for readers who read from the same table at the same time. That means, readers read the **exact** same data.
Hence, all users view the same correct data at all times. This is achieved with deltalog tracking all the changes that users do: read, delete, update, etc.

DeltaLog can also contain statistics on the data; depending on the type of the actual type of data/field, each field can have min, max values. Having this extra metadata on the large set of data can help with faster querying. DeltaTable read mechanism uses uses a simplified [push down predict](https://medium.com/microsoftazure/data-at-scale-learn-how-predicate-pushdown-will-save-you-money-7063b80878d7).

Here is a simplification of deltalog on the file systems from Databricks site: <br>
<img class="responsive" src="/images/Detla/deltalake-deltalog.png" alt="drawing">

The Delta Log itself is a folder that consists out of multiple JSON files. When it reaches 10 files, Delta does a checkpoint and compaction operation( we will dive into it in the next chapter).


Here is an example of a Deltalog JSON file from the OSS test resources:
```json
{"remove":{"path":"part-00001-f1cb1cf9-7a73-439c-b0ea-dcba5c2280a6-c000.snappy.parquet","dataChange":true}}
{"remove":{"path":"part-00000-f4aeebd0-a689-4e1b-bc7a-bbb0ec59dce5-c000.snappy.parquet","dataChange":true}}
```

You can see that the operation was: _remove_ path(it can be a whole field or specific values), in this operation the metadata field _dataChange_ is set to true.

Here is a more complex JSON file:
```json
{"metaData":{"id":"2edf2c02-bb63-44e9-a84c-517fad0db296","format":{"provider":"parquet","options":{}},"schemaString":"{\"type\":\"struct\",\"fields\":[{\"name\":\"id\",\"type\":\"integer\",\"nullable\":true,\"metadata\":{}},{\"name\":\"value\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}}]}","partitionColumns":["id"],"configuration":{}}}
{"remove":{"path":"part-00001-6d252218-2632-416e-9e46-f32316ec314a-c000.snappy.parquet","dataChange":true}}
{"remove":{"path":"part-00000-348d7f43-38f6-4778-88c7-45f379471c49-c000.snappy.parquet","dataChange":true}}
{"add":{"path":"id=5/part-00000-f1e0b560-ca00-409e-a274-f1ab264bc412.c000.snappy.parquet","partitionValues":{"id":"5"},"size":362,"modificationTime":1501109076000,"dataChange":true}}
{"add":{"path":"id=6/part-00000-adb59f54-6b8f-4bfd-9915-ae26bd0f0e2c.c000.snappy.parquet","partitionValues":{"id":"6"},"size":362,"modificationTime":1501109076000,"dataChange":true}}
{"add":{"path":"id=4/part-00001-36c738bf-7836-479b-9cc1-7a4934207856.c000.snappy.parquet","partitionValues":{"id":"4"},"size":362,"modificationTime":1501109076000,"dataChange":true}}
```

Here there is the _metadata_ object entry - it means that there has been an update to the table schema or that a new table was created.
Later we see 2 _remove_ operations, followed by 3 _add_ operations. These operations objects can have a "stat" field, that stat can contain statistical information, such as the number of records, minValues, maxValues, and more.

These JSON files might also contain operation objects with fields such as - "STREAMING UPDATE", notebook- if the operation took place from a notebook, isolationLevel, etc.

This information is valuable for managing the table overall and helps delta with optimizing read files, this optimization reduce the chances of running a full scan on the storage.

To simplified it, DeltaTable a result of a set of actions (deltalog).



## DeltaLog and Atomicity
From the [first part](https://blog.adipolak.com/post/delta-lake-essential-fundamentals), you already know that atomicity means that a transaction either happened or not. The DeltaLog itself consists of atomic operations; each line in the log (like the ones you saw above) represents an action,which is an atomic unit; These are called commits.
The transactions that took place on the data can be broken into multiple components in which each one individually represents a commit in the deltalog. Breaking complex operations into small transactions helps with ensuring atomicity.



## DeltaLog and Isolation
Operations such as Update, Delete, Add can harm isolation; Hence, since we want to guarantee isolation with DeltaTable, readers get access to the table snapshot. This guarantees all parallel readers read the exact data. For handling deletion operations, delta postpones the actual delete operation on the files ; it first tag the files as deleted and later, remove it only when considered safe (similar to Cassandra delete operations with a tombstone).


In Delta 0.8.1 source code, there is a comment stating that it's recommended to have the delete operations retention set to at least 2 weeks and that generally it should be larger than the duration of a job. <br>
*Note:* This will impact streaming workload too, because there will be a need to delete/vacuum the actual files at some point, which might result in blocking the stream.
<img class="responsive" src="/images/Detla/delta-tombston-retention.png" alt="drawing">



## DeltaLog and Consistency
Delta Lake solves the problem of consistency by solving conflicts with an optimistic concurrency algorithm.
The class in charge of this algorithm is the OptimisticTransaction class. It achieves it by using [Java 8 ReentrantLock](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/locks/ReentrantLock.html) that is "owned" by DeltaLog instance. <br>
Here is the code snippet: <br>

<img class="responsive" src="/images/Detla/delta-log-optimistic-concurrency-algo.png" alt="drawing">

DeltaTable instance actively uses the ReentrantLock lock in the OptimisticTransaction under `doCommitRetryIteratively` function.
The optimistic approach was chosen here because in the big data world there is a tendency to add more data than update it.
It's less common to find and update a specific record unless there was some data corruption. It can be that investigations if missing data or corrupted data scenario will lead to the conclusion that it's better to update than delete and re-write. But in practice, update scenario is less common.

Here is the code for the optimistic algorithm:
<img class="responsive" src="/images/Detla/delta-log-OptimisticTransaction.png" alt="drawing">

It works like this:
In line 572, the program records the attempted version as the `commitVersion` instance which is of type `var`.
`var` in Scala represents a mutable object instance, which means its value can change.
In line 575, it starts the `while(true)` loop and maintains an `attemptNumber` counter; if it's `==0`, it will try to commit; if it fails here, that means that a file with this `commitVersion` was already written/committed into the table and it will throw an exception. That exception is being caught in lines 592+593. From there, with each failure, the algorithm is increasing the attemptNumber by 1.
After the first failure, the program won't go into the first if statement on line 577; it will go straights into the `else if` on line 579.
If the program reached the state where `attemptNumber` is bigger than the maximum allowed/configured, it will throw a `DeltaErrors.maxCommitRetriesExceededException` exception.
maxCommitRetriesExceededException exception will provide information about the commit version, the first commit version attempt, the number of attempts commits, and total time spent attempting this commit in ms.
Otherwise, it will try to record this update with checkForConflict functionality in line 588.
Multiple scenarios can bring us to this state.

To support the users, DeltaLake introduces a set of conflict exceptions to that provides more information about the data and the conflicts:

<img class="responsive" src="/images/Detla/delte-concurrent-exceptions.png" alt="drawing">

Let's look at some of the conflict scenarios:

### Two Writers:
This is the case of two writers who appends data to the same table simultaneously, without reading anything. In this scenario, one writer will commit, and the second writer will read the first one's updates before adding its own updates. Suppose it was only appended operation, like a counter which both are executing. In that case, there is no need to redo all computation, and it will automatically commit; if that's not the case, writer number two will need to redo the computation given the new information from writer one.


### Delete and Read:
In a more complex scenario like this one, there is no automated solution. For concurrent Delete-Read, there is a dedicated `ConcurentDeleteReadException` exception.
That means that if there is a request to delete a file that at the same time is being used for a read, the program throws an exception.

### Delete and Delete:
When two operations delete the same file, it might be due to a compaction mechanism or other operation, here too an exception will occur.



## DeltaLog and Durability
Since all transactions made on a DeltaTable are being stored directly to disk/file system, durability is given. All commits are being _persistent_ to disk and if there is an event of system failure, they can be restored from the disk.
(Unless there is a true disaster like fire etc and damage to the actual disks holding the information).


------------------------------------------
For exploring and learning about delta, I did a deep dive into the code source itself, if you are interested in that, I captured it through videos, please let me know if that is useful for you.


# What's next?

Next we will see more examples, scenarios and use cases for DeltaLake! We will learn about the compaction mechanism, schema enforcement and how it can enforce exactly once operation.

As always, I would love to get your comments and feedback on [Adi Polak](https://twitter.com/intent/follow?original_referer=http%3A%2F%2Flocalhost%3A1313%2F&ref_src=twsrc%5Etfw&region=follow_link&screen_name=AdiPolak&tw_p=followbutton) 🐦.


{{< youtube id="i24ZA6mmvDI" >}}




