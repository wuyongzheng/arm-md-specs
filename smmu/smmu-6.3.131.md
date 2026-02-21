## 6.3.131 SMMU\_R\_CR2

The SMMU\_R\_CR2 characteristics are:

## Purpose

Realm state SMMU programming interface control and configuration register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_CR2 is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:4]

Reserved, RES0.

## REC\_CFG\_ATS, bit [3]

## When SMMU\_R\_IDR0.ATS == 1 and SMMU\_IDR0.ATSRECERR == 1:

Record ATS Translation Request errors for Realm state in the Event queue.

| REC_CFG_ATS   | Meaning                                                                               |
|---------------|---------------------------------------------------------------------------------------|
| 0b0           | SMMUrecords only the base set of Events for Realm state ATS-related and PRI requests. |
| 0b1           | SMMUrecords an extended set of Events for Realm state ATS-related and PRI requests.   |

See section 3.9.1.2 Responses to ATS Translation Requests and section 8.1 PRI queue overflow for details of which events are recorded or not.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PTM, bit [2]

## When SMMU\_IDR0.BTM == 1:

Realm state Private TLB Maintenance.

| PTM   | Meaning                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The SMMUparticipates in broadcast TLB maintenance for Realm state, if implemented. See SMMU_IDR0.BTM.                                         |
| 0b1   | The SMMUis not required to invalidate any local TLB entries on receipt of broadcast TLB maintenance operations for Realm translation regimes. |

- Broadcast invalidation for Non-secure and Secure EL1, Non-secure and Secure EL2, Non-secure and Secure EL2-E2H or EL3 translation regimes are not affected by this flag, see SMMU\_S\_CR2.PTM.
- This field resets to an IMPLEMENTATION SPECIFIC value. Arm recommends SMMU\_R\_CR2.PTM is reset to 1 where it is supported, but software cannot rely on this value.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RECINVSID, bit [1]

Record event C\_BAD\_STREAMID from invalid input StreamIDs for Realm state.

| RECINVSID   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | C_BAD_STREAMID events are not recorded for the Realm state programming interface.             |
| 0b1         | C_BAD_STREAMID events are permitted to be recorded for the Realm state programming interface. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## E2H, bit [0]

Enable Realm state EL2-E2H translation regime.

| E2H   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | EL2 translation regime, without ASIDs or VMIDs. |
| 0b1   | EL2-E2H translation regime used, with ASID.     |

- This field affects the STE.STRW encoding 0b10 , which selects a hypervisor translation regime for the resulting translations. The translations are tagged without ASID in EL2 mode, or with ASID in EL2-E2H mode. Note: Arm expects software to set this bit to match HCR\_EL2.E2H in host PEs.
- This bit is permitted to be cached in configuration caches and TLBs. Changes to this bit must be accompanied by invalidation of configuration and translations associated with streams configured with StreamWorld == Realm-EL2 or Realm-EL2-E2H.
- This bit affects the StreamWorld of Realm streams only.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_R\_CR2

This register is made read-only when the associated SMMU\_R\_CR0.SMMUEN is Updated to 1. This register must only be changed when SMMU\_R\_CR0.SMMUEN == 0.

A write to this register after SMMU\_R\_CR0.SMMUEN has been changed but before its Update completes is IGNORED.

Accesses to this register use the following encodings:

Accessible at offset 0x002C from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_R\_CR0.SMMUEN == 0 and SMMU\_R\_CR0ACK.SMMUEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.