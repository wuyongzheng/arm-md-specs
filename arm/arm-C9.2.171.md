## C9.2.171 MOV (vector to tile, two registers)

Move Z two-vector operand to ZA two-slice operand

This instruction operates on a horizontal or vertical ZA two-slice operand within a ZA tile of the specified element size.

The first slice of the two-slice operand is selected by rounding down the sum of the slice index register and the immediate offset to the nearest lower multiple of 2, modulo the number of slices in the tile.

The immediate offset is a multiple of 2 in the range 0 to the number of elements in a 128-bit vector segment minus 2.

This instruction is unpredicated.

This is an alias of MOV A (vector to tile, two registers). This means:

- The encodings in this description are named to match the encodings of MOV A (vector to tile, two registers).
- The description of MOVA (vector to tile, two registers) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from 4 classes: 8-bit, 16-bit, 32-bit, and 64-bit

## 8-bit

(FEAT\_SME2)

<!-- image -->

## Encoding for the 8-bit variant

```
MOV ZA0<HV>.B[<Ws>, <offs1>:<offs2>], { <Zn1>.B-<Zn2>.B } is equivalent to MOVA ZA0<HV>.B[<Ws>, <offs1>:<offs2>], { <Zn1>.B-<Zn2>.B }
```

and is always the preferred disassembly.

## 16-bit

(FEAT\_SME2)

<!-- image -->

## Encoding for the 16-bit variant

```
MOV <ZAd><HV>.H[<Ws>, <offs1>:<offs2>], { <Zn1>.H-<Zn2>.H }
```

## is equivalent to

```
MOVA <ZAd><HV>.H[<Ws>, <offs1>:<offs2>], { <Zn1>.H-<Zn2>.H }
```

and is always the preferred disassembly.

## 32-bit

(FEAT\_SME2)

<!-- image -->

## Encoding for the 32-bit variant

MOV

&lt;ZAd&gt;&lt;HV&gt;.S[&lt;Ws&gt;, &lt;offs1&gt;:&lt;offs2&gt;], {

## is equivalent to

```
MOVA <ZAd><HV>.S[<Ws>, <offs1>:<offs2>], { <Zn1>.S-<Zn2>.S }
```

and is always the preferred disassembly.

64-bit

(FEAT\_SME2)

<!-- image -->

## Encoding for the 64-bit variant

```
MOV <ZAd><HV>.D[<Ws>, <offs1>:<offs2>], { <Zn1>.D-<Zn2>.D }
```

## is equivalent to

```
MOVA <ZAd><HV>.D[<Ws>, <offs1>:<offs2>], { <Zn1>.D-<Zn2>.D }
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

&lt;Zn1&gt;.S-&lt;Zn2&gt;.S

}

## &lt;offs1&gt;

For the '8-bit' variant: is the first slice index offset, encoded as 'off3' field times 2.

For the '16-bit' variant: is the first slice index offset, encoded as 'off2' field times 2.

For the '32-bit' variant: is the first slice index offset, encoded as 'o1' field times 2.

For the '64-bit' variant: is the first slice index offset, with implicit value 0.

## &lt;offs2&gt;

For the '8-bit' variant: is the second slice index offset, encoded as 'off3' field times 2 plus 1.

For the '16-bit' variant: is the second slice index offset, encoded as 'off2' field times 2 plus 1.

For the '32-bit' variant: is the second slice index offset, encoded as 'o1' field times 2 plus 1.

For the '64-bit' variant: is the second slice index offset, with implicit value 1.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;ZAd&gt;

For the '16-bit' variant: is the name of the ZA tile ZA0-ZA1 to be accessed, encoded in the 'ZAd' field.

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3 to be accessed, encoded in the 'ZAd' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7 to be accessed, encoded in the 'ZAd' field.

## Operation

The description of MOVA (vector to tile, two registers) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOVA (vector to tile, two registers) gives the operational information for this instruction.