## 12.1 Error propagation, consumption and containment in the SMMU

This guidance section relates SMMU-specific concepts to the Arm RAS System Architecture.

Generally, SMMU activity can be considered to be driven on demand from incoming transactions from client devices. Consequently, an external transaction might cause the SMMU to consume errors from:

1. Internal state errors.
2. External state errors, for example reading a translation table entry, configuration structure or command with an associated error.

If the SMMU consumes an error while performing translation for an external transaction, containment of the error can be achieved by deferring the error to the source of the transaction. This might involve terminating the transaction with an abort, or otherwise returning error information to the client. A detected error that is silently propagated might lead to silent data corruption (SDC). The termination of a transaction that could be affected by an SMMU error ensures isolation of the error and represents a non-silent error propagation from the SMMU to the client device.

When the SMMU consumes an error from either internal or external state, Arm expects the implementation to report the error and enter error recovery in addition to containment by deferring the error.

Note: An example of an error propagation on write is a write of queue records affected by the error. The error might be propagated with affected data. An implementation might non-silently propagate the error so that the system can poison the data in memory.

An error can be consumed by the SMMU in a way that can affect external or internal state. This includes:

1. Reading a register containing an error in order to calculate an address for access to a queue entry.
2. Reading a register containing an error in order to write the data of a written queue entry.
3. Consuming an error from the system when reading from the Command queue.
4. Reading a cache entry containing an error in response to an incoming transaction.
5. Reading a register containing an error in response to an incoming transaction.
6. Consuming an error from the system when fetching data into a cache in response to an incoming transaction.

Containment of these errors avoids silently affecting external or internal state. The effect of the error means, for the corresponding scenarios in the previous list:

1. Internal consistency is lost.
2. The error might be transient (for example, it is overwritten when the queue entry is written), in which case internal consistency is not lost. The error is deferred into the memory system (error on write) and an implementation might record the error. If the error is non-transient, internal consistency might be lost.
3. An implementation might have unsuccessfully tried to correct the error, or might accept the error. However, internal consistency is not lost.
4. The transaction (and therefore other agents in the system) would be affected, and isolation broken, unless the transaction is terminated. The error can therefore be deferred to the client. SMMU internal consistency might not be lost.
5. An error in a register might not be correctable. The error can be deferred to the client and recorded. Internal consistency might have been lost if the register could affect future transactions.
6. The transaction would be affected by the error, unless the transaction is terminated (deferring the error to the client). SMMU internal consistency might not be lost.

If internal consistency is lost, invoking a Service Failure Mode (SFM) can isolate further errors from the system. This might reduce the severity of the error by ceasing subsequent duplicate error reports caused by the same failure, and by reducing the chance that the loss of internal consistency can silently propagate an error.