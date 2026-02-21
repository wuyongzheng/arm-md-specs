## 6.3.100 SMMU\_VATOS\_SID

The SMMU\_VATOS\_SID characteristics are:

## Purpose

VATOS StreamID register.

## Configuration

This register is present only when SMMU\_IDR0.VATOS == 1. Otherwise, direct accesses to SMMU\_VATOS\_SID are RES0.

## Attributes

SMMU\_VATOS\_SID is a 64-bit register.

This register is part of the SMMUv3\_VATOS block.

## Field descriptions

<!-- image -->

This register has a similar encoding and behavior to SMMU\_GATOS\_SID, except it applies to the Virtual ATOS interface. See Chapter 9 Address Translation Operations for details.

## Bits [63:53]

Reserved, RES0.

## SSID\_VALID, bit [52]

## When SMMU\_IDR1.SSIDSIZE != 0:

SubstreamID valid.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SUBSTREAMID, bits [51:32]

SubstreamID of request.

- If SMMU\_IDR1.SSIDSIZE &lt; 20, bits [51:(32 + SMMU\_IDR1.SSIDSIZE)] are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## STREAMID, bits [31:0]

StreamID of request.

- This is written with the StreamID (used to locate translations/CDs) of the request later submitted to SMMU\_VATOS\_ADDR.
- If SMMU\_IDR1.SID\_SIZE &lt; 32, bits [31:SMMU\_IDR1.SID\_SIZE] are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

- Bits of SubstreamID and StreamID outside of the supported range are RES0.

## Accessing SMMU\_VATOS\_SID

This register is Guarded by SMMU\_VATOS\_CTRL.RUN and must only be altered when RUN == 0.

See SMMU\_GATOS\_CTRL for more detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x0A08 from SMMUv3\_VATOS

- When SMMU\_VATOS\_CTRL.RUN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.