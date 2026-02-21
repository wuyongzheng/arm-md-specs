## 6.3.160 SMMU\_R\_DPT\_CFG\_FAR

The SMMU\_R\_DPT\_CFG\_FAR characteristics are:

## Purpose

This register reports details of the Realm state Device Permission Table lookup error.

## Configuration

This register is present only when SMMU\_R\_IDR3.DPT == 1. Otherwise, direct accesses to SMMU\_R\_DPT\_CFG\_FAR are RES0.

## Attributes

SMMU\_R\_DPT\_CFG\_FAR is a 64-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## FADDR, bits [55:12]

The physical address input to the DPT check that caused the DPT lookup error.

If FAULT == 0, the value of this field is zero.

Access to this field is RO.

## Bits [11:8]

Reserved, RES0.

## DPT\_FAULTCODE, bits [7:4]

| DPT_FAULTCODE   | Meaning                                                 |
|-----------------|---------------------------------------------------------|
| 0b0000          | DPT_DISABLED SMMU_R_CR0.DPT_WALK_EN is zero.            |
| 0b0001          | DPT_WALK_FAULT Invalid DPT configuration or descriptor. |
| 0b0010          | DPT_GPC_FAULT GPC fault on DPT fetch.                   |
| 0b0011          | DPT_EABT External abort on DPT fetch.                   |

If FAULT == 0, the value of this field is zero.

Access to this field is RO.

## Bits [3:2]

Reserved, RES0.

## LEVEL, bit [1]

Reports the level of the fault.

| LEVEL   | Meaning   |
|---------|-----------|
| 0b0     | Level 0   |
| 0b1     | Level 1   |

If FAULT == 0, the value of this field is zero.

Access to this field is RO.

## FAULT, bit [0]

| FAULT   | Meaning                                                                                  |
|---------|------------------------------------------------------------------------------------------|
| 0b0     | There have been zero DPT lookup faults since this register was last cleared to 0.        |
| 0b1     | There have been one or more DPT lookup faults since this register was last cleared to 0. |

A write of one to this field is IGNORED and does not trigger an update of SMMU\_R\_GERROR, and does not make this fault active.

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

Note: If A DPT lookup resolves to an entry that marks 'No access', that is not a DPT lookup fault and it is not reported in this register.

See also:

- Section 3.24.4 DPT lookup errors .

## Accessing SMMU\_R\_DPT\_CFG\_FAR

This register is read-write, with the following constraints:

- Any write to this register is IGNORED unless the write clears the FAULT bit.
- When a write clears the FAULT bit, the entire register is cleared to zero.

Accesses to this register use the following encodings:

Accessible at offset 0x0210 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.