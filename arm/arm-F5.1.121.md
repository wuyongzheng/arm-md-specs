## F5.1.121 MSR (immediate)

Move immediate value to Special register moves selected bits of an immediate value to the corresponding bits in the APSR, CPSR, or SPSR\_&lt;current\_mode&gt;.

Because of the Do-Not-Modify nature of its reserved bits, the immediate form of MSR is normally only useful at the Application level for writing to APSR\_nzcvq ( CPSR\_f ).

If an MSR (immediate) moves selected bits of an immediate value to the CPSR, the PE checks whether the value being written to PSTATE.M is legal. See Illegal changes to PSTATE.M.

An MSR (immediate) executed in User mode:

- Is CONSTRAINED UNPREDICTABLE if it attempts to update the SPSR.
- Otherwise, does not update any CPSR field that is accessible only at EL1 or higher,

An MSR (immediate) executed in System mode is CONSTRAINED UNPREDICTABLE if it attempts to update the SPSR.

The CPSR.E bit is writable from any mode using an MSR instruction. Arm deprecates using this to change its value.

<!-- image -->

## Encoding

Applies when (!(R == 0 &amp;&amp; mask ==

```
MSR{<c>}{<q>}
```

```
0000))
```

```
<spec_reg>, #<imm>
```

## Decode for this encoding

```
SEE "Related encodings";
```

```
if mask == '0000' && R == '0' then constant bits(32) imm32 = A32ExpandImm(imm12); constant boolean write_spsr = (R == '1'); if mask == '0000' then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If mask == '0000' &amp;&amp; R == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Related encodings: Move Special Register and Hints (immediate).

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;spec\_reg&gt;

Is one of:

- APSR\_&lt;bits&gt; .
- CPSR\_&lt;fields&gt; .
- SPSR\_&lt;fields&gt; .

For CPSR and SPSR, &lt;fields&gt; is a sequence of one or more of the following:

```
c mask<0> = '1' to enable writing of bits<7:0> of the destination PSR. x mask<1> = '1' to enable writing of bits<15:8> of the destination PSR. s mask<2> = '1' to enable writing of bits<23:16> of the destination PSR. f mask<3> = '1' to enable writing of bits<31:24> of the destination PSR.
```

For APSR, &lt;bits&gt; is one of nzcvq , g , or nzcvqg . These map to the following CPSR\_&lt;fields&gt; values:

- APSR\_nzcvq is the same as CPSR\_f (mask== '1000').
- APSR\_g is the same as CPSR\_s (mask == '0100').
- APSR\_nzcvqg is the same as CPSR\_fs (mask == '1100').

Arm recommends the APSR\_&lt;bits&gt; forms when only the N, Z, C, V , Q, and GE[3:0] bits are being written. For more information, see The Application Program Status Register, APSR.

## &lt;imm&gt;

Is an immediate value. See Modified immediate constants in A32 instructions for the range of values.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if write_spsr then if PSTATE.M IN {M32_User,M32_System} then UNPREDICTABLE; else SPSRWriteByInstr(imm32, mask); else // Attempts to change to an illegal mode will invoke the Illegal Execution state mechanism CPSRWriteByInstr(imm32, mask);
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.M IN {M32\_User,M32\_System} &amp;&amp; write\_spsr , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .