## D24.2.136 MFAR\_EL3, Physical Fault Address Register (EL3)

The MFAR\_EL3 characteristics are:

## Purpose

Records the faulting physical address for a Granule Protection Check, synchronous External abort, or SError exception taken to EL3.

## Configuration

This register is present only when (FEAT\_PFAR is implemented or FEAT\_RME is implemented) and FEAT\_AA64 is implemented. Otherwise, direct accesses to MFAR\_EL3 are UNDEFINED.

## Attributes

MFAR\_EL3 is a 64-bit register.

## Field descriptions

When FEAT\_RME is implemented and the exception is a GPC exception:

<!-- image -->

## NS, bit [63]

Together with MFAR\_EL3.NSE, reports the physical address space of the access that triggered the exception.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSE, bit [62]

Together with MFAR\_EL3.NS, reports the physical address space of the access that triggered the exception.

For a description of the values derived by evaluating NS and NSE together, see MFAR\_EL3.NS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [61:56]

Reserved, RES0.

## FPA[55:52], bits [55:52]

## When FEAT\_D128 is implemented:

When FEAT\_D128 is implemented, extension to MFAR\_EL3.FPA[47:12].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FPA[51:48], bits [51:48]

## When FEAT\_LPA is implemented:

When FEAT\_LPA is implemented, extension to MFAR\_EL3.FPA[47:12].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FPA, bits [47:12]

Bits [47:12] of the Faulting Physical Address.

For implementations with fewer than 48 physical address bits, the corresponding upper bits in this field are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## When FEAT\_PFAR is implemented and the exception is a synchronous External abort or SError exception:

<!-- image -->

| 63   | 62 61   | 60   | 56 55   | 52 51     |           | 48 47   | 32   |
|------|---------|------|---------|-----------|-----------|---------|------|
| NS   | NSE     |      | RES0    | PA[55:52] | PA[51:48] | PA      |      |
| NSE2 | NSE2    | NSE2 | NSE2    | NSE2      | NSE2      | NSE2    | NSE2 |
| 31   |         |      |         |           |           |         | 0    |
| PA   | PA      | PA   | PA      | PA        | PA        | PA      | PA   |

## NS, bit [63]

## When FEAT\_RME\_GDI is implemented:

Together with MFAR\_EL3.NSE and MFAR\_EL3.NSE2, reports the physical address space of the access that triggered the exception.

| NSE2   | NSE   | NS   | Meaning                                                       |
|--------|-------|------|---------------------------------------------------------------|
| 0b0    | 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0    | 0b0   | 0b1  | Non-secure.                                                   |
| 0b0    | 0b1   | 0b0  | Root.                                                         |
| 0b0    | 0b1   | 0b1  | Realm.                                                        |
| 0b1    | 0b0   | 0b0  | System Agent.                                                 |
| 0b1    | 0b0   | 0b1  | NS Protected.                                                 |
| 0b1    | 0b1   | 0b0  | Reserved.                                                     |
| 0b1    | 0b1   | 0b1  | Reserved.                                                     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_RME is implemented:

Together with MFAR\_EL3.NSE, reports the physical address space of the access that triggered the exception.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Non-secure. Reports the physical address space of the access that triggered the exception.

| NS   | Meaning                            |
|------|------------------------------------|
| 0b0  | Secure physical address space.     |
| 0b1  | Non-secure physical address space. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSE, bit [62]

## When FEAT\_RME is implemented:

Together with MFAR\_EL3.NS, reports the physical address space of the access that triggered the exception.

For a description of the values derived by evaluating NS and NSE together, see MFAR\_EL3.NS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSE2, bit [61]

## When FEAT\_RME\_GDI is implemented:

Together with MFAR\_EL3.NS and MFAR\_EL3.NSE, reports the physical address space of the access that triggered the exception.

For a description of the values derived by evaluating NS, NSE, and NSE2 together, see MFAR\_EL3.NS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [60:56]

Reserved, RES0.

## PA[55:52], bits [55:52]

## When FEAT\_D128 is implemented:

When FEAT\_D128 is implemented, extension to MFAR\_EL3.PA[47:0].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PA[51:48], bits [51:48]

## When FEAT\_LPA is implemented:

When FEAT\_LPA is implemented, extension to MFAR\_EL3.PA[47:0].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PA, bits [47:0]

Physical Address. Bits [47:0] of the aborting physical address.

For implementations with fewer than 48 physical address bits, the corresponding upper bits in this field are RES0.

The recorded address can be any address within the same naturally-aligned fault granule as the faulting physical address, where the size of the fault granule is IMPLEMENTATION DEFINED and no larger than the larger than:

- The size of the range of values permitted to be recorded in FAR\_EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MFAR\_EL3

MFAR\_EL3 is not valid and reads UNKNOWN if ESR\_EL3.EC is recorded indicating an Abort or SError exception and ESR\_EL3.PFV is recorded as 0.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MFAR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0110 | 0b0000 | 0b101 |

```
IsFeatureImplemented(FEAT_RME)) &&
```

```
if !((IsFeatureImplemented(FEAT_PFAR) || ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = MFAR_EL3;
```

MSR MFAR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0110 | 0b0000 | 0b101 |

```
IsFeatureImplemented(FEAT_RME)) &&
```

```
if !((IsFeatureImplemented(FEAT_PFAR) || ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then MFAR_EL3 = X[t, 64];
```