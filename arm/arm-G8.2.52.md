## G8.2.52 ELR\_hyp, Exception Link Register (Hyp mode)

The ELR\_hyp characteristics are:

## Purpose

When taking an exception to Hyp mode, holds the address to return to.

## Configuration

AArch32 System register ELR\_hyp bits [31:0] are architecturally mapped to AArch64 System register ELR\_EL2[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to ELR\_hyp are UNDEFINED.

## Attributes

ELR\_hyp is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## ADDR, bits [31:0]

Return address.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ELR\_hyp

ELR\_hyp is accessible only at Hyp mode and Monitor mode.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| R   | M   | M1     |
|-----|-----|--------|
| 0b0 | 0b1 | 0b1110 |

MSR{&lt;c&gt;}{&lt;q&gt;} ELR\_hyp, &lt;Rn&gt;

| R   | M M1       |
|-----|------------|
| 0b0 | 0b1 0b1110 |