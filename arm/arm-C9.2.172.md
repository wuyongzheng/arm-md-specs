## C9.2.172 MOV (vector to tile, four registers)

Move Z four-vector operand to ZA four-slice operand

This instruction operates on a horizontal or vertical ZA four-slice operand within a ZA tile of the specified element size.

The first slice of the four-slice operand is selected by rounding down the sum of the slice index register and the immediate offset to the nearest lower multiple of 4, modulo the number of slices in the tile.

The immediate offset is a multiple of 4 in the range 0 to the number of elements in a 128-bit vector segment minus 4.

This instruction is unpredicated.

This is an alias of MOV A (vector to tile, four registers). This means:

- The encodings in this description are named to match the encodings of MOV A (vector to tile, four registers).
- The description of MOVA (vector to tile, four registers) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from 4 classes: 8-bit, 16-bit, 32-bit, and 64-bit

## 8-bit

(FEAT\_SME2)

<!-- image -->

## Encoding for the 8-bit variant

```
MOV ZA0<HV>.B[<Ws>, <offs1>:<offs4>], { <Zn1>.B-<Zn4>.B } is equivalent to MOVA ZA0<HV>.B[<Ws>, <offs1>:<offs4>], { <Zn1>.B-<Zn4>.B }
```

and is always the preferred disassembly.

## 16-bit

(FEAT\_SME2)

<!-- image -->

## Encoding for the 16-bit variant

```
MOV <ZAd><HV>.H[<Ws>, <offs1>:<offs4>], { <Zn1>.H-<Zn4>.H }
```

## is equivalent to

```
MOVA <ZAd><HV>.H[<Ws>, <offs1>:<offs4>], { <Zn1>.H-<Zn4>.H }
```

and is always the preferred disassembly.

## 32-bit

(FEAT\_SME2)

<!-- image -->

## Encoding for the 32-bit variant

```
MOV <ZAd><HV>.S[<Ws>, <offs1>:<offs4>], { <Zn1>.S-<Zn4>.S } is equivalent to MOVA <ZAd><HV>.S[<Ws>, <offs1>:<offs4>], { <Zn1>.S-<Zn4>.S }
```

and is always the preferred disassembly.

64-bit

(FEAT\_SME2)

<!-- image -->

## Encoding for the 64-bit variant

```
MOV <ZAd><HV>.D[<Ws>, <offs1>:<offs4>], { <Zn1>.D-<Zn4>.D }
```

## is equivalent to

```
MOVA <ZAd><HV>.D[<Ws>, <offs1>:<offs4>], { <Zn1>.D-<Zn4>.D }
```

and is always the preferred disassembly.

## Assembler Symbols

&lt;HV&gt;

Is the horizontal or vertical slice indicator, encoded in 'V':

|   V | <HV>   |
|-----|--------|
|   0 | H      |
|   1 | V      |

<!-- image -->

&lt;Ws&gt;

Is the 32-bit name of the slice index register W12-W15, encoded in the 'Rs' field.

## &lt;offs1&gt;

For the '8-bit' variant: is the first slice index offset, encoded as 'off2' field times 4.

For the '16-bit' variant: is the first slice index offset, encoded as 'o1' field times 4.

For the '32-bit' and '64-bit' variants: is the first slice index offset, with implicit value 0.

## &lt;offs4&gt;

For the '8-bit' variant: is the fourth slice index offset, encoded as 'off2' field times 4 plus 3.

For the '16-bit' variant: is the fourth slice index offset, encoded as 'o1' field times 4 plus 3.

For the '32-bit' and '64-bit' variants: is the fourth slice index offset, with implicit value 3.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;ZAd&gt;

For the '16-bit' variant: is the name of the ZA tile ZA0-ZA1 to be accessed, encoded in the 'ZAd' field.

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3 to be accessed, encoded in the 'ZAd' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7 to be accessed, encoded in the 'ZAd' field.

## Operation

The description of MOVA (vector to tile, four registers) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOVA (vector to tile, four registers) gives the operational information for this instruction.