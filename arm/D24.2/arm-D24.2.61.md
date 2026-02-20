## D24.2.61 HAFGRTR\_EL2, Hypervisor Activity Monitors Fine-Grained Read Trap Register

The HAFGRTR\_EL2 characteristics are:

## Purpose

Provides controls for traps of MRS reads of Activity Monitors System registers.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_AMUv1 is implemented, FEAT\_FGT is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to HAFGRTR\_EL2 are UNDEFINED.

## Attributes

HAFGRTR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:50]

Reserved, RES0.

AMEVTYPER1&lt;x&gt;\_EL0 , bits [19+2x], for x = 15 to 0

Trap MRS reads of AMEVTYPER1&lt;x&gt;\_EL0 at EL1 and EL0 using AArch64 and MRC reads of AMEVTYPER1&lt;x&gt; at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| AMEVTYPER1<x>_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0                 | MRS reads of AMEVTYPER1<x>_EL0 at EL1 and EL0 using AArch64 and MRC reads of AMEVTYPER1<x> at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                |
| 0b1                 | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, EL1 is using AArch64, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then, unless the read generates a higher priority exception: • MRS reads of AMEVTYPER1<x>_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of AMEVTYPER1<x> at EL0 using AArch32 are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When x &gt;= UInt(AMCGCR\_EL0.CG1NC), access to this field is RES0.
- When !IsG1ActivityMonitorImplemented(x), access to this field is RES0.

## AMEVCNTR1&lt;x&gt;\_EL0 , bits [18+2x], for x = 15 to 0

Trap MRS reads of AMEVCNTR1&lt;x&gt;\_EL0 at EL1 and EL0 using AArch64 and MRC reads of AMEVCNTR1&lt;x&gt; at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| AMEVCNTR1<x>_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0                | MRS reads of AMEVCNTR1<x>_EL0 at EL1 and EL0 using AArch64 and MRC reads of AMEVCNTR1<x> at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                |
| 0b1                | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, EL1 is using AArch64, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then, unless the read generates a higher priority exception: • MRS reads of AMEVCNTR1<x>_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of AMEVCNTR1<x> at EL0 using AArch32 are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When x &gt;= UInt(AMCGCR\_EL0.CG1NC), access to this field is RES0.
- When !IsG1ActivityMonitorImplemented(x), access to this field is RES0.

## AMCNTEN&lt;x&gt;, bits [17x], for x = 1 to 0

Trap MRS reads and MRC reads of multiple System registers.

Enables a trap to EL2 the following operations:

- At EL1 and EL0 using AArch64: MRS reads of AMCNTENCLR\_EL0 and AMCNTENSET\_EL0.
- At EL0 using AArch32 when EL1 is using AArch64: MRC reads of AMCNTENCLR and AMCNTENSET.

| AMCNTEN<x>   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | The operations listed above are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 0b1          | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, EL1 is using AArch64, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then, unless the read generates a higher priority exception: • MRS reads at EL1 and EL0 using AArch64 of AMCNTENCLR_EL0 and AMCNTENSET_EL0 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads at EL0 using AArch32 of AMCNTENCLRand AMCNTENSETare trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [16:5]

Reserved, RES0.

## AMEVCNTR0&lt;x&gt;\_EL0 , bits [x+1], for x = 3 to 0

Trap MRS reads of AMEVCNTR0&lt;x&gt;\_EL0 at EL1 and EL0 using AArch64 and MRC reads of AMEVCNTR0&lt;x&gt; at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| AMEVCNTR0<x>_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0                | MRS reads of AMEVCNTR0<x>_EL0 at EL1 and EL0 using AArch64 and MRC reads of AMEVCNTR0<x> at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                |
| 0b1                | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, EL1 is using AArch64, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then, unless the read generates a higher priority exception: • MRS reads of AMEVCNTR0<x>_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of AMEVCNTR0<x> at EL0 using AArch32 are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

When x &gt;= 4, access to this field is RES0.

## Accessing HAFGRTR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HAFGRTR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_FGT) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x1E8]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HAFGRTR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HAFGRTR_EL2;
```

MSR HAFGRTR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_FGT) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x1E8] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else
```

```
UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HAFGRTR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HAFGRTR_EL2 = X[t, 64];
```