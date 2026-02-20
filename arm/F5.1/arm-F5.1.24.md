## F5.1.24 BKPT

Breakpoint causes a Breakpoint Instruction exception.

Breakpoint is always unconditional, even when inside an IT block.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

BKPT{&lt;q&gt;}

{#}&lt;imm&gt;

## Decode for this encoding

```
constant bits(16) imm16 = imm12:imm4; if cond != '1110' then UNPREDICTABLE; end // BKPT must be encoded with
```

## CONSTRAINED UNPREDICTABLE behavior

If cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

T1

## Encoding

BKPT{&lt;q&gt;}

{#}&lt;imm&gt;

## Decode for this encoding

```
constant bits(16) imm16 = ZeroExtend(imm8, 16);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
AL condition
```

Listing F5-7

<!-- image -->

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields. A BKPT instruction must be unconditional.

## &lt;imm&gt;

For the 'A1' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm12:imm4' field. This value:

- Is recorded in the Comment field of ESR\_ELx.ISS if the Software Breakpoint Instruction exception is taken to an exception level that is using AArch64.
- Is ignored otherwise.

For the 'T1' variant: is a 8-bit unsigned immediate, in the range 0 to 255, encoded in the 'imm8' field. This value:

- Is recorded in the Comment field of ESR\_ELx.ISS if the Software Breakpoint Instruction exception is taken to an exception level that is using AArch64.
- Is ignored otherwise.

## Operation

EncodingSpecificOperations();

AArch32.SoftwareBreakpoint(imm16);