## Chapter 17

## Memory System Resource Partitioning and Monitoring

This section describes the SMMU extensions to support Memory System Resource Partitioning and Monitoring, MPAM [3].

This support is described in three areas:

1. How MPAM identifiers are assigned to client device transactions.
2. How MPAM identifiers are generated for SMMU-originated transactions.
3. SMMUsupport for partitioning of internal resources.

The MPAM architecture defines new per-transaction attributes that affect system behavior or the behavior of components that the transactions pass through or Completers that satisfy a transaction. The additional attributes are two identifiers:

- Partition ID, or PARTID.
- Performance Monitoring Group, or PMG.

The PARTID and PMG namespaces are specific to a Security state. A Non-secure stream is assigned a Non-secure PARTID and PMG. In the general case, a Secure stream is assigned a Secure PARTID and PMG.

In the default case, SMMU-originated accesses and client-originated accesses for Realm state use the Realm PARTID space.

See section 17.7 Determination of PARTID space values for full details.