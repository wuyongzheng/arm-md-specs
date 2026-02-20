## D24.2.144 PFAR\_EL2, Physical Fault Address Register (EL2)

The PFAR\_EL2 characteristics are:

## Purpose

Records the faulting physical address for a synchronous External abort, or SError exception taken to EL2.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_PFAR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PFAR\_EL2 are UNDEFINED.

## Attributes

PFAR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## NS, bit [63]

## When FEAT\_RME\_GDI is implemented:

Together with PFAR\_EL2.NSE and PFAR\_EL2.NSE2, reports the physical address space of the access that triggered the exception.

| NSE2   | NSE   | NS   | Meaning                                                       |
|--------|-------|------|---------------------------------------------------------------|
| 0b0    | 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0    | 0b0   | 0b1  | Non-secure.                                                   |
| 0b0    | 0b1   | 0b0  | Reserved.                                                     |
| 0b0    | 0b1   | 0b1  | Realm.                                                        |
| 0b1    | 0b0   | 0b0  | System Agent.                                                 |
| 0b1    | 0b0   | 0b1  | NS Protected.                                                 |
| 0b1    | 0b1   | 0b0  | Reserved.                                                     |
| 0b1    | 0b1   | 0b1  | Reserved.                                                     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_RME is implemented:

Together with PFAR\_EL2.NSE, reports the physical address space of the access that triggered the exception.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Reserved.                                                     |
| 0b1   | 0b1  | Realm.                                                        |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When EL3 is implemented or FEAT\_Secure is implemented:

Non-secure. Reports the physical address space of the access that triggered the exception.

| NS   | Meaning                            |
|------|------------------------------------|
| 0b0  | Secure physical address space.     |
| 0b1  | Non-secure physical address space. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSE, bit [62]

## When FEAT\_RME is implemented:

Together with PFAR\_EL2.NS, reports the physical address space of the access that triggered the exception.

For a description of the values derived by evaluating NS and NSE together, see MFAR\_EL3.NS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSE2, bit [61]

## When FEAT\_RME\_GDI is implemented:

Together with PFAR\_EL2.NS and PFAR\_EL2.NSE, reports the physical address space of the access that triggered the exception.

For a description of the values derived by evaluating NS, NSE, and NSE2 together, see PFAR\_EL2.NS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [60:56]

Reserved, RES0.

## PA[55:52], bits [55:52]

## When FEAT\_D128 is implemented:

When FEAT\_D128 is implemented, extension to PFAR\_EL2.PA[47:0].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PA[51:48], bits [51:48]

## When FEAT\_LPA is implemented:

When FEAT\_LPA is implemented, extension to PFAR\_EL2.PA[47:0].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PA, bits [47:0]

Physical Address. Bits [47:0] of the aborting physical address.

For implementations with fewer than 48 physical address bits, the corresponding upper bits in this field are RES0.

The recorded address can be any address within the same naturally-aligned fault granule as the faulting physical address, where the size of the fault granule is IMPLEMENTATION DEFINED and no larger than the larger than:

- The size of the range of values permitted to be recorded in FAR\_EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PFAR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name PFAR\_EL2 or PFAR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

PFAR\_EL2 is not valid and reads UNKNOWN if ESR\_EL2.PFV is recorded as 0.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PFAR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0110 | 0b0000 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_PFAR) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PFAREn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.PFAREn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PFAR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = PFAR_EL2;
```

MSR PFAR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0110 | 0b0000 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_PFAR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.PFAREn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.PFAREn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PFAR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then PFAR_EL2 = X[t, 64];
```

```
then
```