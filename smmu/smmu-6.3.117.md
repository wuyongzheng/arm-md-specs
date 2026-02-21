## 6.3.117 SMMU\_ROOT\_GPT\_CFG\_FAR

The SMMU\_ROOT\_GPT\_CFG\_FAR characteristics are:

## Purpose

Reports details of the originating access that experienced a GPT lookup error.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ROOT\_GPT\_CFG\_FAR is a 64-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

## FPAS, bits [63:62]

The physical address space of the access that failed.

| FPAS   | Meaning    |
|--------|------------|
| 0b00   | Secure     |
| 0b01   | Non-secure |
| 0b10   | Root       |
| 0b11   | Realm      |

If FAULT == 0, the value of this field is 0b00 .

Note: The encoding for Root is only applicable for NoStreamID devices.

Access to this field is RO.

## Bits [61:60]

Reserved, RES0.

## CFG\_ERR, bits [59:56]

| Value   | Meaning                                                                                                                                                                       |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0     | Invalid configuration of GPT configuration registers. This corresponds to GPT walk fault at Level 0 arising from invalid configuration of GPCCR_EL3 in the RME specification. |
| 0x1     | SMMU_ROOT_GPT_BASE.ADDR exceeds the address size configured in SMMU_ROOT_GPT_BASE_CFG.PPS. This corresponds to GPT address size fault at Level 0 in the RME specification.    |

| Value   | Meaning                                                                                                                                                                            |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x2     | External abort on GPT entry fetch. This corresponds to Synchronous External abort on GPT fetch in the RME specification.                                                           |
| 0x3     | Invalid configuration of GPT entry. This corresponds to GPT walk fault arising from an invalid GPT entry in the RME specification.                                                 |
| 0x4     | Next-level address in GPT entry exceeds the address size configured in SMMU_ROOT_GPT_BASE_CFG.PPS. This corresponds to GPT address size fault at Level 0 in the RME specification. |

If FAULT == 0, the value of this field is 0x0 .

Access to this field is RO.

## FADDR, bits [55:12]

The physical address input to the Granule Protection Check that failed.

If FAULT == 0, the value of this field is zero.

Access to this field is RO.

## FAULTCODE, bits [11:4]

If REASON == TRANSACTION, then the value of this field is zero.

If REASON == TRANSLATION, then:

| Value   | Name          | Meaning                                  |
|---------|---------------|------------------------------------------|
| 0x03    | GPF_STE_FETCH | STE fetch experienced GPF                |
| 0x09    | GPF_CD_FETCH  | CD fetch experienced GPF                 |
| 0x0B    | GPF_WALK_EABT | Translation table access experienced GPF |
| 0x25    | GPF_VMS_FETCH | VMS fetch experienced GPF                |

## If REASON == GERROR, then:

| Value   | Name           | Meaning                                              |
|---------|----------------|------------------------------------------------------|
| 0x00    | CMDQ_GPF       | Command queue read experienced a GPF                 |
| 0x02    | EVENTQ_GPF     | Event queue write experienced a GPF                  |
| 0x03    | PRIQ_GPF       | PRI queue write experienced a GPF                    |
| 0x04    | MSI_CMDQ_GPF   | Command queue MSI experienced a GPF                  |
| 0x05    | MSI_EVENTQ_GPF | Event queue MSI experienced a GPF                    |
| 0x06    | MSI_PRIQ_GPF   | PRI queue MSI experienced a GPF                      |
| 0x07    | MSI_GERROR_GPF | GERROR reporting MSI experienced a GPF               |
| 0x10    | OTHER_GPF      | An unknown SMMU-originated access experienced a GPF. |

If FAULT == 0, the value of this field is 0x00 .

Access to this field is RO.

## REASON, bits [3:1]

Reports the originator of the access.

| REASON   | Meaning                                                                                     |
|----------|---------------------------------------------------------------------------------------------|
| 0b001    | TRANSLATION, GPF on an SMMU-originated access required for translation of a client request. |
| 0b010    | GERROR, GPF on an SMMU-originated access not relating to a client translation.              |
| 0b011    | TRANSACTION, GPF on the output address of a client translation.                             |

If FAULT == 0, the value of this field is 0b000 .

Access to this field is RO.

## FAULT, bit [0]

| FAULT   | Meaning                                                                                  |
|---------|------------------------------------------------------------------------------------------|
| 0b0     | There have been zero GPT lookup errors since this register was last cleared to 0.        |
| 0b1     | There have been one or more GPT lookup errors since this register was last cleared to 0. |

A write of 1 to this bit is IGNORED, does not trigger the GPT\_CFG\_FAR interrupt, and does not make this fault active.

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

It is IMPLEMENTATION DEFINED which of the following encodings is used to report GPFs on MSI accesses from a PMCG or a RAS record interrupt:

- REASON = GERROR and FAULTCODE = OTHER\_GPF
- REASON = TRANSACTION

## Accessing SMMU\_ROOT\_GPT\_CFG\_FAR

All writes to this register are IGNORED unless the write clears the FAULT bit.

When a write clears the FAULT bit, the whole register is cleared to zero.

Accesses to this register use the following encodings:

Accessible at offset 0x0040 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.