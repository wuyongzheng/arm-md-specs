## 6.3.12 SMMU\_CR2

The SMMU\_CR2 characteristics are:

## Purpose

Non-secure SMMU programming interface control and configuration register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_CR2 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 31          | 4 3 2 1 0   |
|-------------|-------------|
| RES0        | PTM E2H     |
| REC_CFG_ATS | RECINVSID   |

## Bits [31:4]

Reserved, RES0.

## REC\_CFG\_ATS, bit [3]

## When SMMU\_IDR0.ATSRECERR == 1:

Record Configuration-related errors for ATS and PRI in the Event queue.

| REC_CFG_ATS   | Meaning                                                                   |
|---------------|---------------------------------------------------------------------------|
| 0b0           | SMMUrecords only the base set of Events for ATS-related and PRI requests. |
| 0b1           | SMMUrecords an extended set of Events for ATS-related and PRI requests.   |

See section 3.9.1.2 Responses to ATS Translation Requests and section 8.1 PRI queue overflow for details of which events are recorded or not.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PTM, bit [2]

## When SMMU\_IDR0.BTM == 1:

Private TLB Maintenance.

| PTM   | Meaning                                                                                                                                                                                      |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The SMMUparticipates in broadcast TLB maintenance, if implemented. See SMMU_IDR0.BTM.                                                                                                        |
| 0b1   | The SMMUis not required to invalidate any local TLB entries on receipt of broadcast TLB maintenance operations for Non-secure EL1, Non-secure EL2 or Non-secure EL2-E2H translation regimes. |

- Broadcast invalidation for Secure EL1, Secure EL2, Secure EL2-E2H or EL3 translation regimes are not affected by this flag, see SMMU\_S\_CR2.PTM.
- This field resets to an IMPLEMENTATION SPECIFIC value. Arm recommends PTM is reset to 1 where it is supported, but software cannot rely on this value.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RECINVSID, bit [1]

Record event C\_BAD\_STREAMID from invalid input StreamIDs.

| RECINVSID   | Meaning                                                                                      |
|-------------|----------------------------------------------------------------------------------------------|
| 0b0         | C_BAD_STREAMID events are not recorded for the Non-secure programming interface.             |
| 0b1         | C_BAD_STREAMID events are permitted to be recorded for the Non-secure programming interface. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## E2H, bit [0]

## When SMMU\_IDR0.Hyp == 1:

Enable Non-secure EL2-E2H translation regime.

| E2H   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | EL2 translation regime, without ASIDs or VMIDs. |
| 0b1   | EL2-E2H translation regime used, with ASID.     |

- This field affects the STE.STRW encoding 0b10 , which selects a hypervisor translation regime for the resulting translations. The translations are tagged without ASID in EL2 mode, or with ASID in EL2-E2H mode. Note: Arm expects software to set this bit to match HCR\_EL2.E2H in host PEs.
- This bit is permitted to be cached in configuration caches and TLBs. Changes to this bit must be accompanied by invalidation of configuration and translations associated with streams configured with StreamWorld == NS-EL2 or NS-EL2-E2H.

- This bit affects the StreamWorld of Non-secure streams only.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing SMMU\_CR2

This register is made read-only when the associated SMMU\_CR0.SMMUEN is Updated to 1. This register must only be changed when SMMU\_CR0.SMMUEN == 0.

A write to this register after SMMU\_CR0.SMMUEN has been changed but before its Update completes is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- Apply the new value.
- Ignore the write. In SMMUv3.2 and later, this is the only permitted behavior.

When this register is changed, the new value takes effect (affects SMMU behavior corresponding to the field changed) at an UNPREDICTABLE time, bounded by a subsequent Update of SMMUEN to 1. As a side effect of SMMUEN completing Update to 1, a prior change to this register is guaranteed to have taken effect.

Accesses to this register use the following encodings:

Accessible at offset 0x002C from SMMUv3\_PAGE\_0

- When SMMU\_CR0.SMMUEN == 0 and SMMU\_CR0ACK.SMMUEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.

## Additional information

## 6.3.12.1 PTM

A change to PTM is permitted to take effect at any time prior to a subsequent Update of SMMUEN to 1. If incoming broadcast TLB invalidates are received after PTM is changed but before Update of SMMUEN completes, it is UNPREDICTABLE whether the invalidations take effect.

Broadcast invalidations issued after SMMUEN has Updated to 1 are guaranteed to be treated with the value of PTM prior to the SMMUEN update, if PTM has not been modified after SMMUEN was written.

## 6.3.12.2 RECINVSID

This field only has an effect on transactions received when SMMUEN == 1, therefore a change cannot affect transactions in flight.

## 6.3.12.3 E2H

All Non-secure EL2/EL2-E2H configuration and translation cache entries must be invalidated when E2H is changed. The equivalent requirement exists for Secure EL2/EL2-E2H and changes to SMMU\_S\_CR2.E2H, if implemented.

Note: The behavior of the CMD\_TLBI\_EL2\_VAA and CMD\_TLBI\_EL2\_ASID commands depends on the value of E2H. Because, after write of SMMU\_CR2, the effective action of E2H is UNPREDICTABLE until SMMUEN is transitioned to 1, it is UNPREDICTABLE whether these two commands behave according to E2H == 0 or E2H == 1. Consequently, CMD\_TLBI\_EL2\_ALL must be used to invalidate EL2 translation cache entries.