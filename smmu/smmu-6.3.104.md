## 6.3.104 SMMU\_S\_VATOS\_SID

The SMMU\_S\_VATOS\_SID characteristics are:

## Purpose

Secure VATOS StreamID register.

## Configuration

This register is present only when SMMU\_IDR0.VATOS == 1 and SMMU\_S\_IDR1.SEL2 == 1. Otherwise, direct accesses to SMMU\_S\_VATOS\_SID are RES0.

## Attributes

SMMU\_S\_VATOS\_SID is a 64-bit register.

This register is part of the SMMUv3\_S\_VATOS block.

## Field descriptions

<!-- image -->

This register is encoded in a similar way to SMMU\_S\_GATOS\_SID, except it applies to the Secure Virtual ATOS interface. See Chapter 9 Address Translation Operations for details.

- Bit [53] is RES1 and the SMMU\_S\_VATOS\_SID.STREAMID field is taken as a Secure StreamID.

Note: The Secure VATOS interface does not support ATOS requests for Non-secure StreamIDs because SMMU\_S\_VATOS\_SEL checks that an STE.S2VMID field matches the secure VMID in SMMU\_S\_VATOS\_SEL.

## Bits [63:54]

Reserved, RES0.

## Bit [53]

Reserved, RES1.

## SSID\_VALID, bit [52]

## When SMMU\_IDR1.SSIDSIZE != 0:

SubstreamID valid.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SUBSTREAMID, bits [51:32]

SubstreamID of request.

- If SMMU\_IDR1.SSIDSIZE &lt; 20, bits [51:32 + SMMU\_IDR1.SSIDSIZE] are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## STREAMID, bits [31:0]

Secure StreamID of request.

- This is written with the StreamID (used to locate translations/CDs) of the request later submitted to SMMU\_S\_VATOS\_ADDR.
- If SMMU\_IDR1.SID\_SIZE &lt; 32 and SMMU\_S\_IDR1.S\_SIDSIZE &lt; 32, bits [31:MAX(SMMU\_IDR1.SIDSIZE, SMMU\_S\_IDR1.S\_SIDSIZE)] are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

Bits of SUBSTREAMID and STREAMID outside of the supported range are RES0.

## Accessing SMMU\_S\_VATOS\_SID

This register is Guarded by SMMU\_S\_VATOS\_CTRL.RUN and must only be altered when RUN == 0.

See SMMU\_GATOS\_CTRL for more detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x0A08 from SMMUv3\_S\_VATOS

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_VATOS\_CTRL.RUN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.