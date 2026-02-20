## F5.1.122 MSR (register)

Move general-purpose register to Special register moves selected bits of a general-purpose register to the APSR, CPSR or SPSR\_&lt;current\_mode&gt;.

Because of the Do-Not-Modify nature of its reserved bits, a read-modify-write sequence is normally required when the MSR instruction is being used at Application level and its destination is not APSR\_nzcvq ( CPSR\_f ).

If an MSR (register) moves selected bits of an immediate value to the CPSR, the PE checks whether the value being written to PSTATE.M is legal. See Illegal changes to PSTATE.M.

An MSR (register) executed in User mode:

- Is UNPREDICTABLE if it attempts to update the SPSR.
- Otherwise, does not update any CPSR field that is accessible only at EL1 or higher.

An MSR (register) executed in System mode is UNPREDICTABLE if it attempts to update the SPSR.

The CPSR.E bit is writable from any mode using an MSR instruction. Arm deprecates using this to change its value.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
MSR{<c>}{<q>} <spec_reg>, <Rn>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant boolean write_spsr = (R == '1'); if mask == '0000' then UNPREDICTABLE; if n == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If mask == '0000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

T1

<!-- image -->

## Encoding

```
MSR{<c>}{<q>} <spec_reg>, <Rn>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant boolean write_spsr = (R == '1'); if mask == '0000' then UNPREDICTABLE; // Armv8-A removes UNPREDICTABLE for R13 if n == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If mask == '0000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;spec\_reg&gt;

Is one of:

- APSR\_&lt;bits&gt; .
- CPSR\_&lt;fields&gt; .
- SPSR\_&lt;fields&gt; .

For CPSR and SPSR, &lt;fields&gt; is a sequence of one or more of the following:

- c mask&lt;0&gt; = '1' to enable writing of bits&lt;7:0&gt; of the destination PSR. x mask&lt;1&gt; = '1' to enable writing of bits&lt;15:8&gt; of the destination PSR. s mask&lt;2&gt; = '1' to enable writing of bits&lt;23:16&gt; of the destination PSR. f mask&lt;3&gt; = '1' to enable writing of bits&lt;31:24&gt; of the destination PSR.

For APSR, &lt;bits&gt; is one of nzcvq , g , or nzcvqg . These map to the following CPSR\_&lt;fields&gt; values:

- APSR\_nzcvq is the same as CPSR\_f (mask== '1000').
- APSR\_g is the same as CPSR\_s (mask == '0100').
- APSR\_nzcvqg is the same as CPSR\_fs (mask == '1100').

Arm recommends the APSR\_&lt;bits&gt; forms when only the N, Z, C, V , Q, and GE[3:0] bits are being written. For more information, see The Application Program Status Register, APSR.

Is the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if write_spsr then if PSTATE.M IN {M32_User,M32_System} then UNPREDICTABLE; else SPSRWriteByInstr(R[n], mask); else // Attempts to change to an illegal mode will invoke the Illegal Execution state mechanism CPSRWriteByInstr(R[n], mask);
```

<!-- image -->

## CONSTRAINED UNPREDICTABLE behavior

If write\_spsr &amp;&amp; PSTATE.M IN {M32\_User,M32\_System} , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .