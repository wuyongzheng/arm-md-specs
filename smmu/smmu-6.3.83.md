## 6.3.83 SMMU\_S\_GATOS\_CTRL

The SMMU\_S\_GATOS\_CTRL characteristics are:

## Purpose

Secure Global ATOS translation control register.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1 and SMMU\_IDR0.ATOS == 1. Otherwise, direct accesses to SMMU\_S\_GATOS\_CTRL are RES0.

## Attributes

SMMU\_S\_GATOS\_CTRL is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## RUN, bit [0]

Run ATOS translation.

- Arm recommends that software writes this bit to 1 to initiate the translation operation, after initializing the ATOS\_SID and ATOS\_ADDR registers.
- The SMMU clears the RUN flag after the translation completes and its result is visible in ATOS\_PAR.
- A write of 0 to this flag might change the value of the flag but has no other effect. Software must only write 0 to this flag when the flag is zero.

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

See Chapter 9 Address Translation Operations for more information on the overall behavior of ATOS operations.

## Accessing SMMU\_S\_GATOS\_CTRL

RUN is Guarded by SMMU\_S\_CR0.SMMUEN and must only be set when SMMUEN == 1 and RUN == 0.

See SMMU\_GATOS\_CTRL for more detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x8100 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_GATOS\_CTRL.RUN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.