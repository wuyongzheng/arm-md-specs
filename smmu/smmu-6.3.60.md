## 6.3.60 SMMU\_S\_CR2

The SMMU\_S\_CR2 characteristics are:

## Purpose

Secure SMMU programming interface control and configuration register.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_CR2 are RES0.

## Attributes

SMMU\_S\_CR2 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 31   | 3 2 1 0   |
|------|-----------|
| RES0 | PTM E2H   |

## Bits [31:3]

Reserved, RES0.

## PTM, bit [2]

## When SMMU\_IDR0.BTM == 1:

Private TLB Maintenance.

| PTM   | Meaning                                                                                                                                                                               |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The SMMUparticipates in broadcast TLB maintenance, if implemented.                                                                                                                    |
| 0b1   | The SMMUis not required to invalidate any local TLB entries on receipt of broadcast TLB maintenance operations for Secure EL1, Secure EL2, Secure EL2-E2H or EL3 translation regimes. |

- Broadcast invalidation for Non-secure EL1, Non-secure EL2 or Non-secure EL2-E2H translation regimes are not affected by this flag, see SMMU\_CR2.PTM.
- Arm recommends that this field resets to 1, but software cannot rely on this value.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## Otherwise:

Reserved, RES0.

## RECINVSID, bit [1]

Record event C\_BAD\_STREAMID from invalid input StreamIDs.

| RECINVSID   | Meaning                                                                                  |
|-------------|------------------------------------------------------------------------------------------|
| 0b0         | C_BAD_STREAMID events are not recorded for the Secure programming interface.             |
| 0b1         | C_BAD_STREAMID events are permitted to be recorded for the Secure programming interface. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## E2H, bit [0]

## When SMMU\_S\_IDR1.SEL2 == 1:

Enable Secure EL2-E2H translation regime.

| E2H   | Meaning                                            |
|-------|----------------------------------------------------|
| 0b0   | Secure EL2 translation regime used, without ASID.  |
| 0b1   | Secure EL2-E2H translation regime used, with ASID. |

- This field affects the STE.STRW encoding 0b10 , which selects a hypervisor translation regime for the resulting translations. The translations are tagged without ASID in EL2 mode, or with ASID in EL2-E2H mode.

Note: Arm expects software to set this bit to match the Secure HCR\_EL2.E2H in host PEs.

- This bit is permitted to be cached in configuration caches and TLBs. Changes to this bit must be accompanied by invalidation of configuration and translations associated with streams configured with StreamWorld == S-EL2 or S-EL2-E2H.
- This bit affects the StreamWorld of Secure streams only.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing SMMU\_S\_CR2

This register is made read-only when the SMMU\_S\_CR0.SMMUEN is Updated to 1. This register must only be changed when SMMU\_S\_CR0.SMMUEN == 0.

A write to this register after SMMU\_S\_CR0.SMMUEN has been changed before its Update completes is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- Apply the new value.
- Ignore the write.

When this register is changed, the new value takes effect (affects SMMU behavior corresponding to the field changed) at an UNPREDICTABLE time, bounded by a subsequent Update to SMMUEN to 1. As a side effect of SMMUEN completing Update to 1, a prior change to this register is guaranteed to have taken effect.

Accesses to this register use the following encodings:

Accessible at offset 0x802C from SMMUv3\_PAGE\_0

Chapter 6. Memory map and registers 6.3. Register formats

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_CR0.SMMUEN == 0 and SMMU\_S\_CR0ACK.SMMUEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.