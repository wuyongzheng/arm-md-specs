## C3.10 Data processing - SVE2

The following subsections describe the SVE2 processing instructions:

- Down-counting loops.
- Constructive multiply.
- Uniform DSP operations.
- Widening DSP operations.
- Narrowing DSP operation.
- Unary narrowing operations.
- Non-widening pairwise arithmetic.
- Widening pairwise arithmetic.
- Bitwise ternary logical instructions.
- Large integer arithmetic.
- Multiplication by indexed elements.
- Complex integer arithmetic.
- Conversions.
- Floating-point widening multiply-accumulate.
- Floating-point integer binary logarithm.
- Cross-lane match detect.
- Bit permutation.
- Polynomial arithmetic.
- Vector permutation.
- Table lookup.
- Cryptography support.
- BFloat16 arithmetic.
- BFloat16 minimum/maximum.
- Floating-point adjust exponent.
- Floating-point multiply-accumulate.
- Dot product.
- Floating-point matrix multiply-accumulate.
- Floating-point round.
- Quadword operations.
- Integer shift and convert.
- Predicate element index.
- Multi-vector predication.
- Permute vector.
- Predicate pair loop control.
- Predicate move.
- Predicate select.

## C3.10.1 Down-counting loops

Adown-counting WHILE instruction decrements the value of the first scalar operand and compares the value with a second, fixed scalar operand. The instruction generates a destination predicate with all of the following characteristics:

- The predicate elements starting from the highest-numbered element are true while the comparison remains true.
- The predicate elements thereafter, down to the lowest-numbered element, are false when the comparison becomes false.

All 32 bits or 64 bits of the scalar operands are significant for the purposes of comparison. The full 32-bit or 64-bit value of the first operand is decremented by 1 for each destination predicate element, irrespective of the element size. The first general-purpose register operand is not updated.

If all of the following occur, a comparison can never fail, resulting in an all-true predicate:

- The comparison includes an equality test.
- The second scalar operand is equal to the minimum integer value of the selected size and type of comparison.

Table C3-191 Down counting loop instructions

| Mnemonic   | Instruction                                                                       | See                 |
|------------|-----------------------------------------------------------------------------------|---------------------|
| WHILEGE    | While decrementing signed 32-bit or 64-bit scalar greater than or equal to scalar | WHILEGE (predicate) |
| WHILEGT    | While decrementing signed 32-bit or 64-bit scalar greater than scalar             | WHILEGT (predicate) |
| WHILEHI    | While decrementing unsigned 32-bit or 64-bit scalar higher than scalar            | WHILEHI (predicate) |
| WHILEHS    | While decrementing unsigned 32-bit or 64-bit scalar higher or same as scalar      | WHILEHS (predicate) |

## C3.10.2 Constructive multiply

SVE2 includes the following constructive, three-operand versions of the integer multiply instructions:

Table C3-192 Constructive multiply instructions

| Mnemonic   | Instruction                                          | See                        |
|------------|------------------------------------------------------|----------------------------|
| MUL        | Multiply vectors (unpredicated)                      | MUL(vectors, unpredicated) |
| SMULH      | Signed multiply returning high half (unpredicated)   | SMULH(unpredicated)        |
| UMULH      | Unsigned multiply returning high half (unpredicated) | UMULH(unpredicated)        |

## C3.10.3 Uniform DSP operations

The uniform DSP instructions are based on AArch64 Advanced SIMD instructions with the same mnemonic. The instructions operate on integer operands and produce results with a uniform element size. The operation of an instruction might include one or more of rounding, halving, saturation, and accumulation.

Table C3-193 Uniform DSP instructions

| Mnemonic   | Instruction                               | See    |
|------------|-------------------------------------------|--------|
| SABA       | Signed absolute difference and accumulate | SABA   |
| SHADD      | Signed halving addition                   | SHADD  |
| SHSUB      | Signed halving subtract                   | SHSUB  |
| SHSUBR     | Signed halving subtract reversed vectors  | SHSUBR |

| Mnemonic   | Instruction                                                                                | See                         |
|------------|--------------------------------------------------------------------------------------------|-----------------------------|
| SLI        | Shift left and insert (immediate)                                                          | SLI                         |
| SQABS      | Signed saturating absolute value                                                           | SQABS                       |
| SQADD      | Signed saturating addition (predicated)                                                    | SQADD(vectors, predicated)  |
| SQDMULH    | Signed saturating doubling multiply high (unpredicated)                                    | SQDMULH(vectors)            |
| SQNEG      | Signed saturating negate                                                                   | SQNEG                       |
| SQRDMLAH   | Signed saturating rounding doubling multiply-add high to accumulator (unpredicated)        | SQRDMLAH(indexed)           |
| SQRDMLSH   | Signed saturating rounding doubling multiply-subtract high from accumulator (unpredicated) | SQRDMLSH(vectors)           |
| SQRDMULH   | Signed saturating rounding doubling multiply high (unpredicated)                           | SQRDMULH(vectors)           |
| SQRSHL     | Signed saturating rounding shift left by vector (predicated)                               | SQRSHL                      |
| SQRSHLR    | Signed saturating rounding shift left reversed vectors (predicated)                        | SQRSHLR                     |
| SQSHL      | Signed saturating shift left by immediate                                                  | SQSHL (immediate)           |
| SQSHL      | Signed saturating shift left by vector (predicated)                                        | SQSHL (vectors)             |
| SQSHLR     | Signed saturating shift left reversed vectors (predicated)                                 | SQSHLR                      |
| SQSHLU     | Signed saturating shift left unsigned by immediate                                         | SQSHLU                      |
| SQSUB      | Signed saturating subtraction (predicated)                                                 | SQSUB (vectors, predicated) |
| SQSUBR     | Signed saturating subtraction reversed vectors (predicated)                                | SQSUBR                      |
| SRHADD     | Signed rounding halving addition                                                           | SRHADD                      |
| SRI        | Shift right and insert (immediate)                                                         | SRI                         |
| SRSHL      | Signed rounding shift left by vector (predicated)                                          | SRSHL                       |
| SRSHLR     | Signed rounding shift left reversed vectors (predicated)                                   | SRSHLR                      |
| SRSHR      | Signed rounding shift right by immediate                                                   | SRSHR                       |
| SRSRA      | Signed rounding shift right and accumulate (immediate)                                     | SRSRA                       |
| SSRA       | Signed shift right and accumulate (immediate)                                              | SSRA                        |
| SUQADD     | Signed saturating addition of unsigned value                                               | SUQADD                      |
| UABA       | Unsigned absolute difference and accumulate.                                               | UABA                        |
| UHADD      | Unsigned halving addition.                                                                 | UHADD                       |
| UHSUB      | Unsigned halving subtract                                                                  | UHSUB                       |
| UHSUBR     | Unsigned halving subtract reversed vectors                                                 | UHSUBR                      |
| UQADD      | Unsigned saturating addition (predicated)                                                  | UQADD(vectors, predicated)  |
| UQRSHL     | Unsigned saturating rounding shift left by vector (predicated)                             | UQRSHL                      |
| UQRSHLR    | Unsigned saturating rounding shift left reversed vectors (predicated)                      | UQRSHLR                     |
| UQSHL      | Unsigned saturating shift left by immediate                                                | UQSHL(immediate)            |
| UQSHL      | Unsigned saturating shift left by vector (predicated)                                      | UQSHL(vectors)              |
| UQSHLR     | Unsigned saturating shift left reversed vectors (predicated)                               | UQSHLR                      |
| UQSUB      | Unsigned saturating subtraction (predicated)                                               | UQSUB(vectors, predicated)  |
| UQSUBR     | Unsigned saturating subtraction reversed vectors (predicated)                              | UQSUBR                      |
| URECPE     | Unsigned reciprocal estimate (predicated)                                                  | URECPE                      |

| Mnemonic   | Instruction                                                | See     |
|------------|------------------------------------------------------------|---------|
| URHADD     | Unsigned rounding halving addition.                        | URHADD  |
| URSHL      | Unsigned rounding shift left by vector (predicated)        | URSHL   |
| URSHLR     | Unsigned rounding shift left reversed vectors (predicated) | URSHLR  |
| URSHR      | Unsigned rounding shift right by immediate                 | URSHR   |
| URSQRTE    | Unsigned reciprocal square root estimate (predicated)      | URSQRTE |
| URSRA      | Unsigned rounding shift right and accumulate (immediate)   | URSRA   |
| USQADD     | Unsigned saturating addition of signed value               | USQADD  |
| USRA       | Unsigned shift right and accumulate (immediate)            | USRA    |

## C3.10.4 Widening DSP operations

The widening DSP instructions are based on AArch64 Advanced SIMD instructions with similar mnemonics. The instructions operate on integer values and produce results that are twice the width of some or all of the inputs. The instructions read the narrow inputs from either the even-numbered (bottom) or odd-numbered (top) source elements and place each result in the double-width destination elements that overlap the narrow source elements.

Table C3-194 Widening DSP instructions

| Mnemonic   | Instruction                                                                 | See                |
|------------|-----------------------------------------------------------------------------|--------------------|
| SABALB     | Signed absolute difference and accumulate long (bottom)                     | SABALB             |
| SABALT     | Signed absolute difference and accumulate long (top)                        | SABALT             |
| SABDLB     | Signed absolute difference long (bottom)                                    | SABDLB             |
| SABDLT     | Signed absolute difference long (top)                                       | SABDLT             |
| SADDLB     | Signed add long (bottom)                                                    | SADDLB             |
| SADDLT     | Signed add long (top)                                                       | SADDLT             |
| SADDWB     | Signed add wide (bottom)                                                    | SADDWB             |
| SADDWT     | Signed add wide (top)                                                       | SADDWT             |
| SMLALB     | Signed multiply-add long to accumulator (bottom)                            | SMLALB(vectors)    |
| SMLALT     | Signed multiply-add long to accumulator (top)                               | SMLALT (vectors)   |
| SMLSLB     | Signed multiply-subtract long from accumulator (bottom)                     | SMLSLB (vectors)   |
| SMLSLT     | Signed multiply-subtract long from accumulator (top)                        | SMLSLT (vectors)   |
| SMULLB     | Signed multiply long (bottom)                                               | SMULLB(vectors)    |
| SMULLT     | Signed multiply long (top)                                                  | SMULLT (vectors)   |
| SQDMLALB   | Signed saturating doubling multiply-add long to accumulator (bottom)        | SQDMLALB(vectors)  |
| SQDMLALT   | Signed saturating doubling multiply-add long to accumulator (top)           | SQDMLALT(vectors)  |
| SQDMLSLB   | Signed saturating doubling multiply-subtract long from accumulator (bottom) | SQDMLSLB(vectors)  |
| SQDMLSLT   | Signed saturating doubling multiply-subtract long from accumulator (top)    | SQDMLSLT (vectors) |
| SQDMULLB   | Signed saturating doubling multiply long (bottom)                           | SQDMULLB(vectors)  |
| SQDMULLT   | Signed saturating doubling multiply long (top)                              | SQDMULLT(vectors)  |
| SSHLLB     | Signed shift left long by immediate (bottom)                                | SSHLLB             |

| Mnemonic   | Instruction                                               | See              |
|------------|-----------------------------------------------------------|------------------|
| SSHLLT     | Signed shift left long by immediate (top)                 | SSHLLT           |
| SSUBLB     | Signed subtract long (bottom)                             | SSUBLB           |
| SSUBLT     | Signed subtract long (top)                                | SSUBLT           |
| SSUBWB     | Signed subtract wide (bottom)                             | SSUBWB           |
| SSUBWT     | Signed subtract wide (top)                                | SSUBWT           |
| UABALB     | Unsigned absolute difference and accumulate long (bottom) | UABALB           |
| UABALT     | Unsigned absolute difference and accumulate long (top)    | UABALT           |
| UABDLB     | Unsigned absolute difference long (bottom)                | UABDLB           |
| UABDLT     | Unsigned absolute difference long (top)                   | UABDLT           |
| UADDLB     | Unsigned add long (bottom)                                | UADDLB           |
| UADDLT     | Unsigned add long (top)                                   | UADDLT           |
| UADDWB     | Unsigned add wide (bottom)                                | UADDWB           |
| UADDWT     | Unsigned add wide (top)                                   | UADDWT           |
| UMLALB     | Unsigned multiply-add long to accumulator (bottom)        | UMLALB(vectors)  |
| UMLALT     | Unsigned multiply-add long to accumulator (top)           | UMLALT(vectors)  |
| UMLSLB     | Unsigned multiply-subtract long from accumulator (bottom) | UMLSLB(vectors)  |
| UMLSLT     | Unsigned multiply-subtract long from accumulator (top)    | UMLSLT (vectors) |
| UMULLB     | Unsigned multiply long (bottom)                           | UMULLB(vectors)  |
| UMULLT     | Unsigned multiply long (top)                              | UMULLT(vectors)  |
| USHLLB     | Unsigned shift left long by immediate (bottom)            | USHLLB           |
| USHLLT     | Unsigned shift left long by immediate (top)               | USHLLT           |
| USUBLB     | Unsigned subtract long (bottom)                           | USUBLB           |
| USUBLT     | Unsigned subtract long (top)                              | USUBLT           |
| USUBWB     | Unsigned subtract wide (bottom)                           | USUBWB           |
| USUBWT     | Unsigned subtract wide (top)                              | USUBWT           |

## C3.10.5 Narrowing DSP operation

The narrowing DSP instructions are based on AArch64 Advanced SIMD instructions with similar mnemonics. The instructions operate on integer values and produce results that are half the width of the inputs. The instructions read wide source elements and place each result in one of the following:

- The overlapped even-numbered (bottom) half-width destination elements. The odd-numbered destination elements are set to zero.
- The overlapped odd-numbered (top) half-width destination elements. The even-numbered destination elements are unchanged, which means that the instructions are implicitly merging operations.

| Mnemonic   | Instruction                                                                  | See       |
|------------|------------------------------------------------------------------------------|-----------|
| ADDHNB     | Add narrow high part (bottom)                                                | ADDHNB    |
| ADDHNT     | Add narrow high part (top)                                                   | ADDHNT    |
| RADDHNB    | Rounding add narrow high part (bottom)                                       | RADDHNB   |
| RADDHNT    | Rounding add narrow high part (top)                                          | RADDHNT   |
| RSHRNB     | Rounding shift right narrow by immediate (bottom)                            | RSHRNB    |
| RSHRNT     | Rounding shift right narrow by immediate (top)                               | RSHRNT    |
| RSUBHNB    | Rounding subtract narrow high part (bottom)                                  | RSUBHNB   |
| RSUBHNT    | Rounding subtract narrow high part (top)                                     | RSUBHNT   |
| SHRNB      | Shift right narrow by immediate (bottom)                                     | SHRNB     |
| SHRNT      | Shift right narrow by immediate (top)                                        | SHRNT     |
| SQRSHRNB   | Signed saturating rounding shift right narrow by immediate (bottom)          | SQRSHRNB  |
| SQRSHRNT   | Signed saturating rounding shift right narrow by immediate (top)             | SQRSHRNT  |
| SQRSHRUNB  | Signed saturating rounding shift right unsigned narrow by immediate (bottom) | SQRSHRUNB |
| SQRSHRUNT  | Signed saturating rounding shift right unsigned narrow by immediate (top)    | SQRSHRUNT |
| SQSHRNB    | Signed saturating shift right narrow by immediate (bottom)                   | SQSHRNB   |
| SQSHRNT    | Signed saturating shift right narrow by immediate (top)                      | SQSHRNT   |
| SQSHRUNB   | Signed saturating shift right unsigned narrow by immediate (bottom)          | SQSHRUNB  |
| SQSHRUNT   | Signed saturating shift right unsigned narrow by immediate (top)             | SQSHRUNT  |
| SUBHNB     | Subtract narrow high part (bottom)                                           | SUBHNB    |
| SUBHNT     | Subtract narrow high part (top)                                              | SUBHNT    |
| UQRSHRNB   | Unsigned saturating rounding shift right narrow by immediate (bottom)        | UQRSHRNB  |
| UQRSHRNT   | Unsigned saturating rounding shift right narrow by immediate (top)           | UQRSHRNT  |
| UQSHRNB    | Unsigned saturating shift right narrow by immediate (bottom)                 | UQSHRNB   |
| UQSHRNT    | Unsigned saturating shift right narrow by immediate (top)                    | UQSHRNT   |

## C3.10.6 Unary narrowing operations

The unary narrowing instructions are unpredicated and do not write to the source register. The instructions read elements from the source vector and saturate each value to the half-width destination element size. The instructions place the narrow results in one of the following:

- The overlapped even-numbered (bottom) half-width elements. The odd-numbered elements are set to zero.
- The overlapped odd-numbered (top) half-width elements. The even-numbered elements are unchanged.

Non-saturating (truncating) conversions can be performed using existing SVE instructions such as shifts, masks, and permutes.

## Table C3-196 Unary narrowing instructions

| Mnemonic   | Instruction                                        | See     |
|------------|----------------------------------------------------|---------|
| SQXTNB     | Signed saturating extract narrow (bottom)          | SQXTNB  |
| SQXTNT     | Signed saturating extract narrow (top)             | SQXTNT  |
| SQXTUNB    | Signed saturating unsigned extract narrow (bottom) | SQXTUNB |
| SQXTUNT    | Signed saturating unsigned extract narrow (top)    | SQXTUNT |
| UQXTNB     | Unsigned saturating extract narrow (bottom)        | UQXTNB  |
| UQXTNT     | Unsigned saturating extract narrow (top)           | UQXTNT  |

## C3.10.7 Non-widening pairwise arithmetic

The non-widening pairwise arithmetic instructions operate on pairs of adjacent elements in each source vector and produce a result element that is the same size as a single input element. The results from the first and second source vectors are interleaved, so that the source and result elements overlap. The result is destructively placed in the first source vector. The AArch64 Advanced SIMD instructions do not interleave the results from the first and second source vectors. Predication applies to the destination vector. The even-numbered predicate elements enable an operation on a pair of elements in the first source vector. The odd-numbered predicate elements enable an operation on a pair of elements in the second source vector. Inactive elements in the destination vector register are not modified.

Table C3-197 Non-widening pairwise arithmetic instructions

| Mnemonic   | Instruction                            | See     |
|------------|----------------------------------------|---------|
| ADDP       | Add pairwise                           | ADDP    |
| FADDP      | Floating-point add pairwise            | FADDP   |
| FMAXNMP    | Floating-point maximum number pairwise | FMAXNMP |
| FMAXP      | Floating-point maximum pairwise        | FMAXP   |
| FMINNMP    | Floating-point minimum number pairwise | FMINNMP |
| FMINP      | Floating-point minimum pairwise        | FMINP   |
| SMAXP      | Signed maximum pairwise                | SMAXP   |
| SMINP      | Signed minimum pairwise                | SMINP   |
| UMAXP      | Unsigned maximum pairwise              | UMAXP   |
| UMINP      | Unsigned minimum pairwise              | UMINP   |

## C3.10.8 Widening pairwise arithmetic

The widening pairwise arithmetic instructions operate on pairs of adjacent elements in a single source vector and produce a double-width result element that is accumulated into the destination vector. Inactive elements in the destination vector register are not modified.

## Table C3-198 Widening pairwise arithmetic instructions

| Mnemonic   | Instruction                               | See    |
|------------|-------------------------------------------|--------|
| SADALP     | Signed add and accumulate long pairwise   | SADALP |
| UADALP     | Unsigned add and accumulate long pairwise | UADALP |

## C3.10.9 Bitwise ternary logical instructions

The bitwise ternary logical instructions enable complex bit processing codes to be accelerated using multiple bitwise logical operations in a shorter instruction sequence. All of the following operations are supported by the bitwise ternary logical instructions:

- The BCAX instruction combines a ternary bitwise clear with an exclusive-OR.
- The EOR3 instruction provides a ternary exclusive-OR.
- The XAR instruction combines an exclusive-OR with rotation by a constant amount.
- The bitwise select instructions, BSL , BSL1N , BSL2N , and NBSL , can be used with other bitwise logical instructions to generate all 256 possible bitwise combinations of three input bits using at most three instructions.

The bitwise ternary logical instructions are unpredicated.

## Table C3-199 Bitwise ternary logical instructions

| Mnemonic   | Instruction                                        | See   |
|------------|----------------------------------------------------|-------|
| BCAX       | Bitwise clear and exclusive-OR                     | BCAX  |
| BSL        | Bitwise select                                     | BSL   |
| BSL1N      | Bitwise select with first input inverted           | BSL1N |
| BSL2N      | Bitwise select with second input inverted          | BSL2N |
| EOR3       | Bitwise exclusive-OR of three vectors              | EOR3  |
| NBSL       | Bitwise inverted select                            | NBSL  |
| XAR        | Bitwise exclusive-OR and rotate right by immediate | XAR   |

## C3.10.10 Large integer arithmetic

The large integer arithmetic instructions aid the processing of large integers in vector registers by maintaining multiple carry chains that are interleaved in accumulator vectors.A large integer arithmetic instruction takes as input all of the following:

- Either the even-numbered (bottom) or odd-numbered (top) elements of the first source vector.
- A1-bit carry input from the least-significant bit of the odd-numbered elements of the second source vector.

The inputs to the instruction are added to or subtracted from the even-numbered elements of the destination and accumulator vector. The 1-bit carry output is placed in the corresponding odd-numbered element of the destination vector.

## Table C3-200 Large integer arithmetic instructions

| Mnemonic   | Instruction                       | See   |
|------------|-----------------------------------|-------|
| ADCLB      | Add with carry long (bottom)      | ADCLB |
| ADCLT      | Add with carry long (top)         | ADCLT |
| SBCLB      | Subtract with carry long (bottom) | SBCLB |
| SBCLT      | Subtract with carry long (top)    | SBCLT |

## C3.10.11 Multiplication by indexed elements

The multiplication by indexed elements instructions take all integer elements in each 128-bit vector segment of the first source vector and multiplies them by the indexed element in the corresponding segment of the second source vector.

The products might be destructively added to or subtracted from the corresponding elements of an addend vector.

The second source vector elements are specified using an immediate index that selects the same element position in each 128-bit vector segment. The index range is 0 to one less than the number of elements per 128-bit segment, encoded in 1 to 3 bits depending on the element size.

Table C3-201 Multiplication by indexed elements instructions

| Mnemonic   | Instruction                                                                           | See               |
|------------|---------------------------------------------------------------------------------------|-------------------|
| MLA        | Multiply-add to accumulator (indexed)                                                 | MLA(indexed)      |
| MLS        | Multiply-subtract from accumulator (indexed)                                          | MLS(indexed)      |
| MUL        | Multiply (indexed)                                                                    | MUL(indexed)      |
| SMLALB     | Signed multiply-add long to accumulator (bottom, indexed)                             | SMLALB(indexed)   |
| SMLALT     | Signed multiply-add long to accumulator (top, indexed)                                | SMLALT (indexed)  |
| SMLSLB     | Signed multiply-subtract long from accumulator (bottom, indexed)                      | SMLSLB (indexed)  |
| SMLSLT     | Signed multiply-subtract long from accumulator (top, indexed)                         | SMLSLT (indexed)  |
| SQDMLALT   | Signed saturating doubling multiply-add long to accumulator (top, indexed)            | SQDMLALT(indexed) |
| SQDMLSLB   | Signed saturating doubling multiply-subtract long from accumulator (bottom, indexed)  | SQDMLSLB(indexed) |
| SQDMLSLT   | Signed saturating doubling multiply-subtract long from accumulator (top, indexed)     | SQDMLSLB(indexed) |
| SQDMULLT   | Signed saturating doubling multiply long (top, indexed)                               | SQDMULLT(indexed) |
| SQRDMLAH   | Signed saturating rounding doubling multiply-add high to accumulator (indexed)        | SQRDMLAH(indexed) |
| SQRDMLSH   | Signed saturating rounding doubling multiply-subtract high from accumulator (indexed) | SQRDMLSH(indexed) |
| SQRDMULH   | Signed saturating rounding doubling multiply high (indexed)                           | SQRDMULH(indexed) |
| UMLALB     | Unsigned multiply-add long to accumulator (bottom, indexed)                           | UMLALB(indexed)   |
| UMLALT     | Unsigned multiply-add long to accumulator (top, indexed)                              | UMLALT(indexed)   |
| UMLSLB     | Unsigned multiply-subtract long from accumulator (bottom, indexed)                    | UMLSLB(indexed)   |
| UMLSLT     | Unsigned multiply-subtract long from accumulator (top, indexed)                       | UMLSLT (indexed)  |
| UMULLB     | Unsigned multiply long (bottom, indexed)                                              | UMULLB(indexed)   |
| UMULLT     | Unsigned multiply long (top, indexed)                                                 | UMULLT(indexed)   |

## C3.10.12 Complex integer arithmetic

Complex integer arithmetic instructions operate on signed integer complex numbers in vectors containing the following interleaved element pairs:

- The even-numbered elements contain the real parts of the complex numbers.
- The odd-numbered elements contain the imaginary parts of the complex numbers.

## C3.10.12.1 Uniform complex integer arithmetic

The uniform complex integer arithmetic instructions operate on vectors containing integral complex numbers. The instructions operate on complex numbers that are in polar form.

The CADD instructions rotate the complex numbers in the second source vector before adding element pairs to the corresponding elements of the first source vector, in a destructive manner. The rotation direction is 90 degrees or 270 degrees from the positive real axis towards the positive imaginary axis.

The CMLA instructions transform the operands to enable multiply-add or multiply-subtract operations on complex numbers by combining two of the instructions. The following transformations are done:

- The complex numbers in the second source vector are rotated by 0 degrees or 180 degrees before multiplying by the duplicated real components of the first source vector.
- The complex numbers in the second source vector are rotated by 90 degrees or 270 degrees before multiplying by the duplicated imaginary components of the first source vector.

The resulting products are added to the corresponding components of the destination and addend vector.

Two CMLA instructions can be used, as follows:

- CMLA Zda.S, Zn.S, Zm.S, #A
- CMLA Zda.S, Zn.S, Zm.S, #B

Some meaningful combinations of A and B are:

- A=0, B=90. The complex number vectors, Zn and Zm, are multiplied and the products are added to the complex numbers in Zda.
- A=0, B=270. The complex number conjugates in Zn are multiplied by the complex numbers in Zm and the products are added to the complex numbers in Zda.
- A=180, B=270. The two complex number vectors, Zn and Zm, are multiplied and the products are subtracted from the complex numbers in Zda.
- A=180, B=90. The complex number conjugates in Zn are multiplied by the complex numbers in Zm and the products are subtracted from the complex numbers in Zda.

The CMLA indexed form uses a single complex number in each 128-bit segment of the second source vector as the multiplier for all complex numbers in the corresponding first source vector segment. The complex numbers in the second source vector are specified using an immediate index that selects the same complex number position in each 128-bit vector segment. The index range is 0 to one less than the number of complex numbers per 128-bit segment, encoded in 1 to 2 bits depending on the complex number size.

Table C3-202 Uniform complex integer arithmetic instructions

| Mnemonic   | Instruction                                        | See           |
|------------|----------------------------------------------------|---------------|
| CADD       | Complex integer add with rotate                    | CADD          |
| CMLA       | Complex integer multiply-add with rotate           | CMLA(vectors) |
|            | Complex integer multiply-add with rotate (indexed) | CMLA(indexed) |

| Mnemonic   | Instruction                                                                          | See                |
|------------|--------------------------------------------------------------------------------------|--------------------|
| SQCADD     | Saturating complex integer add with rotate                                           | SQCADD             |
| SQRDCMLAH  | Saturating rounding doubling complex integer multiply-add high with rotate           | SQRDCMLAH(vectors) |
| SQRDCMLAH  | Saturating rounding doubling complex integer multiply-add high with rotate (indexed) | SQRDCMLAH(indexed) |

## C3.10.12.2 Widening complex integer arithmetic

The widening complex integer instructions deinterleave the real and imaginary components of integral complex numbers, and generate complex result components that have a higher numeric precision than the input values. The instructions differ from other complex instructions that process the real and imaginary components of complex numbers and write the complex result components to the destination.

The following instructions are useful when generating the widened components of the result of a complex multiply-add:

- SQDMLALBT , the imaginary results.
- SQDMLSLT , the real results.
- SQDMLALB , the conjugate real results.
- SQDMLSLBT , the conjugate imaginary results.

The following instructions are useful when generating the widened components of the result of a complex addition (X + jY) or (X - jY), given complex numbers X and Y:

- SADDLBT , the imaginary results when computing (X + jY) or real values when computing (X - jY).
- SSUBLBT , the real results when computing (X + jY) or imaginary values when computing (X - jY).

## Table C3-203 Widening complex integer arithmetic instructions

| Mnemonic   | Instruction                                                                       | See       |
|------------|-----------------------------------------------------------------------------------|-----------|
| SADDLBT    | Signed add long (bottom + top)                                                    | SADDLBT   |
| SQDMLALBT  | Signed saturating doubling multiply-add long to accumulator (bottom × top)        | SQDMLALBT |
| SQDMLSLBT  | Signed saturating doubling multiply-subtract long from accumulator (bottom × top) | SQDMLSLBT |
| SSUBLBT    | Signed subtract long (bottom - top)                                               | SSUBLBT   |
| SSUBLTB    | Signed subtract long (top - bottom)                                               | SSUBLTB   |

## C3.10.12.3 Complex integer dot product

The complex integer dot product instructions delimit the source vectors into pairs of 8-bit or 16-bit signed integer complex numbers. The complex numbers in the first source vector are multiplied by the corresponding complex numbers in the second source vector. The wide real or wide imaginary part of the product is accumulated into a 32-bit or 64-bit destination vector element that overlaps all four of the elements that form a pair of complex number values in the first source vector.

Each instruction implicitly deinterleaves the real and imaginary components of their complex number inputs, so that the destination vector accumulates four wide real sums or four wide imaginary sums.

The complex numbers in the second source vector are rotated by 0, 90, 180, or 270 degrees in the direction from the positive real axis towards the positive imaginary axis, considered in polar form, by applying the following transformations before the dot product operations:

- If the rotation is #0, the imaginary parts of the complex numbers in the second source vector are negated. The destination vector accumulates the real parts of a complex dot product.
- If the rotation is #90, the real and imaginary parts of the complex numbers the second source vector are swapped. The destination vector accumulates the imaginary parts of a complex dot product.

- If the rotation is #180, there is no transformation. The destination vector accumulates the real parts of a complex conjugate dot product.
- If the rotation is #270, the real parts of the complex numbers in the second source vector are negated and then swapped with the imaginary parts. The destination vector accumulates the imaginary parts of a complex conjugate dot product.

The indexed form of the instruction selects a single complex number pair within each 128-bit segment of the second source vector to multiply with all complex number pairs within the corresponding 128-bit segment of the first source vector. The complex number pairs within the second source vector are specified using an immediate index which selects the same complex number pair position within each 128-bit vector segment. The index range is from 0 to one less than the number of complex number pairs per 128-bit segment, encoded in 1 or 2 bits depending on the size of the complex number pair.

Each complex number is represented in a vector register as an even and odd pair of elements. The real part is the even-numbered element and the imaginary part is the odd-numbered element.

Table C3-204 Complex integer dot product instructions

| Mnemonic   | Instruction                           | See           |
|------------|---------------------------------------|---------------|
| CDOT       | Complex integer dot product           | CDOT(vectors) |
|            | Complex integer dot product (indexed) | CDOT(indexed) |

## C3.10.13 Conversions

## C3.10.13.1 Floating-point conversions

The floating-point extra conversion instructions convert to and from fully packed vectors of narrower floating-point elements.

The FCVTLT instruction converts the top or odd-numbered narrow floating-point vector elements to wider elements of the next higher precision. The conversion is similar to what is done by the widening integer instructions.

The FCVTNT and FCVXNT instructions convert wider floating-point vector elements to the top or odd-numbered narrower elements of the next lower precision. The conversion is similar to what is done by the narrowing integer instructions.

The FCVTXNT and FCVTX instructions convert from double-precision to fully packed half-precision in two narrowing steps, double-precision to single-precision and then single-precision to half-precision. The two-step conversion is done without an intermediate rounding error by using von Neumann rounding, which rounds an inexact mantissa to an odd value.

The existing SVE FCVT instructions implement the corresponding widening and narrowing conversions on the bottom or even-numbered half-width elements.

Table C3-205 Floating-point extra conversion instructions

| Mnemonic   | Instruction                                                    | See                 |
|------------|----------------------------------------------------------------|---------------------|
| FCVTLT     | Floating-point up convert long (top, predicated)               | FCVTLT              |
| FCVTNT     | Floating-point down convert narrow (top, predicated)           | FCVTNT (predicated) |
| FCVTX      | Floating-point down convert, rounding to odd (predicated)      | FCVTX               |
| FCVTXNT    | Floating-point down convert, rounding to odd (top, predicated) | FCVTXNT             |

## C3.10.13.2 FP8 floating-point conversions

Convert each floating-point element of the source vector while scaling the value, and place the results in the corresponding elements of the destination vector.

For instructions that convert other floating-point formats to FP8 formats, each input element is scaled by adding the value specified in FPMR.NSCALE to its unbounded exponent during the conversion.

For instructions that convert FP8 formats to other floating-point formats, each input element is scaled by subtracting the value specified in FPMR.LSCALE or FPMR.LSCALE2 from its unbounded exponent during the conversion.

For more information, see the instruction descriptions.

## Table C3-206 FP8 floating-point convert instructions

| Mnemonic           | Instruction                                                                      | See                   |
|--------------------|----------------------------------------------------------------------------------|-----------------------|
| BF1CVT, BF2CVT     | 8-bit floating-point convert to BFloat16                                         | BF1CVT, BF2CVT        |
| BF1CVTLT, BF2CVTLT | 8-bit floating-point convert to BFloat16 (top)                                   | BF1CVTLT, BF2CVTLT    |
| BFCVTN             | BFloat16 convert, narrow and interleave to 8-bit floating-point                  | BFCVTN                |
| F1CVT, F2CVT       | 8-bit floating-point convert to half-precision                                   | F1CVT, F2CVT          |
| F1CVTLT, F2CVTLT   | 8-bit floating-point convert to half-precision (top)                             | F1CVTLT, F2CVTLT      |
| FCVTN              | Half-precision convert, narrow and interleave to 8-bit floating-point            | FCVTN                 |
| FCVTNB             | Single-precision convert, narrow and interleave to 8-bit floating-point (bottom) | FCVTNB                |
| FCVTNT             | Single-precision convert, narrow and interleave to 8-bit floating-point (top)    | FCVTNT (unpredicated) |

## C3.10.14 Multiply-accumulate

## C3.10.14.1 Floating-point widening multiply-accumulate

The floating-point widening multiply-accumulate instructions multiply the even-numbered or odd-numbered half-precision elements of the two source vectors and then destructively add or subtract the single-precision intermediate products. Intermediate rounding is not done. The result is placed into the overlapping single-precision elements of the addend vector.

The instructions implicitly convert the half-precision inputs to single-precision and can be used to mitigate the impact of round-off errors when accumulating half-precision floating-point values over many iterations.

The instructions are unpredicated and preserve the multiplier and multiplicand source vectors.

Table C3-207 Floating-point widening multiply-accumulate instructions

| Mnemonic   | Instruction                                                             | See              |
|------------|-------------------------------------------------------------------------|------------------|
| FMLALB     | Floating-point fused multiply-add long to accumulator (bottom)          | FMLALB(vectors)  |
| FMLALB     | Floating-point fused multiply-add long to accumulator (bottom, indexed) | FMLALB(indexed)  |
| FMLALT     | Floating-point fused multiply-add long to accumulator (top)             | FMLALT (vectors) |
| FMLALT     | Floating-point fused multiply-add long to accumulator (top, indexed)    | FMLALT (indexed) |
| FMLSLB     | Floating-point fused multiply-subtract long from accumulator (bottom)   | FMLSLB (vectors) |

| Mnemonic   | Instruction                                                                    | See              |
|------------|--------------------------------------------------------------------------------|------------------|
| FMLSLB     | Floating-point fused multiply-subtract long from accumulator (bottom, indexed) | FMLSLB (indexed) |
| FMLSLT     | Floating-point fused multiply-subtract long from accumulator (top)             | FMLSLT (vectors) |
| FMLSLT     | Floating-point fused multiply-subtract long from accumulator (top, indexed)    | FMLSLT (indexed) |

## C3.10.14.2 FP8 floating-point widening multiply-accumulate

The FP8 floating-point multiply-accumulate instructions widen the 8-bit floating-point elements in the source vectors to half-precision or single-precision format and multiply the corresponding elements. They generate a fused, downscaled product and accumulate into the corresponding elements of the destination vector, without intermediate rounding.

For these instructions, the unbounded intermediate product is scaled by subtracting the value specified in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

## Table C3-208 FP8 floating-point widening multiply-accumulate instructions

| Mnemonic   | Instruction                                                                              | See                           |
|------------|------------------------------------------------------------------------------------------|-------------------------------|
| FMLALB     | 8-bit floating-point multiply-add long to half-precision (bottom, indexed)               | FMLALB(indexed, FP8 to FP16)  |
| FMLALB     | 8-bit floating-point multiply-add long to half-precision (bottom)                        | FMLALB(vectors, FP8 to FP16)  |
| FMLALLBB   | 8-bit floating-point multiply-add long long to single-precision (bottom bottom, indexed) | FMLALLBB (indexed)            |
| FMLALLBB   | 8-bit floating-point multiply-add long long to single-precision (bottom bottom)          | FMLALLBB (vectors)            |
| FMLALLBT   | 8-bit floating-point multiply-add long long to single-precision (bottom top, indexed)    | FMLALLBT (indexed)            |
| FMLALLBT   | 8-bit floating-point multiply-add long long to single-precision (bottom top)             | FMLALLBT (vectors)            |
| FMLALLTB   | 8-bit floating-point multiply-add long long to single-precision (top bottom, indexed)    | FMLALLTB (indexed)            |
| FMLALLTB   | 8-bit floating-point multiply-add long long to single-precision (top bottom)             | FMLALLTB (vectors)            |
| FMLALLTT   | 8-bit floating-point multiply-add long long to single-precision (top top, indexed)       | FMLALLTT (indexed)            |
| FMLALLTT   | 8-bit floating-point multiply-add long long to single-precision (top top)                | FMLALLTT (vectors)            |
| FMLALT     | 8-bit floating-point multiply-add long to half-precision (top, indexed)                  | FMLALT (indexed, FP8 to FP16) |
| FMLALT     | 8-bit floating-point multiply-add long to half-precision (top)                           | FMLALT (vectors, FP8 to FP16) |

## C3.10.15 Floating-point integer binary logarithm

The floating-point integer binary logarithm instruction returns the signed integer base 2 logarithm of each floating-point input element |x| after normalization.

The instruction produces the unbiased exponent of x used in the representation of the floating-point value. For positive x, x = significand × 2 exponent .

The integer results are placed in elements of the destination vector, which have the same width as the floating-point input elements:

- If x is normal, the result is the base 2 logarithm of x.
- If x is subnormal, the result corresponds to the normalized representation.
- If x is infinite, the result is 2 (esize-1) -1.
- If x is ±0.0 or NaN, the result is -2 (esize-1) .

Inactive elements in the destination vector register are not modified.

## Table C3-209 Floating-point integer binary logarithm instruction

| Mnemonic   | Instruction                                | See   |
|------------|--------------------------------------------|-------|
| FLOGB      | Floating-point base 2 logarithm as integer | FLOGB |

## C3.10.16 Floating-point minimum/maximum absolute value

## Table C3-210 Floating-point absolute minimum/maximum instructions

| Mnemonic   | Instruction                                  | See   |
|------------|----------------------------------------------|-------|
| FAMAX      | Floating-point absolute maximum (predicated) | FAMAX |
| FAMIN      | Floating-point absolute minimum (predicated) | FAMIN |

## C3.10.17 Cross-lane match detect

This section includes instructions that detect or count matching elements within another vector, or within a 128-bit vector segment.

## C3.10.17.1 Vector Histogram Count

The vector histogram count instructions create vector histograms.

- HISTSEG compares each 8-bit byte element in the first source vector with all of the elements in the corresponding 128-bit segment of the second source vector. The instruction counts the matching elements and places the result in the corresponding destination vector element. The instruction is unpredicated.
- HISTCNT compares each active 32-bit or 64-bit element in the first source vector with all elements in the second source vector that have an element number less than or equal to the Active element in the first source vector. The number of matching elements is counted and the result is placed in the corresponding destination vector element. Inactive elements in the destination vector are set to zero. Inactive elements in the second source vector do not cause a match.

## Table C3-211 Vector histogram count instructions

| Mnemonic   | Instruction                                | See     |
|------------|--------------------------------------------|---------|
| HISTCNT    | Count matching elements in vector          | HISTCNT |
| HISTSEG    | Count matching elements in vector segments | HISTSEG |

## C3.10.17.2 Character match

The character match instructions can be used to scan each 128-bit segment of the second source vector for an 8-bit or 16-bit character string from the first source vector.

The MATCH and NMATCH instructions compare each active 8-bit or 16-bit character in the first source vector with all of the characters in the corresponding 128-bit segment of the second source vector. When the first source character matches any ( MATCH ) or does not match any ( NMATCH ) character in the second segment, a true value is placed in the corresponding destination predicate element, otherwise a false value is placed in the destination predicate element. Inactive elements in the destination predicate register are set to zero.

The instruction sets the NZC condition flags based on the predicate result, and sets the V flag to zero.

## Table C3-212 Character match instructions

| Mnemonic   | Instruction                                              | See    |
|------------|----------------------------------------------------------|--------|
| MATCH      | Detect any matching elements, setting the condition flag | MATCH  |
| NMATCH     | Detect no matching elements, setting the condition flags | NMATCH |

## C3.10.17.3 Contiguous conflict detection

The contiguous conflict detection instructions check two addresses for a conflict or overlap between address ranges that could result in a loop-carried dependency through memory. The address range has the form [addr,addr+ VL ÷8], where VL is the Effective SVE vector length in bits. A conflict can occur when contiguous load and store instructions use these addresses within the same loop iteration.

The instructions generate a predicate with elements that are true when the addresses cannot conflict within the same iteration, and false thereafter. The instructions set the NZC condition flags based on the predicate result, and the V flag is set to zero.

## Table C3-213 Contiguous conflict detection instructions

| Mnemonic   | Instruction                                    | See     |
|------------|------------------------------------------------|---------|
| WHILERW    | While free of read-after-write conflicts       | WHILERW |
| WHILEWR    | While free of write-after-read/write conflicts | WHILEWR |

## C3.10.18 Bit permutation

The bit permutation instructions are optional. The bit permutation instructions are configured by the ID\_AA64ZFR0\_EL1.BitPerm bit. The instructions can be used to scatter, gather, or separate a set of bits within each first source vector element under the control of a bit mask or sieve in the corresponding second source vector elements. The instructions are unpredicated.

The BDEP instruction scatters the lowest-numbered contiguous bits within each first source vector element to the bit positions that are indicated by nonzero bits in the corresponding mask element of the second source vector. The order of the bits is preserved. The bits corresponding to a zero mask bit are set to zero.

The BEXT instruction gathers bits in each first source vector element from the bit positions that are indicated by nonzero bits in the corresponding mask element of the second source vector. The bits are gathered to the lowest-numbered contiguous bits of the corresponding destination element, preserving their order. The remaining higher-numbered bits are set to zero.

The BGRP instruction selects bits from each first source vector element and groups them into the corresponding destination element, using a corresponding mask element in the second source vector, as follows:

- The nonzero bits in the mask element select the bit positions from the corresponding first source vector element. The selected bits are gathered into the lowest-numbered contiguous bits of the destination element.
- The zero bits in the mask element select the bit positions from the corresponding first source vector element. The selected bits are gathered into the highest-numbered contiguous bits of the destination element.

The bit order within each group is preserved.

Table C3-214 Bit permutation instructions

| Mnemonic   | Instruction                                           | See   |
|------------|-------------------------------------------------------|-------|
| BDEP       | Scatter lower bits into positions selected by bitmask | BDEP  |
| BEXT       | Gather lower bits from positions selected by bitmask  | BEXT  |
| BGRP       | Group bits to right or left as selected by bitmask    | BGRP  |

## C3.10.19 Polynomial arithmetic

The polynomial arithmetic instructions support polynomial arithmetic over [0, 1], where exclusive-OR takes the place of addition. The instructions can be used in applications such as CRC calculations, AES-GCM, elliptic curve cryptography, Diffie-Hellman key exchange, and others.

The PMUL and widening PMLAL , PMULL , PMULLB , and PMULLT instructions perform polynomial multiplication over [0,1]. PMLAL additionally performs a bitwise exclusive-OR of the multiplication result on the element in the destination vector.

The PMULLB and PMULLT instructions read the source operands from either the even-numbered (bottom) or odd-numbered (top) elements, respectively. The widened results are placed in the double-width destination elements that overlap with the corresponding source elements.

The multi-vector PMLAL and PMULL instructions produce results in two destination vectors. The double-width results computed from even-numbered source elements are placed in the first destination vector, while the double-width results computed from odd-numbered source elements are placed in the second destination vector.

The EORBT and EORTB instructions operate on the even-numbered elements of the first source vector register and the odd-numbered elements of the second source vector register. The result is either placed in the even-numbered elements of the destination vector, leaving the odd-numbered elements unchanged, or placed in the odd-numbered elements of the destination vector, leaving the even-numbered elements unchanged.

These instructions are unpredicated.

Table C3-215 Polynomial arithmetic instructions

| Mnemonic   | Instruction                                          | See    |
|------------|------------------------------------------------------|--------|
| EORBT      | Interleaving exclusive-OR (bottom, top)              | EORBT  |
| EORTB      | Interleaving exclusive-OR (top, bottom)              | EORTB  |
| PMLAL      | Multi-vector polynomial multiply long and accumulate | PMLAL  |
| PMUL       | Polynomial multiply vectors (unpredicated)           | PMUL   |
| PMULL      | Multi-vector polynomial multiply long                | PMULL  |
| PMULLB     | Polynomial multiply long (bottom)                    | PMULLB |
| PMULLT     | Polynomial multiply long (top)                       | PMULLT |

## C3.10.20 Vector permutation

The vector concatenation instructions EXT and SPLICE have constructive versions that are introduced in SVE2 that preserve both of the source operands. In the constructive versions of the instruction, only the first source vector register number is encoded, which requires the source vectors to be in consecutively numbered registers (modulo 32).

The EXPAND instruction copies the lowest numbered source vector elements to active elements of the destination vector, this complements the COMPACT instruction.

For more information see Table C3-185.

## Table C3-216 Vector permutation instructions

| Mnemonic   | Instruction                                            | See     |
|------------|--------------------------------------------------------|---------|
| COMPACT    | Copy active vector elements to lower-numbered elements | COMPACT |
| EXPAND     | Copy low-numbered vector elements to active elements   | EXPAND  |
| EXT        | Extract vector from pair of vectors                    | EXT     |
| SPLICE     | Splice two vectors under predicate control             | SPLICE  |

## C3.10.21 Table lookup

## C3.10.21.1 Extended table lookup permute

The SVE2 extended table lookup instructions, TBL and TBX enable the construction of table lookups or programmable vector permutes where the table consists of two or more vector registers.

Because the index values can select any element in a vector, the instructions are not naturally vector length agnostic.

## Table C3-217 Extended table lookup instructions

| Mnemonic   | Instruction                                                    | See   |
|------------|----------------------------------------------------------------|-------|
| TBL        | Programmable table lookup in one or two vector table (zeroing) | TBL   |
| TBX        | Programmable table lookup in single vector table (zeroing)     | TBX   |

## C3.10.21.2 Lookup table using 2-bit or 4-bit indices

Copy indexed elements from the first source vector(s) to the destination vector, using packed indices from a portion of the second source vector.

## Table C3-218 SVE2 lookup table using 2-bit or 4-bit indices instructions

| Mnemonic   | Instruction                      | See   |
|------------|----------------------------------|-------|
| LUTI2      | Lookup table using 2-bit indices | LUTI2 |
| LUTI4      | Lookup table using 4-bit indices | LUTI4 |

## C3.10.22 Cryptography support

## C3.10.22.1 AES-128 instructions

AES-128 is a 128-bit block cipher that is computed using a combination of linear EOR operations, the use of rotations by fixed values, and a set of 8-bit non-linear substitutions.

The AESE , AESMC , and AESEMC instructions accelerate a single encryption round, and the AESD , AESIMC , and AESDIMC instructions accelerate a single decryption round. These instructions read a 16-byte state from a 128-bit segment of the first source vectors, and a round key from a 128-bit segment of the second source vector.

The AES instructions are unpredicated.

## Table C3-219 AES-128 instructions

| Mnemonic   | Instruction                                                      | See            |
|------------|------------------------------------------------------------------|----------------|
| AESD       | Multi-vector AES single round decryption                         | AESD (indexed) |
|            | AES single round decryption                                      | AESD (vectors) |
| AESDIMC    | Multi-vector AES single round decryption and inverse mix columns | AESDIMC        |
| AESE       | Multi-vector AES single round encryption                         | AESE (indexed) |
|            | AES single round encryption                                      | AESE (vectors) |
| AESEMC     | Multi-vector AES single round encryption and mix columns         | AESEMC         |
| AESIMC     | AES inverse mix columns                                          | AESIMC         |
| AESMC      | AES mix columns                                                  | AESMC          |

## C3.10.22.2 SHA-3 instructions

The SHA-3 instructions accelerate the SHA-3 hash algorithm.

The SHA-3 hash is based on a running digest of 1600 bits, arranged as a five by five array of 64-bit values. The instructions map the 25 64-bit values into 25 vector registers, with each 64-bit value occupying the same 64-bit element in each vector. A series of transformations is done on these registers during a round of the SHA-3 hash calculation.

Two or more parallel SHA-3 hash calculations are combined as a SIMD operation, where one calculation operates on the 0th 64-bit element of each vector, and the other calculation operates on the first 64-bit element of each vector. The SIMD operation is useful for the fast parallel hash algorithm recently introduced into the SHA-3 standard that allows a single input stream to be computed using multiple SHA-3 hashes in parallel.

The SHA3 instructions are unpredicated.

## Table C3-220 SHA-3 instructions

| Mnemonic   | Instruction                               | See   |
|------------|-------------------------------------------|-------|
| RAX1       | Bitwise rotate left by 1 and exclusive-OR | RAX1  |

See also Bitwise ternary logical instructions.

## C3.10.22.3 SM4 instructions

SM4 is the standard Chinese symmetric encryption algorithm which can be accelerated using a similar approach to that used for AES.

SM4 is a 128-bit wide block cipher that is computed using a combination of linear EOR operations, the use of fixed-value rotations, and a set of 8-bit non-linear substitutions.

- The SM4E instruction reads 16 bytes of input data from each 128-bit segment of the first source vector, and four iterations of 32-bit round keys from the corresponding 128-bit segments of the second source vector. Each input data block is encrypted by four rounds in accordance with the SM4 standard, and destructively placed in the corresponding segments of the first source vector.
- The SM4EKEY instruction reads four rounds of 32-bit input key values from each 128-bit segment of the first source vector, and four rounds of 32-bit constants from the corresponding 128-bit segment of the second source vector. The four rounds of output key values are derived in accordance with the SM4 standard, and placed in the corresponding segments of the destination vector.

The SM4 instructions are unpredicated.

## Table C3-221 SM4 instructions

| Mnemonic   | Instruction                   | See     |
|------------|-------------------------------|---------|
| SM4E       | SM4 encryption and decryption | SM4E    |
| SM4EKEY    | SM4 key updates               | SM4EKEY |

## C3.10.23 BFloat16 arithmetic

## C3.10.23.1 Add and subtract

Add or subtract BFloat16 elements of the second source vector from the corresponding elements of the first source vector and destructively place the results in the corresponding elements of the first source vector.

## Table C3-222 SVE2 BFloat16 add and subtract instructions

| Mnemonic   | Instruction                                                         | See                                     |
|------------|---------------------------------------------------------------------|-----------------------------------------|
| BFADD      | BFloat16 floating-point add vectors (predicated, unpredicated)      | BFADD(predicated) BFADD(unpredicated)   |
| BFSUB      | BFloat16 floating-point subtract vectors (predicated, unpredicated) | BFSUB (predicated) BFSUB (unpredicated) |

## C3.10.23.2 Multiply and multiply-accumulate

Multiply all BFloat16 elements of the first source vector by the specified element in the corresponding second source vector and place the results in the corresponding elements of the destination vector. The accumulate instructions add or subtract the result without intermediate rounding from the corresponding elements of the destination vector.

BFMLA and BFMLS perform a fused multiply-add or multiply-subtract of BFloat16 values without intermediate rounding.

## Table C3-223 SVE2 BFloat16 multiply and multiply-accumulate instructions

| Mnemonic   | Instruction                                                         | See                                                     |
|------------|---------------------------------------------------------------------|---------------------------------------------------------|
| BFMUL      | BFloat16 floating-point multiply vectors by indexed elements        | BFMUL(indexed)                                          |
|            | BFloat16 floating-point multiply vectors (predicated, unpredicated) | BFMUL(vectors, predicated) BFMUL(vectors, unpredicated) |

| Mnemonic   | Instruction                                                                 | See             |
|------------|-----------------------------------------------------------------------------|-----------------|
| BFMLA      | BFloat16 floating-point fused multiply-add vectors by indexed elements      | BFMLA(indexed)  |
|            | BFloat16 floating-point fused multiply-add vectors                          | BFMLA(vectors)  |
| BFMLS      | BFloat16 floating-point fused multiply-subtract vectors by indexed elements | BFMLS (indexed) |
|            | BFloat16 floating-point fused multiply-subtract vectors                     | BFMLS (vectors) |

## C3.10.24 BFloat16 minimum/maximum

Determine the maximum or minimum active BFloat16 elements of the second source vector and corresponding elements of the first source vector and destructively place the results in the corresponding elements of the first source vector.

## Table C3-224 SVE2 BFloat16 minimum/maximum instructions

| Mnemonic   | Instruction                                         | See     |
|------------|-----------------------------------------------------|---------|
| BFMAX      | BFloat16 floating-point maximum (predicated)        | BFMAX   |
| BFMAXNM    | BFloat16 floating-point maximum number (predicated) | BFMAXNM |
| BFMIN      | BFloat16 floating-point minimum (predicated)        | BFMIN   |
| BFMINNM    | BFloat16 floating-point minimum number (predicated) | BFMINNM |

## C3.10.25 Floating-point adjust exponent

The SVE2 BFSCALE instruction performs BFloat16 scaling by integer powers of two.

## Table C3-225 SVE2 floating-point adjust exponent instructions

| Mnemonic   | Instruction                                     | See     |
|------------|-------------------------------------------------|---------|
| BFSCALE    | Scales BFloat16 values by integer powers of two | BFSCALE |

## C3.10.26 Clamp to minimum/maximum

Clamp each element in the destination vectors to between the minimum value in the corresponding element of the first source vector and the maximum value in the corresponding element of the second source vector and destructively place the clamped results in the corresponding elements of the destination vector.

## C3.10.26.1 Floating-point clamp to minimum/maximum

## Table C3-226 SVE2.1 Floating-point clamp to minimum/maximum instructions

| Mnemonic   | Instruction                                             | See     |
|------------|---------------------------------------------------------|---------|
| BFCLAMP    | BFloat16 floating-point clamp to minimum/maximum number | BFCLAMP |
| FCLAMP     | Floating-point clamp to minimum/maximum number          | FCLAMP  |

## C3.10.26.2 Integer clamp to minimum/maximum

## Table C3-227 SVE2.1 Integer clamp to minimum/maximum instructions

| Mnemonic   | Instruction                              | See    |
|------------|------------------------------------------|--------|
| SCLAMP     | Signed clamp to minimum/maximum vector   | SCLAMP |
| UCLAMP     | Unsigned clamp to minimum/maximum vector | UCLAMP |

## C3.10.27 Dot product

## C3.10.27.1 Floating-point dot product

Compute the dot product of a pair of values held in the corresponding elements of the first source vectors multiplied by the corresponding elements of the second source vector. The dot product is then destructively added to the corresponding element of the destination vector.

## Table C3-228 SVE2.1 Floating-point dot product instructions

| Mnemonic   | Instruction                                       | See            |
|------------|---------------------------------------------------|----------------|
| FDOT       | Half-precision floating-point indexed dot product | FDOT (indexed) |
|            | Half-precision floating-point dot product         | FDOT (vectors) |

## C3.10.27.2 FP8 floating-point dot product

The FP8 floating-point dot product instructions accumulate the dot product of two or four adjacent FP8 source elements into half-precision or single-precision destination elements. They generate a fused, downscaled sum-of-products and accumulate into each destination element, without intermediate rounding.

For these instructions, the unbounded intermediate sum-of-products is scaled by subtracting the value specified in FPMR.LSCALE. For more information, see the instruction descriptions.

## Table C3-229 SVE2 FP8 floating-point dot product instructions

| Mnemonic   | Instruction                                                | See                                |
|------------|------------------------------------------------------------|------------------------------------|
| FDOT       | 8-bit floating-point indexed dot product to half-precision | FDOT (2-way, indexed, FP8 to FP16) |
|            | 8-bit floating-point dot product to half-precision         | FDOT (2-way, vectors, FP8 to FP16) |

| Mnemonic   | Instruction                                                  | See                   |
|------------|--------------------------------------------------------------|-----------------------|
|            | 8-bit floating-point indexed dot product to single-precision | FDOT (4-way, indexed) |
|            | 8-bit floating-point dot product to single-precision         | FDOT (4-way, vectors) |

## C3.10.28 Floating-point matrix multiply-accumulate

## C3.10.28.1 Floating-point matrix multiply-accumulate

The FMMLA (widening, FP16 to FP32) instruction is implemented by FEAT\_SVE\_F16F32MM. This instruction delimits each source and destination vector into 128-bit segments. The 128-bit segments are organized as follows:

- In the first source vector, a 2x4 matrix of half-precision values in row-by-row order.
- In the second source vector, a 4x2 matrix of half-precision values in column-by-column order.
- In the destination vector, a 2x2 matrix of single-precision values in row-by-row order.

One matrix multiplication is performed per vector segment and accumulated into the destination vector segment.

The intermediate single-precision sums-of-products are rounded before they are summed, and the intermediate sum is rounded before addition to the single-precision destination elements.

## Table C3-230 SVE2 Floating-point matrix multiply-accumulate instructions

| Mnemonic   | Instruction                                                   | See                                                 |
|------------|---------------------------------------------------------------|-----------------------------------------------------|
| FMMLA      | Half-precision matrix multiply-accumulate to single-precision | FMMLA(widening, half-precision to single-precision) |

## C3.10.28.2 FP8 floating-point matrix multiply-accumulate

The FP8 FMMLA (widening, FP8 to FP32) instruction is implemented by FEAT\_F8F32MM. This instruction delimits each source and destination vector into 128-bit segments. The 128-bit segments are organized as follows:

- In the first source vector, a 2x8 matrix of 8-bit floating-point values in row-by-row order.
- In the second source vector, an 8x2 matrix of 8-bit floating-point values in column-by-column order.
- In the destination vector, a 2x2 matrix of single-precision values in row-by-row order.

One matrix multiplication is performed per vector segment and accumulated into the destination vector segment.

The FP8 FMMLA (widening, FP8 to FP16) instruction is implemented by FEAT\_F8F16MM. This instruction delimits each source and destination vector into 64-bit segments. The 64-bit segments are organized as follows:

- In the first source vector, a 2x4 matrix of 8-bit floating-point values in row-by-row order.
- In the second source vector, a 4x2 matrix of 8-bit floating-point values in column-by-column order.
- In the destination vector, a 2x2 matrix of half-precision values in row-by-row order.

One matrix multiplication is performed per vector segment and accumulated into the destination vector segment.

These instructions generate a fused, downscaled sum-of-products and accumulate into each destination element, without intermediate rounding. For these instructions, the intermediate sum of products is downscaled by subtracting the value in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

## Table C3-231 SVE2 FP8 Floating-point matrix multiply-accumulate instructions

| Mnemonic   | Instruction                                                         | See                          |
|------------|---------------------------------------------------------------------|------------------------------|
| FMMLA      | 8-bit floating-point matrix multiply-accumulate to single-precision | FMMLA(widening, FP8 to FP32) |
| FMMLA      | 8-bit floating-point matrix multiply-accumulate to half-precision   | FMMLA(widening, FP8 to FP16) |

## C3.10.29 Floating-point round to integral value

The following instructions round a floating-point value to an integral floating-point value of 32-bit or 64-bit integer size.

These instructions can cause floating-point exceptions, for more information see Floating-point exceptions and exception traps.

## Table C3-232 SVE2 Floating-point round to integral value instructions

| Mnemonic   | Instruction                                                                      | See      |
|------------|----------------------------------------------------------------------------------|----------|
| FRINT32X   | Floating-point round to 32-bit integer, using current rounding mode (predicated) | FRINT32X |
| FRINT32Z   | Floating-point round to 32-bit integer, towards zero (predicated)                | FRINT32Z |
| FRINT64X   | Floating-point round to 64-bit integer, using current rounding mode (predicated) | FRINT64X |
| FRINT64Z   | Floating-point round to 64-bit integer, towards zero (predicated)                | FRINT64Z |

## C3.10.30 Quadword operations

## C3.10.30.1 Permute within quadwords

In these instructions the same permutation pattern is applied within each quadword.

## Table C3-233 SVE2.1 Permute within quadwords instructions

| Mnemonic   | Instruction                                                                   | See   |
|------------|-------------------------------------------------------------------------------|-------|
| DUPQ       | Broadcast indexed element within each quadword vector segment (unpredicated)  | DUPQ  |
| EXTQ       | Extract vector segment from each pair of quadword vector segments             | EXTQ  |
| TBLQ       | Programmable table lookup within each quadword vector segment (zeroing)       | TBLQ  |
| TBXQ       | Programmable table lookup within each quadword vector segment (merging)       | TBXQ  |
| UZPQ1      | Concatenate even elements within each pair of quadword vector segments        | UZPQ1 |
| UZPQ2      | Concatenate odd elements within each pair of quadword vector segments         | UZPQ2 |
| ZIPQ1      | Interleave elements from low halves of each pair of quadword vector segments  | ZIPQ1 |
| ZIPQ2      | Interleave elements from high halves of each pair of quadword vector segments | ZIPQ2 |

## C3.10.30.2 Reduction to quadword

In the reductions to quadwords instructions a full SVE vector is reduced to a single 128-bit vector. The result of the operations is placed into the corresponding element of the 128-bit Advanced SIMD and floating-point destination register.

## Table C3-234 SVE2.1 Reduction to quadword instructions

| Mnemonic   | Instruction                                                                   | See      |
|------------|-------------------------------------------------------------------------------|----------|
| ADDQV      | Unsigned add reduction of quadword vector segments                            | ADDQV    |
| ANDQV      | Bitwise ANDreduction of quadword vector segments                              | ANDQV    |
| EORQV      | Bitwise exclusive ORreduction of quadword vector segments                     | EORQV    |
| FADDQV     | Floating-point add recursive reduction of quadword vector segments            | FADDQV   |
| FMAXNMQV   | Floating-point maximum number recursive reduction of quadword vector segments | FMAXNMQV |
| FMAXQV     | Floating-point maximum reduction of quadword vector segments                  | FMAXQV   |
| FMINNMQV   | Floating-point minimum number recursive reduction of quadword vector segments | FMINNMQV |
| FMINQV     | Floating-point minimum recursive reduction of quadword vector segments        | FMINQV   |
| ORQV       | Bitwise inclusive ORreduction of quadword vector segments                     | ORQV     |
| SMAXQV     | Signed maximum reduction of quadword vector segments                          | SMAXQV   |
| SMINQV     | Signed minimum reduction of quadword vector segments                          | SMINQV   |
| UMAXQV     | Unsigned maximum reduction of quadword vector segments                        | UMAXQV   |
| UMINQV     | Unsigned minimum reduction of quadword vector segments                        | UMINQV   |

## C3.10.31 Integer shift and convert

Convert or shift the value of each element of the source vectors and place the results in the corresponding destination vector elements.

These are narrowing, interleaving, saturating variants of the integer shift and convert instructions, to avoid write after write dependencies for merging narrowing top instructions.

## Table C3-235 SVE2.1 Integer shift and convert instructions

| Mnemonic   | Instruction                                                                        | See      |
|------------|------------------------------------------------------------------------------------|----------|
| SQCVTN     | Signed saturating extract narrow and interleave                                    | SQCVTN   |
| SQCVTUN    | Signed saturating unsigned extract narrow and interleave                           | SQCVTUN  |
| SQRSHRN    | Signed saturating rounding shift right narrow by immediate and interleave          | SQRSHRN  |
| SQRSHRUN   | Signed saturating rounding shift right unsigned narrow by immediate and interleave | SQRSHRUN |
| UQCVTN     | Unsigned saturating extract narrow and interleave                                  | UQCVTN   |
| UQRSHRN    | Unsigned saturating rounding shift right narrow by immediate and interleave        | UQRSHRN  |

## C3.10.32 Predicate element index

Determine the index of the first or last active TRUE predicate element.

## Table C3-236 SVE2 Scalar index instructions

| Mnemonic   | Instruction                                               | See    |
|------------|-----------------------------------------------------------|--------|
| FIRSTP     | Scalar index of first TRUE predicate element (predicated) | FIRSTP |
| LASTP      | Scalar index of last TRUE predicate element (predicated)  | LASTP  |

## C3.10.33 Multi-vector predication

Multi-vector predication is required when using the Contiguous multi-vector loads and stores, and also reduces the number of predicate registers and predicate computations in a loop.

The WHILE instructions generate a predicate-as-counter encoding. These instructions have an operand that indicates the number of vectors (2 or 4) to be controlled by this predicate, which determines:

- The maximum value that can be stored in the count.
- The number of elements that are considered Active when computing the Any Active element and Last Active element SVE condition flags.

CNTP has an operand that indicates the limit of the number of elements to be counted. The limit corresponds to the total number of elements in either 2 or 4 vectors.

For more information, see Predicate-as-counter.

## Table C3-237 SVE2.1 Multi-vector predication instructions

| Mnemonic   | Instruction                                                                             | See                            |
|------------|-----------------------------------------------------------------------------------------|--------------------------------|
| CNTP       | Set scalar to count from predicate-as-counter                                           | CNTP (predicate as counter)    |
| PEXT       | Set pair of predicates from predicate-as-counter                                        | PEXT (predicate pair)          |
| PEXT       | Set predicate from predicate-as-counter                                                 | PEXT (predicate)               |
| PTRUE      | Initialize predicate-as-counter to all active                                           | PTRUE (predicate as counter)   |
| WHILEGE    | While decrementing signed scalar greater than or equal to scalar (predicate-as-counter) | WHILEGE (predicate as counter) |
| WHILEGT    | While decrementing signed scalar greater than scalar (predicate-as-counter)             | WHILEGT (predicate as counter) |
| WHILEHI    | While decrementing unsigned scalar higher than scalar (predicate-as-counter)            | WHILEHI (predicate as counter) |
| WHILEHS    | While decrementing unsigned scalar higher or same as scalar (predicate-as-counter)      | WHILEHS (predicate as counter) |
| WHILELE    | While incrementing signed scalar less than or equal to scalar (predicate-as-counter)    | WHILELE (predicate as counter) |
| WHILELO    | While incrementing unsigned scalar lower than scalar (predicate-as-counter)             | WHILELO (predicate as counter) |
| WHILELS    | While incrementing unsigned scalar lower or same as scalar (predicate-as-counter)       | WHILELS (predicate as counter) |
| WHILELT    | While incrementing signed scalar less than scalar (predicate-as-counter)                | WHILELT (predicate as counter) |

## C3.10.34 Permute vector

This instruction is a fixed permute instruction, which is a doubleword variant of the reverse within elements instructions.

## Table C3-238 SVE2.1 Permute vector instruction

| Mnemonic   | Instruction                                         | See   |
|------------|-----------------------------------------------------|-------|
| REVD       | Reverse 64-bit doublewords in elements (predicated) | REVD  |

## C3.10.35 Predicate pair loop control

Generate a pair of predicate registers to simplify loop unrolling.

## Table C3-239 SVE2.1 Predicate pair loop control instructions

| Mnemonic   | Instruction                                                                           | See                      |
|------------|---------------------------------------------------------------------------------------|--------------------------|
| WHILEGE    | While decrementing signed scalar greater than or equal to scalar (pair of predicates) | WHILEGE (predicate pair) |
| WHILEGT    | While decrementing signed scalar greater than scalar (pair of predicates)             | WHILEGT (predicate pair) |
| WHILEHI    | While decrementing unsigned scalar higher than scalar (pair of predicates)            | WHILEHI (predicate pair) |
| WHILEHS    | While decrementing unsigned scalar higher or same as scalar (pair of predicates)      | WHILEHS (predicate pair) |
| WHILELE    | While incrementing signed scalar less than or equal to scalar (pair of predicates)    | WHILELE (predicate pair) |
| WHILELO    | While incrementing unsigned scalar lower than scalar (pair of predicates)             | WHILELO (predicate pair) |
| WHILELS    | While incrementing unsigned scalar lower or same as scalar (pair of predicates)       | WHILELS (predicate pair) |
| WHILELT    | While incrementing signed scalar less than scalar (pair of predicates)                | WHILELT (predicate pair) |

## C3.10.36 Predicate move

With the PMOV (to predicate) instruction, based on the specified element size and immediate index, the selected bits in a vector register are expanded into a predicate register ready to be used as an SVE governing predicate.

With the PMOV (to vector) instruction a portion of a bitarray is created and can be stored to memory or further processed in registers.

## Table C3-240 SVE2.1 Predicate move instructions

| Mnemonic   | Instruction                | See                |
|------------|----------------------------|--------------------|
| PMOV       | Move predicate from vector | PMOV(to predicate) |
|            | Move predicate to vector   | PMOV(to vector)    |

## C3.10.37 Predicate select

PSEL places contents of the first source predicate register into a destination register or sets the destination to all-FALSE.

## Table C3-241 SVE2.1 Predicate select instruction

| Mnemonic   | Instruction                                              | See   |
|------------|----------------------------------------------------------|-------|
| PSEL       | Predicate select between predicate register or all-false | PSEL  |