## 6.3.128 SMMU\_R\_CR0

The SMMU\_R\_CR0 characteristics are:

## Purpose

SMMURealm state programming interface control and configuration register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_CR0 is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:11]

Reserved, RES0.

## DPT\_WALK\_EN, bit [10]

## When SMMU\_R\_IDR3.DPT == 1:

Enable DPT walks for Realm state.

| DPT_WALK_EN   | Meaning                       |
|---------------|-------------------------------|
| 0b0           | Realm DPT walks are disabled. |
| 0b1           | Realm DPT walks are enabled.  |

This field has similar Update behavior to other CR0 fields, in that: When it is writable and its value is changed by a write, the SMMU begins a transition which is then acknowledged by updating SMMU\_R\_CR0ACK.DPT\_WALK\_EN to the new value.

Completion of an Update from 0 to 1 means that:

- The SMMU may make fetches of DPT information, and cache DPT entries where permitted.
- Transactions for a stream with STE.EATS configured to 0b11 do not result in a DPT\_DISABLED DPT lookup fault.

Completion of an Update from 1 to 0 means that:

- The SMMU has completed all outstanding fetches of DPT information and will not make subsequent fetches.
- Previously-cached last-level DPT information in TLBs might continue to be used until completion of appropriate CMD\_DPTI\_* commands. Note: Completion of a CMD\_DPTI\_ALL command is guaranteed to be sufficient to remove all DPT information cached in TLBs. Note: Completion of a CMD\_DPTI\_ALL command is also sufficient to guarantee observability of all Events resulting from the prior DPT\_WALK\_EN = 1 configuration.

- Previously-cached STEs configured with STE.EATS = 0b11 might continue to be used until completion of appropriate Configuration invalidation commands.

## See also:

- STE.EATS
- 3.24 Device Permission Table .

The reset behavior of this field is:

- This field resets to '0' .

Accessing this field has the following behavior:

- When SMMU\_R\_CR0.DPT\_WALK\_EN != SMMU\_R\_CR0ACK.DPT\_WALK\_EN, access to this field is RO.
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

## When SMMU\_R\_IDR0.ATS == 1:

Realm state ATS behavior.

| ATSCHK   | Meaning                                                                                                                                                                    |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1      | Safe mode, all ATS Translated traffic is checked against the corresponding STE.EATS field to determine whether the StreamID is allowed to produce Translated transactions. |

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## CMDQEN, bit [3]

Enable Realm state Command queue processing.

| CMDQEN   | Meaning                                                                |
|----------|------------------------------------------------------------------------|
| 0b0      | Processing of commands from the Realm state Command queue is disabled. |
| 0b1      | Processing of commands from the Realm state Command queue is enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## EVENTQEN, bit [2]

Enable Realm state Event queue writes.

| EVENTQEN   | Meaning                                             |
|------------|-----------------------------------------------------|
| 0b0        | Writes to the Realm state Event queue are disabled. |
| 0b1        | Writes to the Realm state Event queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## PRIQEN, bit [1]

## When SMMU\_R\_IDR0.PRI == 1:

Enable Realm state PRI queue writes.

| PRIQEN   | Meaning                                           |
|----------|---------------------------------------------------|
| 0b0      | Writes to the Realm state PRI queue are disabled. |
| 0b1      | Writes to the Realm state PRI queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## SMMUEN, bit [0]

Realm state SMMU enable.

| SMMUEN   | Meaning                                                                                        |
|----------|------------------------------------------------------------------------------------------------|
| 0b0      | All Realm streams are terminated with an abort, according to SMMU_R_GBPA.                      |
| 0b1      | All Realm streams are checked against configuration structures, and might undergo translation. |

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_R\_CR0

Accesses to this register use the following encodings:

Accessible at offset 0x0020 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## Additional information

For more information, see the additional information section in SMMU\_CR0.