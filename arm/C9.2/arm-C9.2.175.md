## C9.2.175 MOV (vector to tile, single)

Move Z vector to ZA tile slice

This instruction operates on individual horizontal or vertical slices within a named ZA tile of the specified element size. The slice number within the tile is selected by the sum of the slice index register and immediate offset, modulo the number of such elements in a vector. The immediate offset is in the range 0 to the number of elements in a 128-bit vector segment minus 1. Inactive elements in the destination slice remain unmodified.

This is an alias of MOV A (vector to tile, single). This means:

- The encodings in this description are named to match the encodings of MOV A (vector to tile, single).
- The description of MOVA (vector to tile, single) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from 5 classes: 8-bit, 16-bit, 32-bit, 64-bit, and 128-bit

8-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 8-bit variant

```
MOV ZA0<HV>.B[<Ws>, <offs>], <Pg>/M, <Zn>.B
```

```
is equivalent to
```

```
MOVA ZA0<HV>.B[<Ws>, <offs>], <Pg>/M, <Zn>.B
```

and is always the preferred disassembly.

16-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 16-bit variant

```
MOV <ZAd><HV>.H[<Ws>, <offs>], <Pg>/M, <Zn>.H
```

```
is equivalent to MOVA <ZAd><HV>.H[<Ws>, <offs>], <Pg>/M, <Zn>.H
```

and is always the preferred disassembly.

32-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 32-bit variant

MOV

&lt;ZAd&gt;&lt;HV&gt;.S[&lt;Ws&gt;, &lt;offs&gt;],

## is equivalent to

```
MOVA <ZAd><HV>.S[<Ws>, <offs>], <Pg>/M, <Zn>.S
```

and is always the preferred disassembly.

64-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 64-bit variant

```
MOV <ZAd><HV>.D[<Ws>, <offs>], <Pg>/M, <Zn>.D
```

is equivalent to

MOVA

&lt;ZAd&gt;&lt;HV&gt;.D[&lt;Ws&gt;, &lt;offs&gt;], &lt;Pg&gt;/M, &lt;Zn&gt;.D

and is always the preferred disassembly.

128-bit

(FEAT\_SME)

<!-- image -->

## Encoding for the 128-bit variant

MOV

&lt;ZAd&gt;&lt;HV&gt;.Q[&lt;Ws&gt;, &lt;offs&gt;],

## is equivalent to

```
MOVA <ZAd><HV>.Q[<Ws>, <offs>], <Pg>/M, <Zn>.Q
```

and is always the preferred disassembly.

&lt;Pg&gt;/M,

&lt;Pg&gt;/M,

&lt;Zn&gt;.S

&lt;Zn&gt;.Q

## Assembler Symbols

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

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;Pg&gt;

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;ZAd&gt;

For the '16-bit' variant: is the name of the ZA tile ZA0-ZA1 to be accessed, encoded in the 'ZAd' field.

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3 to be accessed, encoded in the 'ZAd' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7 to be accessed, encoded in the 'ZAd' field.

For the '128-bit' variant: is the name of the ZA tile ZA0-ZA15 to be accessed, encoded in the 'ZAd' field.

## Operation

The description of MOVA (vector to tile, single) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOVA (vector to tile, single) gives the operational information for this instruction.