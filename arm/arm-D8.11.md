## D8.11 Checked Pointer Arithmetic

RQRKMW

ILYNBW

All statements in this section require implementation of FEAT\_CPA.

It is possible that bits[63:56] of the V A might be modified in an attempt to circumvent features using these bits, including but not limited to:

- Memory Tagging Extensions (MTE). See The Memory Tagging Extension.
- Pointer Authentication Codes (PAC). See Pointer authentication.
- Software only schemes using address tag bits. See Address tagging and Logical Address Tagging.

## IKCTBC Checked Pointer Arithmetic has all of the following properties:

- It is independent of the value of bits[63:56] of the V A.
- It is independent of the use case of bits[63:56] of the V A.
- It is independent of whether address tagging is enabled by TCR\_ELx.TBI.
- If Checked Pointer Arithmetic for Multiplication is enabled, all of the following:
- -Arecorded attempted modification of bits[63:56] of the V A is preserved by a pointer arithmetic instruction.
- -Arecorded multiply overflow is preserved by a pointer arithmetic instruction.

If an instruction has all of the following, it is a Checked Pointer Arithmetic instruction:

- An Explicit Memory effect.
- An explicit base address register operand.
- One or more explicit transfer register operands containing data elements that are loaded from or stored to corresponding addressed memory locations.

## IYVGDD All of the following are not Checked Pointer Arithmetic instructions:

- LDR (literal) , because it implicitly uses the PC and does not have an explicit base address register operand.
- System register accesses by MRS , MRRS , MSR , and MSSR instructions that are transformed into memory accesses by the Effective value of HCR\_EL2.NV2, because they implicitly use VNCR\_EL2 and do not have an explicit base address register operand.
- System instructions such as DC and IC , because they do not have an explicit transfer register operand.
- Memory Copy and Memory Set instructions introduced by FEAT\_MOPS, because they do not have a transfer register operand that is loaded from or stored to a corresponding addressed memory location.

## RLHJPP FEAT\_CPA introduces all of the following Checked Pointer Arithmetic instructions:

- The scalar instructions ADDPT , SUBPT , MADDPT , and MSUBPT .
- The SVE instructions ADDPT , SUBPT , MADPT , and MLAPT .

If FEAT\_CPA2 is implemented, the Checked Pointer Arithmetic instructions are controlled by the following register fields:

- SCTLR2\_EL1.{CPTM0, CPTM, CPTA0, CPTA}.
- SCTLR2\_EL2.{CPTM0, CPTM, CPTA0, CPTA}.
- SCTLR2\_EL3.{CPTM, CPTA}.

Note

If an unprivileged Checked Pointer Arithmetic instruction, such as LDTR or STTR , behaves as if the instruction was executed at EL0, then it is subject to the effects of SCTLR2\_ELx.CPTA0. Other tag preserving pointer instructions, such as ADDPT and MADDPT , are subject to the effects of SCTLR2\_ELx.CPTA.

For Checked Pointer Arithmetic instructions, if Checked Pointer Arithmetic for Addition is enabled, then all of the following apply:

- Bits[63:56] from the base register are preserved in the result.
- If bits[55:54] of the base register are 0b10 or 0b01 then bits[55:54] of the base register are preserved in the result.
- If bits[55:54] of the base register are 0b11 or 0b00 and the operation would have modified bits[63:56] from the base register when computing the result, then bit[55] of the result is set to bit[55] of the base register and bit[54] of the result is set to NOT (bit[55]) of the base register.

RTHDQL

ILWVFP

RXCDRZ

## The AArch64 Virtual Memory System Architecture D8.11 Checked Pointer Arithmetic

RGTPHB

For a pointer arithmetic instruction, a multiply overflow is defined as the expression

product&lt;127:0&gt; != SignExtend(product&lt;63:0&gt;, 128);

where

integer product = SInt(multiplicand1) * SInt(multiplicand2);

where each multiplicand is a 64 bit number.

RSJZHH

For Checked Pointer Arithmetic instructions, if Checked Pointer Arithmetic for Multiplication is enabled, then the

following applies:

- If bits[55:54] of the base register are 0b11 or 0b00 and a multiply overflow is detected, then bit[55] of the result is set to bit[55] of the base register and bit[54] of the result is set to NOT (bit[55]) of the base register.

RWQDKJ

Predicting the results of comparing base[63:56] with result[63:56] and of comparing base[55] with base[54] is a form of control flow prediction.

Note

Categorizing the prediction of comparing base[63:56] with result[63:56] and of comparing base[55] with base[54] as a form of control flow prediction means that the speculation is not restricted by CSDB. Treating this as control flow prediction is consistent with predicting MTE tag check failures, which are also classified as control flow prediction.

RTSFPY

When a Checked Pointer Arithmetic instruction accesses a sequential set of bytes that crosses the 0xXXFF\_FFFF\_FFFF\_FFFF boundary, it is CONSTRAINED UNPREDICTABLE whether Checked Pointer Arithmetic is applied to the V A accessed for the bytes above this boundary.

RQVJHR

If Checked Pointer Arithmetic is not enabled, then Checked Pointer Arithmetic instructions add the offset value to the base register value without checking bits[63:56] and without any special handling of bits[55:54].

- IJKJWP An operation that corrupts bits[63:56] results in a pointer with bit[55] != bit[54], which implies the following:

- Consumption of the pointer by a PAC insertion instruction inserts an invalid PAC as FEAT\_PAuth requires the pointer to be canonical.

- If the MMU is enabled, then consumption of the pointer by address translation likely generates a Translation fault.

- If the MMU is disabled, then consumption of the pointer by address translation likely generates a Address Size fault.

IQDPCR

Use of Checked Pointer Arithmetic requires a V A size less than or equal to 54 bits. This corresponds to a TCR\_ELx.TnSZ field value of 10 or greater.

If FEAT\_CPA2 and FEAT\_LVA3 are implemented, Checked Pointer Arithmetic is enabled, and the VA size is greater than 54 bits, then Checked Pointer Arithmetic will corrupt legitimate pointers.