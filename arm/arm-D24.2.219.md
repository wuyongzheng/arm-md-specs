## D24.2.219 VMPIDR\_EL2, Virtualization Multiprocessor ID Register

The VMPIDR\_EL2 characteristics are:

## Purpose

Holds the value of the Virtualization Multiprocessor ID. This is the value returned by EL1 reads of MPIDR\_EL1, which in a multiprocessor system, provides an additional PE identification system.

## Configuration

If EL2 is not implemented, reads of this register return the value of the MPIDR\_EL1 and writes to the register are ignored.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register VMPIDR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register VMPIDR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to VMPIDR\_EL2 are UNDEFINED.

## Attributes

VMPIDR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:40]

Reserved, RES0.

## Aff3, bits [39:32]

Affinity level 3. See the description of VMPIDR\_EL2.Aff0 for more information.

Aff3 is not supported in AArch32 state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [31]

Reserved, RES1.

## U, bit [30]

Indicates a Uniprocessor system, as distinct from PE 0 in a multiprocessor system.

| U   | Meaning                                       |
|-----|-----------------------------------------------|
| 0b0 | Processor is part of a multiprocessor system. |
| 0b1 | Processor is part of a uniprocessor system.   |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [29:25]

Reserved, RES0.

## MT, bit [24]

Indicates whether the lowest level of affinity consists of logical PEs that are implemented using a multithreading type approach. See the description of VMPIDR\_EL2.Aff0 for more information about affinity levels.

| MT   | Meaning                                                                 |
|------|-------------------------------------------------------------------------|
| 0b0  | Performance of PEs at the lowest affinity level is largely independent. |
| 0b1  | Performance of PEs at the lowest affinity level is very interdependent. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Aff2, bits [23:16]

Affinity level 2. See the description of VMPIDR\_EL2.Aff0 for more information.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Aff1, bits [15:8]

Affinity level 1. See the description of VMPIDR\_EL2.Aff0 for more information.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Aff0, bits [7:0]

Affinity level 0.

The value of the MPIDR.{Aff2, Aff1, Aff0} or MPIDR\_EL1.{Aff3, Aff2, Aff1, Aff0} set of fields of each PE must be unique within the system as a whole.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VMPIDR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VMPIDR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0000 | 0b0000 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x050]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = VMPIDR_EL2; elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then X[t, 64] = MPIDR_EL1; else X[t, 64] = VMPIDR_EL2;
```

MSR VMPIDR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0000 | 0b0000 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x050] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then VMPIDR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then return; else VMPIDR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, MPIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0000 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.MPIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() then X[t, 64] = VMPIDR_EL2; else X[t, 64] = MPIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = MPIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPIDR_EL1;
```