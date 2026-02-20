## F5.1.287 USAD8

Unsigned Sum of Absolute Differences

Unsigned Sum of Absolute Differences performs four unsigned 8-bit subtractions, and adds the absolute values of the differences together.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
USAD8{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if d == 15 || n == 15 || m == 15 then
```

T1

<!-- image -->

## Encoding

```
USAD8{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
UNPREDICTABLE;
```

## Assembler Symbols

&lt;c&gt; See Standard assembler syntax fields. &lt;q&gt; See Standard assembler syntax fields.

&lt;Rd&gt;

&lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer absdiff1 = Abs(UInt(R[n]<7:0>) -UInt(R[m]<7:0>)); constant integer absdiff2 = Abs(UInt(R[n]<15:8>) -UInt(R[m]<15:8>)); constant integer absdiff3 = Abs(UInt(R[n]<23:16>) UInt(R[m]<23:16>)); constant integer absdiff4 = Abs(UInt(R[n]<31:24>) UInt(R[m]<31:24>)); constant integer result = absdiff1 + absdiff2 + absdiff3 + absdiff4; R[d] = result<31:0>;
```

Is the general-purpose destination register, encoded in the 'Rd' field.