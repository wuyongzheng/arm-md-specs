## F5.1.27 BX

Branch and Exchange causes a branch to an address and instruction set specified by a register.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
BX{<c>}{<q>} <Rm>
```

## Decode for this encoding

```
constant integer m = UInt(Rm);
```

T1

## Encoding

```
BX{<c>}{<q>} <Rm>
```

## Decode for this encoding

```
constant integer m = UInt(Rm); if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;Rm&gt;

For the 'A1' variant: is the general-purpose register holding the address to be branched to, encoded in the 'Rm' field. The PC can be used.

For the 'T1' variant: is the general-purpose register holding the address to be branched to, encoded in the 'Rm' field. The PC can be used.

<!-- image -->

Note

If &lt;Rm&gt; is the PC at a non word-aligned address, it results in UNPREDICTABLE behavior because the address passed to the BXWritePC() pseudocode function has bits&lt;1:0&gt; = '10'.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); BXWritePC(R[m], BranchType_INDIR);
```