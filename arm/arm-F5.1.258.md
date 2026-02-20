## F5.1.258 TBB, TBH

Table Branch Byte or Halfword causes a PC-relative forward branch using a table of single byte or halfword offsets. A base register provides a pointer to the table, and a second register supplies an index into the table. The branch length is twice the value returned from the table.

<!-- image -->

## Encoding for the Byte variant

Applies when

```
(H == 0)
```

```
TBB{<c>}{<q>} [<Rn>, <Rm>] // (Outside or last in IT block)
```

## Encoding for the Halfword variant

```
Applies when (H == 1) TBH{<c>}{<q>} [<Rn>, <Rm>, LSL #1] // (Outside or last
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean is_tbh = (H == '1'); // Armv8-A removes UNPREDICTABLE for R13 if m == 15 then UNPREDICTABLE; if
```

```
InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

&lt;Rn&gt;

Is the general-purpose base register holding the address of the table of branch lengths, encoded in the 'Rn' field. The PC can be used. If it is, the table immediately follows this instruction.

## &lt;Rm&gt;

For the 'Byte' variant: is the general-purpose index register, encoded in the 'Rm' field. This register contains an integer pointing to a single byte in the table. The offset in the table is the value of the index.

For the 'Halfword' variant: is the general-purpose index register, encoded in the 'Rm' field. This register contains an integer pointing to a halfword in the table. The offset in the table is twice the value of the index.

```
in IT block)
```

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); integer halfwords; if is_tbh then halfwords = UInt(MemU[R[n]+LSL(R[m],1), 2]); else halfwords = UInt(MemU[R[n]+R[m], 1]); BranchWritePC(PC32 + 2*halfwords, BranchType_INDIR);
```