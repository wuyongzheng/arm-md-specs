## A5.3 Host view of memory management

This section describes memory management from the Host's point of view.

## A5.3.1 Host IPA state

DYZTZJ A Realm IPA has an associated Host IPA state (HIPAS).

The HIPAS values are shown in the following table.

| Name              | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| HIPAS_ARCH_DEV    | Protected IPA which is associated with an architectural device. |
| HIPAS_DATA        | Protected IPA which is associated with a DATA Granule.          |
| HIPAS_MAPPED_NS   | Unprotected IPA which is associated with a physical Granule.    |
| HIPAS_NARCH_DEV   | Protected IPA which is associated with a GRAN_DEV Granule.      |
| HIPAS_UNMAPPED_NS | Unprotected IPA which is not associated with any Granule.       |
| HIPAS_VOID        | Protected IPA which is not associated with any Granule.         |

ITRSKJ HIPAS values are stored in leaf entries of a primary Realm Translation Table (RTT).

IGZMKQ HIPAS transitions are caused by execution of RMI commands.

INQCGS A mapping at a Protected IPA is valid if HIPAS\_DATA and RIPAS\_RAM.

IMKNDK A mapping at a Protected IPA is valid if HIPAS\_NARCH\_DEV and RIPAS\_DEV.

ISTBRZ The RMM emulates access to a Protected IPA if HIPAS\_ARCH\_DEV and RIPAS\_DEV.

DRAFT

IYMNSR

The following table summarizes, for each combination of RIPAS and HIPAS for a Protected IPA:

- the translation table entry attributes, and
- the behavior which results from Realm access to that IPA.

The TTD.VALID and TTD.NS columns refer to the value of the corresponding fields in the architecturally-defined Stage 2 translation table descriptor which is written by the RMM.

| RIPAS     | HIPAS     | TTD.VALID   | TTD.NS   | Data access                | Instruction fetch                 |
|-----------|-----------|-------------|----------|----------------------------|-----------------------------------|
| EMPTY     | VOID      | 0           |          | SEA to Realm               | SEA to Realm                      |
| EMPTY     | DATA      | 0           |          | SEA to Realm               | SEA to Realm                      |
| EMPTY     | NARCH_DEV | 0           |          | SEA to Realm               | SEA to Realm                      |
| EMPTY     | ARCH_DEV  | 0           |          | SEA to Realm               | SEA to Realm                      |
| RAM       | VOID      | 0           |          | REC exit due to Data Abort | REC exit due to Instruction Abort |
| RAM       | DATA      | 1           | 0        | Data access                | Instruction fetch                 |
| RAM       | NARCH_DEV | 0           |          | REC exit due to Data Abort | REC exit due to Instruction Abort |
| RAM       | ARCH_DEV  | 0           |          | REC exit due to Data Abort | REC exit due to Instruction Abort |
| DESTROYED | VOID      | 0           |          | REC exit due to Data Abort | REC exit due to Instruction Abort |
| DESTROYED | DATA      | DRAFT 0     |          | REC exit due to Data Abort | REC exit due to Instruction Abort |
| DESTROYED | NARCH_DEV | 0           |          | REC exit due to Data Abort | REC exit due to Instruction Abort |
| DESTROYED | ARCH_DEV  | 0           |          | REC exit due to Data Abort | REC exit due to Instruction Abort |
| DEV       | NARCH_DEV | 1           | 0        | Device access              | SEA to Realm                      |
| DEV       | ARCH_DEV  | 0           |          | Emulated by RMM            | SEA to Realm                      |

## See also:

- A5.2.3 Realm access to a Protected IPA
- A5.2.4 RSI command access to a Protected IPA
- A5.6 Realm Translation Table
- Chapter A9 Realm device assignment
- A9.8 Virtual SMMU

## A5.3.2 Memory mapping operations overview

- IHSFHR The set of memory mapping and unmapping operations which can be performed by execution of RMI commands is listed below.
- Create or remove mappings within a contiguous range of Protected IPA space to conventional memory which is contiguous in Realm PAS.

DPMBDL

IVPLYJ

ISZBBJ

- Create or remove mappings within a contiguous range of Protected IPA space to conventional memory which is non-contiguous in Realm PAS.
- Create or remove mappings within a contiguous range of Protected IPA space to device memory which is contiguous in Realm PAS.
- Create or remove mappings within a contiguous range of Protected IPA space to device memory which is non-contiguous in Realm PAS.
- Create or remove mappings within a contiguous range of Protected IPA space to device memory which is emulated by the RMM.
- Create or remove mappings within a contiguous range of Unprotected IPA space to conventional memory which is contiguous in Non-secure PAS.
- Create or remove mappings within a contiguous range of Unprotected IPA space to conventional memory which is non-contiguous in Non-secure PAS.
- Propagate mappings within a contiguous range of IPA space from the primary RTT tree to an auxiliary RTT tree.
- Remove mappings within a contiguous range of IPA space from an auxiliary RTT tree.

## See also:

- A5.2.1 Realm IPA space
- A10.3.1 Auxiliary RTT

## A5.3.3 Range-based memory operations

- DMPJJT A Range-based memory operation is an operation which creates or removes mappings within a contiguous range of IPA space.

IKQYXN

A Range-based memory operation implements the Range RMI operation which returns progress address programming model.

- IWWGNX RMI operations which can lead to an intermediate state

A Range-based memory operation implements the programming model.

## See also:

- B4.3.2 Stateful RMI operations
- B4.3.5 Range RMI operations

## A5.3.3.1 Output address set

DRAFT

An output address set is a set of physical addresses which are (or will be, following a mapping operation) stored in the output address field of a set of RTT entries.

The output addresses which are operated on by a Range-based memory operation identify one of the following:

- Physical resources, such as DRAM or device memory, which are mapped into the IPA space of the Realm
- An architectural device which is managed by the RMM.

When Range-based memory operation maps or unmaps physical resources, it operates on an output address set which is one of the following:

- A single contiguous PA range, defined as [base, base + size) .
- A list of PA ranges, each of which is defined as a (base, size) tuple.

In this case, the output address set contains the following addresses:

```
-[entry_1.base, entry_1.base + entry_1.size) -[entry_2.base, entry_2.base + entry_2.size) -. . . -[entry_n.base, entry_n.base + entry_n.size)
```

- DWMHWQ An RMI Address List is a data structure which contains a list of RMI Address Range Descriptors , each of which describes a region of contiguous address space.
- IQRTQC To perform a Range-based memory mapping operation which operates on an output address set, the Host provides to the RMM a 64-bit value and a flag. The flag specifies whether the 64-bit value is:
- A single RMI Address Range Descriptor, provided directly in a register, or
- The base address of an RMI Address List which is stored in Non-secure Granules. In this case, the total size of the output address set described by the list entries must be equal to the size of the target IPA range.
- RDCNQB When used as a command input value or output value, the address of an RMI Address List is aligned to the size of an RMI Address Range Descriptor.
- ILZLVV When performing a Range-based memory unmapping operation which operates on an output address set, the Host provides to the RMM a flag which specifies whether the output address set should be:
- Returned as a single RMI Address Range Descriptor, provided directly in a register, or
- Returned by populating an RMI Address List in a Non-secure Granule provided by the Host, or
- Not returned.
- XVKKQN The Host may optionally maintain a shadow copy of the Realm's IPA to PA mappings. In this case, the Host does
- not required the output address set to be returned on unmapping.
- DRAFT See also: · B4.4 RMI Address Range Descriptor A5.3.3.2 Range-based memory mapping operation The amount of progress made on a Range-based memory mapping operation during a single RMI call is determined by a combination of constraints imposed by the RMM architecture, and IMPLEMENTATION DEFINED properties of the RMM implementation. The following architectural constraints apply to the RTTE at the base of the target IPA range: · If the state of the RTTE is not RTTE\_VOID then the command fails with (RMI\_ERROR\_RTT, walk.level). · If base of the target IPA range is not aligned to the size of the IPA space described by the RTTE then the command fails with (RMI\_ERROR\_RTT, walk.level).
- If the size of the IPA space described by the RTTE is larger than the total size of the target IPA range then the command fails with (RMI\_ERROR\_RTT, walk.level).

If the operation uses an output address set then the following architectural constraints apply to the tracking region which includes the start of the set:

- If the tracking region is untracked then the command fails with RMI\_ERROR\_TRACKING.
- If start of the output address set is not aligned to the granularity of the tracking region then the command fails with (RMI\_ERROR\_RTT, walk.level).
- If the granularity of the tracking region is larger than the total size of the target IPA range then the command fails with RMI\_ERROR\_TRACKING.

If the operation uses an output address set then the following architectural constraints apply to the Granule at the start of the set:

- If the state of the Granule is not GRAN\_DELEGATED then the command fails with RMI\_ERROR\_INPUT.

If the operation uses an output address set and ATS is enabled for the target Realm then the following architectural constraints apply to the DPT entry which includes the start of the set:

- If the Level 0 DPT is in an intermediate state then the command fails with RMI\_BLOCKED.
- If the Level 0 DPT has not been created then the command fails with RMI\_ERROR\_DPT.
- If the DPT entry is in an intermediate state then the command fails with RMI\_BLOCKED.
- ILPPYG

IVRXMQ

- If start of the output address set is not aligned to the size of the PA space described by the DPT entry then the command fails with RMI\_ERROR\_DPT.
- If the size of the PA space described by the DPT entry is larger than the total size of the target IPA range then the command fails with (RMI\_ERROR\_RTT, walk.level).

If none of the above checks failed then the operation starts to operate on the target IPA range. The operation terminates when any of the following is true:

- The operation has started to transition an RTTE entry from RTTE\_VOID, but has not completed the work needed for the entry to reach the target state. The RTTE entry transitions to an intermediate state and the command returns RMI\_INCOMPLETE.
- The operation reaches an RTTE, tracking region, Granule or DPT entry which fails one of the above checks. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made. If no changes of system state occur before the operation is resumed then the next command will fail the same check at the beginning, and return an error code as described above. This indicates that in order to progress the operation, the Host must first unfold the RTT, transition the tracking region to fine granularity, or create a Level 1 DPT.
- DRAFT · The operation reaches an RTTE, tracking region or DPT entry which passes the above checks, but whose size is too large to process for an IMPLEMENTATION DEFINED reason. For example, an implementation may limit the maximum size of the address space which can be processed during a single RMI command, either to ensure that the command's execution time does not exceed an IMPLEMENTATION DEFINED budget, or to limit complexity of the implementation. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made. If no changes of system state occur before the operation is resumed then the next command will fail the same check at the beginning, and return an error code as described above. This indicates that in order to progress the operation, the Host must first unfold the RTT, transition the tracking region to fine granularity, or create a Level 1 DPT. · The operation neither encounters a failing check, nor reaches the end of the IPA range, but yields for an IMPLEMENTATION DEFINED reason. For example, this could be due to the command's execution time having exceeded an IMPLEMENTATION DEFINED budget. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made. · The operation reaches the end of the target IPA range. The command returns RMI\_SUCCESS with out\_top == top . On successful execution of a Range-based memory mapping operation, all of the following are true:
- The HIPAS of the IPA range [base, out\_top) transitions from HIPAS\_VOID to the target HIPAS value. For example, when creating a mapping to conventional memory, the target HIPAS value is HIPAS\_DATA.
- If the operation uses an output address set then the IPA range [base, out\_top) is mapped linearly to the first out\_top -base bytes of the output address set.
- If the operation uses an output address set then the state of the Granules within the first out\_top - base bytes of the output address set transitions from GRAN\_DELEGATED to the target Granule state. For example, when creating a mapping to conventional memory, the target Granule state is GRAN\_DATA.
- IHCNBP If the return value of a Range-based memory mapping operation is RMI\_INCOMPLETE and the operation uses an RMI Address List then it is IMPLEMENTATION DEFINED whether data is read from the list.

## A5.3.3.3 Range-based memory unmapping operation

- IBWPHJ The amount of progress made on a Range-based memory unmapping operation during a single RMI call is determined by the combination of constraints imposed by the RMM architecture, and IMPLEMENTATION DEFINED properties of the RMM implementation.

The following architectural constraints apply to the RTTE at the base of the target IPA range:

- If base of the target IPA range is not aligned to the size of the IPA space described by the RTTE then the command fails with (RMI\_ERROR\_RTT, walk.level).

IWLYBJ

- If the size of the IPA space described by the RTTE is larger than the total size of the target IPA range then the command fails with (RMI\_ERROR\_RTT, walk.level).

If the above checks pass then the start of the output address set is read from the above RTTE.

If the operation is removing DATA or RIPAS\_DEV mappings then the following architectural constraints apply to the tracking region which includes the start of the set:

- If start of the output address set is not aligned to the granularity of the tracking region then the command fails with (RMI\_ERROR\_RTT, walk.level).
- If the granularity of the tracking region is larger than the total size of the target IPA range then the command fails with RMI\_ERROR\_TRACKING.

If the operation removing DATA or RIPAS\_DEV mappings then the following architectural constraints apply to the Granule at the start of the set:

- If the state of the Granule is not the expected Granule state then the command fails with RMI\_ERROR\_INPUT. For example, when removing a mapping to conventional memory, the expected Granule state is GRAN\_DATA.

If the operation removing DATA or RIPAS\_DEV mappings then and ATS is enabled for the target Realm then the following architectural constraints apply to the DPT entry which includes the start of the set:

- If the Level 0 DPT is in an intermediate state then the command fails with RMI\_BLOCKED.
- If the DPT entry is in an intermediate state then the command fails with RMI\_BLOCKED.
- DRAFT · If start of the output address set is not aligned to the size of the PA space described by the DPT entry then the command fails with RMI\_ERROR\_DPT. · If the size of the PA space described by the DPT entry is larger than the total size of the target IPA range then the command fails with (RMI\_ERROR\_RTT, walk.level). If none of the above checks failed then the operation starts to operate on the target IPA range. The operation terminates when any of the following is true: · The operation has started to transition an RTTE entry to RTTE\_VOID, but has not completed the work needed. The RTTE entry transitions to an intermediate state and the command returns RMI\_INCOMPLETE. · The operation reaches an RTTE, tracking region, Granule or DPT entry which fails one of the above checks. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made. If no changes of system state occur before the operation is resumed then the next command will fail the same check at the beginning, and return an error code as described above.
- The operation reaches an RTTE, tracking region or DPT entry which passes the above checks, but whose size is too large to process for an IMPLEMENTATION DEFINED reason. For example, an implementation may limit the maximum size of the address space which can be processed during a single RMI command, either to ensure that the command's execution time does not exceed an IMPLEMENTATION DEFINED budget, or to limit complexity of the implementation. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made. If no changes of system state occur before the operation is resumed then the next command will fail with RMI\_ERROR\_RTT, RMI\_ERROR\_TRACKING or RMI\_ERROR\_DPT. This indicates that in order to progress the operation, the Host must first unfold the RTT, transition the tracking region to fine granularity, or create a Level 1 DPT.
- The operation neither encounters a failing check, nor reaches the end of the IPA range, but yields for an IMPLEMENTATION DEFINED reason. For example, this could be due to the command's execution time having exceeded an IMPLEMENTATION DEFINED budget. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made.
- The operation reaches the end of the target IPA range. The command returns RMI\_SUCCESS with out\_top == top .

On successful execution of a Range-based memory unmapping operation, all of the following are true:

- The HIPAS of the IPA range [base, out\_top) transitions to HIPAS\_VOID.

- If the Host has requested the output address set then the first out\_top -base bytes of the output address set are returned, either as the base of a single contiguous PA range, or by populating an RMI Address List and returning the number of entries which have been written.
- If the operation uses an output address set then the state of the Granules within the first out\_top - base bytes of the output address set transitions to GRAN\_DELEGATED.
- IQPWSR If the return value of a Range-based memory unmapping operation is RMI\_INCOMPLETE and the operation uses an RMI Address List then it is IMPLEMENTATION DEFINED whether data is written to the list.

## A5.3.4 Mapping initial Realm image in Protected IPA space

- IMLHNJ RMI\_RTT\_DATA\_MAP\_INIT is not a Range-based memory mapping operation.
- IRGJSN Execution of RMI\_RTT\_DATA\_MAP\_INIT creates a mapping from a page Protected IPA space to conventional memory which is in Realm PAS.
- IQGGXX On execution of RMI\_RTT\_DATA\_MAP\_INIT, contents of the target conventional memory are initialized with contents provided by the Host.
- IGNLVS Execution of RMI\_RTT\_DATA\_MAP\_INIT modifies the RIM of the target Realm.
- IDPWJH RMI\_RTT\_DATA\_MAP\_INIT can be executed only when the state of the target Realm is REALM\_NEW.
- RQDPHR On execution of RMI\_RTT\_DATA\_MAP\_INIT, if the state of the target RTTE is not RTTE\_VOID then the command fails with (RMI\_ERROR\_RTT, walk.level).
- RFPBKD On execution of RMI\_RTT\_DATA\_MAP\_INIT, if the tracking region for the target output address is not tracked with fine granularity then the command fails with RMI\_ERROR\_TRACKING.
- RBXHRK On execution of RMI\_RTT\_DATA\_MAP\_INIT, if the state of the Granule at the target output address is not GRAN\_DELEGATED then the command fails with RMI\_ERROR\_INPUT.
- RCVGHZ On execution of RMI\_RTT\_DATA\_MAP\_INIT, if ATS is enabled for the target Realm and the DPT entry for the target output address is in an intermediate state then the command fails with RMI\_BLOCKED.
- RTNRZH On execution of RMI\_RTT\_DATA\_MAP\_INIT, if ATS is enabled for the target Realm and the Level 1 DPT has not been created then the command fails with RMI\_ERROR\_DPT.
- RTDBWS On successful execution of RMI\_RTT\_DATA\_MAP\_INIT, the target IPA transitions from HIPAS\_VOID to HIPAS\_DATA.

DRAFT

- RMPZTK On successful execution of RMI\_RTT\_DATA\_MAP\_INIT, the target IPA is mapped to the target output address.
- RDGFMY On successful execution of RMI\_RTT\_DATA\_MAP\_INIT, the state of the Granule at the target output address transitions from GRAN\_DELEGATED to GRAN\_DATA.
- IGSXTP RMI\_RTT\_DATA\_MAP\_INIT implements the RMI operations which can lead to an intermediate state programming model.

See also:

- A5.3.6 Remove mappings from Protected IPA space to conventional memory
- B4.3.2 Stateful RMI operations
- B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command

## A5.3.5 Create mappings from Protected IPA space to wiped conventional memory

- IDSDWH Execution of RMI\_RTT\_DATA\_MAP creates mappings from a contiguous range of Protected IPA space to conventional memory which is in Realm PAS.
- IJZVPQ RMI\_RTT\_DATA\_MAP is a Range-based memory mapping operation which uses an output address set.
- INCMHC On execution of RMI\_RTT\_DATA\_MAP, contents of the target conventional memory are wiped.

- INKXWT RMI\_RTT\_DATA\_MAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.
- IFPQRZ Execution of RMI\_RTT\_DATA\_MAP does not modify the RIM of the target Realm.

See also:

- A2.3.8 Granule wiping
- A5.3.3 Range-based memory operations
- A5.3.6 Remove mappings from Protected IPA space to conventional memory
- B4.5.65 RMI\_RTT\_DATA\_MAP command

## A5.3.6 Remove mappings from Protected IPA space to conventional memory

- IRDQXH Execution of RMI\_RTT\_DATA\_UNMAP removes mappings to conventional memory from a contiguous range of Protected IPA space.
- ILYGYD RMI\_RTT\_DATA\_UNMAP is a Range-based memory unmapping operation which uses an output address set.
- IZNJNQ RMI\_RTT\_DATA\_UNMAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.
- IRFGPW Execution of RMI\_RTT\_DATA\_UNMAP does not modify the RIM of the target Realm.

See also:

- A5.3.3 Range-based memory operations
- A5.3.4 Mapping initial Realm image in Protected IPA space
- A5.3.5 Create mappings from Protected IPA space to wiped conventional memory
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command

## A5.3.7 Create mappings from Protected IPA space to device memory

- IHSDRR Execution of RMI\_RTT\_DEV\_MAP creates mappings from a contiguous range of Protected IPA space to device memory which is in Realm PAS.
- IDQYFW RMI\_RTT\_DEV\_MAP is a Range-based memory mapping operation which uses an output address set.
- ICXPPN RMI\_RTT\_DEV\_MAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.

DRAFT

- IDVLFV If RMI\_RTT\_DEV\_MAP reaches an output address which is not within the address ranges of the target VDEV then the command fails with RMI\_ERROR\_INPUT.
- IJMBJL Execution of RMI\_RTT\_DEV\_MAP does not modify the RIM of the target Realm.

See also:

- A5.3.3 Range-based memory operations
- A5.3.8 Remove mappings from Protected IPA space to device memory
- Chapter A9 Realm device assignment
- B4.5.69 RMI\_RTT\_DEV\_MAP command

## A5.3.8 Remove mappings from Protected IPA space to device memory

- IPQJZG Execution of RMI\_RTT\_DEV\_UNMAP removes mappings to device memory from a contiguous range of Protected IPA space.
- IVWLSQ RMI\_RTT\_DEV\_UNMAP is a Range-based memory unmapping operation which uses an output address set.
- ICDBSP RMI\_RTT\_DEV\_UNMAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.

- IWSNLS If RMI\_RTT\_DEV\_UNMAP reaches an output address which is not within the address ranges of the target VDEV then the command fails with RMI\_ERROR\_INPUT.
- ICKCGK Execution of RMI\_RTT\_DEV\_UNMAP does not modify the RIM of the target Realm.

See also:

- A5.3.3 Range-based memory operations
- A5.3.7 Create mappings from Protected IPA space to device memory
- Chapter A9 Realm device assignment
- B4.5.70 RMI\_RTT\_DEV\_UNMAP command

## A5.3.9 Create mappings from Protected IPA space to an architectural device

- IKSWRM Execution of RMI\_RTT\_ARCH\_DEV\_MAP creates mappings from a contiguous range of Protected IPA space to an architectural device.

- IWNLDF In this version of the specification, the only supported type of architectural device is SMMUv3.

- INLHMS RMI\_RTT\_ARCH\_DEV\_MAP is a Range-based memory mapping operation which does not use an output address set.

- IQCYDD RMI\_RTT\_ARCH\_DEV\_MAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.

- IWLRSK Execution of RMI\_RTT\_ARCH\_DEV\_MAP does not modify the RIM of the target Realm.

## See also:

- A5.3.3 Range-based memory operations
- A5.3.10 Remove mappings from Protected IPA space to an architectural device
- A9.8 Virtual SMMU
- B4.5.55 RMI\_RTT\_ARCH\_DEV\_MAP command

## A5.3.10 Remove mappings from Protected IPA space to an architectural device

- IVZXRD Execution of RMI\_RTT\_ARCH\_DEV\_UNMAP removes mappings to an architectural device from a contiguous range of Protected IPA space.

DRAFT

- ITMVLH RMI\_RTT\_ARCH\_DEV\_UNMAP is a Range-based memory unmapping operation which does not use an output address set.
- IVQWHL RMI\_RTT\_ARCH\_DEV\_UNMAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.
- IZBTRN Execution of RMI\_RTT\_ARCH\_DEV\_UNMAP does not modify the RIM of the target Realm.

## See also:

- A5.3.3 Range-based memory operations
- A5.3.9 Create mappings from Protected IPA space to an architectural device
- A9.8 Virtual SMMU
- B4.5.56 RMI\_RTT\_ARCH\_DEV\_UNMAP command

## A5.3.11 Create mappings from Unprotected IPA space

- IGZKZN Execution of RMI\_RTT\_UNPROT\_MAP creates mappings from a contiguous range of Protected IPA space to conventional memory which is in Non-Secure PAS.
- IQLBDR RMI\_RTT\_UNPROT\_MAP is a Range-based memory mapping operation which uses an output address set.
- IZRHBP RMI\_RTT\_UNPROT\_MAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.

ITVTMR

ILVBNM

IXTPQV

Execution of RMI\_RTT\_UNPROT\_MAP does not modify the RIM of the target Realm.

See also:

- A5.3.3 Range-based memory operations
- A5.3.12 Remove mappings from Unprotected IPA space
- B4.5.77 RMI\_RTT\_UNPROT\_MAP command

## A5.3.12 Remove mappings from Unprotected IPA space

- IVRXCD Execution of RMI\_RTT\_UNPROT\_UNMAP removes mappings to conventional memory from a contiguous range of Unprotected IPA space.
- IRRJNY RMI\_RTT\_UNPROT\_UNMAP is a Range-based memory unmapping operation which uses an output address set.
- IQMMTB RMI\_RTT\_UNPROT\_UNMAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.
- ICLVCM Execution of RMI\_RTT\_UNPROT\_UNMAP does not modify the RIM of the target Realm.

See also:

- A5.3.3 Range-based memory operations
- A5.3.11 Create mappings from Unprotected IPA space
- B4.5.78 RMI\_RTT\_UNPROT\_UNMAP command

## A5.3.13 Create mappings within Protected IPA space in auxiliary RTT tree

- IBQRQH Execution of RMI\_RTT\_AUX\_PROT\_MAP propagates mappings within a contiguous range of Protected IPA space from the primary RTT tree to an auxiliary RTT tree.
- ICKYCM RMI\_RTT\_AUX\_PROT\_MAP is a Range-based memory mapping operation which does not use an output address set.
- IXGMXX RMI\_RTT\_AUX\_PROT\_MAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.
- ILPYYG On execution of RMI\_RTT\_AUX\_PROT\_MAP, the 'block' flag controls the behaviour when the auxiliary RTT walk reaches an entry which extends beyond the start or the end of the target IPA range.

DRAFT

- If the value is RMI\_RTT\_AUX\_BLOCK\_CREATE then the RMM modifies the auxiliary RTT entry. The result is that the IPA range which is mapped extends beyond the start or the end of the target IPA range.
- If the value is RMI\_RTT\_AUX\_BLOCK\_NO\_CREATE then the command fails and returns an error to the caller. The expected result is that the Host will unfold the auxiliary RTT tree before re-trying the mapping operation.

On execution of RMI\_RTT\_AUX\_PROT\_MAP, the 'invalid\_pri' flag controls the behaviour when the primary RTT walk reaches an entry whose state is RTTE\_VOID.

- If the value is RMI\_RTT\_AUX\_INVALID\_CONTINUE then the RMM skips the corresponding entry in the auxiliary RTT and continues the mapping operation.
- If the value is RMI\_RTT\_AUX\_INVALID\_STOP then the command fails and returns an error to the caller.

Execution of RMI\_RTT\_AUX\_PROT\_MAP does not modify the RIM of the target Realm.

See also:

- A5.3.3 Range-based memory operations
- A5.3.14 Remove mappings within Protected IPA space in auxiliary RTT tree
- B4.5.60 RMI\_RTT\_AUX\_PROT\_MAP command

## A5.3.14 Remove mappings within Protected IPA space in auxiliary RTT tree

- IPTPPN Execution of RMI\_RTT\_AUX\_PROT\_UNMAP removes mappings within a contiguous range of Protected IPA space from an auxiliary RTT tree.
- IBFRKG RMI\_RTT\_AUX\_PROT\_UNMAP is a Range-based memory mapping operation which does not use an output address set.
- INZHMK RMI\_RTT\_AUX\_PROT\_UNMAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.
- IQWNXW Execution of RMI\_RTT\_AUX\_PROT\_UNMAP does not modify the RIM of the target Realm.

## See also:

- A5.3.3 Range-based memory operations
- A5.3.13 Create mappings within Protected IPA space in auxiliary RTT tree
- B4.5.61 RMI\_RTT\_AUX\_PROT\_UNMAP command

## A5.3.15 Create mappings within Unprotected IPA space in auxiliary RTT tree

- IDTGQS Execution of RMI\_RTT\_AUX\_UNPROT\_MAP propagates mappings within a contiguous range of Unprotected IPA space from the primary RTT tree to an auxiliary RTT tree.
- IKXHFT RMI\_RTT\_AUX\_UNPROT\_MAP is a Range-based memory mapping operation which does not use an output address set.
- IVXQXC RMI\_RTT\_AUX\_UNPROT\_MAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.
- IBLXRL Execution of RMI\_RTT\_AUX\_UNPROT\_MAP does not modify the RIM of the target Realm.

See also:

- A5.3.3 Range-based memory operations
- A5.3.16 Remove mappings within Unprotected IPA space in auxiliary RTT tree
- B4.5.62 RMI\_RTT\_AUX\_UNPROT\_MAP command

## A5.3.16 Remove mappings within Unprotected IPA space in auxiliary RTT tree

DRAFT

- IKMGVK Execution of RMI\_RTT\_AUX\_UNPROT\_UNMAP removes mappings within a contiguous range of Unprotected IPA space from an auxiliary RTT tree.
- IHSHRL RMI\_RTT\_AUX\_UNPROT\_UNMAP is a Range-based memory mapping operation which does not use an output address set.
- IXVKCY RMI\_RTT\_AUX\_UNPROT\_UNMAP can be executed either when the state of the target Realm is REALM\_NEW or when the state of the target Realm is REALM\_ACTIVE.
- IWXJQM Execution of RMI\_RTT\_AUX\_UNPROT\_UNMAP does not modify the RIM of the target Realm.

## See also:

- A5.3.3 Range-based memory operations
- A5.3.15 Create mappings within Unprotected IPA space in auxiliary RTT tree
- B4.5.63 RMI\_RTT\_AUX\_UNPROT\_UNMAP command

## A5.3.17 Changes to HIPAS of a Protected IPA

## A5.3.17.1 Changes to HIPAS of a Protected IPA while Realm state is REALM\_NEW

This section describes how the HIPAS of a Protected IPA can change while the Realm state is REALM\_NEW.

IYNFGD The following diagram summarizes HIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_NEW.

Figure A5.2: HIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_NEW

<!-- image -->

## See also:

- B4.5.65 RMI\_RTT\_DATA\_MAP command
- B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command
- B4.5.68 RMI\_RTT\_DESTROY command
- B4.5.69 RMI\_RTT\_DEV\_MAP command
- B4.5.70 RMI\_RTT\_DEV\_UNMAP command

## A5.3.17.2 Changes to HIPAS of a Protected IPA while Realm state is REALM\_ACTIVE

This section describes how the HIPAS of a Protected IPA can change while the Realm state is REALM\_ACTIVE.

IWKZXY The following diagram summarizes HIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_ACTIVE.

DRAFT

Figure A5.3: HIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_ACTIVE

<!-- image -->

See also:

Chapter A5. Realm memory management A5.3. Host view of memory management

- B4.5.65 RMI\_RTT\_DATA\_MAP command
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command
- B4.5.68 RMI\_RTT\_DESTROY command
- B4.5.69 RMI\_RTT\_DEV\_MAP command
- B4.5.70 RMI\_RTT\_DEV\_UNMAP command

DRAFT

## A5.3.18 Summary of changes to HIPAS and RIPAS of a Protected IPA

- ITJMCP The following diagram summarizes HIPAS and RIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_NEW.

Transitions due to execution of RMI\_RTT\_DESTROY are omitted from the diagram. Execution of this command results in a transition to HIPAS\_VOID, RIPAS\_DESTROYED.

Figure A5.4: HIPAS and RIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_NEW

<!-- image -->

<!-- image -->

A5.3. Host view of memory management

IVGKNJ The following diagram summarizes HIPAS and RIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_ACTIVE.

Transitions due to execution of RMI\_RTT\_DESTROY are omitted from the diagram. Execution of this command results in a transition to HIPAS\_VOID, RIPAS\_DESTROYED.

Figure A5.5: HIPAS and RIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_ACTIVE

<!-- image -->

## See also:

- B4.5.65 RMI\_RTT\_DATA\_MAP command
- B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command

Chapter A5. Realm memory management A5.3. Host view of memory management

- B4.5.68 RMI\_RTT\_DESTROY command
- B4.5.69 RMI\_RTT\_DEV\_MAP command
- B4.5.70 RMI\_RTT\_DEV\_UNMAP command
- B4.5.71 RMI\_RTT\_DEV\_VALIDATE command
- B4.5.73 RMI\_RTT\_INIT\_RIPAS command
- B4.5.75 RMI\_RTT\_SET\_RIPAS command

<!-- image -->

## A5.3.19 Dependency of RMI command execution on RIPAS and HIPAS values

IHLHZS The following table summarizes dependencies on RMI command execution on the current Protected IPA.

| Command                | Dependency on RIPAS                                             | Dependency on HIPAS               | New RIPAS             | New HIPAS   |
|------------------------|-----------------------------------------------------------------|-----------------------------------|-----------------------|-------------|
| RMI_RTT_ARCH_DEV_MAP   | EMPTY                                                           | VOID                              | Unchanged             | ARCH_DEV    |
| RMI_RTT_ARCH_DEV_UNMAP | Not DEV                                                         | ARCH_DEV                          | Unchanged             | VOID        |
| RMI_RTT_ARCH_DEV_UNMAP | DEV                                                             | ARCH_DEV                          | DESTROYED             | VOID        |
| RMI_RTT_CREATE         | None                                                            | None                              | Unchanged             | Unchanged   |
| RMI_RTT_DESTROY        | None                                                            | HIPAS of all entries is VOID      | DESTROYED             | VOID        |
| RMI_RTT_DATA_MAP_INIT  | None                                                            | VOID                              | RAM                   | DATA        |
| RMI_RTT_DATA_MAP       | None                                                            | VOID                              | Unchanged             | DATA        |
| RMI_RTT_DATA_UNMAP     | NotRAM                                                          | DATA                              | Unchanged             | VOID        |
| RMI_RTT_DATA_UNMAP     | RAM                                                             | DATA                              | DESTROYED             | VOID        |
| RMI_RTT_DEV_MAP        | None                                                            | VOID                              | Unchanged             | NARCH_DEV   |
| RMI_RTT_DEV_UNMAP      | Not DEV                                                         | NARCH_DEV                         | Unchanged             | VOID        |
| RMI_RTT_DEV_UNMAP      | DEV                                                             | NARCH_DEV                         | DESTROYED             | VOID        |
| RMI_RTT_FOLD           | RIPAS of all entries is identical                               | HIPAS of all entries is identical | Unchanged             | Unchanged   |
| RMI_RTT_INIT_RIPAS     | None                                                            | VOID                              | RAM                   | Unchanged   |
| RMI_RTT_SET_RIPAS      | DRAFT Optionally, Realm may specify that RIPAS is not DESTROYED | None                              | As specified by Realm | Unchanged   |
| RMI_RTT_DEV_VALIDATE   | None                                                            | HIPAS of all entries is NARCH_DEV | DEV                   | Unchanged   |

Successful execution of RMI\_RTT\_DATA\_MAP does not depend on the RIPAS value of the target IPA.

ILCSVH Successful execution of RMI\_RTT\_DATA\_UNMAP does not depend on the RIPAS value of the target IPA.

IMMSBL

Successful execution of RMI\_RTT\_DESTROY does not depend on the RIPAS values of entries in the target RTT.

ITJCGT

Successful execution of RMI\_RTT\_FOLD does depend on the RIPAS values of entries in the target RTT.

ILDCJK Successful execution of RMI\_RTT\_DEV\_UNMAP does not depend on the RIPAS value of the target IPA. See also:

- B4.5.55 RMI\_RTT\_ARCH\_DEV\_MAP command
- B4.5.56 RMI\_RTT\_ARCH\_DEV\_UNMAP command
- B4.5.64 RMI\_RTT\_CREATE command
- B4.5.65 RMI\_RTT\_DATA\_MAP command
- B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command
- B4.5.68 RMI\_RTT\_DESTROY command
- B4.5.69 RMI\_RTT\_DEV\_MAP command

- B4.5.70 RMI\_RTT\_DEV\_UNMAP command
- B4.5.71 RMI\_RTT\_DEV\_VALIDATE command
- B4.5.72 RMI\_RTT\_FOLD command
- B4.5.73 RMI\_RTT\_INIT\_RIPAS command
- B4.5.75 RMI\_RTT\_SET\_RIPAS command

## A5.3.20 Changes to HIPAS of an Unprotected IPA

IYNYBY The following diagram summarises HIPAS transitions for an Unprotected IPA.

Figure A5.6: HIPAS transitions for an Unprotected IPA

<!-- image -->

## See also:

- A5.6 Realm Translation Table
- B4.5.65 RMI\_RTT\_DATA\_MAP command
- B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command
- B4.5.68 RMI\_RTT\_DESTROY command
- B4.5.73 RMI\_RTT\_INIT\_RIPAS command
- B4.5.75 RMI\_RTT\_SET\_RIPAS command
- B5.4.7 RSI\_IPA\_STATE\_SET command

DRAFT