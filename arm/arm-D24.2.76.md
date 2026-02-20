## D24.2.76 HPFAR\_EL2, Hypervisor IPA Fault Address Register

The HPFAR\_EL2 characteristics are:

## Purpose

Holds the faulting IPA for some aborts on a stage 2 translation taken to EL2 and GPC exceptions due to a fault on an access for a stage 2 translation.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

The HPFAR\_EL2 is written for:

- ATranslation fault, Access Flag fault, or Address Size fault on a stage 2 translation not on a stage 1 translation table walk.
- ATranslation fault, Access Flag fault, Address Size fault, or Permission fault on stage 2 translation of an address accessed in a stage 1 translation table walk.
- If FEAT\_RME is implemented, a Granule Protection Check fault in the second stage of translation.

For all other exceptions taken to EL2, this register is UNKNOWN.

Note

The address held in this register is an address accessed by the instruction fetch or data access that caused the exception that gave rise to the Instruction Abort exception or Data Abort exception. It is the lower address that gave rise to the fault that is reported. Where different faults from different addresses arise from the same instruction, such as for an instruction that loads or stores an unaligned address that crosses a page boundary, the architecture does not prioritize which fault is reported.

AArch64 System register HPFAR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HPFAR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to HPFAR\_EL2 are UNDEFINED.

## Attributes

HPFAR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

Execution at EL1 or EL0 makes HPFAR\_EL2 become UNKNOWN.

## NS, bit [63]

## When FEAT\_SEL2 is implemented:

Faulting IPA address space.

| NS   | Meaning                                        |
|------|------------------------------------------------|
| 0b0  | Faulting IPA is from the Secure IPA space.     |
| 0b1  | Faulting IPA is from the Non-secure IPA space. |

For Data Abort exceptions or Instruction Abort exceptions taken to Non-secure EL2:

- This field is RES0.
- The address is from the Non-secure IPA space.

If FEAT\_RME is implemented, for Data Abort exceptions or Instruction Abort exceptions taken to Realm EL2:

- This field is RES0.
- The address is from the Realm IPA space.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [62:48]

Reserved, RES0.

FIPA, bits [47:4]

## When FEAT\_D128 is implemented:

<!-- image -->

## FIPA, bits [43:0]

Bits [55:12] of the Faulting Intermediate Physical Address.

For implementations with fewer than 55 physical address bits, the corresponding upper bits in this field are RES0.

When FEAT\_MOPS is implemented, the value presented in FIPA on a synchronous exception that set the HPFAR\_EL2 from any of the Memory Copy and Memory Set instructions is within the address range of the current stage 2 translation granule, aligned to the size of the current stage 2 translation granule, of the address that generated the Data abort. In this case, bits[(n-1):0] of the value are UNKNOWN, where 2 n is the current stage 2 translation granule size in bytes.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When FEAT\_LPA is implemented and FEAT\_D128 is not implemented:

<!-- image -->

## Bits [43:40]

Reserved, RES0.

## FIPA, bits [39:0]

Bits [51:12] of the Faulting Intermediate Physical Address.

For implementations with fewer than 52 physical address bits, the corresponding upper bits in this field are RES0.

When FEAT\_MOPS is implemented, the value presented in FIPA on a synchronous exception that set the HPFAR\_EL2 from any of the Memory Copy and Memory Set instructions is within the address range of the current stage 2 translation granule, aligned to the size of the current stage 2 translation granule, of the address that generated the Data abort. In this case, bits[(n-1):0] of the value are UNKNOWN, where 2 n is the current stage 2 translation granule size in bytes.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_LPA is not implemented:

<!-- image -->

## Bits [43:36]

Reserved, RES0.

## FIPA, bits [35:0]

Bits[47:12] Faulting Intermediate Physical Address.

For implementations with fewer than 48 physical address bits, the corresponding upper bits in this field are RES0.

When FEAT\_MOPS is implemented, the value presented in FIPA on a synchronous exception that set the HPFAR\_EL2 from any of the Memory Copy and Memory Set instructions is within the address range of the current stage 2 translation granule, aligned to the size of the current stage 2 translation granule, of the address that generated the Data abort. In this case, bits[(n-1):0] of the value are UNKNOWN, where 2 n is the current stage 2 translation granule size in bytes.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [3:0]

Reserved, RES0.

## Accessing HPFAR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HPFAR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0110 | 0b0000 | 0b100 |

if !IsFeatureImplemented(FEAT\_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = HPFAR\_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HPFAR\_EL2;

MSR HPFAR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0110 | 0b0000 | 0b100 |

if !IsFeatureImplemented(FEAT\_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then HPFAR\_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HPFAR\_EL2 = X[t, 64];