## 6.3.10 SMMU\_CR0ACK

The SMMU\_CR0ACK characteristics are:

## Purpose

Provides acknowledgment of changes to configurations and controls in the Non-secure SMMU programming interface, SMMU\_CR0.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_CR0ACK is a 32-bit register.

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

## See SMMU\_CR0.DPT\_WALK\_EN.

The reset behavior of this field is:

- This field resets to '0' .

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

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## CMDQEN, bit [3]

Enable Command queue processing.

| CMDQEN   | Meaning                                                               |
|----------|-----------------------------------------------------------------------|
| 0b0      | Processing of commands from the Non-secure Command queue is disabled. |

| CMDQEN   | Meaning                                                              |
|----------|----------------------------------------------------------------------|
| 0b1      | Processing of commands from the Non-secure Command queue is enabled. |

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

Non-secure SMMU enable.

| SMMUEN   | Meaning                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------|
| 0b0      | All Non-secure streams bypass SMMU, with attributes determined from SMMU_GBPA.                      |
| 0b1      | All Non-secure streams are checked against configuration structures, and might undergo translation. |

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_CR0ACK

Accesses to this register use the following encodings: Accessible at offset 0x0024 from SMMUv3\_PAGE\_0 Accesses to this register are RO.