## D24.2.138 MPIDR\_EL1, Multiprocessor Affinity Register

The MPIDR\_EL1 characteristics are:

## Purpose

In a multiprocessor system, provides an additional PE identification mechanism.

## Configuration

In a uniprocessor system, Arm recommends that each Aff&lt;n&gt; field of this register returns a value of 0.

AArch64 System register MPIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register MPIDR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MPIDR\_EL1 are UNDEFINED.

## Attributes

MPIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:40]

Reserved, RES0.

## Aff3, bits [39:32]

Affinity level 3. See the description of Aff0 for more information.

Aff3 is not supported in AArch32 state.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bit [31]

Reserved, RES1.

## U, bit [30]

Indicates a Uniprocessor system, as distinct from PE 0 in a multiprocessor system.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| U   | Meaning                                       |
|-----|-----------------------------------------------|
| 0b0 | Processor is part of a multiprocessor system. |

Access to this field is RO.

## Bits [29:25]

Reserved, RES0.

## MT, bit [24]

Indicates whether the lowest level of affinity consists of logical PEs that are implemented using an interdependent approach, such as multithreading. See the description of Aff0 for more information about affinity levels.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MT   | Meaning                                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Performance of PEs with different affinity level 0 values, and the same values for affinity level 1 and higher, is largely independent. |
| 0b1  | Performance of PEs with different affinity level 0 values, and the same values for affinity level 1 and higher, is very interdependent. |

## Note

This field does not indicate that multithreading is implemented and does not indicate that PEs with different affinity level 0 values, and the same values for affinity level 1 and higher are implemented.

Access to this field is RO.

## Aff2, bits [23:16]

Affinity level 2. See the description of Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Aff1, bits [15:8]

Affinity level 1. See the description of Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Aff0, bits [7:0]

Affinity level 0. The value of the MPIDR.{Aff2, Aff1, Aff0} or MPIDR\_EL1.{Aff3, Aff2, Aff1, Aff0} set of fields of each PE must be unique within the system as a whole.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing MPIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

| U   | Meaning                                     |
|-----|---------------------------------------------|
| 0b1 | Processor is part of a uniprocessor system. |

MRS &lt;Xt&gt;, MPIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0000 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.MPIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() then X[t, 64] = VMPIDR_EL2; else X[t, 64] = MPIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = MPIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPIDR_EL1;
```