## 6.3.37 SMMU\_GATOS\_CTRL

The SMMU\_GATOS\_CTRL characteristics are:

## Purpose

Global ATOS translation control register.

## Configuration

This register is present only when SMMU\_IDR0.ATOS == 1. Otherwise, direct accesses to SMMU\_GATOS\_CTRL are RES0.

## Attributes

SMMU\_GATOS\_CTRL is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## RUN, bit [0]

Run ATOS translation.

- Software must write this bit to 1 to initiate the translation operation, after initializing the ATOS\_SID and ATOS\_ADDR registers.
- The SMMU clears the RUN flag after the translation completes and its result is visible in ATOS\_PAR.
- A write of 0 to this flag might change the value of the flag but has no other effect. Software must only write 0 to this flag when the flag is zero.

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

SMMU\_GATOS\_{CTRL, SID, ADDR, PAR} are only present if SMMU\_IDR0.ATOS == 1; otherwise, they are Reserved. See Chapter 9 Address Translation Operations for more information on the overall behavior of ATOS operations.

## Accessing SMMU\_GATOS\_CTRL

RUN is Guarded by SMMU\_CR0.SMMUEN and must only be set when SMMUEN == 1 and RUN == 0.

ATOS\_CTRL.RUN must not be set to 1 after SMMU\_CR0.SMMUEN has been written to 0, including at a point prior to the completion of an Update to SMMUEN.

In SMMUv3.1 and earlier, behavior of doing so is CONSTRAINED UNPREDICTABLE and one of the following occurs:

- The write is IGNORED.
- The value is stored and visible for readback, but no other effect occurs and RUN is not cleared by the SMMU unless SMMUEN is later Updated to 1.

In SMMUv3.2 and later, such a write is IGNORED

Between software writing ATOS\_CTRL.RUN == 1 and observing the SMMU having cleared it to 0 again:

- In SMMUv3.1 and earlier, writes to ATOS\_SID, ATOS\_ADDR and VATOS\_SEL (if appropriate) are CONSTRAINED UNPREDICTABLE and one of the following occurs:
- -The write is IGNORED.
- -Translation is performed with any value of the written register. After completion, ATOS\_PAR is UNKNOWN.

Note: HTTU might have been performed to an UNPREDICTABLE set of translation table descriptors that could otherwise have been updated using any given value of the written register.

- In SMMUv3.2 and later, writes to ATOS\_SID, ATOS\_ADDR and VATOS\_SEL (if appropriate) are IGNORED.
- In SMMUv3.1 and earlier, writes to ATOS\_CTRL are CONSTRAINED UNPREDICTABLE and one of the following occurs:
- -The write is IGNORED.
- -The value is stored and visible for readback, but translation is unaffected and completes normally. Note: If RUN == 0 was written, it is not possible to determine that the translation has completed.
- -Reads of ATOS\_PAR return UNKNOWN.
- In SMMUv3.2 and later, writes to ATOS\_CTRL are IGNORED.

The completion of an Update of SMMU\_CR0.SMMUEN from 1 to 0 while RUN == 1 is contingent on the completion of the ATOS operation, which clears RUN. Clearing SMMU\_CR0.SMMUEN while RUN == 1 is CONSTRAINED UNPREDICTABLE and the completion of the SMMUEN == 0 Update ensures one of the following behaviors:

- The operation has completed normally and a valid translation/fault response is reported.
- The ATOS operation has been aborted, reporting ATOS\_PAR.FAULT == 1 and ATOS\_PAR.FAULTCODE == INTERNAL\_ERR.
- -The translation table walks for the ongoing ATOS translation might have been partially performed. If HTTU was performed during the translation, an UNPREDICTABLE set of the translation table descriptors relevant to the translation table walks might have been updated.

An Update of SMMU\_CR0.SMMUEN from 0 to 1 clears RUN, if RUN was set while SMMU\_CR0.SMMUEN == 0. Completion of the Update occurs after RUN has been cleared for all Non-secure ATOS register groups.

The behavior specified here is consistent across all SMMU\_*ATOS\_* registers and their corresponding SMMUEN and ATOS\_CTRL.RUN bits.

Accesses to this register use the following encodings:

Accessible at offset 0x0100 from SMMUv3\_PAGE\_0

- When SMMU\_GATOS\_CTRL.RUN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.