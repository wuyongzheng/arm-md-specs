## 6.3.90 SMMU\_S\_VATOS\_SEL

The SMMU\_S\_VATOS\_SEL characteristics are:

## Purpose

Secure VATOS VMID selection.

## Configuration

This register is present only when SMMU\_IDR0.VATOS == 1 and SMMU\_S\_IDR1.SEL2 == 1. Otherwise, direct accesses to SMMU\_S\_VATOS\_SEL are RES0.

## Attributes

SMMU\_S\_VATOS\_SEL is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

When requests are made through VATOS, this field is compared to the S2VMID field of the STE selected in the request. The request is denied if the STE configuration means that translations are not tagged with a VMID, or the VMID values do not match (indicating a lookup for a StreamID not assigned to the VM that has been granted access to the V ATOS interface). See section 9.1.6 SMMU\_(S\_)VATOS\_SEL .

Note: The Secure VATOS interface does not support ATOS requests for Non-secure StreamIDs because SMMU\_S\_VATOS\_SEL checks that an STE.S2VMID field matches the secure VMID in SMMU\_S\_VATOS\_SEL.

## Bits [31:16]

Reserved, RES0.

## VMID, bits [15:0]

VMID associated with the VM that is using the VATOS interface.

- When SMMU\_IDR0.VMID16 == 0, bits [15:8] of this field are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

This register is similar to SMMU\_VATOS\_SEL, but configures a Secure VMID to associate with the Secure VATOS interface.

## Accessing SMMU\_S\_VATOS\_SEL

This register is Guarded by SMMU\_S\_VATOS\_CTRL.RUN and must only be altered when RUN == 0.

See SMMU\_GATOS\_CTRL for more detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x8180 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_VATOS\_CTRL.RUN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.