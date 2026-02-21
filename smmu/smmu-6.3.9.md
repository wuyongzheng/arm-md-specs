## 6.3.9 SMMU\_CR0

The SMMU\_CR0 characteristics are:

## Purpose

Non-secure SMMU programming interface control and configuration register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_CR0 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:11]

Reserved, RES0.

## DPT\_WALK\_EN, bit [10]

## When SMMU\_IDR3.DPT == 1:

Enable DPT walks for Non-secure state.

| DPT_WALK_EN   | Meaning                            |
|---------------|------------------------------------|
| 0b0           | Non-secure DPT walks are disabled. |
| 0b1           | Non-secure DPT walks are enabled.  |

This field has similar Update behavior to other CR0 fields, in that: When it is writable and its value is changed by a write, the SMMU begins a transition which is then acknowledged by updating SMMU\_CR0ACK.DPT\_WALK\_EN to the new value.

Completion of an Update from 0 to 1 means that:

- The SMMU may make fetches of DPT information, and cache DPT entries where permitted.
- Transactions for a stream with STE.EATS configured to 0b11 do not result in a DPT\_DISABLED DPT lookup fault.

Completion of an Update from 1 to 0 means that:

- The SMMU has completed all outstanding fetches of DPT information and will not make subsequent fetches.
- Previously-cached last-level DPT information in TLBs might continue to be used until completion of appropriate CMD\_DPTI\_* commands. Note: Completion of a CMD\_DPTI\_ALL command is guaranteed to be sufficient to remove all DPT information cached in TLBs. Note: Completion of a CMD\_DPTI\_ALL command is also sufficient to guarantee observability of all Events resulting from the prior DPT\_WALK\_EN = 1 configuration.

- Previously-cached STEs configured with STE.EATS = 0b11 might continue to be used until completion of appropriate Configuration invalidation commands.

## See also:

- STE.EATS.
- 3.24 Device Permission Table .

The reset behavior of this field is:

- This field resets to '0' .

Accessing this field has the following behavior:

- When SMMU\_CR0.DPT\_WALK\_EN != SMMU\_CR0ACK.DPT\_WALK\_EN, access to this field is RO.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Bit [9]

Reserved, RES0.

## VMW, bits [8:6]

## When SMMU\_IDR0.VMW == 1:

VMID Wildcard.

| VMW   | Meaning                                    |
|-------|--------------------------------------------|
| 0b000 | TLB invalidations match VMID tags exactly. |
| 0b001 | TLB invalidations match VMID[N:1].         |
| 0b010 | TLB invalidations match VMID[N:2].         |
| 0b011 | TLB invalidations match VMID[N:3].         |
| 0b100 | TLB invalidations match VMID[N:4].         |

- All other values are reserved, and behave as 0b000 .
- -N == upper bit of VMID as determined by SMMU\_IDR0.VMID16.
- This field has no effect on VMID matching on translation lookup.

The reset behavior of this field is:

- This field resets to '000' .

## Otherwise:

Reserved, RES0.

## Bit [5]

Reserved, RES0.

## ATSCHK, bit [4]

## When SMMU\_IDR0.ATS == 1:

ATS behavior.

| ATSCHK   | Meaning                                                                                                                                                                    |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Fast mode, all ATS Translated traffic passes through theSMMU without Stream table or TLB lookup.                                                                           |
| 0b1      | Safe mode, all ATS Translated traffic is checked against the corresponding STE.EATS field to determine whether the StreamID is allowed to produce Translated transactions. |

## See also:

- Section 3.9.1.2 Responses to ATS Translation Requests .
- Section 13.6 PCIe and ATS attribute/permissions handling .
- Section 17.3 PCIe ATS transactions .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## CMDQEN, bit [3]

Enable Command queue processing.

| CMDQEN   | Meaning                                                               |
|----------|-----------------------------------------------------------------------|
| 0b0      | Processing of commands from the Non-secure Command queue is disabled. |
| 0b1      | Processing of commands from the Non-secure Command queue is enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## EVENTQEN, bit [2]

Enable Event queue writes.

| EVENTQEN   | Meaning                                            |
|------------|----------------------------------------------------|
| 0b0        | Writes to the Non-secure Event queue are disabled. |
| 0b1        | Writes to the Non-secure Event queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## PRIQEN, bit [1]

## When SMMU\_IDR0.PRI == 1:

Enable PRI queue writes.

| PRIQEN   | Meaning                               |
|----------|---------------------------------------|
| 0b0      | Writes to the PRI queue are disabled. |
| 0b1      | Writes to the PRI queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## SMMUEN, bit [0]

Non-secure SMMU enable

| SMMUEN   | Meaning                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------|
| 0b0      | All Non-secure streams bypass SMMU, with attributes determined from SMMU_GBPA.                      |
| 0b1      | All Non-secure streams are checked against configuration structures, and might undergo translation. |

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_CR0

Accesses to this register use the following encodings:

Accessible at offset 0x0020 from SMMUv3\_PAGE\_0

Accesses to this register are RW.

## Additional information

Each field in this register has a corresponding field in SMMU\_CR0ACK. An individual field is described as Updated after the value of the field observed in SMMU\_CR0ACK matches the value that was written to the field in SMMU\_CR0. Reserved fields in SMMU\_CR0 are not reflected in SMMU\_CR0ACK. To ensure a field change has taken effect, software must poll the equivalent field in SMMU\_CR0ACK after writing the field in this register.

Each field in this register is independent and unaffected by ongoing update procedures of adjacent fields.

Update of a field must complete in finite time, but is not required to occur immediately. The Update process has side effects which are guaranteed to be complete by the time update completes.

A field that has been written is considered to be in a transitional state until Update has completed. Any SMMU function depending on its value observes the old value until the new value takes effect at an UNPREDICTABLE point before Update completes, whereupon the new value is guaranteed to be used. Therefore:

- A new value written to a field cannot be assumed to have taken effect until Update completes.
- A new value written to a field cannot be assumed not to have taken effect immediately after the write is observed by the SMMU.

A written value is observable to reads of the register even before Update has completed.

Anywhere this specification refers to behavior depending on a field value (for example, a rule of the form 'REG must only be changed if SMMUEN == 0'), it is the post-Update value that is referred to. In this example, the

rule would be broken were REG to be changed after the point that SMMU\_(*\_)CR0.SMMUEN has been written to 1 even if Update has not completed. Similarly, a field that has been written and is still in a transitional state (pre-Update completion) must be considered to still have the old value for the purposes of constraints the old value places upon software. For example, SMMU\_CMDQ\_CONS must not be written when CMDQEN == 1, or during an as-yet incomplete transition to 0 (as CMDQEN must still be considered to be 1).

After altering a field value, software must not alter the value of the field again before the Update of the initial alteration is complete. Behavior on doing so is CONSTRAINED UNPREDICTABLE and one of the following occurs:

- The new value is stored and the Update completes with any of the values written:
- -This behavior is only permitted in SMMUv3.1 and earlier.
- -Note: The effective field value in use might not match that read back from this register.
- The new value is ignored and Update completes using the first value (reflected in SMMU\_CR0ACK.
- Cease Update if the new value is the same as the original value before the first write. Note: This means no update side effects would occur.

Note: A write with the same value (on that is not altered) is permitted. This might occur when altering an unrelated field in the same register while an earlier field Update is in process.

## 6.3.9.1 VMW

Update completes after both of the following occur:

- All received broadcast TLB maintenance operations are guaranteed to behave under the new value.
- A fetched CMD\_TLBI\_* command specifying a VMID is guaranteed to be processed using the new value.

This field is permitted to be cached in a TLB; an Update of this field must be followed by invalidation of all StreamWorld EL1 TLB entries, for all enabled stages of translation, for the appropriate Security state.

This field must not be changed while a CMD\_TLBI\_* command specifying a VMID, or incoming broadcast TLB invalidation operations could be being processed. If this is done, the invalidations are not guaranteed to affect TLB entries with the specified VMIDs.

Note: Arm recommends that software stops issuing invalidation commands and uses CMD\_SYNC to ensure any prior invalidation commands are complete before changing this value. Similarly, Arm recommends that software completes all relevant broadcast TLBI operations before changing this field, and avoids issuing subsequent operations until Update is complete.

## 6.3.9.2 ATSCHK

Update completes after both of the following occur:

- Newly-fetched configuration is guaranteed to be interpreted with the new value.
- ATS Translated Transactions are guaranteed to be treated with the new value.

This bit is permitted to be cached in configuration caches. Update of this bit must be followed by invalidation of all STEs associated with ATS traffic.

In addition, this bit must not be cleared when traffic could encounter valid STEs having EATS == 0b10 . See STE.EATS and section 3.9.2 Changing ATS configuration for details of this rule. If this is done, ATS Translated transactions through such STEs have an IPA address and will be presented to the system directly instead of undergoing stage 2 translation. The point at which this begins to occur is UNPREDICTABLE.

## 6.3.9.3 CMDQEN

When SMMU\_(*\_)CR0.CMDQEN completes update from 1 to 0:

- Command processing has stopped.
- Any commands that are in progress have been Consumed in their entirety, and no new commands are fetched from the Command queue. All previous Command queue reads have completed and no reads will later become visible to the system that originated from the previous CMDQEN == 1 configuration.
- Consumed commands are not guaranteed to be complete unless the last Consumed command was a CMD\_SYNC (whose effects are to force completion of prior commands).

- The index after the last Consumed command or the index of the first unprocessed command, if any, is observable in SMMU\_(*\_)CMDQ\_CONS.

Note: Completion of an Update of CMDQEN from 1 to 0 does not guarantee that an outstanding CMD\_SYNC MSI has completed.

When CMDQEN has completed Update to 1, the SMMU begins processing commands if the CMDQ\_PROD / CMDQ\_CONS indexes indicate the queue is non-empty and no Command queue error is present. See Chapter 4 Commands .

Commands are not fetched when CMDQEN == 0.

## 6.3.9.4 EVENTQEN

When SMMU\_(*\_)CR0.EVENTQEN is transitioned from 1 to 0, SMMU accesses to the queue stop. EVENTQEN completes Update when all committed event records that are in progress become visible in the queue and any Event queue abort conditions are visible in SMMU\_(*\_)GERROR.EVENTQ\_ABT\_ERR. Uncommitted events from terminated faulting transactions are discarded when the queue becomes unwritable. See section 7.2 Event queue recorded faults and events .

## 6.3.9.5 PRIQEN

The effective value of PRIQEN is dependent on SMMUEN, however the value of SMMU\_CR0ACK.PRIQEN is solely affected by the actual value of the SMMU\_CR0.PRIQEN field.

When the effective value of SMMU\_CR0.PRIQEN is transitioned from 1 to 0, page request writes into the queue stop. PRIQEN completes Update when all committed page request records that are in progress become visible in the queue. When the effective value of PRIQEN == 0, incoming requests are discarded; see section 8.2 Miscellaneous .

The SMMU\_PRIQ\_* registers are Guarded by the actual value of the SMMU\_CR0.PRIQEN field, not the effective value.

Note: This means that clearing SMMUEN but leaving PRIQEN == 1 is not a permitted method for changing the SMMU\_PRIQ\_* register configuration.

## 6.3.9.6 SMMUEN

SMMU\_CR0.SMMUEN controls translation through the Non-secure interface and behavior of transactions on Non-secure streams. When SMMU\_S\_IDR1.SECURE\_IMPL == 1, SMMU\_S\_CR0.SMMUEN controls transactions on Secure streams and the SMMU might be translating Secure transactions, even if SMMU\_CR0.SMMUEN == 0. In all cases, the effect of the SMMUEN of one programming interface does not affect transactions or requests associated with the other programming interface.

When SMMU\_(*\_)CR0.SMMUEN == 0:

- Incoming transactions on streams with Security state matching that of the SMMUEN do not undergo translation, and their behavior is controlled by SMMU\_(*\_)GBPA:
- -If SMMU\_(*\_)GBPA.ABORT == 0, the transactions bypass the SMMU with attributes determined by the other fields in SMMU\_(*\_)GBPA. This includes transactions supplied with a SubstreamID.
- -If SMMU\_(*\_)GBPA.ABORT == 1, the transactions are terminated with abort.
- When SMMU\_CR0.SMMUEN == 0, the ATS interface is not operational:
- -Incoming ATS Translation Requests are returned with Unsupported Request status.
- -CMD\_ATC\_INV and CMD\_PRI\_RESP commands are ignored.
- -The effective value of PRIQEN is 0 (for SMMU\_CR0.SMMUEN) and incoming PRI Page Requests are discarded.
- -All clients of the interface must undergo re-initialization when the SMMU is re-enabled. For PCIe clients, this will mean endpoint ATS and PRI facilities need to undergo re-initialization.
- -ATS Translated transactions are terminated with an abort.
- Configuration or translation structures are not accessed:

- -The SMMU does not access the Stream table and ignores the contents of SMMU\_(*\_)STRTAB\_* configuration registers, which might be written by software when in this state.
- -Translation and configuration cache entries are not inserted or modified, except for invalidation by maintenance commands or broadcast operations.
* Note: Maintenance commands issued while SMMUEN == 0 can therefore guarantee the targeted entries do not exist in SMMU caches after the command has completed.
* Note: The 'other' Security state might still have SMMUEN == 1 and therefore be inserting cache entries for that Security state. As these entries are not visible to or affected by the Non-secure programming interface, this is only a consideration for the Secure programming interface which can maintain Non-secure cache entries.
- -Prefetch commands do not access configuration or translations nor insert entries thereof into caches.
- -HTTU is not performed. Speculative setting of Access flag is prohibited.
- As translation does not occur for bypassing transactions, translation-related events are not recorded. See section 7.2 Event queue recorded faults and events for events that are permitted to be recorded when SMMUEN == 0.
- ATOS translation requests are not processed, see SMMU\_GATOS\_CTRL.
- Commands and events are still processed, or recorded, as controlled by CMDQEN and EVENTQEN.

Completion of an Update of SMMUEN from 0 to 1 ensures that:

- Configuration written to SMMU\_(*\_)CR2 has taken effect.
- All new transactions will be treated with STE configuration relevant to their stream, and will not undergo SMMUbypass.
- All associated ATOS\_CTRL.RUN fields are 0, see SMMU\_GATOS\_CTRL.

Completion of an Update of SMMUEN from 1 to 0 ensures that:

- All stalled transactions that might be present and that are associated with the programming interface of the SMMUEN have been marked to be terminated with an abort and no new transactions can become stalled.
- -The STAG value of a stall event record relating to a stalled transaction affected by this update is returned to the set of values that the SMMU might use in future stall event records.
- -This transition does not guarantee that stalled transactions have already been terminated by the time of the completion. Software must wait for completion of outstanding transactions in an IMPLEMENTATION DEFINED manner.
- -Note: New transactions cannot stall because SMMU translation is disabled.
- Effective PRIQEN value has transitioned to 0, including PRIQEN side effects.
- ATOS-specific initialization and termination has completed, see SMMU\_GATOS\_CTRL for details.
- ATOStranslation requests that are underway have either completed or are terminated with a INTERNAL\_ERR fault. The ATOS\_CTRL.RUN fields of all affected ATOS register groups have been cleared, and ATOS\_PAR has been updated with the result by the time Update completes.
- All new transactions associated with the programming interface of the SMMUEN will undergo SMMU bypass (using the SMMU\_(*\_)GBPA attributes).

Note: At the point of transitioning SMMUEN, there might be transactions that are in progress that are buffered in the interconnect. The SMMU has no control over these transactions and the system might provide a mechanism to ensure they are flushed before SMMUEN is cleared, if required.

The path of a transaction through the SMMU is atomic with respect to changes of SMMUEN, the SMMU treats a transaction as though SMMUEN did not change mid-way during the path of the transaction path through the SMMU, even if temporally this is not the case. Therefore, when SMMUEN changes, two groups of transactions that are progress are formed for transactions relevant to the Security state of the SMMUEN in question: those that behave according to the old SMMUEN value, and those that behave according to the new value, so that it appears as though the SMMUEN change instantaneously takes effect at some point in time and incoming transactions are processed in their entirety either before or after this point. There is no requirement for the boundary between

Chapter 6. Memory map and registers 6.3. Register formats these groups to be predictable when SMMUEN is altered in the middle of a stream of transactions. However, interconnect ordering guarantees are maintained throughout. The completion of an update to SMMUEN guarantees that all new transactions arriving at the SMMU will be treated with the new value.

A change to SMMUEN is not required to invalidate cached configuration or TLB entries.