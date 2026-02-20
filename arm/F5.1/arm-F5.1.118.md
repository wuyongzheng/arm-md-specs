## F5.1.118 MRS

Move Special register to general-purpose register moves the value of the APSR, CPSR, or SPSR\_&lt;current\_mode&gt; into a general-purpose register.

Arm recommends the APSR form when only the N, Z, C, V , Q, and GE[3:0] bits are being written. For more information, see APSR.

An MRS that accesses the SPSRs is UNPREDICTABLE if executed in User mode or System mode.

An MRS that is executed in User mode and accesses the CPSR returns an UNKNOWN value for the CPSR.{E, A, I, F, M} fields.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
MRS{<c>}{<q>} <Rd>, <spec_reg>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant boolean read_spsr = (R == '1'); if d == 15 then UNPREDICTABLE; end
```

T1

<!-- image -->

## Encoding

```
MRS{<c>}{<q>} <Rd>, <spec_reg>
```

## Decode for this encoding

```
= (R == '1'); for R13
```

```
constant integer d = UInt(Rd); constant boolean read_spsr // Armv8-A removes UNPREDICTABLE if d == 15 then UNPREDICTABLE; end
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Listing F5-52

Listing F5-53

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;spec\_reg&gt;

Is the special register to be accessed, encoded in 'R':

|   R | <spec_reg>     |
|-----|----------------|
|   0 | CPSR&#124;APSR |
|   1 | SPSR           |

Listing F5-54

```
if ConditionPassed() then EncodingSpecificOperations(); if read_spsr then if PSTATE.M IN {M32_User,M32_System} then UNPREDICTABLE; else R[d] = SPSR_curr[]; end else // CPSR has same bit assignments as SPSR, but with the IT, J, SS, IL, and T bits masked out. constant bits(32) maskval = '11111000 11101111 00000011 11011111'; bits(32) psr_val = GetPSRFromPSTATE(AArch32_NonDebugState, 32) AND maskval; if PSTATE.EL == EL0 then // If accessed from User mode return UNKNOWN values for E, A, I, F bits, bits<9:6>, // and for the M field, bits<4:0> psr_val<22> = bits(1) UNKNOWN; psr_val<9:6> = bits(4) UNKNOWN; psr_val<4:0> = bits(5) UNKNOWN; end R[d] = psr_val; end end
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.M IN {M32\_User, M32\_System} &amp;&amp; read\_spsr , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

## Operation