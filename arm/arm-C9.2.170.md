## C9.2.170 MOV (tile to vector, single)

Move ZA tile slice to Z vector

This instruction operates on individual horizontal or vertical slices within a named ZA tile of the specified element size. The slice number within the tile is selected by the sum of the slice index register and immediate offset, modulo the number of such elements in a vector. The immediate offset is in the range 0 to the number of elements in a 128-bit vector segment minus 1. Inactive elements in the destination vector remain unmodified.

This is an alias of MOV A (tile to vector, single). This means:

- The encodings in this description are named to match the encodings of MOV A (tile to vector, single).
- The description of MOVA (tile to vector, single) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from 5 classes: 8-bit, 16-bit, 32-bit, 64-bit, and 128-bit

8-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 8-bit variant

```
MOV <Zd>.B, <Pg>/M, ZA0<HV>.B[<Ws>, <offs>]
```

## is equivalent to

```
MOVA <Zd>.B, <Pg>/M, ZA0<HV>.B[<Ws>, <offs>]
```

and is always the preferred disassembly.

16-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 16-bit variant

```
MOV <Zd>.H, <Pg>/M, <ZAn><HV>.H[<Ws>, <offs>]
```

## is equivalent to

```
MOVA <Zd>.H, <Pg>/M, <ZAn><HV>.H[<Ws>, <offs>]
```

and is always the preferred disassembly.

32-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 32-bit variant

```
MOV <Zd>.S, <Pg>/M, <ZAn><HV>.S[<Ws>, <offs>]
```

## is equivalent to

```
MOVA <Zd>.S, <Pg>/M, <ZAn><HV>.S[<Ws>, <offs>]
```

and is always the preferred disassembly.

64-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 64-bit variant

```
MOV <Zd>.D, <Pg>/M, <ZAn><HV>.D[<Ws>, <offs>]
```

## is equivalent to

```
MOVA <Zd>.D, <Pg>/M, <ZAn><HV>.D[<Ws>, <offs>]
```

and is always the preferred disassembly.

128-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 128-bit variant

MOV

&lt;Zd&gt;.Q, &lt;Pg&gt;/M, &lt;ZAn&gt;&lt;HV&gt;.Q[&lt;Ws&gt;, &lt;offs&gt;]

## is equivalent to

```
MOVA <Zd>.Q, <Pg>/M, <ZAn><HV>.Q[<Ws>, <offs>]
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Pg&gt;

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;HV&gt;

Is the horizontal or vertical slice indicator, encoded in 'V':

|   V | <HV>   |
|-----|--------|
|   0 | H      |
|   1 | V      |

## &lt;Ws&gt;

Is the 32-bit name of the slice index register W12-W15, encoded in the 'Rs' field.

## &lt;offs&gt;

For the '8-bit' variant: is the slice index offset, in the range 0 to 15, encoded in the 'off4' field.

For the '16-bit' variant: is the slice index offset, in the range 0 to 7, encoded in the 'off3' field.

For the '32-bit' variant: is the slice index offset, in the range 0 to 3, encoded in the 'off2' field.

For the '64-bit' variant: is the slice index offset, in the range 0 to 1, encoded in the 'o1' field.

For the '128-bit' variant: is the slice index offset, with implicit value 0.

## &lt;ZAn&gt;

For the '16-bit' variant: is the name of the ZA tile ZA0-ZA1 to be accessed, encoded in the 'ZAn' field.

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3 to be accessed, encoded in the 'ZAn' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7 to be accessed, encoded in the 'ZAn' field.

For the '128-bit' variant: is the name of the ZA tile ZA0-ZA15 to be accessed, encoded in the 'ZAn' field.

## Operation

The description of MOVA (tile to vector, single) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOVA (tile to vector, single) gives the operational information for this instruction.