## 10.5 Registers

The total number of counter groups that are associated with one SMMU is IMPLEMENTATION DEFINED. Each counter group is represented by one 4KB page (Page 0) with one optional additional 4KB page (Page 1), both of which are at IMPLEMENTATION DEFINED base addresses.

If Page 1 is present, the registers for counter values, overflow status and shadow capture control appear in Page 1 instead of Page 0. Presence is indicated by SMMU\_PMCG\_CFGR.RELOC\_CTRS. Arm recommends that Page 1 is implemented and, if so, Arm strongly recommends that Page 1 is located within an aligned 64KB system address span that is otherwise unused.

Note: This permits a hypervisor to use a 64KB stage 2 granule to expose the Page 1 counter values for direct access by a virtual machine. Arm expects that guest access to stage 1 registers (for counter configuration) will be trapped and controlled by the hypervisor, rather than accessed directly.

Access behaviors follow the same rules as for the SMMU registers described in section 6.2 Register overview . In particular:

- Aligned 32-bit access is permitted to 64-bit registers.
- It is IMPLEMENTATION DEFINED whether 64-bit accesses to 64-bit registers are atomic.
- All registers are little-endian.

Unless otherwise specified, software is permitted to read or write a register at any time. Writes to read-only registers are IGNORED.

## 10.5.1 SMMU\_PMCGn address map

The map of the base PMCG register Page 0 is shown here:

| Offset                              | Register           | Notes                                                                                                                                                     |
|-------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x000 + stride*n ( 0x000 to 0x1FF ) | SMMU_PMCG_EVCNTRn  | 32- or 64-bit, RW, 0 <= n < 64 Registers placed on a 4-byte stride if SMMU_PMCG_CFGR.SIZE <= 31 (counters 32-bit or smaller), otherwise an 8-byte stride. |
| 0x400 + 4*n ( 0x400 to              | SMMU_PMCG_EVTYPERn | 32-bit, RW, 0 <= n < 64                                                                                                                                   |
| 0x600 + stride*n ( 0x600 to 0x7FF ) | SMMU_PMCG_SVRn     | 32- or 64-bit, RO, 0 <= n < 64 Stride same as for SMMU_PMCG_EVCNTRn.                                                                                      |
| 0xA00 + 4*n ( 0xA00 to              | SMMU_PMCG_SMRn     | 32-bit, RW, 0 <= n < 64                                                                                                                                   |

Chapter 10. Performance Monitors Extension 10.5. Registers

| Offset   | Register                                 | Notes              |
|----------|------------------------------------------|--------------------|
| 0xC00    | SMMU_PMCG_CNTENSET0                      | 64-bit,RW          |
| 0xC20    | SMMU_PMCG_CNTENCLR0                      | 64-bit,RW          |
| 0xC40    | SMMU_PMCG_INTENSET0                      | 64-bit,RW          |
| 0xC60    | SMMU_PMCG_INTENCLR0                      | 64-bit,RW          |
| 0xC80    | SMMU_PMCG_OVSCLR0                        | 64-bit,RW          |
| 0xCC0    | SMMU_PMCG_OVSSET0                        | 64-bit,RW          |
| 0xD88    | SMMU_PMCG_CAPR                           | 32-bit,WO          |
| 0xDF8    | SMMU_PMCG_SCR                            | 32-bit, Secure,RW  |
| 0xE00    | SMMU_PMCG_CFGR                           | 32-bit, RO         |
| 0xE04    | SMMU_PMCG_CR                             | 32-bit,RW          |
| 0xE08    | SMMU_PMCG_IIDR                           | 32-bit, RO         |
| 0xE20    | SMMU_PMCG_CEID0                          | 64-bit, RO         |
| 0xE28    | SMMU_PMCG_CEID1                          | 64-bit, RO         |
| 0xE40    | Alias of SMMU_PMCG_SCR, otherwise RAZ/WI | 32-bit, Secure,RW  |
| 0xE48    | SMMU_PMCG_ROOTCR                         | 32-bit, Root,RW    |
| 0xE50    | SMMU_PMCG_IRQ_CTRL                       | 32-bit,RW          |
| 0xE54    | SMMU_PMCG_IRQ_CTRLACK                    | 32-bit, RO         |
| 0xE58    | SMMU_PMCG_IRQ_CFG0                       | 64-bit,RW          |
| 0xE60    | SMMU_PMCG_IRQ_CFG1                       | 32-bit,RW          |
| 0xE64    | SMMU_PMCG_IRQ_CFG2                       | 32-bit,RW          |
| 0xE68    | SMMU_PMCG_IRQ_STATUS                     | 32-bit, RO         |
| 0xE6C    | SMMU_PMCG_GMPAM                          | 32-bit,RW          |
| 0xE70    | SMMU_PMCG_AIDR                           | 32-bit, RO         |
| 0xE74    | SMMU_PMCG_MPAMIDR                        | 32-bit, RO         |
| 0xE78    | SMMU_PMCG_S_MPAMIDR                      | 32-bit, Secure, RO |

| Offset      | Register               | Notes                  |
|-------------|------------------------|------------------------|
| 0xE80 -     | IMPLEMENTATION DEFINED |                        |
| 0xEFF 0xFB0 | SMMU_PMCG_ID_REGS      | IMPLEMENTATION DEFINED |

When Page 1 is present (SMMU\_PMCG\_CFGR.RELOC\_CTRS == 1), the following registers are relocated to Page 1 and their corresponding Page 0 locations become RES0. Offsets are shown relative to the base address of Page 1.

| Offset                            | Register          | Notes                                          |
|-----------------------------------|-------------------|------------------------------------------------|
| 0x000 + n*stride (0x000 to 0x1FF) | SMMU_PMCG_EVCNTRn | Same as for corresponding locations in Page 0. |
| 0x600 + n*stride (0x600 to 0x7FF) | SMMU_PMCG_SVRn    | Same as for corresponding locations in Page 0. |
| 0xC80                             | SMMU_PMCG_OVSCLR0 | Same as for corresponding locations in Page 0. |
| 0xCC0                             | SMMU_PMCG_OVSSET0 | Same as for corresponding locations in Page 0. |
| 0xD88                             | SMMU_PMCG_CAPR    | Same as for corresponding locations in Page 0. |

## 10.5.2 Register details

## 10.5.2.1 SMMU\_PMCG\_EVCNTR&lt;n&gt;, n = 0 - 63

The SMMU\_PMCG\_EVCNTR&lt;n&gt; characteristics are:

## Purpose

Provides Counters for PMCG events.

## Configuration

When counter size is &lt;= 32 bits (SMMU\_PMCG\_CFGR.SIZE &lt;= 31), these registers are 32 bits in size. Otherwise, these registers are 64 bits in size. Present in an array of n registers, all of size 32 or 64, each corresponding to counter n.

The counter value is incremented when an event matching SMMU\_PMCG\_EVTYPERn.EVENT occurs, the counter is enabled (the respective CNTEN == 1) and, if the event type is filterable by StreamID, filters match. See section 10.4 StreamIDs and filtering for information on filtering.

When a counter value is incremented by the PMCG, the increment is atomic with respect to external writes to this register.

Registers corresponding to unimplemented counters are RES0.

## Attributes

SMMU\_PMCG\_EVCNTR&lt;n&gt; is a:

- 32-bit register when UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &lt;= 31.
- 64-bit register when UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &gt; 31.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

When UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &lt;= 31:

```
COUNTER_VALUE 31 0
```

## COUNTER\_VALUE, bits [31:0]

```
Counter value[N:0]. R == SMMU_PMCG_CFGR.SIZE + 1. If R < 32, bits [31:R] are RES0. The reset behavior of this field is:
```

- This field resets to an UNKNOWN value.

## When UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &gt; 31:

```
COUNTER_VALUE 63 32 COUNTER_VALUE 31 0
```

## COUNTER\_VALUE, bits [63:0]

```
Counter value[N:0].
```

R == SMMU\_PMCG\_CFGR.SIZE + 1.

If R &gt; 32 and R &lt; 64, bits [63:R] are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_PMCG\_EVCNTR&lt;n&gt;

Accesses to this register use the following encodings:

## When UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &lt;= 31

Accessible at offset 0x000 + (4 * n) from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## When UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &gt; 31

Accessible at offset 0x000 + (8 * n) from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.2 SMMU\_PMCG\_EVTYPER&lt;n&gt;, n = 0 - 63

The SMMU\_PMCG\_EVTYPER&lt;n&gt; characteristics are:

## Purpose

These registers contain per-counter configuration, in particular the event type counted.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_EVTYPER&lt;n&gt; is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## OVFCAP, bit [31]

## When SMMU\_PMCG\_CFGR.CAPTURE == 1:

Overflow capture.

| OVFCAP   | Meaning                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------|
| 0b0      | An overflow of counter n does not trigger a capture of all counters.                                      |
| 0b1      | An overflow of counter n triggers a capture of all counters in the same way as by SMMU_PMCG_CAPR.CAPTURE. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FILTER\_SEC\_SID, bit [30]

## When n == 0 or SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0:

Filter Secure StreamIDs.

| FILTER_SEC_SID   | Meaning                                             |
|------------------|-----------------------------------------------------|
| 0b0              | Count events originating from Non-secure StreamIDs. |
| 0b1              | Count events originating from Secure StreamIDs.     |

- This bit is RES0 if the PMCG does not implement support for Secure state. Otherwise, this bit is effectively 0 if support for Secure state is implemented but Secure observation is disabled (SMMU\_PMCG\_SCR.SO == 0).
- For event types that can be filtered on StreamID, this bit is considered in conjunction with FILTER\_SID\_SPAN and SMMU\_PMCG\_SMRn.STREAMID to determine how filtering is applied, based on StreamID and SEC\_SID. See section 10.4 StreamIDs and filtering .

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FILTER\_SID\_SPAN, bit [29]

## When n == 0 or SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0:

Filter StreamID.

| FILTER_SID_SPAN   | Meaning                                                                                                          |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| 0b0               | SMMU_PMCG_SMRn.STREAMID filters event on an exact StreamID match, if the event type can be filtered on StreamID. |
| 0b1               | The SMMU_PMCG_SMRn.STREAMID field encodes a match span of StreamID values. See 10.4 StreamIDs and filtering .    |

Note: The span can encode ALL, equivalent to disabling filtering on StreamID.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FILTER\_REALM\_SID, bit [28]

<!-- formula-not-decoded -->

Count events relating to Realm StreamIDs.

| FILTER_REALM_SID   | Meaning                                          |
|--------------------|--------------------------------------------------|
| 0b0                | Do not count events relating to Realm StreamIDs. |
| 0b1                | Count events relating to Realm StreamIDs.        |

If SMMU\_PMCG\_ROOTCR.RLO is 0, this bit is treated as 0 for all purposes other than read back of the bit value.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [27:20]

Reserved, RES0.

## FILTER\_MPAM\_SP, bits [19:18]

## When SMMU\_PMCG\_CFGR.FILTER\_PARTID\_PMG == 1 and (n == 0 or SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0):

Select MPAM\_SP for SMMU\_PMCG\_SMRn.{PARTID, PMG}.

SMMU\_PMCG\_SMRn.{PARTID, PMG} are treated as belonging to the following PARTID spaces:

| FILTER_MPAM_SP   | Meaning                                                             |
|------------------|---------------------------------------------------------------------|
| 0b00             | If SMMU_PMCG_SCR.SO is 1 then Secure. Otherwise treated as 0b01.    |
| 0b01             | Non-secure.                                                         |
| 0b10             | Reserved, behaves as 0b00.                                          |
| 0b11             | If SMMU_PMCG_ROOTCR.RLO is 1 then Realm. Otherwise treated as 0b01. |

If SMMU\_PMCG\_ROOTCR.ROOTCR\_IMPL = 0 then bit [19] is RES0, and bit [18] selects only between Non-secure and Secure PARTID space.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FILTER\_PMG, bit [17]

## When SMMU\_PMCG\_CFGR.FILTER\_PARTID\_PMG == 1 and (n == 0 or SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0):

Filter events by the value specified in SMMU\_PMCG\_SMRn.PMG.

| FILTER_PMG   | Meaning                                                                    |
|--------------|----------------------------------------------------------------------------|
| 0b0          | Events are not filtered by PMG.                                            |
| 0b1          | Only count events associated with the PMG specified in SMMU_PMCG_SMRn.PMG. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FILTER\_PARTID, bit [16]

## When SMMU\_PMCG\_CFGR.FILTER\_PARTID\_PMG == 1 and (n == 0 or SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0):

Filter events by the value specified in SMMU\_PMCG\_SMRn.PARTID.

| FILTER_PARTID   | Meaning                                                                          |
|-----------------|----------------------------------------------------------------------------------|
| 0b0             | Events are not filtered by PARTID.                                               |
| 0b1             | Only count events associated with the PARTID specified in SMMU_PMCG_SMRn.PARTID. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVENT, bits [15:0]

Event.

- Event type that causes this counter to increment.
- An IMPLEMENTATION DEFINED number of low-order bits of this register are implemented, unimplemented upper bits are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

When SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0, the field FILTER\_SID\_SPAN and, if Secure state is supported, FILTER\_SEC\_SID, are present in every implemented SMMU\_PMCG\_EVTYPERn register and correspond to counter SMMU\_PMCG\_EVCNTRn for all implemented values of n.

When SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 1, these fields are present only in SMMU\_PMCG\_EVTYPER0 and the FILTER\_SID\_SPAN and FILTER\_SEC\_SID fields in SMMU\_PMCG\_EVTYPERx, for x &gt;= 1, are RES0.

The same relationship with SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE applies to FILTER\_PARTID, FILTER\_PMG and FILTER\_MPAM\_NS.

See SMMU\_PMCG\_SMRn and 10.4 StreamIDs and filtering for information on StreamID filtering. When filtering is enabled, an event is counted only if it matches the filter conditions for the counter.

Note: Event types that cannot be filtered on StreamID are always counted, as they cannot be filtered out using FILTER\_* configuration.

If FILTER\_PARTID == 1 or FILTER\_PMG == 1, FILTER\_SID\_SPAN is IGNORED and events are not filtered by StreamID.

If FILTER\_PARTID == 0 and FILTER\_PMG == 0, FILTER\_MPAM\_NS is IGNORED.

See SMMU\_PMCG\_SMRn and 10.4.3 PARTID- and PMG-based filtering for information on PARTIDand PMG-based filtering. When filtering is enabled, an event is counted only if it matches the filter conditions for the counter.

Note: Event types that cannot be filtered on PARTID and PMG are always counted, as they cannot be filtered out using FILTER\_* configuration.

Registers corresponding to unimplemented counters are RES0.

## Accessing SMMU\_PMCG\_EVTYPER&lt;n&gt;

Accesses to this register use the following encodings:

Accessible at offset 0x400 + (4 * n) from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.3 SMMU\_PMCG\_SVR&lt;n&gt;, n = 0 - 63

The SMMU\_PMCG\_SVR&lt;n&gt; characteristics are:

## Purpose

PMCG Shadow value, 0 &lt;= n &lt; 64.

## Configuration

When counter size is &lt;= 32 bits (SMMU\_PMCG\_CFGR.SIZE &lt;= 31), these registers are 32 bits in size. Otherwise, these registers are 64 bits in size. Present in an array of registers (all of size 32 or 64) each corresponding to counter n.

When counter value capture is implemented (SMMU\_PMCG\_CFGR.CAPTURE == 1), these registers hold the captured counter values of the corresponding entries in SMMU\_PMCG\_EVCNTRn. Registers corresponding to unimplemented counters are RES0.

If counter value capture is not implemented (SMMU\_PMCG\_CFGR.CAPTURE == 0), all SMMU\_PMCG\_SVRn registers are RES0.

This register is present only when SMMU\_PMCG\_CFGR.CAPTURE == 1. Otherwise, direct accesses to SMMU\_PMCG\_SVR&lt;n&gt; are RES0.

## Attributes

SMMU\_PMCG\_SVR&lt;n&gt; is a:

- 32-bit register when UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &lt;= 31.
- 64-bit register when UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &gt; 31.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

When UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &lt;= 31:

|                      | 0   |
|----------------------|-----|
| SHADOW_COUNTER_VALUE |     |

## SHADOW\_COUNTER\_VALUE, bits [31:0]

Shadow counter value[N:0].

R == SMMU\_PMCG\_CFGR.SIZE + 1.

If R &lt; 32, bits [31:R-1] are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## When UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &gt; 31:

```
SHADOW_COUNTER_VALUE 63 32 SHADOW_COUNTER_VALUE 31 0
```

## SHADOW\_COUNTER\_VALUE, bits [63:0]

Shadow counter value[N:0].

R == SMMU\_PMCG\_CFGR.SIZE + 1.

If R &gt; 32 and R &lt; 64, bits [63:R-1] are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_PMCG\_SVR&lt;n&gt;

Accesses to this register use the following encodings:

## When UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &lt;= 31

Accessible at offset 0x600 + (4 * n) from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When UInt(SMMUv3\_PMCG.SMMU\_PMCG\_CFGR.SIZE) &gt; 31

Accessible at offset 0x600 + (8 * n) from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.4 SMMU\_PMCG\_SMR&lt;n&gt;, n = 0 - 63

The SMMU\_PMCG\_SMR&lt;n&gt; characteristics are:

## Purpose

PMCG Counter stream match filter, 0 &lt;= n &lt; 64.

## Configuration

This register is present only when n == 0 or SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0. Otherwise, direct accesses to SMMU\_PMCG\_SMR&lt;n&gt; are RES0.

## Attributes

SMMU\_PMCG\_SMR&lt;n&gt; is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

## When SMMUv3\_PMCG.SMMU\_PMCG\_EVTYPER&lt;n&gt;.FILTER\_PARTID == 1 or SM-MUv3\_PMCG.SMMU\_PMCG\_EVTYPER&lt;n&gt;.FILTER\_PMG == 1:

<!-- image -->

| 31   | 24 23   | 16 15   | 0      |
|------|---------|---------|--------|
| RES0 | PMG     |         | PARTID |

Filtering by MPAM PARTID and/or PMG values occurs.

Filtering by StreamID does not occur.

See section 10.4.3 PARTID- and PMG-based filtering .

## Bits [31:24]

Reserved, RES0.

## PMG, bits [23:16]

PMG value by which PMCG filters events.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## PARTID, bits [15:0]

PARTID value by which PMCG filters events.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

<!-- image -->

## STREAMID, bits [31:0]

- When the corresponding SMMU\_PMCG\_EVTYPERn.EVENT indicates an event that cannot be filtered on StreamID, the value in this field is IGNORED.
- Otherwise:

- -When the corresponding SMMU\_PMCG\_EVTYPERn.FILTER\_SID\_SPAN == 0, the respective counter only counts events associated with a StreamID matching this field exactly.
- -When FILTER\_SID\_SPAN == 1, this field encodes a mask value that allows a span of least-significant StreamID bits to be ignored for the purposes of filtering on a StreamID match. When all implemented bits of this field are written to 1, any StreamID is matched. See section 10.4 StreamIDs and filtering .
- -When Secure observation is enabled, SMMU\_PMCG\_EVTYPERn.FILTER\_SEC\_SID determines whether the StreamID is matched from Secure or Non-secure StreamID spaces, see section 10.4 StreamIDs and filtering for the behavior of the match-all encodings with respect to Secure/Non-secure namespaces.
- This field implements an IMPLEMENTATION DEFINED number of contiguous bits (from 0 upwards) corresponding to the PMCG StreamID size, see section 10.4.1 Counter Group StreamID size . Bits outside this range read as zero, writes ignored (RAZ/WI).

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information for Otherwise

These registers contain StreamID-match configuration for filtering events on StreamID.

When SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0, each SMMU\_PMCG\_SMRn corresponds to counter SMMU\_PMCG\_EVCNTRn for all implemented values of n.

When SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 1, SMMU\_PMCG\_SMR0 applies to all counters in the group and registers SMMU\_PMCG\_SMRx for x &gt;= 1 are RES0.

See section 10.4 StreamIDs and filtering for more information on StreamIDs in PMCGs.

Note: To count events for a given StreamID, software must choose a counter in the appropriate counter group to use for the required event type (which is determined in an IMPLEMENTATION DEFINED manner) and then write the full StreamID value into the STREAMID field of this register.

Registers corresponding to unimplemented counters are RES0.

## Accessing SMMU\_PMCG\_SMR&lt;n&gt;

Accesses to this register use the following encodings:

Accessible at offset 0xA00 + (4 * n) from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.5 SMMU\_PMCG\_CNTENSET0

The SMMU\_PMCG\_CNTENSET0 characteristics are:

## Purpose

Counter enable, SET.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_CNTENSET0 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 63    | 32    |       |
|-------|-------|-------|
| CNTEN | CNTEN | CNTEN |
| 31    | 0     |       |
| CNTEN | CNTEN | CNTEN |

## CNTEN, bits [63:0]

Counter enable.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

Access to this field is W1S.

## Additional Information

64-bit register containing a bitmap of per-counter enables. Bit CNTEN[n] corresponds to counter n, which is enabled if CNTEN[n] == 1 and SMMU\_PMCG\_CR.E == 1.

Write 1 to a bit location to set the per-counter enable. Reads return the state of enables. High-order bits of the bitmap beyond the number of implemented counters are RES0.

## Accessing SMMU\_PMCG\_CNTENSET0

Accesses to this register use the following encodings:

Accessible at offset 0xC00 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.6 SMMU\_PMCG\_CNTENCLR0

The SMMU\_PMCG\_CNTENCLR0 characteristics are:

## Purpose

Counter enable, CLEAR.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_CNTENCLR0 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 63    | 32    |       |
|-------|-------|-------|
| CNTEN | CNTEN | CNTEN |
| 31    | 0     |       |
| CNTEN | CNTEN | CNTEN |

## CNTEN, bits [63:0]

Counter enable.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

Access to this field is W1C.

## Additional Information

Bitmap indexed similar to SMMU\_PMCG\_CNTENSET0.

Write 1 to a bit location to clear the per-counter enable. Reads return the state of enables. High-order bits of the bitmap beyond the number of implemented counters are RES0.

## Accessing SMMU\_PMCG\_CNTENCLR0

Accesses to this register use the following encodings:

Accessible at offset 0xC20 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.7 SMMU\_PMCG\_INTENSET0

The SMMU\_PMCG\_INTENSET0 characteristics are:

## Purpose

Counter interrupt contribution enable, SET.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_INTENSET0 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 63    | 32    |       |
|-------|-------|-------|
| INTEN | INTEN | INTEN |
| 31    | 0     |       |
| INTEN | INTEN | INTEN |

## INTEN, bits [63:0]

Per counter interrupt enable.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

Access to this field is W1S.

## Additional Information

Bitmap indexed similar to SMMU\_PMCG\_CNTENSET0.

Write 1 to a bit location to set the per-counter interrupt enable. Reads return the state of interrupt enables. High-order bits of the bitmap beyond the number of implemented counters are RES0.

Overflow of counter n triggers a PMCG interrupt if, at the time that the overflow occurs, the corresponding INTEN[n] == 1 &amp;&amp; SMMU\_PMCG\_IRQ\_CTRL.IRQEN == 1.

## Accessing SMMU\_PMCG\_INTENSET0

Accesses to this register use the following encodings:

Accessible at offset 0xC40 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.8 SMMU\_PMCG\_INTENCLR0

The SMMU\_PMCG\_INTENCLR0 characteristics are:

## Purpose

Counter interrupt contribution enable CLEAR.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_INTENCLR0 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 63    | 32    |       |
|-------|-------|-------|
| INTEN | INTEN | INTEN |
| 31    | 0     |       |
| INTEN | INTEN | INTEN |

## INTEN, bits [63:0]

Per counter interrupt enable.

Bitmap indexed similar to SMMU\_PMCG\_CNTENSET0.

Write 1 to a bit location to clear the per-counter interrupt enable. Reads return the state of interrupt enables. High-order bits of the bitmap beyond the number of implemented counters are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

Access to this field is W1C.

## Accessing SMMU\_PMCG\_INTENCLR0

Accesses to this register use the following encodings:

Accessible at offset 0xC60 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.9 SMMU\_PMCG\_OVSCLR0

The SMMU\_PMCG\_OVSCLR0 characteristics are:

## Purpose

Overflow status, CLEAR.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_OVSCLR0 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 63   | 32   |     |
|------|------|-----|
| OVS  | OVS  | OVS |
| 31   | 0    |     |
| OVS  | OVS  | OVS |

## OVS, bits [63:0]

Overflow counter status.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

Access to this field is W1C.

## Additional Information

Bitmap indexed similar to SMMU\_PMCG\_CNTENSET0.

Write 1 to a bit location to clear the per-counter overflow status. Reads return the state of overflow status. High-order bits of the bitmap beyond the number of implemented counters are RES0.

Overflow of counter n (a transition past the maximum unsigned value of the counter causing the value to become, or pass, zero) sets the corresponding OVS[n] bit. In addition, this event can trigger the PMCG interrupt and cause a capture of the PMCG counter values (see SMMU\_PMCG\_EVTYPERn.

## Accessing SMMU\_PMCG\_OVSCLR0

Accesses to this register use the following encodings:

Accessible at offset 0xC80 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.10 SMMU\_PMCG\_OVSSET0

The SMMU\_PMCG\_OVSSET0 characteristics are:

## Purpose

Overflow status, SET.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_OVSSET0 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 63   | 32   |     |
|------|------|-----|
| OVS  | OVS  | OVS |
| 31   | 0    |     |
| OVS  | OVS  | OVS |

## OVS, bits [63:0]

Overflow counter status.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

Access to this field is W1S.

## Additional Information

Bitmap indexed similar to SMMU\_PMCG\_CNTENSET0.

Write 1 to a bit location to set the per-counter overflow status. Reads return the state of overflow status. High-order bits of the bitmap beyond the number of implemented counters are RES0.

Software setting an OVS bit is similar to an OVS bit becoming set because of a counter overflow, except it is IMPLEMENTATION SPECIFIC whether enabled overflow side effects of triggering the PMCG interrupt or causing a capture of the PMCG counter values are performed.

## Accessing SMMU\_PMCG\_OVSSET0

Accesses to this register use the following encodings:

Accessible at offset 0xCC0 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.11 SMMU\_PMCG\_CAPR

The SMMU\_PMCG\_CAPR characteristics are:

## Purpose

Counter shadow value capture.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_CAPR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## CAPTURE, bit [0]

## Capture.

- When counter capture is supported (SMMU\_PMCG\_CFGR.CAPTURE == 1), a write of 1 to this bit triggers a capture of all SMMU\_PMCG\_EVCNTRn values within the PMCG into their respective SMMU\_PMCG\_SVRn shadow register.
- This register reads as zero.
- When SMMU\_PMCG\_CFGR.CAPTURE == 0, this field is RES0.

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_PMCG\_CAPR

Accesses to this register use the following encodings:

Accessible at offset 0xD88 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are WO.

## 10.5.2.12 SMMU\_PMCG\_SCR

The SMMU\_PMCG\_SCR characteristics are:

## Purpose

PMCG Secure control register.

## Configuration

This register is present only when the PMCG supports Secure state. Otherwise, direct accesses to SMMU\_PMCG\_SCR are RES0.

## Attributes

SMMU\_PMCG\_SCR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## READS\_AS\_ONE, bit [31]

| READS_AS_ONE   | Meaning                                                                                |
|----------------|----------------------------------------------------------------------------------------|
| 0b1            | Secure software can use READS_AS_ONE to discover support for Secure state in the PMCG. |

Access to this field is RO.

## Bits [30:5]

Reserved, RES0.

## NAO, bit [4]

## When SMMU\_PMCG\_ROOTCR.ROOTCR\_IMPL == 1:

Permit counting of events not attributable to a specific Security state.

| NAO   | Meaning                                                        |
|-------|----------------------------------------------------------------|
| 0b0   | Counting non-attributable events is prevented.                 |
| 0b1   | Counting non-attributable events is not prevented by this bit. |

## See also:

- 10.4.4 Counting of non-attributable events .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_MPAM\_NS, bit [3]

## When SMMU\_PMCG\_S\_MPAMIDR.HAS\_MPAM\_NS == 1:

| MSI_MPAM_NS   | Meaning                                                        |
|---------------|----------------------------------------------------------------|
| 0b0           | PMCG MSIs that target a Secure PA use Secure PARTID space.     |
| 0b1           | PMCG MSIs that target a Secure PA use Non-secure PARTID space. |

This bit is RES0 if SMMU\_PMCG\_SCR.{NSMSI, NSRA} are configured for Non-secure MSIs.

See section 17.5 Assignment of PARTID and PMG for PMCG-originated MSIs .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## NSMSI, bit [2]

## When SMMU\_PMCG\_CFGR.MSI == 1:

Non-secure MSIs.

| NSMSI   | Meaning                                    |
|---------|--------------------------------------------|
| 0b0     | Generated MSIs target Secure PA space.     |
| 0b1     | Generated MSIs target Non-secure PA space. |

The reset behavior of this field is:

- This field resets to '1' .

## Otherwise:

Reserved, RES0.

## NSRA, bit [1]

Non-secure register access.

| NSRA   | Meaning                                                                                                        |
|--------|----------------------------------------------------------------------------------------------------------------|
| 0b0    | Non-secure Register Access is disabled. • Non-secure access to any PMCG register is RAZ/WI.                    |
| 0b1    | Non-secure Register Access is enabled. • If the PMCG supports MSIs, generated MSIs target Non-secure PA space. |

The reset behavior of this field is:

- This field resets to '1' .

## SO, bit [0]

Secure observation

| SO   | Meaning                                                                               |
|------|---------------------------------------------------------------------------------------|
| 0b0  | Secure observation is disabled. • SMMU_PMCG_EVTYPERn.FILTER_SEC_SID is effectively 0. |
| 0b1  | Secure observation is enabled.                                                        |

- See 10.6 Support for Secure state .

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

If the PMCG does not implement support for Secure state, this register is RAZ/WI.

If the PMCG does not implement Secure state but the system does, both Secure and Non-secure accesses are permitted to PMCG registers. In this case, any MSIs generated from the PMCG must be issued to the Non-secure PA space.

Note: If software transitions control of a PMCG between Security states, Arm recommends following this procedure:

- Set NSRA == 0 and NSMSI == 1.
- -Non-secure register access is disabled, but any active MSI configuration remains Non-secure.
- Clear SMMU\_PMCG\_IRQ\_CTRL.IRQEN and wait for Update of SMMU\_PMCG\_IRQ\_CTRLACK.
- -Outstanding Non-secure MSIs are complete.
- Set NSMSI == 0 and reprogram MSI registers as required.

## Accessing SMMU\_PMCG\_SCR

If SMMU\_PMCG\_ROOTCR.ROOTCR\_IMPL == 1, there is an alias of this register at offset 0xE40 .

Accesses to this register use the following encodings:

Accessible at offset 0xDF8 from SMMUv3\_PMCG

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

Accessible at offset 0xE40 from SMMUv3\_PMCG

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.13 SMMU\_PMCG\_CFGR

The SMMU\_PMCG\_CFGR characteristics are:

## Purpose

PMCG Configuration identification register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_CFGR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## Bits [31:26]

Reserved, RES0.

## FILTER\_PARTID\_PMG, bit [25]

This bit is Reserved, RES0 prior to SMMUv3.3.

| FILTER_PARTID_PMG   | Meaning                                           |
|---------------------|---------------------------------------------------|
| 0b0                 | This PMCG cannot filter events by PARTID nor PMG. |
| 0b1                 | This PMCG can filter events by PARTID and PMG.    |

See section 10.4 StreamIDs and filtering .

## MPAM, bit [24]

## When SMMU\_PMCG\_CFGR.MSI == 1:

Memory Partitioning And Monitoring (MPAM) support.

| MPAM   | Meaning                            |
|--------|------------------------------------|
| 0b0    | MPAM is not supported by the PMCG. |
| 0b1    | MPAM is supported by the PMCG.     |

- MPAM support is optional.
- If the system supports MPAM but the PMCG does not, the PARTID and PMG values for PMCG-originated MSIs are zero.

- This bit is Reserved, RES0 prior to SMMUv3.2.
- Note: This field indicates that the PMCG supports issuing MSIs with PARTID and PMG information. Support for filtering of events by PARTID and PMG values is indicated in FILTER\_PARTID\_PMG.

## Otherwise:

Reserved, RES0.

## SID\_FILTER\_TYPE, bit [23]

StreamID filter type.

| SID_FILTER_TYPE   | Meaning                                                                                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | Separate StreamID or MPAM filtering is supported for each counter in the PMCG.                                                                                                                    |
| 0b1               | The StreamID or MPAM filter configured by SMMU_PMCG_SMR0 and SMMU_PMCG_EVTYPERn.{FILTER_SID_SPAN, FILTER_SEC_SID, FILTER_PARTID, FILTER_PMG, FILTER_MPAM_NS} applies to all counters in the PMCG. |

## CAPTURE, bit [22]

## Capture.

| CAPTURE   | Meaning                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------|
| 0b0       | Capture of counter values into SVRn registers not supported. • SMMU_PMCG_SVRn and SMMU_PMCG_CAPR are RES0. |
| 0b1       | Capture of counter values supported.                                                                       |

## MSI, bit [21]

Counter group supports Message Signalled Interrupt.

| MSI   | Meaning                     |
|-------|-----------------------------|
| 0b0   | Group does not support MSI. |
| 0b1   | Group can send MSI.         |

## RELOC\_CTRS, bit [20]

Relocation controls.

- When 1, Page 1 is present and the following registers are relocated to the equivalent offset on Page 1 (their Page 0 locations become RES0):
- -SMMU\_PMCG\_EVCNTRn.
- -SMMU\_PMCG\_SVRn.
- -SMMU\_PMCG\_OVSCLR0.
- -SMMU\_PMCG\_OVSSET0.
- -SMMU\_PMCG\_CAPR.

## Bits [19:14]

Reserved, RES0.

## SIZE, bits [13:8]

## Size

- Size of PMCG counters in bits, minus one. Valid values are:
- Other values are Reserved.

| SIZE     | Meaning               |
|----------|-----------------------|
| 0b011111 | 31 (32-bit counters). |
| 0b100011 | 35 (36-bit counters). |
| 0b100111 | 39 (40-bit counters). |
| 0b101011 | 43 (44-bit counters). |
| 0b101111 | 47 (48-bit counters). |
| 0b111111 | 63 (64-bit counters). |

## Bits [7:6]

Reserved, RES0.

## NCTR, bits [5:0]

N counters.

- The number of counters available in the group is given by NCTR+1.

## Additional Information

The capability of each counter group to send MSIs is specific to the group and is not affected by the core SMMUMSI capability (SMMU\_IDR0.MSI).

## Accessing SMMU\_PMCG\_CFGR

Accesses to this register use the following encodings:

Accessible at offset 0xE00 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

31

## 10.5.2.14 SMMU\_PMCG\_CR

The SMMU\_PMCG\_CR characteristics are:

## Purpose

PMCG Control Register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_CR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

## Bits [31:1]

Reserved, RES0.

## E, bit [0]

Global counter enable.

- Global counter enable, where 1 == Enabled. When 0, no events are counted and values in SMMU\_PMCG\_EVCNTRn registers do not change. This bit takes precedence over the CNTEN bits set through SMMU\_PMCG\_CNTENSET0.

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_PMCG\_CR

Accesses to this register use the following encodings:

Accessible at offset 0xE04 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

RES0

1

0

E

## 10.5.2.15 SMMU\_PMCG\_IIDR

The SMMU\_PMCG\_IIDR characteristics are:

## Purpose

SMMUPMCGImplementation Identification Register

## Configuration

Implementation of this register is OPTIONAL.

## Attributes

SMMU\_PMCG\_IIDR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

| 31        | 20 19   | 16 15    | 12 11       |
|-----------|---------|----------|-------------|
| ProductID | Variant | Revision | Implementer |

## ProductID, bits [31:20]

Identifies the PMCG part.

Matches the {SMMU\_PMCG\_PIDR1.PART\_1, SMMU\_PMCG\_PIDR0.PART\_0} fields, if SMMU\_PMCG\_PIDR0 and SMMU\_PMCG\_PIDR1 are present.

This field reads as an IMPLEMENTATION DEFINED value.

## Variant, bits [19:16]

Distinguishes product variants, or major revisions of the product.

Matches the SMMU\_PMCG\_PIDR2.REVISION field, if SMMU\_PMCG\_PIDR2 is present.

This field reads as an IMPLEMENTATION DEFINED value.

## Revision, bits [15:12]

Distinguishes minor revisions of the product.

Matches the SMMU\_PMCG\_PIDR3.REVAND field, if SMMU\_PMCG\_PIDR3 is present.

This field reads as an IMPLEMENTATION DEFINED value.

## Implementer, bits [11:0]

SMMU\_PMCG\_IIDR[11:8] contain the JEP106 continuation code for the implementer.

SMMU\_PMCG\_IIDR[7] is zero.

SMMU\_PMCG\_IIDR[6:0] contain the JEP106 identification code for the implementer.

SMMU\_PMCG\_IIDR[11:8] match SMMU\_PMCG\_PIDR4.DES\_2 and SMMU\_PMCG\_IIDR[6:0] match the {SMMU\_PMCG\_PIDR2.DES\_1, SMMU\_PMCG\_PIDR1.DES\_0} fields, if SMMU\_PMCG\_PIDR{1, 2, 4} are present.

This field reads as an IMPLEMENTATION DEFINED value.

## Additional Information

Note: Zero is not a valid JEP106 identification code. A value of zero for SMMU\_PMCG\_IIDR indicates this register is not implemented.

Note: For an Arm implementation, bits[11:0] are 0x43B.

## Accessing SMMU\_PMCG\_IIDR

Accesses to this register use the following encodings:

Accessible at offset 0xE08 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.16 SMMU\_PMCG\_CEID0

The SMMU\_PMCG\_CEID0 characteristics are:

## Purpose

Common Event ID bitmap, lower.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_CEID0 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## N, bits [63:0]

Event N.

Lower half of 128-bit bitmap comprised of two consecutive 64-bit registers.

In this register, bit (N &amp; 63) relates to event number N, for 0 &lt;= N &lt; 64.

## For each bit:

- 0b0 : Event N cannot be counted by counters in this group.
- 0b1 : Event N can be counted by counters in this group.

See section 10.3 Monitor events for event numbers.

## Accessing SMMU\_PMCG\_CEID0

Accesses to this register use the following encodings:

Accessible at offset 0xE20 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.17 SMMU\_PMCG\_CEID1

The SMMU\_PMCG\_CEID1 characteristics are:

## Purpose

Common Event ID bitmap, Upper.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_CEID1 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 63   | 32   |
|------|------|
| N    |      |
| 31   | 0    |
| N    |      |

## N, bits [63:0]

Event N.

Upper half of 128-bit bitmap comprised of two consecutive 64-bit registers.

In this register, bit (N &amp; 63) relates to event number N, for 64 &lt;= N &lt; 128.

## For each bit

- 0b0 : Event N cannot be counted by counters in this group.
- 0b1 : Event N can be counted by counters in this group.

See section 10.3 Monitor events for event numbers.

## Accessing SMMU\_PMCG\_CEID1

Accesses to this register use the following encodings:

Accessible at offset 0xE28 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.18 SMMU\_PMCG\_ROOTCR

The SMMU\_PMCG\_ROOTCR characteristics are:

## Purpose

PMCG Root Control Register.

## Configuration

This register is present only when SMMU\_PMCG\_ROOTCR.ROOTCR\_IMPL == 1. Otherwise, direct accesses to SMMU\_PMCG\_ROOTCR are RES0.

## Attributes

SMMU\_PMCG\_ROOTCR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 31 30       | 4 3 2 1     |
|-------------|-------------|
| 1           | NAO RLO RTO |
| ROOTCR_IMPL | RES0        |

## ROOTCR\_IMPL, bit [31]

Presence of SMMU\_PMCG\_ROOTCR

| ROOTCR_IMPL   | Meaning                          |
|---------------|----------------------------------|
| 0b1           | SMMU_PMCG_ROOTCR is implemented. |

Access to this field is RO.

## Bits [30:4]

Reserved, RES0.

## NAO, bit [3]

Permit counting of events not attributable to a specific Security state.

| NAO   | Meaning                                                           |
|-------|-------------------------------------------------------------------|
| 0b0   | Counting of non-attributable events is prevented.                 |
| 0b1   | Counting of non-attributable events is not prevented by this bit. |

Note: This bit has the opposite reset polarity to SMMU\_PMCG\_SCR.NAO. The ability to count non-attributable events is therefore controlled by Secure software by default. If this is unacceptable for the security model of a system, then Root firmware must clear this bit as part of system initialization.

See also:

- 10.4.4 Counting of non-attributable events .

The reset behavior of this field is:

- This field resets to '1' .

## Bit [2]

Reserved, RES0.

## RLO, bit [1]

Permit counting of events relating to Realm StreamIDs.

| RLO   | Meaning                                                          |
|-------|------------------------------------------------------------------|
| 0b0   | Counting of events relating to Realm StreamIDs is not permitted. |
| 0b1   | Counting of events relating to Realm StreamIDs is permitted.     |

## See also:

- SMMU\_PMCG\_EVTYPERn.FILTER\_REALM\_SID.

The reset behavior of this field is:

- This field resets to '0' .

## RTO, bit [0]

Permit counting of events relating to Root state.

| RTO   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | Counting of events relating to Root state is not permitted. |
| 0b1   | Counting of events relating to Root state is permitted.     |

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_PMCG\_ROOTCR

Accesses to this register use the following encodings:

Accessible at offset 0xE48 from SMMUv3\_PMCG

- When an access is Root, accesses to this register are RW.
- Otherwise, accesses to this register are RO.

## 10.5.2.19 SMMU\_PMCG\_IRQ\_CTRL

The SMMU\_PMCG\_IRQ\_CTRL characteristics are:

## Purpose

PMCG IRQ enable and control register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_IRQ\_CTRL is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## IRQEN, bit [0]

IRQ enable

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

Each field in this register has a corresponding field in SMMU\_PMCG\_IRQ\_CTRLACK, with the same Update semantic as fields in SMMU\_CR0 versus SMMU\_CR0ACK.

This register contains the main IRQ enable flag for a per-counter group interrupt source. This enable allows or inhibits both edge-triggered wired outputs (if implemented) and MSI writes (if supported by the counter group). When IRQEN == 0, no interrupt is triggered regardless of individual per-counter overflow INTEN flags (that is, they are overridden). IRQEN also controls overall interrupt completion and MSI configuration changes.

When MSIs are supported, as indicated by SMMU\_PMCG\_CFGR.MSI == 1, IRQ enable flags Guard the MSI address and data payload registers, which must only be changed when their respective enable flag is 0. See SMMU\_PMCG\_IRQ\_CFG0 for details.

Completion of Update to IRQ enables guarantees the following side effects:

- Completion of an Update of IRQEN from 0 to 1 guarantees that the MSI configuration in SMMU\_PMCG\_IRQ\_CFG{0,1,2} will be used for all future MSIs generated from the counter group.
- An Update of IRQEN from 1 to 0 completes when all prior MSIs have become visible to their Shareability domain (have completed). Completion of this Update guarantees that no new MSI writes or wired edge events will later become visible from this source.

An IRQ is triggered from the PMCG if all of the following occur:

- SMMU\_PMCG\_IRQ\_CTRL.IRQEN == 1.

- A counter overflows and sets an OVS bit, whose corresponding INTEN bit was set through SMMU\_PMCG\_INTENSET0.

## Accessing SMMU\_PMCG\_IRQ\_CTRL

Accesses to this register use the following encodings:

Accessible at offset 0xE50 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 10.5.2.20 SMMU\_PMCG\_IRQ\_CTRLACK

The SMMU\_PMCG\_IRQ\_CTRLACK characteristics are:

## Purpose

Provides acknowledgment of changes to PMCG IRQ enable and control register, SMMU\_PMCG\_IRQ\_CTRL.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_IRQ\_CTRLACK is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## IRQEN, bit [0]

IRQ enable.

Acknowledge bit for SMMU\_PMCG\_IRQ\_CTRL.IRQEN.

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

Undefined bits read as zero. Fields in this register are RES0 if their corresponding SMMU\_PMCG\_IRQ\_CTRL field is Reserved.

## Accessing SMMU\_PMCG\_IRQ\_CTRLACK

Accesses to this register use the following encodings:

Accessible at offset 0xE54 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.21 SMMU\_PMCG\_IRQ\_CFG0

The SMMU\_PMCG\_IRQ\_CFG0 characteristics are:

## Purpose

PMCG MSI configuration register.

## Configuration

This register is present only when SMMU\_PMCG\_CFGR.MSI == 1. Otherwise, direct accesses to SMMU\_PMCG\_IRQ\_CFG0 are RES0.

## Attributes

SMMU\_PMCG\_IRQ\_CFG0 is a 64-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## ADDR, bits [55:2]

Physical address of MSI target, bits [55:2].

- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.

Note: An implementation is not required to store these bits.

- Bits [1:0] of the effective address that results from this field are zero.

If ADDR == 0, no MSI is sent. This allows a wired IRQ, if implemented, to be used instead of an MSI.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [1:0]

Reserved, RES0.

## Additional Information

When an implementation does not support MSIs, all fields are RES0.

See SMMU\_PMCG\_SCR.NSMSI for control of the target PA space of the MSI.

## Accessing SMMU\_PMCG\_IRQ\_CFG0

SMMU\_PMCG\_IRQ\_CFG0 is Guarded by SMMU\_PMCG\_IRQ\_CTRL.IRQEN and must only be modified when IRQEN == 0. SMMU\_PMCG\_IRQ\_CFG{0,1,2} have the same behaviors as SMMU\_*\_IRQ\_CFG{0,1,2} with respect to their enables, including the permitted behaviors of writes when IRQEN == 1.

Accesses to this register use the following encodings:

Accessible at offset 0xE58 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- When SMMUv3\_PMCG.SMMU\_PMCG\_IRQ\_CTRL.IRQEN == 1 or SMMUv3\_PMCG.SMMU\_PMCG\_IRQ\_CTRLACK.IRQEN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## 10.5.2.22 SMMU\_PMCG\_IRQ\_CFG1

The SMMU\_PMCG\_IRQ\_CFG1 characteristics are:

## Purpose

PMCG MSI configuration register.

## Configuration

This register is present only when SMMU\_PMCG\_CFGR.MSI == 1. Otherwise, direct accesses to SMMU\_PMCG\_IRQ\_CFG1 are RES0.

## Attributes

SMMU\_PMCG\_IRQ\_CFG1 is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

DATA

31

0

When an implementation does not support MSIs, all fields are RES0.

## DATA, bits [31:0]

MSI data payload.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_PMCG\_IRQ\_CFG1

SMMU\_PMCG\_IRQ\_CFG1 is Guarded by SMMU\_PMCG\_IRQ\_CTRL.IRQEN and must only be modified when IRQEN == 0.

Accesses to this register use the following encodings:

Accessible at offset 0xE60 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- When SMMUv3\_PMCG.SMMU\_PMCG\_IRQ\_CTRL.IRQEN == 1 or SMMUv3\_PMCG.SMMU\_PMCG\_IRQ\_CTRLACK.IRQEN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## 10.5.2.23 SMMU\_PMCG\_IRQ\_CFG2

The SMMU\_PMCG\_IRQ\_CFG2 characteristics are:

## Purpose

PMCG MSI configuration register.

## Configuration

This register is present only when SMMU\_PMCG\_CFGR.MSI == 1. Otherwise, direct accesses to SMMU\_PMCG\_IRQ\_CFG2 are RES0.

## Attributes

SMMU\_PMCG\_IRQ\_CFG2 is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

| 31   | 6 5 4 3   | 0       |
|------|-----------|---------|
| RES0 | SH        | MEMATTR |

## Bits [31:6]

Reserved, RES0.

## SH, bits [5:4]

Shareability.

| SH   | Meaning                     |
|------|-----------------------------|
| 0b00 | Non-shareable.              |
| 0b01 | Reserved, behaves as 0b00 . |
| 0b10 | Outer Shareable.            |
| 0b11 | Inner Shareable.            |

- When MemAttr encodes a Device memory type, the value of this field is IGNORED and the Shareability is effectively Outer Shareable.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## MEMATTR, bits [3:0]

Memory type.

- Encoded the same as the STE.MemAttr field.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

When an implementation does not support MSIs, all fields are RES0.

## Accessing SMMU\_PMCG\_IRQ\_CFG2

SMMU\_PMCG\_IRQ\_CFG2 is Guarded by SMMU\_PMCG\_IRQ\_CTRL.IRQEN and must only be modified when IRQEN == 0.

Accesses to this register use the following encodings:

Accessible at offset 0xE64 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- When SMMUv3\_PMCG.SMMU\_PMCG\_IRQ\_CTRL.IRQEN == 1 or SMMUv3\_PMCG.SMMU\_PMCG\_IRQ\_CTRLACK.IRQEN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## 10.5.2.24 SMMU\_PMCG\_IRQ\_STATUS

The SMMU\_PMCG\_IRQ\_STATUS characteristics are:

## Purpose

PMCG MSI Status register.

## Configuration

This register is present only when SMMU\_PMCG\_CFGR.MSI == 1. Otherwise, direct accesses to SMMU\_PMCG\_IRQ\_STATUS are RES0.

## Attributes

SMMU\_PMCG\_IRQ\_STATUS is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## IRQ\_ABT, bit [0]

MSI abort.

- The SMMU sets this bit to 1 if it detects that an MSI has terminated with an abort.
- This bit is RES0 when SMMU\_PMCG\_CFGR.MSI == 0.
- It is IMPLEMENTATION DEFINED whether an implementation can detect this condition.
- This bit is cleared to 0 when SMMU\_PMCG\_IRQ\_CTRL.IRQEN is Updated from 0 to 1.
- -Note: An IRQEN transition from 1 to 0 does not clear this bit, as this transition also ensures visibility of outstanding MSI writes and clearing IRQ\_ABT at this point might mask possible abort completions of those MSI writes.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_PMCG\_IRQ\_STATUS

In SMMUv3.0, this register location is RES0.

Accesses to this register use the following encodings:

Accessible at offset 0xE68 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.25 SMMU\_PMCG\_GMPAM

The SMMU\_PMCG\_GMPAM characteristics are:

## Purpose

MPAM configuration for PMCG-originated MSI transactions.

## Configuration

This register is present only when SMMU\_PMCG\_CFGR.MPAM == 1. Otherwise, direct accesses to SMMU\_PMCG\_GMPAM are RES0.

## Attributes

SMMU\_PMCG\_GMPAM is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

The configuration of SMMU\_PMCG\_SCR.NSMSI and SMMU\_PMCG\_SCR.NSRA affects whether this register configures Non-secure or Secure PARTID and PMG values, and therefore the maximum supported values for PARTID and PMG.

See section 17.5 Assignment of PARTID and PMG for PMCG-originated MSIs for details.

## Update, bit [31]

Update completion flag.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:24]

Reserved, RES0.

## PO\_PMG, bits [23:16]

PMG of PMCG-orientated MSI transactions.

- This field determines the PMG of PMCG-originated MSI transactions.
- Bits above the combined PMG bit width, as indicated by the greater of SMMU\_PMCG\_MPAMIDR.PMG\_MAX and SMMU\_PMCG\_S\_MPAMIDR.PMG\_MAX, are RES0.
- If a value is programmed that is greater than the corresponding PMG\_MAX limit, an UNKNOWN PMG is used.

The reset behavior of this field is:

- This field resets to 0x00 .

## PO\_PARTID, bits [15:0]

PARTID of PMCG-originated MSI transactions

- This field determines the PARTID of PMCG-originated MSI transactions.

- Bits above the combined PARTID bit width, as indicated by the greater of SMMU\_PMCG\_MPAMIDR.PARTID\_MAX and SMMU\_PMCG\_S\_MPAMIDR.PARTID\_MAX, are RES0.
- If a value is programmed that is greater than the corresponding PARTID\_MAX limit, an UNKNOWN PARTID is used.

The reset behavior of this field is:

- This field resets to 0x0000 .

## Additional Information

The PO\_PMG and PO\_PARTID values determine the MPAM attributes applied to PMCG MSI write transactions.

The Update flag is similar to the SMMU\_(S\_)GMPAM.Update mechanism. It indicates that a change to the register has been accepted and when the Update flag is observed to be zero after a correct update procedure, the new values are guaranteed to be applied to future PMCG-originated accesses.

This register must only be written when Update == 0. A write when an Update == 1, that is when a prior update is underway, is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- Update completes with any value.
- -Note: The effective IDs in use might not match those read back from this register.
- The write is ignored and update completes using the initial value.

If this register is written without simultaneously setting Update to 1, the effect is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The write is ignored.
- The written value is stored and is visible to future reads of the register, but does not affect transactions.
- The written value affects transactions at an UNPREDICTABLE update point:
- -There is no guarantee that all future PMCG-originated accesses after the write will take the new value.

When a write to this register correctly follows the requirements in this section, the new value is observable to future reads of the register even if they occur before the Update has completed.

Note: The Update mechanism provides a way to guarantee that future MSI accesses will use the configured MPAM IDs. It does not synchronize prior or ongoing accesses, which must be completed using existing facilities. For example, prior MSI writes can be completed by updating the corresponding IRQEN to a disabled state.

Note: If a change is made to the Non-secure Register Access, SMMU\_PMCG\_SCR.NSRA, or MSI target PA space configuration, SMMU\_PMCG\_SCR.NSMSI, then the configuration in this register might be invalid in the new configuration.

Note: For example, a Secure PARTID value might not be valid if it is later treated as a Non-secure PARTID value. Or, the existing value might be greater than the corresponding PARTID\_MAX in the new configuration and will be treated as an UNKNOWN value.

Note: When the Security state of the MSI changes, this configuration should be Updated to the required value. Because this scenario might occur when ownership of the MSI configuration changes, a new owner must consider that a previous Update initiated by the previous owner might still be ongoing and must check that this Update has completed before performing a new Update.

## Accessing SMMU\_PMCG\_GMPAM

Accesses to this register use the following encodings:

Accessible at offset 0xE6C from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- When SMMUv3\_PMCG.SMMU\_PMCG\_GMPAM.Update == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## 10.5.2.26 SMMU\_PMCG\_AIDR

The SMMU\_PMCG\_AIDR characteristics are:

## Purpose

This register identifies the SMMU architecture version to which the PMCG implementation conforms.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_PMCG\_AIDR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 31   | 7 4 3 0                   |
|------|---------------------------|
| RES0 | ArchMajorRev ArchMinorRev |

## Bits [31:8]

Reserved, RES0.

ArchMajorRev, bits [7:4]

ArchMinorRev, bits [3:0]

## Additional Information

When considered as {ArchMajorRev, ArchMinorRev}:

- [7:0] == 0x00 == SMMUv3.0 PMCG.
- [7:0] == 0x01 == SMMUv3.1 PMCG.
- [7:0] == 0x02 == SMMUv3.2 PMCG.
- [7:0] == 0x03 == SMMUv3.3 PMCG.
- [7:0] == 0x04 == SMMUv3.4 PMCG.
- All other values Reserved.

## Accessing SMMU\_PMCG\_AIDR

Accesses to this register use the following encodings:

Accessible at offset 0xE70 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.27 SMMU\_PMCG\_MPAMIDR

The SMMU\_PMCG\_MPAMIDR characteristics are:

## Purpose

Per-PMCG Non-secure MPAM capability identification when the PMCG supports MSIs.

## Configuration

This register is present only when SMMU\_PMCG\_CFGR.MPAM == 1 or SMMU\_PMCG\_CFGR.FILTER\_PARTID\_PMG == 1. Otherwise, direct accesses to SMMU\_PMCG\_MPAMIDR are RES0.

## Attributes

SMMU\_PMCG\_MPAMIDR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

| 31   | 24 23   | 16 15      | 0   |
|------|---------|------------|-----|
| RES0 | PMG_MAX | PARTID_MAX |     |

## Bits [31:24]

Reserved, RES0.

## PMG\_MAX, bits [23:16]

Maximum Non-secure PMG value.

- The maximum Non-secure PMG value that is permitted to be used by this PMCG for Non-secure MSIs. This field is RES0 when MPAM is not supported, as indicated by SMMU\_PMCG\_CFGR.MPAM == 0.

## PARTID\_MAX, bits [15:0]

Maximum Non-secure PARTID value.

- The maximum Non-secure PARTID value that is permitted to be used by this PMCG for Non-secure MSIs. This field is RES0 when MPAM is not supported, as indicated by SMMU\_PMCG\_CFGR.MPAM == 0.

## Additional Information

The PMCG Non-secure PMG bit width is defined as the bit position of the most-significant 1 in PMG\_MAX[7:0], plus one, or is defined as zero if PMG\_MAX is zero.

Note: For example, if PMG\_MAX == 0x0f , the PMG bit width is 4.

The PMCG Non-secure PARTID bit width is defined as the bit position of the most-significant 1 in PARTID\_MAX[15:0], plus one, or is defined as zero if PARTID\_MAX is zero.

Note: For example, if PARTID\_MAX == 0x0034 , the PARTID bit width is 6.

Note: PMG\_MAX and PARTID\_MAX specify the maximum values of each ID type that can be configured in the PMCG for a Non-secure MSI. These values do not describe properties of the rest of the system, which are discovered using mechanisms that are outside the scope of this specification.

Note: PMG\_MAX is architecturally permitted to be zero-sized when MPAM is supported by the PMCG.

Note: Because a PMCG might be implemented in a component related to, but separate from the main SMMU, the MPAM capabilities of each PMCG are independent from the MPAM capabilities of the main SMMU.

## Accessing SMMU\_PMCG\_MPAMIDR

Accesses to this register use the following encodings:

Accessible at offset 0xE74 from SMMUv3\_PMCG

- When an access is Non-secure, the PMCG supports Secure state, and SMMUv3\_PMCG.SMMU\_PMCG\_SCR.NSRA == 0, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.28 SMMU\_PMCG\_S\_MPAMIDR

The SMMU\_PMCG\_S\_MPAMIDR characteristics are:

## Purpose

Per-PMCG Secure MPAM capability identification when the PMCG supports MSIs.

## Configuration

This register is present only when the PMCG supports Secure state and (SMMU\_PMCG\_CFGR.MPAM == 1 or SMMU\_PMCG\_CFGR.FILTER\_PARTID\_PMG == 1). Otherwise, direct accesses to SMMU\_PMCG\_S\_MPAMIDR are RES0.

## Attributes

SMMU\_PMCG\_S\_MPAMIDR is a 32-bit register.

This register is part of the SMMUv3\_PMCG block.

## Field descriptions

<!-- image -->

## Bits [31:26]

Reserved, RES0.

## HAS\_MPAM\_NS, bit [25]

See SMMU\_PMCG\_SCR.MSI\_MPAM\_NS.

| HAS_MPAM_NS   | Meaning                                                    |
|---------------|------------------------------------------------------------|
| 0b0           | The MPAM_NS mechanism for Secure state is not implemented. |
| 0b1           | The MPAM_NS mechanism for Secure state is implemented.     |

If SMMU\_PMCG\_CFGR.MSI == 0, HAS\_MPAM\_NS is RES0.

## Bit [24]

Reserved, RES0.

## PMG\_MAX, bits [23:16]

Maximum Secure PMG value.

- The maximum Secure PMG value that is permitted to be used by this PMCG for Secure MSIs. This field is RES0 when MPAM is not supported, as indicated by SMMU\_PMCG\_CFGR.MPAM == 0.

## PARTID\_MAX, bits [15:0]

Maximum Secure PARTID value.

- The maximum Secure PARTID value that is permitted to be used by this PMCG for Secure MSIs. This field is RES0 when MPAM is not supported, as indicated by SMMU\_PMCG\_CFGR.MPAM == 0.

## Additional Information

This register is similar to SMMU\_PMCG\_MPAMIDR except describes the Secure MPAM facilities of the PMCG.

The PMCG Secure PMG bit width is defined as the bit position of the most-significant 1 in PMG\_MAX[7:0], plus one, or is defined as zero if PMG\_MAX is zero.

The PMCG Secure PARTID bit width is defined as the bit position of the most-significant 1 in PARTID\_MAX[15:0], plus one, or is defined as zero if PARTID\_MAX is zero.

## Accessing SMMU\_PMCG\_S\_MPAMIDR

Accesses to this register use the following encodings:

Accessible at offset 0xE78 from SMMUv3\_PMCG

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## 10.5.2.29 SMMU\_PMCG\_ID\_REGS

SMMU\_PMCG register offsets 0xFB0 -0xFFC are defined as a read-only identification register space. For Arm implementations of the SMMU architecture the assignment of this register space, and naming of registers in this space, is consistent with the Arm identification scheme for CoreLink and CoreSight components. Arm strongly recommends that other implementers also use this scheme to provide a consistent software discovery model.

For Arm implementations, the following assignment of fields, consistent with CoreSight ID registers [10], is used:

| Offset   | Name (SMMU_PMCG_- Prefixed)   | Field   | Value   | Meaning                                       |
|----------|-------------------------------|---------|---------|-----------------------------------------------|
| 0xFF0    | CIDR0, Component ID0          | [7:0]   | 0x0D    | Preamble                                      |
| 0xFF4    | CIDR1, Component ID1          | [7:4]   | 0x9     | CLASS                                         |
| 0xFF4    | CIDR1, Component ID1          | [3:0]   | 0x0     | Preamble                                      |
| 0xFF8    | CIDR2, Component ID2          | [7:0]   | 0x05    | Preamble                                      |
| 0xFFC    | CIDR3, Component ID3          | [7:0]   | 0xB1    | Preamble                                      |
| 0xFE0    | PIDR0, Peripheral ID0         | [7:0]   | IMP DEF | Part_0: bits [7:0] of the Part number         |
| 0xFE4    | PIDR1, Peripheral ID1         | [7:4]   | IMP DEF | DES_0: bits [3:0] of the JEP106 Designer code |
| 0xFE4    | PIDR1, Peripheral ID1         | [3:0]   | IMP DEF | PART_1: bits [11:8] of the Part number        |
| 0xFE8    | PIDR2, Peripheral ID2         | [7:4]   | IMP DEF | REVISION                                      |
| 0xFE8    | PIDR2, Peripheral ID2         | [3]     | 1       | JEDEC-assigned value for DES always used      |

Chapter 10. Performance Monitors Extension 10.5. Registers

| Offset   | Name (SMMU_PMCG_- Prefixed)   | Field   | Value   | Meaning                                                           |
|----------|-------------------------------|---------|---------|-------------------------------------------------------------------|
|          |                               | [2:0]   | IMP DEF | DES_1: bits [6:4] bits of the JEP106 Designer code                |
| 0xFEC    | PIDR3, Peripheral ID3         | [7:4]   | IMP DEF | REVAND                                                            |
|          |                               | [3:0]   | IMP DEF | CMOD                                                              |
| 0xFD0    | PIDR4, Peripheral ID4         | [7:4]   | 0       | SIZE                                                              |
|          |                               | [3:0]   | IMP DEF | DES_2: JEP106 Designer continuation code                          |
| 0xFD4    | PIDR5, Peripheral ID5         |         | RES0    | Reserved                                                          |
| 0xFD8    | PIDR6, Peripheral ID6         |         | RES0    | Reserved                                                          |
| 0xFDC    | PIDR7, Peripheral ID7         |         | RES0    | Reserved                                                          |
| 0xFBC    | PMDEVARCH                     | [31:21] | 0x23B   | ARCHITECT ( 0x23B is the resulting encoding of Arm's JEP106 code) |
|          |                               | [20]    | 1       | PRESENT                                                           |
|          |                               | [19:16] | 0       | REVISION                                                          |
|          |                               | [15:0]  | 0x2A56  | ARCHID                                                            |
| 0xFCC    | PMDEVTYPE                     | [7:4]   | 5       | Sub-type: Associated with anSMMU                                  |
|          |                               | [3:0]   | 6       | Class: Performance monitor device type                            |

Fields outside of those defined in this table are RES0.

Note: The Designer code fields (DES\_*) fields for Arm-designed implementations use continuation code 0x4 and Designer code 0x3B .

Note: Non-Arm implementations that follow this CoreSight ID register layout must set the Designer fields appropriate to the implementer.