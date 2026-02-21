## 7.3 Event records

Event records are 32 bytes in size, and are defined later in this section. All Event records are little-endian. Event records are recorded into the Event queue appropriate to the Security status of the StreamID causing the event, unless otherwise specified.

Common fields provided in events are:

- StreamID: The StreamID of the requester that issued the incoming transaction that led to the event
- RnW: The Read/Write nature of the incoming transaction that led to the event
- -0: Write
- -1: Read

Note: The value of this field depends on what triggered the Event. For CMOs see 16.7.2 Non-data transfer transactions , for ATS TR see 3.9.1 ATS Interface and for transactions see 13.1.1 Attribute definitions .

- PnU: Privileged/Unprivileged (post-STE override)
- -0: Unprivileged
- -1: Privileged
- InD: Instruction/Data (post-STE override)
- -0: Data
- -1: Instruction
- InputAddr: The 64-bit address input to the SMMU for the transaction that led to the event. The address includes any sign-extension that might occur before the SMMU input, as described in section 3.4.1 Input address size and Virtual Address size . TBI does not affect the InputAddr field, which includes bits [63:56] in the same form as they were supplied to the SMMU.
- -Note: This field might be interpreted as a V A, an IPA or a PA depending on the scenario and the event number. For example, if F\_TRANSLATION is generated for a stage 1 fault, then InputAddr is a VA.
- SSV: The SubstreamID validity flag
- -0: No SubstreamID was provided with the transaction and the SubstreamID field is UNKNOWN.
- -1: A SubstreamID was provided and the SubstreamID field is valid.
- SubstreamID: The SubstreamID provided with the transaction that led to the event
- -Note: Only valid if SSV == 1.
- S2: Stage of fault
- -0: Stage 1 fault occurred
- -1: Stage 2 fault occurred
- CLASS: The class of the operation that caused the fault
- -0b00 : CD, CD fetch.
- -0b01 : TTD, Stage 1 translation table fetch.
- -0b10 : IN, Input address caused fault.
- -0b11 : Reserved.
- NSIPA: Non-secure IPA
- -In events that record an IPA InputAddr relating to a Secure stream, an NSIPA bit is required to differentiate whether the fault occurred as part of accessing the Secure or Non-secure IPA space.
- -This bit is zero unless the event is recorded on the Secure event queue and S2 == 1, in which case this bit equals the NS bit that was output from stage 1 for the faulting access.
- -Note: This evaluation is made from STE.NSCFG if stage 1 translation was bypassed, or uses the target IPA space from the stage 1 translation.

- -Note: In the case of a stage 2 fault on a Secure stream, this bit indicates whether a translation attempt was made through STE.S2TTB or STE.S\_S2TTB.
- GPCF: Granule Protection Check Fault
- -0: External abort did not arise from a GPC fault.
- -1: The Event record arose from a GPC fault. See also 3.25.3 SMMU-originated accesses .

Note: Arm recommends that software treats receipt of any event that is not architected here as a non-fatal occurrence.

The F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH and F\_WALK\_EABT events contain fields that report a fetch address, which is the address of a specific structure or descriptor that an aborting transaction was originally initiated to access. This STE, CD, VMS or TTD address is as was calculated by a Stream table, CD table or VMS access or translation table walk.

Portions of event records that are not explicitly defined in this section are RES0.

## 7.3.1 Event record merging

Events originating from a stream are permitted to be merged when the stream has not been configured to explicitly inhibit merging with STE.MEV == 0. A merged event record is a single record written to the Event queue representing more than one occurrence of an event.

Two or more events are permitted but not required to be merged by an implementation when:

- The events are identical, or differ only as explicitly stated in event record definitions, and
- If the event type has a Stall field, Stall == 0. Events with a Stall parameter are never merged if Stall == 1.
- The events are not separated by a significant amount of time.
- -Note: The merging feature is intended to rate-limit events occurring at an unusually high frequency. Arm strongly recommends that an implementation writes separate records for events that do not occur in quick succession.

For the purposes of merging events, events are considered identical if all defined fields are the same except where explicitly indicated by an event definition.

The STE.MEV flag controls whether events resulting from a particular stream are merged. When STE.MEV == 0, events (other than listed below) are not merged; this can be useful for debug visibility where one transaction can be matched to one fault event. As STE.MEV is contained in an STE, it can only control the merging of events that are generated after a valid STE is located. The following events might occur before an STE is located, so might always be merged:

- F\_UUT.
- C\_BAD\_STREAMID.
- F\_STE\_FETCH.
- C\_BAD\_STE.

Hardware implementations are required to respect STE.MEV == 0, so that (other than the four events listed in this section) no events are merged. Arm recommends that software expects that event records might be merged even if STE.MEV == 0.

Note: In particular, software running in a virtual machine might set STE.MEV == 0 but a hypervisor might deem merging to remain valuable and cause it to remain enabled.

Note: An event that is recorded when STE.MEV == 1 and where Stall == 0 can therefore be interpreted as representing one or more transactions that faulted for the same reason.

## 7.3.2 F\_UUT

<!-- image -->

| 255                                      | 224                       |                                          |                                          |                                          |                                          |                                          |
|------------------------------------------|---------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| RES0                                     | RES0                      | RES0                                     | RES0                                     | RES0                                     | RES0                                     | RES0                                     |
| 223                                      | 192                       | 223                                      | 223                                      | 223                                      | 223                                      | 223                                      |
| RES0                                     | RES0                      | RES0                                     | RES0                                     | RES0                                     | RES0                                     | RES0                                     |
| 191                                      | 160                       | 191                                      | 191                                      | 191                                      | 191                                      | 191                                      |
| InputAddr[63:0]                          | InputAddr[63:0]           | InputAddr[63:0]                          | InputAddr[63:0]                          | InputAddr[63:0]                          | InputAddr[63:0]                          | InputAddr[63:0]                          |
| 159                                      | 128                       | 159                                      | 159                                      | 159                                      | 159                                      | 159                                      |
| InputAddr[63:0]                          | InputAddr[63:0]           | InputAddr[63:0]                          | InputAddr[63:0]                          | InputAddr[63:0]                          | InputAddr[63:0]                          | InputAddr[63:0]                          |
| 127 100 99 98 97                         | 96                        | 127 100 99 98 97                         | 127 100 99 98 97                         | 127 100 99 98 97                         | 127 100 99 98 97                         | 127 100 99 98 97                         |
| RES0 RnW InD PnU                         | RES0 RnW InD PnU          | RES0 RnW InD PnU                         | RES0 RnW InD PnU                         | RES0 RnW InD PnU                         | RES0 RnW InD PnU                         | RES0 RnW InD PnU                         |
| 95 80 Reason (IMPLEMENTATION DEFINED) 79 | 64                        | 95 80 Reason (IMPLEMENTATION DEFINED) 79 | 95 80 Reason (IMPLEMENTATION DEFINED) 79 | 95 80 Reason (IMPLEMENTATION DEFINED) 79 | 95 80 Reason (IMPLEMENTATION DEFINED) 79 | 95 80 Reason (IMPLEMENTATION DEFINED) 79 |
| 63                                       | 63                        | 63                                       | 63                                       | 63                                       | 63                                       | 63                                       |
| StreamID                                 | StreamID                  | StreamID                                 | StreamID                                 | StreamID                                 | StreamID                                 | StreamID                                 |
| 31                                       | 0                         |                                          |                                          |                                          |                                          |                                          |
| SubstreamID SSV RES0 0x01                | SubstreamID SSV RES0 0x01 | SubstreamID SSV RES0 0x01                | SubstreamID SSV RES0 0x01                | SubstreamID SSV RES0 0x01                | SubstreamID SSV RES0 0x01                | SubstreamID SSV RES0 0x01                |

RES0

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x01           | Unsupported Upstream Transaction. This event is caused for IMPLEMENTATION DEFINED reasons, depending on the bus system, a client device might express an unsupported or illegal transaction type. See section 16.7.1 Reporting of Unsupported Client Transactions . An IMPLEMENTATION DEFINED cause is provided in Reason. The InD/PnU attributes provided in this event are the incoming attributes, not the post-STE override versions. |

This event is permitted to be recorded when SMMUEN == 0.

## 7.3.3 C\_BAD\_STREAMID

<!-- image -->

| 255            | 224            |                |                |
|----------------|----------------|----------------|----------------|
| RES0           | RES0           | RES0           | RES0           |
| 223 192        | 223 192        | 223 192        | 223 192        |
| RES0           | RES0           | RES0           | RES0           |
| 191 160        | 191 160        | 191 160        | 191 160        |
| RES0           | RES0           | RES0           | RES0           |
| 159 128        | 159 128        | 159 128        | 159 128        |
| RES0           | RES0           | RES0           | RES0           |
| 127 96         | 127 96         | 127 96         | 127 96         |
| RES0           | RES0           | RES0           | RES0           |
| 64             | 64             | 64             | 64             |
| RES0           | RES0           | RES0           | RES0           |
| 63 32          | 63 32          | 63 32          | 63 32          |
| StreamID       | StreamID       | StreamID       | StreamID       |
| SubstreamID    | SubstreamID    | SubstreamID    | SubstreamID    |
| SSV RES0 0x02  | SSV RES0 0x02  | SSV RES0 0x02  | SSV RES0 0x02  |
| 12 11 10 8 7 0 | 12 11 10 8 7 0 | 12 11 10 8 7 0 | 12 11 10 8 7 0 |
| 31             | 31             | 31             | 31             |

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x02           | Transaction StreamID out of range. Recorded when SMMU_(*_)CR2.RECINVSID == 1 and any of the following conditions arises: 1. Incoming StreamID >= 2 (SMMU_(*_)STRTAB_BASE_CFG.LOG2SIZE) 2. When SMMU_(*_)STRTAB_BASE_CFG.FMT == 2-level, given StreamID reaches a level 1 descriptor where: a) L1STD.Span == 0 b) L1STD.Span == Reserved c) L1STD.Span > SMMU_(*_)STRTAB_BASE_CFG.SPLIT + 1 d) The given StreamID[SPLIT - 1:0] >= 2 L1STD.Span-1 . |

For out-of-range Secure StreamIDs, this event is recorded on the Secure Event queue and for Non-secure StreamIDs, the Non-secure Event queue. Each Security state might have a different number of StreamIDs (controlled by SMMU\_STRTAB\_BASE\_CFG and SMMU\_S\_STRTAB\_BASE\_CFG.

## 7.3.4 F\_STE\_FETCH

<!-- image -->

| 255 248 247     |      |      | 224     |      |      |      |      |
|-----------------|------|------|---------|------|------|------|------|
|                 | RES0 |      |         |      |      |      |      |
| 223             |      |      | 194 192 |      |      |      |      |
| FetchAddr[55:3] |      |      | RES0    |      |      |      |      |
| 191             |      |      | 160     |      |      |      |      |
| 159             |      |      | 128     |      |      |      |      |
| 127             |      |      | 96      |      |      |      |      |
| 81 80 79        |      | 95   | 64      | 95   | 95   | 95   | 95   |
|                 |      | RES0 | RES0    | RES0 | RES0 | RES0 | RES0 |
| GPCF            |      |      |         |      |      |      |      |
| 63              |      |      | 32      |      |      |      |      |
|                 |      | 31   | 0       | 31   | 31   | 31   | 31   |

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x03           | Fetch of STE caused external abort (access aborted by system/interconnect/Completer, or consumed external error where RAS features available), or the address was out of range as described in 3.4.3 Address sizes of SMMU-originated accesses . FetchAddr is the Physical Address used for the fetch. In SMMUv3.0, bits [47:OAS] are UNKNOWN. In SMMUv3.1, bits [51:OAS] are UNKNOWN. An IMPLEMENTATION DEFINED cause is provided in Reason. |

Note: This event might be injected into a guest VM, as though from a virtual SMMU, when a hypervisor detects invalid guest configuration that would cause a guest STE fetch from an illegal IPA.

Arm recommends that an implementation with RAS features differentiates a failure that arose because of the consumption of an error from a failure caused by the use of an illegal address.

FetchAddr bits [55:OAS] are RES0 if OAS is smaller than 56, where OAS is the system physical address size reported by SMMU\_IDR5.OAS.

## 7.3.5 C\_BAD\_STE

<!-- image -->

| 255                       | 224                       |                           |                           |
|---------------------------|---------------------------|---------------------------|---------------------------|
| RES0                      | RES0                      | RES0                      | RES0                      |
| 223 192                   | 223 192                   | 223 192                   | 223 192                   |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 191 160                   | 191 160                   | 191 160                   | 191 160                   |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 159 128                   | 159 128                   | 159 128                   | 159 128                   |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 127 96                    | 127 96                    | 127 96                    | 127 96                    |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 64                        | 64                        | 64                        | 64                        |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 32                        | 32                        | 32                        | 32                        |
| StreamID                  | StreamID                  | StreamID                  | StreamID                  |
| 12 11 10 8 7 0            | 12 11 10 8 7 0            | 12 11 10 8 7 0            | 12 11 10 8 7 0            |
| SubstreamID SSV RES0 0x04 | SubstreamID SSV RES0 0x04 | SubstreamID SSV RES0 0x04 | SubstreamID SSV RES0 0x04 |
| 31                        | 31                        | 31                        | 31                        |

| Event number   | Reason                                                              |
|----------------|---------------------------------------------------------------------|
| 0x04           | Used STE invalid (V == 0, Reserved field, incorrect configuration). |

See section 5.2.2 Validity of STE for invalid STE configurations.

## 7.3.6 F\_BAD\_ATS\_TREQ

<!-- image -->

| 255   |
|-------|

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x05           | Address Translation Request disallowed for a StreamID and a PCIe ATS Translation Request received. R/W/X/PRIV are the Read/Write/Execute/Privilege permissions requested in the ATS Translation Request, before STE.{INSTCFG/PRIVCFG} overrides are applied: • Write == !NW. • For PCIe ATS, R (Read) is always 1 in a request. Span equals the number of STUs requested. |

Reported in response to an ATS Translation Request in any of the following conditions:

- SMMU\_CR0.SMMUEN == 0
- STE.V == 1 and effective STE.EATS == 0b00
- -Note: See STE.EATS for details. The effective value of EATS is treated as 0b00 in some situations including if STE.Config == 0b100 , or STE is Secure.
- If it is possible for an implementation to observe a Secure ATS Translation Request, this event is recorded.

Note: This event is intended to provide visibility of situations where an ATS Translation Request is prohibited, but an ordinary transaction to the same address from the same StreamID or SubstreamID might complete successfully (where a failure of a TR might otherwise be difficult to debug by issuing an ordinary transaction).

Translation Requests do not cause other events (such as C\_BAD\_STE) to be recorded.

A UR response is made for an ATS Translation Request that causes this event.

## 7.3.7 F\_STREAM\_DISABLED

| 255      |          | 224   |
|----------|----------|-------|
| RES0     | RES0     |       |
| 223      | 223      | 192   |
| RES0     | RES0     |       |
| 191      | 191      | 160   |
| RES0     | RES0     |       |
| 159      | 159      | 128   |
| RES0     | RES0     |       |
| 127      | 127      | 96    |
| RES0     | RES0     |       |
| 95       | 95       | 64    |
| RES0     | RES0     |       |
| 63       | 63       | 32    |
| StreamID | StreamID |       |
| 31       |          | 0     |
|          | 0x06     |       |

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x06           | The STE of a transaction marks non-substream transactions disabled (when STE.Config == 0b1x1 and STE.S1CDMax > 0 and STE.S1DSS == 0b00 ) and the transaction was presented without a SubstreamID. Or, a transaction was presented with SubstreamID 0 when STE.Config == 0b1x1 and STE.S1CDMax > 0 and STE.S1DSS == 0b10 (CD 0 is Reserved for non-substream traffic). Note: This also applies to ATS Translated transactions in implementations with SMMU_IDR3.PASIDTT == 1 when SMMU_CR2.REC_CFG_ATS == 1. |

If STE.V == 1 and STE.Config == 0b000 , incoming traffic is terminated without recording an event.

## 7.3.8 F\_TRANSL\_FORBIDDEN

| 255   |           | 224   |
|-------|-----------|-------|
| RES0  | RES0      | RES0  |
| 223   |           | 192   |
| RES0  | RES0      | RES0  |
| 191   | 160       |       |
| 159   | 128       |       |
| 127   | 100 99 98 | 96    |
|       | RnW       | RES0  |
| 95    | 64        |       |
| 63    |           | 32    |
| 31    |           | 0     |
|       | 0x07      |       |

| Event number   | Reason                                                                                            |
|----------------|---------------------------------------------------------------------------------------------------|
| 0x07           | An incoming PCIe transaction is marked Translated but SMMUbypass is disallowed for this StreamID. |

This event is permitted to be recorded when SMMUEN == 0.

Reported in response to an ATS Translated transaction in any of the following conditions:

- SMMU\_CR0.ATSCHK == 1, STE is valid and either:
- -STE disallows ATS in STE.EATS.
- -STE selects stage 1 bypass &amp; stage 2 bypass (STE.Config == 0b100 ).
- StreamID is Secure, according to SEC\_SID.
- SMMUEN == 0.
- SMMU\_(R\_)IDR3.DPT == 1 and either:

- -The DPT lookup process succeeds, but does not grant access for the transaction being checked. This is referred to as a Device Access fault.
- -The DPT lookup process fails. This fault is also reported in SMMU\_(R\_)DPT\_CFG\_FAR.

Note: This event is intended to provide visibility of situations where an ATS Translated transaction is prohibited, but an ordinary (Untranslated) transaction from the same StreamID or SubstreamID might complete successfully, that is where behavior differs from an ordinary transaction because of the Translated nature of the transaction.

InputAddr[11:0] are IGNORED for the purposes of determining identical events for merging.

## 7.3.9 C\_BAD\_SUBSTREAMID

| 255                   | 224                   |                       |
|-----------------------|-----------------------|-----------------------|
| RES0                  | RES0                  | RES0                  |
| 223 192               | 223 192               | 223 192               |
| RES0                  | RES0                  | RES0                  |
| 191 160               | 191 160               | 191 160               |
| RES0                  | RES0                  | RES0                  |
| 159 128               | 159 128               | 159 128               |
| RES0                  | RES0                  | RES0                  |
| 127 96                | 127 96                | 127 96                |
| RES0                  | RES0                  | RES0                  |
| 64                    | 64                    | 64                    |
| RES0                  | RES0                  | RES0                  |
| 63 32                 | 63 32                 | 63 32                 |
| StreamID              | StreamID              | StreamID              |
| 31 12 11 8 7 0        | 31 12 11 8 7 0        | 31 12 11 8 7 0        |
| SubstreamID RES0 0x08 | SubstreamID RES0 0x08 | SubstreamID RES0 0x08 |

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x08           | Incoming SubstreamID present and one of the following is true: • Stage 1 translation disabled (STE.Config == 0b1x0 ). • Substreams disabled (STE.S1CDMax == 0). This also applies to ATS Translated transactions if SMMU_IDR3.PASIDTT == 1 and SMMU_CR2.REC_CFG_ATS == 1. • SubstreamID >= 2 STE.S1CDMax . • A two-level CD fetch encounters an L1CD structure with V == 0, or an L1CD structure that contains an L2Ptr that is out of range (see 3.4.3 Address sizes of SMMU-originated accesses ). • SMMU_IDR1.SSIDSIZE == 0. • When SMMU_IDR3.PASIDTT == 1 and SMMU_CR2.REC_CFG_ATS == 1, an ATS Translated transaction is presented to the SMMUwith SSV = 1, and either the SubstreamID associated with the transaction exceeds the value permitted by the corresponding STE.S1CDMax configuration or stage 1 translation is disabled. |

When caused by supply of a SubstreamID without stage 1 translation (STE.Config == 0b1x0 ), this behavior arises independent of whether stage 2 translation is enabled.

When this event is generated because of an L1CD.L2Ptr that is out of range, the SubstreamID field indicates the index of the CD that was intended to be fetched when the erroneous L1CD.L2Ptr was used. In the case that an incoming transaction without a SubstreamID caused (through use of STE.S1DSS == 0b10 ) an erroneous L1CD.L2Ptr to be encountered during fetch of the CD at index 0, the SubstreamID is recorded as 0. Otherwise, the SubstreamID that was input with the transaction is recorded.

Note: In this event, SubstreamID is always valid (there is no SSV qualifier).

## 7.3.10 F\_CD\_FETCH

<!-- image -->

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x09           | Fetch of CD caused external abort (access aborted by system/interconnect/Completer, or consumed external error where RAS features available), or in SMMUv3.0 the address was out of range as described in section 3.4.3 Address sizes of SMMU-originated accesses . FetchAddr is the Physical Address used for the fetch. In SMMUv3.0, bits [47:OAS] are UNKNOWN. An IMPLEMENTATION DEFINED cause is provided in Reason. |

Note: This event might be injected into a guest VM, as though from a virtual SMMU, when a hypervisor receives a stage 2 Translation-related fault indicating CD fetch as a cause (with CLASS == CD).

Note: F\_CD\_FETCH does not include an NS bit for FetchAddr. The effective value of NS for FetchAddr can be determined as follows:

- For the Non-secure event queue, Non-secure PA space.
- For the Secure event queue when stage 2 translation is disabled, Secure PA space.
- For the Secure event queue when stage 2 translation is enabled, the target PA space is determined by the value of STE.S2SA for the stream.

FetchAddr bits [55:OAS] are RES0 if OAS is smaller than 56, where OAS is the system physical address size reported by SMMU\_IDR5.OAS.

## 7.3.11 C\_BAD\_CD

<!-- image -->

| 255                       | 224                       |                           |                           |
|---------------------------|---------------------------|---------------------------|---------------------------|
| RES0                      | RES0                      | RES0                      | RES0                      |
| 223 192                   | 223 192                   | 223 192                   | 223 192                   |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 191 160                   | 191 160                   | 191 160                   | 191 160                   |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 159 128                   | 159 128                   | 159 128                   | 159 128                   |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 127 96                    | 127 96                    | 127 96                    | 127 96                    |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 64                        | 64                        | 64                        | 64                        |
| RES0                      | RES0                      | RES0                      | RES0                      |
| 32                        | 32                        | 32                        | 32                        |
| StreamID                  | StreamID                  | StreamID                  | StreamID                  |
| 12 11 10 8 7 0            | 12 11 10 8 7 0            | 12 11 10 8 7 0            | 12 11 10 8 7 0            |
| SubstreamID SSV RES0 0x0a | SubstreamID SSV RES0 0x0a | SubstreamID SSV RES0 0x0a | SubstreamID SSV RES0 0x0a |
| 31                        | 31                        | 31                        | 31                        |

| Event number   | Reason                                                            |
|----------------|-------------------------------------------------------------------|
| 0x0A           | Fetched CD invalid (V == 0, or V == 1 but ILLEGAL configuration). |

See section 5.4.2 Validity of CD for invalid CD configurations.

## 7.3.12 F\_WALK\_EABT

<!-- image -->

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0B           | An external abort occurred fetching (or updating) a translation table descriptor (access aborted by system/interconnect/Completer, or consumed external error where RAS features available). The InD/PnU attributes are the post-STE override values. RnW pertains to the input transaction (InputAddr), not the access causing the abort. InD == 0 when RnW == 0 (see section 13.1.2 Attribute support ). A stage 1-only table walk that encounters EABT on physical access to a descriptor is reported as S2 == 0 (stage 1), CLASS == TT. The SMMUinput transaction address (InputAddr) and descriptor fetch PA (FetchAddr) are provided. Note: This behavior of CLASS == TT when S2 == 0 differs from other F_TRANSLATION, F_ADDR_SIZE, F_ACCESS, F_PERMISSION events relating to a stage 1 fault. A stage 2 table walk can encounter EABT accessing the physical address of a stage 2 descriptor, because of a: • Translation of an IPA for CD fetch - S2 == 1 (stage 2), CLASS == CD - The SMMU input address (InputAddr) and S2 descriptor fetch PA (FetchAddr) are provided • Translation of an IPA for Stage 1 descriptor fetch - S2 == 1 (stage 2), CLASS == TT - The SMMU input address (InputAddr) and S2 descriptor fetch PA (FetchAddr) are provided • Translation of an IPA after successful stage 1 translation (or, in stage 2-only configuration, an input IPA) - S2 == 1 (stage 2), CLASS == IN (Input to stage) - The SMMU input address (InputAddr) and S2 descriptor fetch PA (FetchAddr) are provided. In a nested configuration, a stage 1 walk can encounter EABT accessing the physical address of a stage 1 descriptors having successfully translated the IPA of the descriptor to a PA through stage 2: • S2 == 0 (stage 1), CLASS == TT • This is equivalent to the stage 1-only case. • The SMMUinput address (InputAddr) and S1 descriptor fetch PA (FetchAddr) are provided. An IMPLEMENTATION DEFINED cause is provided in Reason. Note: This event occurs because of an incorrect configuration or, for systems supporting RAS features, consumption of an external error. A stage 1-only translation failing to walk a translation table might result from use of an incorrect or out of range PA in the table. When virtualization is in use, stage 2 translations would normally be fetched correctly. In addition, Arm recommends that hypervisor software does not allow a stage 1 walk to fetch a descriptor from an IPA that successfully translates to PA that causes an abort on access. When a VMSAv8-32 LPAE translation table descriptor fetch leads to an F_WALK_EABT on a system that has OAS < 40, a 40-bit descriptor address was truncated to the OAS to make the fetch. In this case, bits FetchAddr[47:OAS] are UNKNOWN. |

Note: To create the illusion of a guest VM having a stage 1-only virtual SMMU, this event can be injected into the guest if a stage 2 Translation, Access flag, Permission or Address Size fault occurs because of an access made by a stage 1 translation table walk (CLASS == TT).

InputAddr[11:0] are IGNORED for the purposes of determining identical events for merging.

FetchAddr bits [55:OAS] are RES0 if OAS is smaller than 56, where OAS is the system physical address size reported by SMMU\_IDR5.OAS.

## 7.3.13 F\_TRANSLATION

<!-- image -->

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x10           | Translation fault: The address provided to a stage of translation failed the range check defined by TxSZ/SLx, the address was within a disabled TTBx, or a valid translation table descriptor was not found for the address. The RnW, InD and PnU fields provide the access attributes of the input transaction. The InD/PnU attributes are the post-STE override values. InD == 0 when RnW == 0. If fault occurs at stage 1, S2 == 0 and: • CLASS == IN, IPA is UNKNOWN. If fault occurs at stage 2, S2 == 1 and: • If fetching a CD, CLASS == CD, IPA is CD address • If walking stage 1 translation table, CLASS == TT, IPA is the stage 1 translation table descriptor address • If translating an IPA for a transaction (whether by input to stage 2-only configuration, or after successful stage 1 translation), CLASS == IN, and IPA is provided. |

If Stall == 1, not merged. InputAddr[11:0] are IGNORED for the purposes of determining identical events for merging.

IPA bits [55:OAS] are RES0 if OAS is smaller than 56, where OAS is the system physical address size reported by SMMU\_IDR5.OAS.

If SMMU\_R\_IDR3.MEC == 1 then F\_TRANSLATION can be generated as a result of the AMEC bit in some situations. See Chapter 18 Support for Memory Encryption Contexts .

## 7.3.14 F\_ADDR\_SIZE

<!-- image -->

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x11           | Address Size fault: Output address of a translation stage caused Address Size fault. When the stage performs translation, this fault occurs when an intermediate or leaf translation table descriptor outputs an address outside of the effective xPS associated with the translation table (see CD.IPS and STE.S2PS). This does not include a TTB address out of range before the TTW begins as, in this condition, the CD or STE is invalid which results in C_BAD_CD or C_BAD_STE. When stage 1 bypasses translation, this fault occurs when the output address (identical to the input address) is outside the address range implemented, see section 3.4 Address sizes . Refer to F_TRANSLATION for the definition of the CLASS, IPA and S2 fields. The RnW, InD and PnU fields provide the access attributes of the input transaction. The InD/PnU attributes are the post-STE override values. InD == 0 when RnW == 0. If caused by stage 1 translation bypass (because of stage 1 being disabled, unimplemented, or bypassed when STE.S1DSS == 0b01 ), CLASS == IN and S2 == 0 (stage 2 bypass does not cause this fault). |

If Stall == 1, not merged. InputAddr[11:0] are IGNORED for the purposes of determining identical events for merging.

IPA bits [55:OAS] are RES0 if OAS is smaller than 56, where OAS is the system physical address size reported by SMMU\_IDR5.OAS.

## 7.3.15 F\_ACCESS

<!-- image -->

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x12           | Access flag fault due to AF == 0 in a Page or Block descriptor. If HTTU is supported and enabled, a descriptor with AF == 0 is modified such that AF == 1 and this fault is not recorded. Refer to F_TRANSLATION for the definition of the CLASS, IPA and S2 fields. The RnW, InD and PnU fields provide the access attributes of the input transaction. The InD/PnU attributes are the post-STE override values. InD == 0 when RnW == 0. |

If Stall == 1, not merged. InputAddr[11:0] are IGNORED for the purposes of determining identical events for merging.

IPA bits [55:OAS] are RES0 if OAS is smaller than 56, where OAS is the system physical address size reported by SMMU\_IDR5.OAS.

## 7.3.16 F\_PERMISSION

<!-- image -->

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x13           | Permission fault occurred on page access. S2 indicates the stage at which fault occurred. The RnW, InD and PnU fields provide the access attributes of the input transaction. The InD/PnU attributes are the post-STE override values. InD == 0 when RnW == 0. Refer to F_TRANSLATION for the definition of the CLASS, IPA and S2 fields. The TTRnW field is valid when CLASS == TT, that is, a stage 1 translation table walk causes a Permission fault at stage 2. TTRnW is UNKNOWN when CLASS is not TT. TTRnW indicates the read/write property that actually caused the fault as follows: 0 Translation table descriptor Write caused S2 Permission fault. 1 Translation table descriptor Read caused S2 Permission fault. Note: For example, an input read might end up causing a translation table walk write permissions fault at stage 2, when HTTU updates a stage 1 Access flag. Note: When CLASS == TT, the IPA field indicates the stage 1 translation table entry address. Note: Software is expected to use the CLASS field in order to determine the access properties causing the Permission fault. When CLASS == IN, RnW/InD/PnU were inappropriate for the access at the faulting stage. When CLASS == TT, the access is implicitly Data (regardless of the input property) and the faulting R/W property is given by TTRnW. When CLASS == CD, the access is implicitly Data and a read. |

If Stall == 1, not merged. InputAddr[11:0] are IGNORED for the purposes of determining identical events for merging.

In SMMUv3.0, IPA bits [51:48] are RES0.

In an SMMU with RME DA, a translation results in F\_PERMISSION in the following scenarios:

- If the stage 2 translation for the fetch of a Realm L1CD or CD results in a Non-secure address, that results in F\_PERMISSION at stage 2.
- Consistent with FEAT\_RME [2], if the stage 2 translation for a stage 1 translation table walk resolves to a Non-secure address, that results in F\_PERMISSION at stage 2.
- Consistent with FEAT\_RME [2], any Realm instruction fetch that resolves to an Non-secure address results in F\_PERMISSION at the stage that configured the Non-secure output address.

If SMMU\_IDR3.S2PO is 1, then the Overlay bit is set to 1 for stage 2 Permission faults generated as a result of the stage 2 Overlay permission preventing the access. Otherwise, Overlay is reported as 0.

If SMMU\_IDR3.S2PI is 1, then the AssuredOnly bit is set to 1 for stage 2 Permission faults generated only because of the AssuredOnly check. Otherwise, AssuredOnly is 0.

If either SMMU\_IDR3.S2PI or SMMU\_IDR3.S1PI is 1, then the DirtyBit is set to 1 for Permission faults generated from a stage of translation using the Indirect Permission Scheme that has hardware updates of dirty state disabled, and if hardware update of dirty state were enabled the access that caused the fault would have caused an update to the dirty state. Otherwise, DirtyBit is 0.

## 7.3.17 F\_TLB\_CONFLICT

<!-- image -->

| 255   | 248 247   |
|-------|-----------|

RES0

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x20           | A TLB conflict occurred because of the transaction. The nature of this is IMPLEMENTATION DEFINED, defined by the TLB geometry of the implementation. The input address might not be the address that causes the issue, for example an IPA to PA TLB entry might experience the problem, so both addresses are provided. The RnW, InD and PnU fields provide the access attributes of the input transaction. The InD/PnU attributes are the post-STE override values. InD == 0 when RnW == 0. An IMPLEMENTATION DEFINED conflict reason is provided in Reason. This information might be specific to the TLB geometry of the implementation. IPA is valid when S2 == 1, otherwise it is UNKNOWN. |

InputAddr[11:0] are IGNORED for the purposes of determining identical events for merging.

IPA bits [55:OAS] are RES0 if OAS is smaller than 56, where OAS is the system physical address size reported by SMMU\_IDR5.OAS.

## 7.3.18 F\_CFG\_CONFLICT

| 255                             | 224                             |                                 |                                 |
|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
| RES0                            | RES0                            | RES0                            | RES0                            |
| 223 192                         | 223 192                         | 223 192                         | 223 192                         |
| RES0                            | RES0                            | RES0                            | RES0                            |
| 191 160                         | 191 160                         | 191 160                         | 191 160                         |
| RES0                            | RES0                            | RES0                            | RES0                            |
| 159 128                         | 159 128                         | 159 128                         | 159 128                         |
| RES0                            | RES0                            | RES0                            | RES0                            |
| 127 96                          | 127 96                          | 127 96                          | 127 96                          |
| RES0                            | RES0                            | RES0                            | RES0                            |
| 64                              | 64                              | 64                              | 64                              |
| Reason (IMPLEMENTATION DEFINED) | Reason (IMPLEMENTATION DEFINED) | Reason (IMPLEMENTATION DEFINED) | Reason (IMPLEMENTATION DEFINED) |
| 63 32                           | 63 32                           | 63 32                           | 63 32                           |
| StreamID                        | StreamID                        | StreamID                        | StreamID                        |
| 12 11 10 8 7 0                  | 12 11 10 8 7 0                  | 12 11 10 8 7 0                  | 12 11 10 8 7 0                  |
| SubstreamID SSV RES0 0x21       | SubstreamID SSV RES0 0x21       | SubstreamID SSV RES0 0x21       | SubstreamID SSV RES0 0x21       |
| 31                              | 31                              | 31                              | 31                              |

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x21           | A configuration cache conflict occurred due to the transaction. The nature of this is IMPLEMENTATION DEFINED, defined by the configuration cache geometry of the implementation. The STE.CONT property of an STE cache entry causes an overlap of another STE that is not identical , as described in STE.CONT, and this has caused a multiple-match on lookup. An IMPLEMENTATION DEFINED conflict reason is provided in Reason. This information might be specific to the configuration cache geometry of the implementation. |

It is not possible to cause this error by any CD misconfiguration.

Note: A guest VM cannot arrange configuration that would affect any other streams.

## 7.3.19 E\_PAGE\_REQUEST

RES0

255

224

RES0

223

192

InputAddr[63:12]

191

160

InputAddr[63:12]

159

140

RES0

139

128

RES0

127

116

Span

115

108

RES0

107

104

pR

103

pW

102

pX

101100

uR

99

uW

98

uX

97

96

RES0

RES0

95

64

StreamID

63

32

SubstreamID

31

12

SSV

11

RES0

10

8

0x24

7

0

<!-- image -->

RES0

| Event number   | Reason                                                                                                                                                                                                                                                                     |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x24           | Speculative page request hint from a client device to system software, hinting that the given address span will be accessed by a device in the near future. The access is expected to require the read/write/execute properties provided for user/kernel privilege levels. |

No response or action is required, but system software might use this hint to begin a (potentially long-running) page-in of the given address, to decrease the chance of a subsequent access from the device experiencing a page miss.

| Flag fields   | Access anticipated   |
|---------------|----------------------|
| pR            | Privileged Read      |
| pW            | Privileged Write     |
| pX            | Privileged Execute   |
| uR            | Unprivileged Read    |
| uW            | Unprivileged Write   |
| uX            | Unprivileged Execute |

Span is encoded as a positive integer where the size of the intended access span in bytes is (Span*4096).

## 7.3.20 F\_VMS\_FETCH

<!-- image -->

| 255   |      | 248 247     |                 |                 |                 | 224      |         |      |
|-------|------|-------------|-----------------|-----------------|-----------------|----------|---------|------|
|       | RES0 |             |                 | FetchAddr[55:3] |                 |          |         |      |
| 223   |      |             |                 |                 |                 |          | 195 194 | 192  |
|       |      |             | FetchAddr[55:3] |                 |                 |          |         | RES0 |
| 191   |      |             |                 |                 |                 |          |         | 160  |
|       |      |             | RES0            |                 |                 |          |         |      |
| 159   |      |             |                 |                 |                 |          |         | 128  |
|       |      |             | RES0            |                 |                 |          |         |      |
| 127   |      |             |                 |                 |                 |          |         | 96   |
|       |      |             | RES0            |                 |                 |          |         |      |
| 95    |      |             | 81 80 79        |                 |                 |          |         | 64   |
|       |      | RES0        |                 | Reason          | (IMPLEMENTATION | DEFINED) |         |      |
|       |      |             | GPCF            |                 |                 |          |         |      |
| 63    |      |             |                 |                 |                 |          |         | 32   |
|       |      |             | StreamID        |                 |                 |          |         |      |
| 31    |      |             |                 | 12 11 10        |                 |          |         | 0    |
|       |      | SubstreamID |                 | SSV             | RES0            |          | 0x25    |      |

| Event number   | Reason                                                                                                                                                                                                                                                                                                                                                |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x25           | Fetch of VMS caused external abort (access aborted by system/interconnect/Completer, or consumed external error where RAS features available). FetchAddr is the Physical Address used for the fetch. In SMMUv3.0, bits [47:OAS] are UNKNOWN. In SMMUv3.1 and later, bits [51:OAS] are UNKNOWN. An IMPLEMENTATION DEFINED cause is provided in Reason. |

The F\_VMS\_FETCH event has a lower priority than the C\_BAD\_STE event. The priority with respect to subsequent possible events is IMPLEMENTATION DEFINED. See sections 7.3.22 Event queue record priorities and 9.1.5 ATOS\_PAR.FAULTCODE encodings .

Note: If a F\_VMS\_FETCH event is reported, a C\_BAD\_STE has not been reported because a valid STE is required to fetch the VMS. The point at which the VMS is fetched relative to the remainder of the configuration structure walk and translation process is not specified.

FetchAddr bits [55:OAS] are RES0 if OAS is smaller than 56, where OAS is the system physical address size reported by SMMU\_IDR5.OAS.

## 7.3.21 IMPDEF\_EVENTn

| Event number   | Reason                                   |
|----------------|------------------------------------------|
| 0xE0 - 0xEF    | IMPLEMENTATION DEFINED event allocation. |

Notes: Arm recommends that software treats receipt of these events as a non-fatal occurrence even if the exact nature of the event is not recognized.

All other event numbers are Reserved.

Events with a Stall parameter (F\_TRANSLATION, F\_ADDR\_SIZE, F\_ACCESS, F\_PERMISSION) indicate whether a transaction is stalling as a result of the event. When a transaction causes any other event, the transaction is terminated and an abort returned to the client. If a transaction is stalled, the STAG parameter provides a token used to uniquely identify the transaction.

Note: The StreamID and STAG must be provided to a subsequent CMD\_RESUME. Every stall event must have either one associated CMD\_RESUME or a CMD\_STALL\_TERM.

A configuration error always terminates the instigating transaction with an abort to the device.

Multiple addresses might be reported in one event record:

- InputAddr is the address input with the transaction to the SMMU.
- IPA is the post-stage 1 address of the transaction, valid only if the fault occurred at stage 2.
- Fetch PA is the physical address accessed causing the fault to be raised.

The input address is the 64-bit address presented to the SMMU, see section 3.4.1 Input address size and Virtual Address size .

## 7.3.22 Event queue record priorities

Events arising from an ordinary incoming transaction are recorded in the following order, listed from the first that might occur when a transaction is processed to the last that might occur before the transaction is deemed successful, unless otherwise specified. This means that if any event occurs, events prior to that event in this list cannot have occurred:

1. C\_BAD\_STREAMID
2. F\_STE\_FETCH
3. C\_BAD\_STE
4. F\_VMS\_FETCH

F\_VMS\_FETCH is only lower priority than C\_BAD\_STE. Its priority relative to other lower priority events in this list is IMPLEMENTATION DEFINED.

5. C\_BAD\_SUBSTREAMID
6. F\_STREAM\_DISABLED
7. Faults from translation (stage 2, for fetch of CD)
8. F\_CD\_FETCH
9. C\_BAD\_CD
10. Faults from translation (stage 1 or stage 2, for data access of a transaction)

Faults from translation can occur because of a fetch of a CD or stage 1 translation requiring a stage 2 translation, or the final translation for the given transaction address.

A single stage of translation table walk might experience faults in this order:

1. F\_TRANSLATION (for input address outside range defined by TxSZ/SL0, or EPDx == 1)
2. For each level of translation table walked:
- a. F\_WALK\_EABT (on fetch of descriptor)
- b. F\_TRANSLATION (from fetched descriptor)
- c. F\_ADDR\_SIZE (for output of descriptor, indicating next descriptor or walk output address)
3. F\_ACCESS (On the final-level descriptor)
4. F\_PERMISSION (On the final-level descriptor)

A nested Stage 1 + Stage 2 translation table walk might experience faults in this order:

1. F\_TRANSLATION (For stage 1 input address outside range defined by stage 1 TxSZ/SL0, or EPDx == 1)

2. For each level of stage 1 translation table walked, the stage 2 translation for the descriptor of the stage 1s IPA might experience:
- a. F\_TRANSLATION (For stage 2 input address outside range defined by stage 2 T0SZ/SL0)
- b. F\_WALK\_EABT (For stage 2 descriptor fetch)
- c. F\_TRANSLATION (From fetched stage 2 descriptor)
- d. F\_ADDR\_SIZE (For output of stage 2 descriptor, indicating next descriptor or walk output address)
- e. F\_ACCESS (On the final-level stage 2 descriptor)
- f. F\_PERMISSION (On the final-level stage 2 descriptor)
3. For each level of stage 1 translation table walked, after the PA of the descriptor is determined the following might occur:
- a. F\_WALK\_EABT (For stage 1 descriptor fetch)
- b. F\_TRANSLATION (From fetched stage 1 descriptor)
- c. F\_ADDR\_SIZE (For output of stage 1 descriptor)
4. For the final level stage 1 descriptor, the following might then occur:
- a. F\_ACCESS
- b. F\_PERMISSION
5. The IPA relating to the input V A has been determined and permissions have been checked, but the following might occur for each level of the stage 2 translation of that final IPA:
- a. F\_TRANSLATION (For stage 2 input address outside range defined by stage 2 T0SZ/SL0)
- b. F\_WALK\_EABT (For stage 2 descriptor fetch)
- c. F\_TRANSLATION (From fetched stage 2 descriptor)
- d. F\_ADDR\_SIZE (For output of stage 2 descriptor, indicating next descriptor or walk output address)
- e. F\_ACCESS (On the final-level stage 2 descriptor)
- f. F\_PERMISSION (On the final-level stage 2 descriptor)

Note: F\_TLB\_CONFLICT, F\_CFG\_CONFLICT and F\_UUT are raised with IMPLEMENTATION SPECIFIC prioritization.

For an SMMU with RME, then each of F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH and F\_WALK\_EABT can also occur as the result of a granule protection check fault. This does not affect the error reporting priority described in this section. See also section 3.25.3 SMMU-originated accesses .

The flow of events that an incoming ordinary transaction might raise can be characterized as:

- An unsupported transaction fault from the client device might be raised on input.
- Configuration is fetched, in the order of STE then (if relevant) CD:
- -If a CD is fetched, it uses stage 2 translations to do so, if stage 2 is enabled.
- -Stage 2 walk occurs, which might experience an external abort on fetch.
- -Stage 2 page fault on the CD address might occur when the walk completes.
- -External abort on CD fetch might occur.
- When a CD is successfully fetched, start walking stage 1 TT. Stage 2 page faults (or external aborts) might arise from walking stage 1, in the same way as for the initial CD fetch
- When a S1 translation is determined, stage 1 might fault.
- Stage 2 walk occurs for a successful output of stage 1 translation, and this might also fault.

ATS Translation Requests do not lead to the same set of possible errors as, in general, ATS translation errors are reported to the requesting device using the ATS Translation Completion rather than to software through the Event queue. The only Event queue record that can be generated is F\_BAD\_ATS\_TREQ, which can be raised at several points in the translation process.

ATS Translated transactions also differ from ordinary transactions and one of the following behaviors can occur:

- F\_TRANSL\_FORBIDDEN can be raised on input when ATS is disabled/invalid. See section 7.3.8 F\_TRANSL\_FORBIDDEN .
- If SMMU\_(R\_)CR0.SMMUEN == 1, SMMU\_(R\_)CR0.ATSCHK == 1 and SMMU\_(R\_)CR2.REC\_CFG\_ATS == 1, then if the SMMU encounters an error when fetching a configuration structure, the appropriate event is recorded. See section 3.9.1.3 Handling of ATS Translated transactions .
- An ATS Translated transaction that locates the correct configuration and then encounters stage 2 translation (through STE.EATS == 0b10 configuration) can raise stage 2 Translation-related faults.
- Otherwise, any other error on receipt of an ATS Translated transaction (for example, an invalid STE) causes the transaction to be silently terminated.

See Chapter 15 Translation procedure for more details on the translation procedure and possible events at each step.