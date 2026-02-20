## D18.2 Alphabetical list of Statistical Profiling Extension packets

This section lists every SPE packet and their description.

## D18.2.1 Address packet

Purpose

Attributes

Provides an address value for the record. Addresses are always 64 bits.

Multi-part packet comprising:

- 8 or 16-bit header.

- 64-bit payload.

## Address packet header

<!-- image -->

Figure D18-2 Address packet header (Extended format)

Figure D18-3 Address packet header (Short format)

<!-- image -->

Byte 1 bits [7:6], when Extended format; byte 0 bits [7:6], when Short format

This field reads as 0b10 .

SZ, byte 1 bits [5:4], when Extended format; byte 0 bits [5:4], when Short format

Payload size.

| SZ   | Description   |
|------|---------------|
| 0b11 | Doubleword.   |

This field reads as 0b11 .

Byte 1 bit [3], when Extended format; byte 0 bit [3], when Short format

This bit reads as 0b0 .

INDEX, byte 0 bits [1:0], byte 1 bits [2:0], when Extended format; byte 0 bits [2:0], when Short format

| INDEX   | Description                                                                                                                                                                                                                                 |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00000 | Instruction virtual address (PC). The virtual address of the sampled operation.                                                                                                                                                             |
| 0b00001 | Branch target address. The target virtual address of a sampled branch operation.                                                                                                                                                            |
| 0b00010 | Data access virtual address. The virtual address accessed by a sampled data memory accessing operation.                                                                                                                                     |
| 0b00011 | Data access physical address. The physical address accessed by a sampled data memory accessing operation.                                                                                                                                   |
| 0b00100 | Previous branch target address. The target virtual address of the most recently taken branch operation in program order before the sampled operation. This value is defined only if FEAT_SPE_PBT is implemented, and is reserved otherwise. |
| 0b0011x | IMPLEMENTATION DEFINED address.                                                                                                                                                                                                             |
| 0b1xxxx | IMPLEMENTATION DEFINED address.                                                                                                                                                                                                             |

All other values are reserved.

In the Short format header, INDEX[4:3] are zero.

## Byte 0 bits [7:5], when Extended format

This field reads as 0b001 .

## Byte 0 bits [4:2], when Extended format

This field reads-as-zero.

## Address packet payload (instruction virtual address or branch target address)

<!-- image -->

Figure D18-4 Address packet payload

## NS, byte 7 bit [7]

Non-secure state.

For an instruction virtual address (PC) this is the Security state the instruction was executed in. For a branch target address, this is the Security state at the target of the branch.

Note

For an Exception Return, the Security state at the target of the branch might be different to the Security state the instruction was executed in.

## When FEAT\_RME is implemented

With the NSE bit, indicates the Security state associated with the address.

| NSE   | NS   | Description                                                                                      |
|-------|------|--------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure state. This value is defined only if Secure state is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure state.                                                                                |
| 0b1   | 0b1  | Realm state.                                                                                     |

All other values are reserved.

Note

There is no encoding for Root because records are not generated at EL3.

The Security state associated with the address.

| NS   | Description       |
|------|-------------------|
| 0b0  | Secure state.     |
| 0b1  | Non-secure state. |

## EL, byte 7 bits [6:5]

Exception level. The Exception level associated with the address. For an instruction virtual address (PC) this is the Exception level the instruction was executed in. For a branch target address, this is the Exception level at the target of the branch.

| EL   | Description   |
|------|---------------|
| 0b00 | EL0.          |
| 0b01 | EL1.          |
| 0b10 | EL2.          |
| 0b11 | EL3.          |

Note

For an Exception Return, the Exception level at the target of the branch might be different to the Exception level the instruction was executed in.

## NSE, byte 7 bit [4]

Security state.

## Otherwise

Byte 7 bits [3:0]

This field reads as 0b0000 .

ADDR, bytes &lt;6:0&gt;

Address. Bits [55:0] of the instruction virtual address or branch target address.

## Address packet payload (data access virtual address)

Figure D18-5 Address packet payload

<!-- image -->

## TAG, byte &lt;7&gt;

## When FEAT\_RME is implemented

Together with the NS bit, indicates the Security state associated with the address.

## Otherwise

Top-byte tag.

If the applicable TBI bit is 0b1 , then a data access virtual address includes the top-byte tag. Otherwise this field reads-as-zero.

If the applicable TBI bit is 0b0 , then it is IMPLEMENTATION DEFINED whether this field reads as zero or holds bits[63:56] of the address.

## ADDR, bytes &lt;6:0&gt;

Address. Bits [55:0] of the data access virtual address.

This bit reads-as-zero.

## Address packet payload (data access physical address)

<!-- image -->

Figure D18-6 Address packet payload

NS, byte 7 bit [7]

Physical address space identifier.

## When FEAT\_RME is implemented

With the NSE bit, indicates the physical address space of the physical address.

| NSE   | NS   | Description                                                                                                     |
|-------|------|-----------------------------------------------------------------------------------------------------------------|
| 0b0   | 0b0  | Secure physical address space. This value is defined only if Secure PAS is implemented, and reserved otherwise. |
| 0b0   | 0b1  | Non-secure physical address space.                                                                              |
| 0b1   | 0b1  | Realm physical address space.                                                                                   |

All other values are reserved.

Note

There is no encoding for Root because records are not generated at EL3.

The physical address space of the physical address.

| NS   | Description                    |
|------|--------------------------------|
| 0b0  | Secure physical address space. |

## Otherwise

| NS   | Description                        |
|------|------------------------------------|
| 0b1  | Non-secure physical address space. |

## CH, byte 7 bit [6]

Tag Checked.

## When FEAT\_MTE2 is implemented

Indicates whether the access was checked against an Allocation Tag in memory.

| CH   | Description                                         |
|------|-----------------------------------------------------|
| 0b0  | Access not checked.                                 |
| 0b1  | Access checked against an Allocation Tag in memory. |

If Tag Check Faults are configured to be ignored by SCTLR\_EL x .TCF or SCTLR\_EL x .TCF0, then it is IMPLEMENTATION DEFINED whether this bit is 0b1 or 0b0 on a Tag Checked access.

If FEAT\_MTE\_CANONICAL\_TAGS is implemented and a sampled data access physical address is Canonically Tagged, then the value of this bit is 0b0 .

This bit reads-as-zero.

Byte 7 bit [5]

This bit reads as 0b0 .

## NSE, byte 7 bit [4]

Physical address space.

## When FEAT\_RME is implemented

Together with the NS bit, indicates the physical address space associated with the address.

## Otherwise

## Otherwise

This bit reads-as-zero.

## PAT, byte 7 bits [3:0]

Physical Address Tag.

## When FEAT\_MTE2 is implemented

Physical Address Tag for a checked access. If the access is not checked then this field reads as an IMPLEMENTATION DEFINED choice between 0b0000 and the Physical Address Tag used to perform the access.

## Otherwise

## ADDR, bytes &lt;6:0&gt;

Address. Bits [55:0] of the data access physical address.

This field reads-as-zero.

## D18.2.2 Context packet

Purpose

## Attributes

Byte 0 bits [3:2]

This field reads as 0b01 .

INDEX, byte 0 bits [1:0]

Identifies the context value.

| INDEX   | Description                                                                    |
|---------|--------------------------------------------------------------------------------|
| 0b00    | CONTEXTIDR_EL1. Included for all operations if enabled by CollectContextIDR1 . |
| 0b01    | CONTEXTIDR_EL2. Included for all operations if enabled by CollectContextIDR2 . |

All other values are reserved.

Provides context information for the record.

Multi-part packet comprising:

- 8-bit header.
- 32-bit payload.

## Context packet header

Byte 0 bits [7:6]

This field reads as 0b01 .

SZ, byte 0 bits [5:4]

Payload size.

| SZ   | Description   |
|------|---------------|
| 0b10 | Word.         |

This field reads as 0b10 .

Figure D18-7 Context packet header

<!-- image -->

## Context packet payload

CONTEXT, bytes &lt;3:0&gt;

The context value.

Figure D18-8 Context packet payload

<!-- image -->

## D18.2.3 Counter packet

Purpose

## Attributes

Count of cycles the operation spent performing all or part of its behavior. The counter value occupies the least significant bits of the payload. The remaining bits are set to zero.

Multi-part packet comprising:

- 8 or 16-bit header.
- 16-bit payload.

## Counter packet header

Figure D18-9 Counter packet header (Extended format)

<!-- image -->

Figure D18-10 Counter packet header (Short format)

<!-- image -->

Byte 1 bits [7:6], when Extended format; byte 0 bits [7:6], when Short format

This field reads as 0b10 .

SZ, byte 1 bits [5:4], when Extended format; byte 0 bits [5:4], when Short format

Payload size.

| SZ   | Description   |
|------|---------------|
| 0b01 | Halfword.     |

This field reads as 0b01 .

Byte 1 bit [3], when Extended format; byte 0 bit [3], when Short format

This bit reads as 0b1 .

INDEX, byte 0 bits [1:0], byte 1 bits [2:0], when Extended format; byte 0 bits [2:0], when Short format

| INDEX   | Description                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0b00000 | Total latency. Cycle count from the operation being dispatched for issue to the operation being complete. Included for all operations. |
| 0b00001 | Issue latency. The count of cycles when the operation is waiting to be issued.                                                         |

| INDEX Description                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00010 Translation latency. The count of cycles when at least one part of the operation is waiting for the MMUtocomplete an address translation. It is IMPLEMENTATION DEFINED whether a cycle is counted if a part of the operation is accessing memory, having completed an address translation for that part of the operation. For more information, see Additional infomation for each profiled memory access operation. |
| 0b00100 Alternate clock issue latency. As issue latency , but counts cycles in the clock domain specified by PMSIDR_EL1.ALTCLK.                                                                                                                                                                                                                                                                                              |
| 0b0011x IMPLEMENTATION DEFINED counter value.                                                                                                                                                                                                                                                                                                                                                                                |
| 0b1xxxx IMPLEMENTATION DEFINED counter value.                                                                                                                                                                                                                                                                                                                                                                                |

All other values are reserved.

In the Short format header, INDEX[4:3] are zero.

Dispatched for issue means:

- The operation has been decoded.
- The operation might not be ready to start execution because it is waiting for input values. The operation might be put into a queue.

Issued for execution means the operation is ready to start executing:

- For example, for a memory operation, this should be indicative of the cycle count from memory operation being dispatched for issue to access being initiated (virtual address).

## Complete means:

- The operation has completed execution and is no longer capable of stalling any instruction that consumes its output.
- It is IMPLEMENTATION DEFINED whether the operation has committed its results to the architectural state of the PE.
- For example:
- -For an arithmetic, FP or SIMD operation with variable timing, such as divide the results of the operation are available.
- -For load and atomic operations that return data, all data have been returned from memory.
- -For store and atomic operations that do not return data, it is not required that the store has reached its end point for it to be complete.
- -For branch operations, the branch has been resolved as taken or not taken.
- -For barrier operations, the barrier has completed.

For WFE and WFI operations, it is IMPLEMENTATION DEFINED whether:

- The instruction is complete before the PE enters a low-power state or when the PE wakes from the low-power state.
- Counters count in the low power state.
- Sampling an operation is itself a wakeup event.

Byte 0 bits [7:5], when Extended format

This field reads as 0b001 .

## Byte 0 bits [4:2], when Extended format

This field reads-as-zero.

## Counter packet payload

Figure D18-11 Counter packet payload (12-bit counters are implemented)

<!-- image -->

Figure D18-12 Counter packet payload (16-bit counters are implemented)

<!-- image -->

## Byte 1 bits [7:4], when 12-bit counters are implemented

This field reads as 0b0000 .

## COUNT, byte 1 bits [3:0], byte &lt;0&gt;, when 12-bit counters are implemented; bytes &lt;1:0&gt;, when 16-bit counters are implemented

The counter value occupies the least significant bits of the payload. The remaining bits are set to zero. The counters are:

- Unsigned numbers.
- 12 or 16 bits.
- Saturating.

PMSIDR\_EL1.CountSize indicates the size of counter implemented, and:

- If 12-bit counters are implemented, the value 0xFFF indicates the count has saturated.
- If 16-bit counters are implemented, the value 0xFFFF indicates the count has saturated.

## D18.2.4 Data Source packet

## Purpose

## Attributes

Byte 0 bits [7:6]

This field reads as 0b01 .

SZ, byte 0 bits [5:4]

Payload size.

| SZ   | Description   |
|------|---------------|
| 0b00 | Byte.         |
| 0b01 | Halfword.     |

Byte 0 bits [3:0]

This field reads as 0b0011 .

Data Source packet payload

Figure D18-14 Data Source packet payload (SZ == 0b00)

<!-- image -->

Figure D18-15 Data Source packet payload (SZ == 0b01)

<!-- image -->

If the implementation includes support for indicating the loaded data source, the Data Source packet indicates where the data returned for a load operation was sourced. It might also include other information, such as the state of the data at the source. It is IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether this is included for load and atomic operations that generate an External Abort. It is IMPLEMENTATION DEFINED whether this is included for atomic operations that do not return data to a PE register. Included for all other load and atomic operations.

Multi-part packet comprising:

- 8-bit header.

- 8 or 16-bit payload.

## Data Source packet header

Figure D18-13 Data Source packet header

<!-- image -->

SOURCE, byte &lt;0&gt;, when SZ == 0b00 ; bytes &lt;1:0&gt;, when SZ == 0b01

Because the list of data sources varies from system to system, the definition of this field is IMPLEMENTATION DEFINED. If a sampled operation generated multiple data accesses, it is IMPLEMENTATION DEFINED how the data source information is combined.

## D18.2.5 End packet

Purpose

Attributes

Defines the end of a record if a Timestamp packet is not present.

8-bit packet.

Field descriptions

Byte &lt;0&gt;

This field reads as 0b00000001 .

<!-- image -->

Figure D18-16 End packet

## D18.2.6 Events packet

## Purpose

## Attributes

Byte 0 bits [3:0]

This field reads as 0b0010 .

## Events packet payload

Figure D18-18 Events packet payload (SZ == 0b00)

<!-- image -->

Indicates events generated by the sampled operation. If the sampled operation generates one of the specified events, then the corresponding field is set to 0b1 . Otherwise, the corresponding field is set to 0b0 . Where applicable, a corresponding PMU event is defined for each event in the packet.

Multi-part packet comprising:

- 8-bit header.
- 8, 16, 32, or 64-bit payload.

## Events packet header

Byte 0 bits [7:6]

This field reads as 0b01 .

## SZ, byte 0 bits [5:4]

Payload size.

| SZ   | Description   |
|------|---------------|
| 0b00 | Byte.         |
| 0b01 | Halfword.     |
| 0b10 | Word.         |
| 0b11 | Doubleword.   |

Software must treat bits that are not output as zero.

Figure D18-17 Events packet header

<!-- image -->

E[63:48], bytes &lt;7:6&gt;, when SZ ==

Bytes &lt;5:4&gt;, when SZ ==

E[31:26], byte 3 bits [7:1], when SZ == 0b10 or SZ ==

```
0b11 Events 63 to 48. IMPLEMENTATION DEFINED. 0b11 This field reads-as-zero. 0b11 Events 31 to 26.
```

When FEAT\_SPEv1p4 is implemented

<!-- image -->

Figure D18-19 Events packet payload (SZ == 0b01)

Figure D18-20 Events packet payload (SZ == 0b10)

<!-- image -->

Figure D18-21 Events packet payload (SZ == 0b11)

<!-- image -->

Otherwise

Otherwise

This field reads-as-zero.

This field reads as an IMPLEMENTATION DEFINED value.

E[25], byte 3 bit [1], when SZ == 0b10 or SZ == 0b11

SMCUor external coprocessor operation.

When FEAT\_SPE\_SME is implemented

| E[25]   | Description                                                  |
|---------|--------------------------------------------------------------|
| 0b0     | Operation did not execute on an SMCUor external coprocessor. |
| 0b1     | Operation executed on an SMCUor external coprocessor.        |

## When FEAT\_SPEv1p4 is implemented

This bit reads-as-zero.

Otherwise

This bit reads as an IMPLEMENTATION DEFINED value.

E[24], byte 3 bit [0], when SZ == 0b10 or SZ == 0b11

Streaming SVE mode.

When FEAT\_SPE\_SME is implemented

| E[24]   | Description                                              |
|---------|----------------------------------------------------------|
| 0b0     | Operation executed when PE is in Non-streaming SVE mode. |
| 0b1     | Operation executed when PE is in Streaming SVE mode.     |

## When FEAT\_SPEv1p4 is implemented

This bit reads-as-zero.

This bit reads as an IMPLEMENTATION DEFINED value.

E[23], byte 2 bit [7], when SZ == 0b10 or SZ == 0b11

Data snooped.

This event is optional. If this event is implemented, then it is further IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero. If this event is not implemented, then this bit reads-as-zero.

## When FEAT\_SPEv1p4 is implemented

| E[23]   | Description                                                                                 |
|---------|---------------------------------------------------------------------------------------------|
| 0b0     | Operation was not a load, or did not access a cache outside the cache hierarchy of this PE. |
| 0b1     | Load operation that snooped data from a cache outside the cache hierarchy of this PE.       |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with DSNP\_HIT\_RD.

This bit reads-as-zero.

E[22], byte 2 bit [6], when SZ == 0b10 or SZ == 0b11

Recently fetched.

This event is optional. If this event is implemented, then it is further IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero. If this event is not implemented, then this bit reads-as-zero.

When FEAT\_SPEv1p4 is implemented

| E[22]   | Description                                                             |
|---------|-------------------------------------------------------------------------|
| 0b0     | Operation was not a load, or did not hit a recently-fetched cache line. |
| 0b1     | Load operation hit a recently-fetched line in a cache.                  |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with L1D\_LFB\_HIT\_RD, L2D\_LFB\_HIT\_RD, and LL\_LFB\_HIT\_RD.

This bit reads-as-zero.

E[21], byte 2 bit [5], when SZ == 0b10 or SZ == 0b11

Cache data modified.

This event is optional. If this event is implemented, then it is further IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero. If this event is not implemented, then this bit reads-as-zero.

## When FEAT\_SPEv1p4 is implemented

| E[21]   | Description                                                |
|---------|------------------------------------------------------------|
| 0b0     | Operation was not a load, or did not access modified data. |
| 0b1     | Load operation accessed modified data in a cache.          |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with DSNP\_HITM\_RD, L1D\_CACHE\_HITM\_RD, L2D\_CACHE\_HITM\_RD, and LL\_CACHE\_HITM\_RD.

It is IMPLEMENTATION DEFINED whether this bit is valid for a cache hit (L&lt; n &gt;D\_CACHE\_HITM\_RD), a snoop hit (DSNP\_HITM\_RD), or both.

Otherwise

Otherwise

## Otherwise

## Otherwise

Otherwise

This bit reads-as-zero.

E[20], byte 2 bit [4], when SZ == 0b10 or SZ == 0b11

Level 2 data cache miss.

This event is optional. If this event is implemented, then it is further IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero. If this event is not implemented, then this bit reads-as-zero.

When FEAT\_SPEv1p4 is implemented

| E[20]   | Description                                                                                                                                                                                 |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Operation was not a load, or did not access level 2 data cache.                                                                                                                             |
| 0b1     | Load operation accessed and missed the level 2 data or unified cache. This excludes accesses that do not cause a new cache refill but are satisfied from refilling data of a previous miss. |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with L2D\_CACHE\_LMISS\_RD.

This bit reads-as-zero.

E[19], byte 2 bit [3], when SZ == 0b10 or SZ == 0b11

Level 2 data cache access.

This event is optional. If this event is implemented, then it is further IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero. If this event is not implemented, then this bit reads-as-zero.

When FEAT\_SPEv1p4 is implemented

| E[19]   | Description                                                                         |
|---------|-------------------------------------------------------------------------------------|
| 0b0     | Operation was not a load, or did not access level 2 data cache.                     |
| 0b1     | Load operation caused a cache access to at least the level 2 data or unified cache. |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with L2D\_CACHE\_RD.

This bit reads-as-zero.

E[18], byte 2 bit [2], when SZ == 0b10 or SZ == 0b11

Empty predicate.

When FEAT\_SPEv1p1 is implemented and (FEAT\_SVE is implemented or FEAT\_SME is implemented)

| E[18]   | Description                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Operation was neither an SVE nor an SMEoperation, was not predicated, or at least one element in the Governing predicate or predicates was TRUE. |
| 0b1     | SVE or SMEoperation and all elements in the Governing predicate or predicates were FALSE.                                                        |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with SME\_PRED2\_EMPTY\_SPEC and SVE\_PRED\_EMPTY\_SPEC.

Note

For outer product instructions which are widening, predication is considered with respect to the input element size.

This bit reads-as-zero.

E[17], byte 2 bit [1], when SZ == 0b10 or SZ == 0b11

Partial or empty predicate.

When FEAT\_SPEv1p1 is implemented and (FEAT\_SVE is implemented or FEAT\_SME is implemented)

| E[17]   | Description                                                                                                                               |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Operation was neither an SVE nor an SMEoperation, was not predicated, or all elements in the Governing predicate or predicates were TRUE. |
| 0b1     | SVE or SMEoperation and at least one element in the Governing predicate or predicates was FALSE.                                          |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with SME\_PRED2\_NOT\_FULL\_SPEC and SVE\_PRED\_NOT\_FULL\_SPEC.

Note For outer product instructions which are widening, predication is considered with respect to the input element size.

Otherwise

Otherwise

```
This bit reads-as-zero. E[16], byte 2 bit [0], when SZ == 0b10 or SZ == 0b11 Transactional. This bit reads-as-zero. E[15:12], byte 1 bits [7:4], when SZ == 0b01 , SZ == 0b10 , or SZ == 0b11 Events 15 to 12. IMPLEMENTATION DEFINED. E[11], byte 1 bit [3], when SZ == 0b01 , SZ == 0b10 , or SZ == 0b11 Misalignment.
```

When FEAT\_SPEv1p1 is implemented

| E[11]   | Description                                                                                                                  |
|---------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Operation was not a load/store, or a load/store operation that was optimally aligned for the size of data being accessed.    |
| 0b1     | Load/store operation that, due to the alignment of the address and size of data being accessed, incurred additional latency. |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with LDST\_ALIGN\_LAT.

This bit reads-as-zero.

<!-- formula-not-decoded -->

Remote access.

| E[10]   | Description                                                                                                                                                                                                             |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Operation was not a load/store, or did not cause access to another socket.                                                                                                                                              |
| 0b1     | Load/store operation caused an access to another socket in a multi-socket system. This includes each data memory access that accesses another socket in a multi-socket system, including those that do not return data. |

This event is optional. If this event is implemented, then it is further IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero. If this event is not implemented, then this bit reads-as-zero.

If this event and FEAT\_PMUv3 are implemented, then this event is implemented consistently with REMOTE\_ACCESS or REMOTE\_ACCESS\_RD.

E[9], byte 1 bit [1], when SZ == 0b01 , SZ == 0b10 , or SZ == 0b11

Last Level cache miss.

| E[9]   | Description                                                                                                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Operation was not a load/store, or did not miss Last Level cache.                                                                                                                                                                |
| 0b1    | Load/store operation caused an access to at least the Last Level cache but is not completed by the Last Level cache. That is, each:                                                                                              |
|        | • Load operation that does not return data from the Last Level cache. • Store operation that does not update the Last Level cache. The event is not set for operations that are completed by a cache above the Last Level cache. |

This event is optional. If this event is implemented, then it is further IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero. If this event is not implemented, then this bit reads-as-zero.

If this event and FEAT\_PMUv3 are implemented, then this event is implemented consistently with LL\_CACHE\_MISS or LL\_CACHE\_MISS\_RD.

E[8], byte 1 bit [0], when SZ == 0b01 , SZ == 0b10 , or SZ == 0b11

Last Level cache access.

Otherwise

| E[8]   | Description                                                                                  |
|--------|----------------------------------------------------------------------------------------------|
| 0b0    | Operation was not a load/store, or did not access Last Level data or unified cache.          |
| 0b1    | Load/store operation caused a cache access to at least the Last Level data or unified cache. |

This event is optional. If this event is implemented, then it is further IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero. If this event is not implemented, then this bit reads-as-zero.

If this event and FEAT\_PMUv3 are implemented, then this event is implemented consistently with LL\_CACHE or LL\_CACHE\_RD.

Note

The architecture does not define the Last Level cache. The Last Level cache is typically the largest cache on this device shared by all PEs in the inner or outer Shareable domain of this PE. In a multi-socket system, it is IMPLEMENTATION DEFINED whether this includes caches on other sockets.

## E[7], byte 0 bit [7]

Mispredicted.

| E[7]   | Description                                                                            |
|--------|----------------------------------------------------------------------------------------|
| 0b0    | Operation was not a branch, or did not cause correction to the predicted program flow. |
| 0b1    | Abranch that caused a correction to the predicted program flow.                        |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with BR\_MIS\_PRED or BR\_MIS\_PRED\_RETIRED.

## E[6], byte 0 bit [6]

Not taken.

| E[6]   | Description                                                                                                                                                                                                                                                                                                          |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Operation was not a conditional operation, or did not fail its condition code check.                                                                                                                                                                                                                                 |
| 0b1    | Aconditional instruction that failed its condition code check. This includes conditional branches, compare-and-branch, conditional select, and conditional compares:                                                                                                                                                 |
|        | • For a conditional branch or compare-and-branch instruction, this means the branch was not taken. • For a conditional select, this means the second operand was written to the result. • For a condition compare, this means the condition flags were set to the immediate value and not the result of the compare. |

E[5], byte 0 bit [5]

TLB walk.

| E[5]   | Description                                                                                                                                                                                                                                                                  |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Operation was not a load/store, or did not generate TLB walk.                                                                                                                                                                                                                |
| 0b1    | Load/store operation that causes a refill of a data or unified TLB, involving at least one translation table walk access. This includes each complete or partial translation table walk that causes an access to memory, including to data or translation table walk caches. |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with DTLB\_WALK.

## E[4], byte 0 bit [4]

TLB access.

| E[4]   | Description                                                                               |
|--------|-------------------------------------------------------------------------------------------|
| 0b0    | Operation was not a load/store that accessed the TLB.                                     |
| 0b1    | Load/store operation caused an access to at least the first level of data or unified TLB. |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with L1D\_TLB.

## E[3], byte 0 bit [3]

Level 1 data cache refill or miss.

## When FEAT\_SPEv1p4 is implemented

| E[3]   | Description                                                                                                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Operation was not a load/store, or did not miss in the level 1 data cache.                                                                                                                               |
| 0b1    | Load/store operation accessed and missed the first level of data or unified cache. This excludes accesses that do not cause a new cache refill but are satisfied from refilling data of a previous miss. |

It is IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero.

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with L1D\_CACHE\_MISS or L1D\_CACHE\_MISS\_RD.

## Otherwise

| E[3]   | Description                                                                                                                                                                                                                                                                                       |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Operation was not a load/store, or did not cause a level 1 data cache refill.                                                                                                                                                                                                                     |
| 0b1    | Load/store operation caused a refill of at least the first level of data or unified cache. This includes each data memory access that causes a refill from outside the cache. It excludes accesses that do not cause a new cache refill but are satisfied from refilling data of a previous miss. |

It is IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero.

## Otherwise

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with L1D\_CACHE\_REFILL or L1D\_CACHE\_REFILL\_RD.

E[2], byte 0 bit [2]

Level 1 data cache access.

| E[2]   | Description                                                                                      |
|--------|--------------------------------------------------------------------------------------------------|
| 0b0    | Operation was not a load/store, or did not access the level 1 data cache.                        |
| 0b1    | Load/store operation caused a cache access to at least the first level of data or unified cache. |

It is IMPLEMENTATION DEFINED and might be CONSTRAINED UNPREDICTABLE whether a store can finish execution before this event is generated, meaning that, for stores, this event is not recorded and this bit reads-as-zero.

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with L1D\_CACHE or L1D\_CACHE\_RD.

E[1], byte 0 bit [1]

Architecturally retired.

When the PE supports sampling of speculative instructions

| E[1]   | Description                                                                                                          |
|--------|----------------------------------------------------------------------------------------------------------------------|
| 0b0    | Did not retire.                                                                                                      |
| 0b1    | Committed its results to the architectural state of the PE, or completed with a synchronous architectural exception. |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with INST\_RETIRED.

Note

Aconditional instruction can retire even if it fails its condition code check.

This bit reads-as-one.

E[0], byte 0 bit [0]

Generated exception.

| E[0]   | Description                             |
|--------|-----------------------------------------|
| 0b0    | Did not generate an exception.          |
| 0b1    | Completed with a synchronous exception. |

If FEAT\_PMUv3 is implemented, then this event is implemented consistently with EXC\_TAKEN.

If E[1] in the same Events packet is 0, then the meaning of this bit is IMPLEMENTATION DEFINED.

## D18.2.7 Operation Type packet

Purpose

Defines the type of operation sampled. Included for all operations.

Multi-part packet comprising:

- 8-bit header.
- 8-bit payload.

Operation Type packet header

Byte 0 bits [7:6]

This field reads as 0b01 .

SZ, byte 0 bits [5:4]

Payload size.

| SZ   | Description   |
|------|---------------|
| 0b00 | Byte.         |

This field reads as 0b00 .

## Attributes

Byte 0 bits [3:2]

This field reads as 0b10 .

CLASS, byte 0 bits [1:0]

Top-level operation class.

| CLASS   | Description                                                                                                                                                                                                                                    |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00    | The payload is one of the following and the SUBCLASS field in the payload encodes which: • Other. • Data processing, SVE vector. • Data processing, SMEarray.                                                                                  |
| 0b01    | Load, store, or atomic. The payload is one of the following and the SUBCLASS field in the payload encodes which: • Load/store, general. • Load/store, extended. • Load/store, SVE or SME. • Load/store, Memory Copy. • Load/store, Memory Set. |

<!-- image -->

Figure D18-22 Operation Type packet header

| CLASS   | Description                 |
|---------|-----------------------------|
| 0b10    | Branch or exception return. |

All other values are reserved.

## Operation Type packet payload (Other)

Figure D18-23 Operation Type packet payload

<!-- image -->

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Describes the operation type.

| SUBCLASS   | Description                                                                     |
|------------|---------------------------------------------------------------------------------|
| 0b00000xxx | Other operation. Bits [2:0] are further defined as the ASE, FP, and CONDfields. |

Other values are either defined by other payload types for CLASS== 0b00 or reserved.

This field reads as 0b00000xxx .

ASE, byte 0 bit [2]

Advanced SIMD.

When FEAT\_SPE\_FPF is implemented

| ASE   | Description                     |
|-------|---------------------------------|
| 0b0   | Not an Advanced SIMD operation. |
| 0b1   | Advanced SIMD operation.        |

## Otherwise

This bit reads-as-zero.

FP, byte 0 bit [1]

Floating-point.

When FEAT\_SPE\_FPF is implemented

| FP   | Description                     |
|------|---------------------------------|
| 0b0  | Not a floating-point operation. |
| 0b1  | Floating-point operation.       |

## Otherwise

## COND, byte 0 bit [0]

Conditional.

| COND   | Description                                          |
|--------|------------------------------------------------------|
| 0b0    | Unconditional operation.                             |
| 0b1    | Conditional select or conditional compare operation. |

## Operation Type packet payload (Data processing, SVE vector)

## Configurations

This bit reads-as-zero.

Defined only if all of the following are true:

- FEAT\_SPEv1p1 is implemented.
- FEAT\_SVE is implemented.

Figure D18-24 Operation Type packet payload

<!-- image -->

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Describes the operation type.

| SUBCLASS   | Description                                                                               |
|------------|-------------------------------------------------------------------------------------------|
| 0b0xxx1xx0 | SVE vector operation. Bits [6:4,2:1] are further defined as the EVL, PRED, and FP fields. |

Other values are either defined by other payload types for CLASS== 0b00 or reserved.

This field reads as 0b0xxx1xx0 .

## EVL, byte 0 bits [6:4]

Sampled Effective Vector Length.

Describes the size in bits of the vector or vectors operated on by the sampled SVE SIMD operation. That is:

- For a sampled SVE multi-vector SIMD operation, the number of elements in each vector, multiplied by the number of vectors, multiplied by the element size.

- For other sampled SVE SIMD operations, the number of elements in the vector multiplied by the element size.

| EVL   | Description                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------|
| 0b000 | 32 bits.                                                                                                |
| 0b001 | 64 bits.                                                                                                |
| 0b010 | 128 bits.                                                                                               |
| 0b011 | 256 bits.                                                                                               |
| 0b100 | 512 bits.                                                                                               |
| 0b101 | 1024 bits.                                                                                              |
| 0b110 | 2048 bits.                                                                                              |
| 0b111 | More than 2048 bits. This value is defined only if FEAT_SPE_SME is implemented, and reserved otherwise. |

If the sampled effective vector length for the input operands of the sampled SVE SIMD operation and the sampled effective vector length for the output operand of the sampled SVE SIMD operation differ, then the sampled effective vector length of the output operand is used.

The Effective SVE vector length is always a power of two. However, the sampled effective vector length can be any size down to the smallest element size.

If the sampled effective vector length is not a power of two, or is less than 32 bits, then the value is rounded up before it is encoded in this field.

## PRED, byte 0 bit [2]

Predicated SVE operation.

| PRED   | Description                                                                                                                                                                       |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Not predicated.                                                                                                                                                                   |
| 0b1    | Predicated SVE operation. The operation is an SVE operation that writes to a vector destination register under a Governing predicate using either zeroing or merging predication. |

## FP, byte 0 bit [1]

Floating-point operation.

| FP   | Description                     |
|------|---------------------------------|
| 0b0  | Not a floating-point operation. |
| 0b1  | Floating-point operation.       |

## Operation Type packet payload (Data processing, SME array)

## Configurations

Defined only if FEAT\_SPE\_SME is implemented.

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Describes the operation type.

| SUBCLASS   | Description                                                                                                                                                        |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1xxx1xx0 | SMEtile operation. Bits [6:4,2:1] are further defined as the ETS and FP fields. This value is defined only if FEAT_SPE_SME is implemented, and reserved otherwise. |

Other values are either defined by other payload types for CLASS== 0b00 or reserved.

This field reads as 0b1xxx1xx0 .

## ETS, byte 0 bits [6:4,2]

Sampled Effective vector length or Tile Size.

Describes the size in bits of the portion of the ZA array operated on by the sampled SME vector or tile SIMD operation. That is:

- For a sampled SME tile SIMD operation, the number of elements in the ZA tile or tiles multiplied by the element size.
- For a sampled SME multi-vector SIMD operation, the number of elements in each vector, multiplied by the number of vectors, multiplied by the element size.
- For other sampled SME vector SIMD operations, the number of elements in the vector multiplied by the element size.

| ETS    | Description    |
|--------|----------------|
| 0b0000 | 128 bits.      |
| 0b0001 | 256 bits.      |
| 0b0010 | 512 bits.      |
| 0b0011 | 1024 bits.     |
| 0b0100 | 2048 bits.     |
| 0b0101 | 4096 bits.     |
| 0b0110 | 8192 bits.     |
| 0b0111 | 16384 bits.    |
| 0b1000 | 32768 bits.    |
| 0b1001 | 65536 bits.    |
| 0b1010 | 131072 bits.   |
| 0b1011 | 262144 bits.   |
| 0b1111 | Whole ZAarray. |

All other values are reserved.

Figure D18-25 Operation Type packet payload

<!-- image -->

## FP, byte 0 bit [1]

If the sampled effective vector length or tile size for the input operands of the sampled SME SIMD operation and the sampled effective vector length or tile size for the output operand of the sampled SMESIMDoperation differ, then the sampled effective vector length or tile size of the output operand is used.

If the sampled effective vector length or tile size is not a power of two, or is less than 128 bits, then the value is rounded up before it is encoded in this field.

The 0b1111 value is used when the whole ZA array is operated on at once by the sampled instruction or operation. For example the ZERO (tiles) instruction writes to the whole ZA array, and might use this encoding even if the instruction specifies a mask that prevents part of the ZA array being updated.

Floating-point operation.

| FP   | Description                     |
|------|---------------------------------|
| 0b0  | Not a floating-point operation. |
| 0b1  | Floating-point operation.       |

## Operation Type packet payload (Load/store, general)

<!-- image -->

Figure D18-26 Operation Type packet payload (Allocation Tag load/store)

<!-- image -->

Figure D18-27 Operation Type packet payload (General-purpose load/store)

Figure D18-28 Operation Type packet payload (SIMD&amp;FP load/store)

<!-- image -->

Figure D18-29 Operation Type packet payload (System register access transformed to a load/store)

<!-- image -->

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Indicates the load/store type.

| SUBCLASS   | Description                                                                                                                                                                                                               |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000000x | Aload/store targeting the general-purpose registers, other than an atomic operation, load-acquire, store-release, or exclusive.                                                                                           |
| 0b0000010x | Aload/store targeting the SIMD&FP registers, or, if FEAT_SPEv1p1 is not implemented, the SVE registers.                                                                                                                   |
| 0b0001000x | Aload/store targeting unspecified registers. This value is defined only if FEAT_SPEv1p1 is implemented, and reserved otherwise.                                                                                           |
| 0b0001010x | Aload/store of an Allocation Tag or multiple Allocation Tags. This value is defined only if all of the following are true:                                                                                                |
| 0b0011000x | This value is reserved otherwise. An MRS or MSR operation at EL1 transformed to a load/store when the Effective value of HCR_EL2.NV2 is 1. This value is defined only if FEAT_NV2 is implemented, and reserved otherwise. |

Other values are either defined by other payload types for CLASS== 0b01 or reserved.

Bit [0] is further defined as the LDST field.

## LDST, byte 0 bit [0]

Store not load.

| LDST   | Description                                                                                             |
|--------|---------------------------------------------------------------------------------------------------------|
| 0b0    | Memory-reading instruction. That is, a load, a swap, or an atomic that returns a value to the PE.       |
| 0b1    | Not a memory-reading instruction. That is, a store or an atomic that does not return a value to the PE. |

Memory-reading instruction and Memory-writing instruction are defined in Definitions.

## Operation Type packet payload (Load/store, extended)

Figure D18-31 Operation Type packet payload

<!-- image -->

SUBCLASS, byte &lt;0&gt;

Figure D18-30 Operation Type packet payload (Unspecified load/store)

<!-- image -->

Second-level operation class. Indicates the load/store type.

| SUBCLASS   | Description                                                                                                                            |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0b000xxx1x | An atomic operation, load-acquire, store-release, or exclusive. Bits [4:2,0] are further defined as the AT, EXCL, AR, and LDST fields. |

Other values are either defined by other payload types for CLASS== 0b01 or reserved.

This field reads as 0b000xxx1x .

## AR, byte 0 bit [4]

Acquire/Release.

| AR   | Description                                             |
|------|---------------------------------------------------------|
| 0b0  | Load/store/atomic without Acquire or Release semantics. |
| 0b1  | Load/store/atomic with Acquire or Release semantics.    |

## EXCL, byte 0 bit [3]

Exclusive.

| EXCL   | Description                          |
|--------|--------------------------------------|
| 0b0    | Load/store/atomic without Exclusive. |
| 0b1    | Load/store with Exclusive.           |

## AT, byte 0 bit [2]

Atomic load/store.

| AT   | Description   |
|------|---------------|
| 0b0  | Not atomic.   |
| 0b1  | Atomic.       |

## LDST, byte 0 bit [0]

Store not load.

| LDST   | Description                                                                                             |
|--------|---------------------------------------------------------------------------------------------------------|
| 0b0    | Memory-reading instruction. That is, a load, a swap, or an atomic that returns a value to the PE.       |
| 0b1    | Not a memory-reading instruction. That is, a store or an atomic that does not return a value to the PE. |

Memory-reading instruction and Memory-writing instruction are defined in Definitions.

## Operation Type packet payload (Load/store, SVE or SME)

## Configurations

Defined only if all of the following are true:

- Any of the following are true:
- FEAT\_SPEv1p1 is implemented.

- FEAT\_SME is implemented.

- FEAT\_SVE is implemented.

Figure D18-32 Operation Type packet payload

<!-- image -->

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Indicates the load/store type.

| SUBCLASS   | Description                                                                                                              |
|------------|--------------------------------------------------------------------------------------------------------------------------|
| 0bxxxx1x0x | Aload/store targeting the SVE or SMEregisters. Bits [7:4,2,0] are further defined as the PRED, EVL, SG, and LDST fields. |

Other values are either defined by other payload types for CLASS== 0b01 or reserved.

This field reads as 0bxxxx1x0x .

## SG, byte 0 bit [7]

Gather/scatter SVE load/store.

| SG   | Description                            |
|------|----------------------------------------|
| 0b0  | Neither gather load nor scatter store. |
| 0b1  | Gather load or scatter store.          |

## EVL, byte 0 bits [6:4]

Sampled Effective Vector Length.

Describes the size in bits of the vector or vectors operated on by the sampled SVE or SME SIMD load/store operation.

If FEAT\_SPE\_SME is implemented, then the EVL field records the upper bound of the sampled effective vector length multiplied by the number of vectors loaded or stored by the sampled operation. If the sampled effective vector length for the sampled operation is greater than 2048 bits, then EVL is set to 0b111 .

Otherwise, the EVL field records an upper bound of the sampled effective vector length for a single vector loaded or stored by the sampled operation.

| EVL   | Description                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------|
| 0b000 | 32 bits.                                                                                                |
| 0b001 | 64 bits.                                                                                                |
| 0b010 | 128 bits.                                                                                               |
| 0b011 | 256 bits.                                                                                               |
| 0b100 | 512 bits.                                                                                               |
| 0b101 | 1024 bits.                                                                                              |
| 0b110 | 2048 bits.                                                                                              |
| 0b111 | More than 2048 bits. This value is defined only if FEAT_SPE_SME is implemented, and reserved otherwise. |

All other values are reserved.

The Effective SVE vector length is always a power of two. However, the sampled effective vector length can be any size down to the smallest element size.

If the sampled effective vector length is not a power of two, or is less than 32 bits, then the value is rounded up before it is encoded in this field.

## PRED, byte 0 bit [2]

Predicated SVE or SME load/store.

| PRED   | Description                                                                                                                                                                                                                                           |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Not predicated.                                                                                                                                                                                                                                       |
| 0b1    | The operation is one of the following:                                                                                                                                                                                                                |
|        | • If FEAT_SPEv1p2 is implemented, a predicated SVE or SMEload operation that writes to one or more vector destination registers under a Governing predicate using zeroing predication. • Apredicated SVE or SMEstore of one or more vector registers. |

## LDST, byte 0 bit [0]

Store not load.

| LDST   | Description   |
|--------|---------------|
| 0b0    | Load.         |
| 0b1    | Store.        |

## Operation Type packet payload (Load/store, Memory Copy)

## Configurations

Defined only if all of the following are true:

- FEAT\_SPEv1p3 is implemented.
- FEAT\_MOPS is implemented.

Figure D18-33 Operation Type packet payload

<!-- image -->

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Indicates the load/store type.

| SUBCLASS   | Description                                                                             |
|------------|-----------------------------------------------------------------------------------------|
| 0b0010000x | Aload/store from a Memory Copy operation. Bit [0] is further defined as the LDST field. |

Other values are either defined by other payload types for CLASS== 0b01 or reserved.

This field reads as 0b0010000x .

## LDST, byte 0 bit [0]

Store not load.

| LDST   | Description                                                    |
|--------|----------------------------------------------------------------|
| 0b0    | Load. The sampled virtual address is the source address.       |
| 0b1    | Store. The sampled virtual address is the destination address. |

## Operation Type packet payload (Load/store, Memory Set)

## Configurations

Defined only if all of the following are true:

- FEAT\_SPEv1p3 is implemented.
- FEAT\_MOPS is implemented.

Figure D18-34 Operation Type packet payload

<!-- image -->

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Indicates the load/store type.

| SUBCLASS   | Description                         |
|------------|-------------------------------------|
| 0b00100101 | Astore from a Memory Set operation. |

Other values are either defined by other payload types for CLASS== 0b01 or reserved.

This field reads as 0b00100101 .

## Operation Type packet payload (Load/store, GCS)

## Configurations

Defined only if all of the following are true:

- FEAT\_GCS is implemented.
- FEAT\_SPEv1p4 is implemented.

Figure D18-35 Operation Type packet payload

<!-- image -->

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Indicates the load/store type.

| SUBCLASS   | Description                                                                                |
|------------|--------------------------------------------------------------------------------------------|
| 0b01000x0x | Aload/store from a GCS operation. Bits [2,0] are further defined as the COMMandLDSTfields. |

Other values are either defined by other payload types for CLASS== 0b01 or reserved.

This field reads as 0b01000x0x .

## COMM,byte 0 bit [2]

Common. Indicates whether or not the sampled load/store operation is from a Branch with link or Procedure return instruction.

| COMM   | Description                                        |
|--------|----------------------------------------------------|
| 0b0    | Branch with link or Procedure return.              |
| 0b1    | Neither a Branch with link nor a Procedure return. |

## LDST, byte 0 bit [0]

Store not load.

| LDST   | Description                                  |
|--------|----------------------------------------------|
| 0b0    | Load or swap that returns a value to the PE. |
| 0b1    | Store.                                       |

## Operation Type packet payload (Branch)

Figure D18-36 Operation Type packet payload

<!-- image -->

## SUBCLASS, byte &lt;0&gt;

Second-level operation class. Describes the operation type.

| SUBCLASS   | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| 0b000xxxxx | Branch. Bits [4:0] are further defined as the CR, GCS, IND, and CONDfields. |

Other values are reserved.

This field reads as 0b000xxxxx .

## CR, byte 0 bits [4:3]

Information about whether the branch was a subroutine call or a subroutine return instruction.

| CR   | Description                                                                                                 |
|------|-------------------------------------------------------------------------------------------------------------|
| 0b00 | Whether the sampled branch operation is a Branch with link or a Procedure return operation is not recorded. |
| 0b01 | Branch with link.                                                                                           |
| 0b10 | Procedure return.                                                                                           |
| 0b11 | Neither Branch with link nor Procedure return.                                                              |

If FEAT\_SPE\_CRR is not implemented, then the only permitted value is 0b00 .

If FEAT\_SPE\_CRR is implemented, then the value of 0b00 is not permitted.

## GCS, byte 0 bit [2]

Guarded control stack data access.

## When FEAT\_SPEv1p4 is implemented

Indicates whether the sampled branch operation generated a Guarded control stack data access.

| GCS   | Description                           |
|-------|---------------------------------------|
| 0b0   | No Guarded control stack data access. |
| 0b1   | Guarded control stack data access.    |

If FEAT\_GCS is not implemented, then the only permitted value is 0b0 .

This bit reads-as-zero.

## Otherwise

IND, byte 0 bit [1]

Indirect.

| IND   | Description      |
|-------|------------------|
| 0b0   | Direct branch.   |
| 0b1   | Indirect branch. |

## COND, byte 0 bit [0]

Conditional.

| COND   | Description           |
|--------|-----------------------|
| 0b0    | Unconditional branch. |
| 0b1    | Conditional branch.   |

## D18.2.8 Padding

Purpose

Attributes

Allows the PE to create alignment in the protocol buffer.

8-bit packet.

Field descriptions

Byte &lt;0&gt;

This field reads as 0b00000000 .

<!-- image -->

Figure D18-37 Padding

## D18.2.9 Timestamp packet

## Purpose

## Attributes

Byte 0 bits [3:0]

The 64-bit timestamp value when the operation was sampled. The Timestamp packet must come at the end of the record. If the Timestamp packet is not present, an End packet must come at the end of the record.

Multi-part packet comprising:

- 8-bit header.
- 64-bit payload.

## Timestamp packet header

Byte 0 bits [7:6]

This field reads as 0b01 .

SZ, byte 0 bits [5:4]

Payload size.

| SZ   | Description   |
|------|---------------|
| 0b11 | Doubleword.   |

This field reads as 0b11 .

This field reads as 0b0001 .

Figure D18-38 Timestamp packet header

<!-- image -->

## Timestamp packet payload

TS, bytes &lt;7:0&gt;

Timestamp value when the operation was sampled. The value depends on the result of CollectTimeStamp() :

- If TimeStamp\_Virtual , the value of PhysicalCountInt() - CNTVOFF\_EL2.
- If TimeStamp\_Physical , the value of PhysicalCountInt() .
- If TimeStamp\_OffsetPhysical , the value of PhysicalCountInt() - CNTPOFF\_EL2. Only supported when FEAT\_ECV is implemented.

If CollectTimeStamp() returns TimeStamp\_None , then the Timestamp packet is not included and an End packet must come at the end of the record.

However, if the Generic Timer System counter is disabled and CollectTimeStamp() returns a value other than TimeStamp\_None , then it is IMPLEMENTATION DEFINED which of the following occurs:

- The Statistical Profiling Unit behaves as if CollectTimeStamp() returns the value TimeStamp\_None .
- The value of this field in the record is UNKNOWN.

Note

This set of behaviors is only permitted when the actual System counter is disabled, that is, when CNTEN.EN is 0b0 . It does not apply when the System counter is enabled but not accessible at the current Exception level.

Figure D18-39 Timestamp packet payload

<!-- image -->

| 7                | 4                | 2                |                  |
|------------------|------------------|------------------|------------------|
| TS[7:0] Byte     | TS[7:0] Byte     | TS[7:0] Byte     | TS[7:0] Byte     |
| TS[15:8] Byte 1  | TS[15:8] Byte 1  | TS[15:8] Byte 1  | TS[15:8] Byte 1  |
| TS[23:16] Byte   | TS[23:16] Byte   | TS[23:16] Byte   | TS[23:16] Byte   |
| TS[31:24] Byte   | TS[31:24] Byte   | TS[31:24] Byte   | TS[31:24] Byte   |
| TS[39:32] Byte 4 | TS[39:32] Byte 4 | TS[39:32] Byte 4 | TS[39:32] Byte 4 |
| TS[47:40] Byte 5 | TS[47:40] Byte 5 | TS[47:40] Byte 5 | TS[47:40] Byte 5 |
| TS[55:48] Byte 6 | TS[55:48] Byte 6 | TS[55:48] Byte 6 | TS[55:48] Byte 6 |
| TS[63:56] Byte 7 | TS[63:56] Byte 7 | TS[63:56] Byte 7 | TS[63:56] Byte 7 |

## Chapter D19 The Branch Record Buffer Extension

This chapter describes the Branch Record Buffer Extension (BRBE). It contains the following sections:

- About the Branch Record Buffer Extension.
- Branch record filtering.
- Branch record buffer operation.
- Branch record buffer.
- Programmers' model.