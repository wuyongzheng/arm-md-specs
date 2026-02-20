## F5.1.54 HLT

Halting Breakpoint

Halting breakpoint causes a software breakpoint to occur.

Halting breakpoint is always unconditional, even inside an IT block.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

HLT{&lt;q&gt;}

{#}&lt;imm&gt;

## Decode for this encoding

```
if EDSCR.HDE == '0' || !HaltingAllowed() then UNDEFINED; end if cond != '1110' then UNPREDICTABLE; end // HLT must be encoded with AL
```

## CONSTRAINED UNPREDICTABLE behavior

If cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

T1

## Encoding

HLT{&lt;q&gt;} {#}&lt;imm&gt;

## Decode for this encoding

```
if EDSCR.HDE == '0' || !HaltingAllowed() then UNDEFINED; end
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

condition

Listing F5-43

<!-- image -->

Listing F5-44

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields. An HLT instruction must be unconditional.

## &lt;imm&gt;

For the 'A1' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm12:imm4' field. This value is for assembly and disassembly only. It is ignored by the PE, but can be used by a debugger to store more information about the halting breakpoint.

For the 'T1' variant: is a 6-bit unsigned immediate, in the range 0 to 63, encoded in the 'imm6' field. This value is for assembly and disassembly only. It is ignored by the PE, but can be used by a debugger to store more information about the halting breakpoint.

## Operation

EncodingSpecificOperations(); constant boolean is\_async = FALSE; constant FaultRecord fault = NoFault();

Halt(DebugHalt\_HaltInstruction, is\_async, fault);

Listing F5-45