## 10.4 StreamIDs and filtering

Some event types might be filtered by StreamID, so that events are only counted if they are associated with transactions that match the configured StreamID filter. Other event types are considered unrelated to any particular StreamID and are counted by any counter that is configured to count the event (any StreamID filtering configuration is ignored). An implementation provides a StreamID filter per counter, or one StreamID filter that applies to all counters in the PMCG. This is identified through the SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE field.

When SMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE == 0, the StreamID filter configuration is controlled by register fields for each counter. SMMU\_PMCG\_EVTYPERn.{FILTER\_SID\_SPAN,FILTER\_SEC\_SID} and SMMU\_PMCG\_SMRn.STREAMID are associated with counter n as accessed through SMMU\_PMCG\_EVCNTRn.

WhenSMMU\_PMCG\_CFGR.SID\_FILTER\_TYPE==1, the fields SMMU\_PMCG\_EVTYPER0.{FILTER\_SID\_SPAN, FILTER\_SEC\_SID} and SMMU\_PMCG\_SMR0.STREAMID apply to all counters in the group.

When the corresponding counter is configured to count an event type that can be filtered by StreamID, this configuration allows filtering by:

- Exact StreamID match.
- Partial StreamID match where a variable span of StreamID[N:0] are ignored and only upper StreamID bits are required to match the given filter.
- Match any StreamID (filtering disabled).

There are four configuration modes for filtering events by StreamID and SEC\_SID which depend on the values configured in SMMU\_PMCG\_EVTYPERn.FILTER\_SID\_SPAN and SMMU\_PMCG\_SMRn.STREAMID as follows:

| Mode             | Condition                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExactSID         | FILTER_SID_SPAN = 0                                                                                                                                          |
| PartialSID       | FILTER_SID_SPAN = 1, and STREAMID is a mask that is neither: - All-ones in all implemented bits. - All-ones except for the most significant implemented bit. |
| AllSIDOneSECSID  | FILTER_SID_SPAN = 1, and STREAMID is a mask that is all-ones except for the most-significant implemented bit.                                                |
| AllSIDManySECSID | FILTER_SID_SPAN = 1, and STREAMID is a mask that is all-ones in all implemented bits.                                                                        |

When a counter uses the ExactSID mode, SMMU\_PMCG\_SMRn.STREAMID is programmed with a StreamID that is matched exactly. Events that are associated with other StreamIDs do not cause an increment of the counter.

When a counter uses the PartialSID mode, which allows matching a partial StreamID, where the X most-significant bits must match but the Y least-significant bits might differ, SMMU\_PMCG\_SMRn.STREAMID is programmed with a value that contains:

- STREAMID[Y - 1] == 0. That is, the most significant bit in the group of bits that do not need to match is zero.
- STREAMID[(Y - 2):0] bits are all programmed to 1 (where Y &gt; 1).
- The remainder of implemented bits of STREAMID (the X most-significant bits, from bit Y upwards) contain a value that will match the corresponding bits of event StreamID.
- Examples (in binary):
- -0000:0000:0001:1011:1111:0111:1111:0111 matches 0000:0000:0001:1011:1111:0111:1111:xxxx

10.4. StreamIDs and filtering

- -0000:0000:0001:1011:1111:0111:1111:0110 matches 0000:0000:0001:1011:1111:0111:1111:011x -0000:0000:0001:1011:1111:0101:1111:1111 matches 0000:0000:0001:1011:1111:01xx:xxxx:xxxx

The AllSIDOneSECSID mode, which allows matching all the StreamIDs of one Security state, is a particular case of the PartialSID mode, where Y is equal to SMMU\_IDR0.SIDSIZE.

When a counter uses the AllSIDManySECSID mode, which matches any StreamID regardless of its Security state, SMMU\_PMCG\_SMRn.STREAMID is programmed with 1 for all implemented bits:

- Note: The STREAMID field might implement fewer bits than the SMMU StreamID size. Arm recommends that 0xFFFFFFFF is written to this field to ensure that all implemented bits are set without first determining how many bits to write.
- Note: A value with 0 in the most-significant implemented bit and 1 in all bits below that point is an alternative encoding that matches any StreamID. This is the maximum mask given the encoding of the variable mask size, but requires knowledge of the implemented field size. When Secure state is supported, this encoding behaves differently to the 'all 1' encoding in terms of the scope of filtering according to SEC\_SID.

When the PMCG implements support for Secure state (see section 10.6 Support for Secure state ):

- The SMMU\_PMCG\_EVTYPERn.FILTER\_SEC\_SID flag determines whether the StreamID filter configuration (as determined by SMMU\_PMCG\_EVTYPERn.FILTER\_SID\_SPAN and SMMU\_PMCG\_SMRn.STREAMID) applies to the Secure or the Non-secure StreamID namespace. Secure observation can be disabled so that StreamID matching can only match events that are associated with Non-secure StreamIDs, overriding the effective value of this flag.
- When SMMU\_PMCG\_EVTYPERn.FILTER\_SID\_SPAN == 1 and SMMU\_PMCG\_SMRn.STREAMID field is programmed with 1 in all implemented bits, the filter matches all StreamIDs for both Secure and Non-secure namespaces if Secure observation is enabled, and matches all Non-secure StreamIDs if Secure observation is not enabled. In SMMUv3.0, it is IMPLEMENTATION DEFINED whether:
- -The filter matches all StreamIDs in one of the Secure or Non-secure namespaces as determined by the effective value of the SMMU\_PMCG\_EVTYPERn.FILTER\_SEC\_SID flag.
- -The filter matches all StreamIDs for both Secure and Non-secure namespaces if Secure observation is enabled, and matches all Non-secure StreamIDs if Secure observation is not enabled.
- When SMMU\_PMCG\_EVTYPERn.FILTER\_SID\_SPAN == 1 and SMMU\_PMCG\_SMRn.STREAMID is programmed with 0 in the most-significant implemented bit and 1 in all other implemented bits, the filter matches all StreamIDs for the Secure or the Non-secure namespace as determined by the effective value of the SMMU\_PMCG\_EVTYPERn.FILTER\_SEC\_SID flag.

When PMCG implements support for Realm state, in ExactSID, PartialSID and AllSIDOneSECSID modes, StreamID filtering is applied, and SEC\_SID filtering is applied as described in the table below, where Rel and Sec are defined as:

- Rel = SMMU\_PMCG\_EVTYPERn.FILTER\_REALM\_SID &amp; SMMU\_PMCG\_ROOTCR.RLO;
- Sec = SMMU\_PMCG\_EVTYPERn.FILTER\_SEC\_SID &amp; SMMU\_PMCG\_SCR.SO;

|   Rel |   Sec | Result                        |
|-------|-------|-------------------------------|
|     0 |     0 | Count only Non-secure events. |
|     0 |     1 | Count only Secure events.     |
|     1 |     0 | Count only Realm events.      |
|     1 |     1 | Reserved, behaves as {0, 0}.  |

When PMCG implements support for Realm state, in AllSIDManySECSID mode, StreamID

filtering is not applied and SEC\_SID filtering is applied as follows, according to the values of SMMU\_PMCG\_EVTYPERn.{FILTER\_REALM\_SID, FILTER\_SEC\_SID}, SMMU\_PMCG\_SCR.SO and SMMU\_PMCG\_ROOTCR.{RTO, RLO}:

If FILTER\_REALM\_SID = 0 then:

- Non-secure events are counted.
- If SO = 1 then Secure events are additionally counted.

If FILTER\_REALM\_SID = 1 then:

- If FILTER\_SEC\_SID = 0 then:
- -Non-secure events are counted.
- -If RLO = 1 then Realm events are additionally counted.
- If FILTER\_SEC\_SID = 1 then:
- -Non-secure events are counted.
- -If SO = 1 then Secure events are additionally counted.
- -If RLO = 1 then Realm events are additionally counted.
- -If RTO = 1 then NoStreamID accesses to Root PA space are additionally counted.

For the purposes of counting events for NoStreamID accesses, the target PA space of the access is treated as conveying the Security state of the access. NoStreamID accesses are not associated with a StreamID. NoStreamID accesses are only counted in AllSIDOneSECSID and AllSIDManySECSID modes.

## 10.4.1 Counter Group StreamID size

The StreamID that is handled by a PMCG is not required to be the full SMMU-architectural StreamID as seen by the SMMU programming interface. This arises from the possibility that a PMCG represents a sub-component of the SMMU and, in a distributed implementation, the component might only service a subset of the StreamID space of the SMMU. In such an implementation, the upper bits of StreamID might be considered fixed for a given sub-component. For example, block 0 serves clients with StreamIDs 0x00 to 0x0F and block 1 serves clients with StreamIDs 0x10 to 0x1F .

In all cases, the low-order PMCG StreamID bits [N:0] must be equivalent to the SMMU StreamID[N:0]. Where a PMCG StreamID filter is programmed, SMMU\_PMCG\_SMRn.STREAMID might implement fewer bits than indicated by SMMU\_IDR1.SIDSIZE in the SMMU with which the PMCG is associated. The implemented size of the SMMU\_PMCG\_SMRn.STREAMID field is IMPLEMENTATION DEFINED. The association between the span of StreamIDs served by a given PMCG and the overall SMMU StreamID namespace is IMPLEMENTATION DEFINED.

For example, an SMMU with a 17-bit StreamID might be composed of two components A and B, which support client devices with StreamIDs 0 to 0xFFFF and 0x10000 to 0x1FFFF respectively. In order to count events from the client device with StreamID 0x12345 , software programs a counter in the PMCG that is associated with component B to filter on StreamID 0x12345 . However, SMMU\_PMCG\_SMRn.STREAMID might only implement 16 bits and read back the value 0x02345 .

Software must not depend on readback of SMMU\_PMCG\_SMRn.STREAMID returning the full SMMU StreamID. The readback value might be truncated to the PMCG StreamID size.

## 10.4.2 Counting of NoStreamID accesses

NoStreamID accesses are permitted to cause events to be counted, subject to all of the following constraints:

- For the purposes of PMCG filtering, the target PA space of NoStreamID accesses is treated as indicating the effective Security state of the accesses.
- NoStreamID accesses are only counted if counting of events for their effective Security state is enabled.
- NoStreamID accesses are only counted if SMMU\_PMCG\_EVTYPERn.FILTER\_SID\_SPAN == 1, and SMMU\_PMCG\_SMRn.STREAMID is programmed to count accesses from all streams, and that selection of all streams includes the effective Security state of the NoStreamID accesses. Note: This is when

SMMU\_PMCG\_SMRn.STREAMID is all-ones in all implemented bits, or all-ones in all implemented bits except for the most-significant bit.

Note: These requirements mean that if FILTER\_REALM\_SID is zero, or not implemented, then no PMCG events are counted for accesses from NoStreamID devices to Root or Realm physical address spaces.

When a NoStreamID access is permitted to cause events to be counted, then it can count:

- Event ID 1 for the NoStreamID transaction.
- Event IDs 2 and 4 for the GPT-related events, as described in section 10.3 Monitor events .
- IMPLEMENTATION DEFINED GPT-related events.

See also:

- 3.25.1.1 GPC for client devices without a StreamID .

## 10.4.3 PARTID- and PMG-based filtering

If SMMU\_PMCG\_CFGR.FILTER\_PARTID\_PMG == 1, then the PMCG supports filtering of events by MPAM PARTID and PMG.

When PARTID- or PMG-based filtering is enabled in a particular SMMU\_PMCG\_EVTYPERn register, the SMMU PMCG uses the PARTID and/or PMG values configured in the corresponding SMMU\_PMCG\_SMRn register to filter events that are counted in the corresponding SMMU\_PMCG\_EVTYPERn register.

Filtering by PARTID and PMG can be enabled independently, using the configuration bits SMMU\_PMCG\_EVTYPERn.{FILTER\_PARTID, FILTER\_PMG, FILTER\_MPAM\_NS}.

In an SMMU implementation with RME DA, SMMU\_PMCG\_EVTYPERn.FILTER\_MPAM\_NS is replaced by a 2-bit field, FILTER\_MPAM\_SP. This change is architected such that the values of FILTER\_MPAM\_NS directly match the first two values of FILTER\_MPAM\_SP. See SMMU\_PMCG\_EVTYPERn.

If filtering by PARTID and/or PMG is enabled, then filtering by StreamID is not available.

When filtering by PARTID, the SMMU compares the PARTID value configured in SMMU\_PMCG\_SMRn to the output PARTID of each transaction or SMMU-originated access, whether that comes from SMMU\_(S\_)GBPMPAM, SMMU\_(*\_)GMPAM, the STE or the CD.

When filtering by PMG, the SMMU compares the PMG value configured in SMMU\_PMCG\_SMRn to the output PMG of each transaction or SMMU-originated access, whether that comes from SMMU\_(S\_)GBPMPAM, the STE or the CD.

It is IMPLEMENTATION DEFINED whether an SMMU PMCG can filter events 3 and 5 by PARTID and PMG.

For each IMPLEMENTATION DEFINED event, it is IMPLEMENTATION DEFINED whether an SMMU PMCG can filter that event by PARTID and PMG.

If an SMMU PMCG is configured to filter an event by PARTID or PMG and the SMMU does not support filtering by PARTID or PMG for that event ID, the event is counted without filtering.

Note: If filtering by PARTID or PMG is supported and enabled for an event ID and a transaction is terminated before it was assigned with a PARTID and PMG then it is IMPLEMENTATION DEFINED if an event arising from that transaction is counted.

If an SMMU PMCG is configured to filter a filterable event by PARTID or PMG values exceeding those advertised in SMMU\_PMCG\_(S\_)MPAMIDR, it counts no events.

|   Event ID | Description            | Can filter by PARTID or PMG   |
|------------|------------------------|-------------------------------|
|          0 | Clock cycle            | No                            |
|          1 | Transaction or request | Yes                           |

|   Event ID | Description                                                           | Can filter by PARTID or PMG   |
|------------|-----------------------------------------------------------------------|-------------------------------|
|          2 | TLB miss caused by incoming transaction or translation request        | Yes                           |
|          3 | Configuration cache miss caused by transaction or translation request | IMPLEMENTATION DEFINED        |
|          4 | Translation table walk access                                         | Yes                           |
|          5 | Configuration structure access                                        | IMPLEMENTATION DEFINED        |
|          6 | PCIe ATS Translation Request received                                 | Yes                           |
|          7 | PCIe ATS Translated Transaction passed through SMMU                   | Yes                           |

## 10.4.4 Counting of non-attributable events

A non-attributable event is an event that is not directly associated with a single Security state, but might reveal information about a Security state.

Note: None of the architected SMMUv3 events are non-attributable events.

If Realm state is not implemented and Secure state is implemented, non-attributable events are only counted if SMMU\_PMCG\_SCR.SO is 1.

If the Realm programming interface is present, then non-attributable events are only counted if all of the following are true:

- SMMU\_PMCG\_ROOTCR.NAO is 1.
- Either or both of SMMU\_PMCG\_SCR.SO and SMMU\_PMCG\_SCR.NAO are 1.