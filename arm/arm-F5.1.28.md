## F5.1.28 BXJ

Branch and Exchange, previously Branch and Exchange Jazelle.

BXJ behaves as a BX instruction, see BX. This means it causes a branch to an address and instruction set specified by a register.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
BXJ{<c>}{<q>} <Rm>
```

## Decode for this encoding

```
constant integer m = UInt(Rm); if m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
BXJ{<c>}{<q>} <Rm>
```

## Decode for this encoding

```
constant integer m = UInt(Rm); // Armv8-A removes UNPREDICTABLE for R13 if m == 15 then UNPREDICTABLE; if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

&lt;Rm&gt;

Is the general-purpose register holding the address to be branched to, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); BXWritePC(R[m],
```

```
BranchType_INDIR);
```