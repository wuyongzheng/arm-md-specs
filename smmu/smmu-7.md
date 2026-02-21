## Chapter 7 Faults, errors and Event queue

There are three ways that unexpected or erroneous events can be reported to software:

1. Commands given to the SMMU might be in some way incorrect and the Command queue has a mechanism to report such problems.
2. A set of configuration errors and faults are recorded in the Event queue. These include events that arise from incoming device traffic, such as a configuration error (discovered when configuration is fetched on receipt of device traffic) or a page fault arising from the device traffic address.
3. A global register-based SMMU\_GERROR mechanism reports events arising from a failure to record into the Event or PRI queues and other catastrophic events that cannot be written to memory. This might happen when the Event queue base pointer incorrectly indicates non-existent memory, or queue overflow.