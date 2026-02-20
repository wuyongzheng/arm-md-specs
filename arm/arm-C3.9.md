## C3.9 Data processing - SVE

The following subsections describe the SVE processing instructions:

- SVE Vector integer operations
- SVE Vector address calculation
- SVE Bitwise logical operations
- SVE Bitwise shift, reverse, and count
- SVE Vector floating-point operations
- Predicate operations
- Loop control
- SVE Move operations
- Index vector generation
- Move prefix
- Reduction operations

## C3.9.1 SVE Vector integer operations

## C3.9.1.1 SVE Integer arithmetic

For binary operations, the Integer arithmetic instructions perform arithmetic operations on a source vector containing integer element values, and a second source vector of either integer element values or an immediate value.

For ternary operations, these instructions perform arithmetic operations on a source vector containing integer element values, a second source vector of either integer element values or an immediate value, and a third source vector containing integer element values.

## Table C3-156 Integer arithmetic instructions

| Mnemonic   | Instruction                                             | See                                                 |
|------------|---------------------------------------------------------|-----------------------------------------------------|
| ABS        | Absolute value                                          | ABS                                                 |
| ADD        | Add vectors (predicated)                                | ADD(vectors, predicated)                            |
| ADD        | Add vectors (unpredicated)                              | ADD(vectors, unpredicated)                          |
| ADD        | Add immediate                                           | ADD(immediate)                                      |
| CNOT       | Logically invert Boolean condition                      | CNOT                                                |
| MAD        | Multiply-add, writing to the multiplicand register      | MAD                                                 |
| MLA        | Multiply-add, writing to the addend register            | MLA(indexed) MLA(vectors)                           |
| MLS        | Multiply-subtract, writing to the addend register       | MLS(indexed) MLS(vectors)                           |
| MSB        | Multiply-subtract, writing to the multiplicand register | MSB                                                 |
| MUL        | Multiply by immediate                                   | MUL(immediate)                                      |
| MUL        | Multiply vectors                                        | MUL(vectors, predicated) MUL(vectors, unpredicated) |
| NEG        | Negate                                                  | NEG                                                 |
| SABD       | Signed absolute difference                              | SABD                                                |
| SDIV       | Signed divide                                           | SDIV                                                |

| Mnemonic   | Instruction                            | See                                                       |
|------------|----------------------------------------|-----------------------------------------------------------|
| SDIVR      | Signed reversed divide                 | SDIVR                                                     |
| SMAX       | Signed maximum with immediate          | SMAX(immediate)                                           |
| SMAX       | Signed maximum vectors                 | SMAX(vectors)                                             |
| SMIN       | Signed minimum with immediate          | SMIN (immediate)                                          |
| SMIN       | Signed minimum vectors                 | SMIN (vectors)                                            |
| SMULH      | Signed multiply returning high half    | SMULH(predicated) SMULH(unpredicated)                     |
| SQADD      | Signed saturating add immediate        | SQADD(immediate)                                          |
| SQADD      | Signed saturating add vectors          | SQADD(vectors, predicated) SQADD(vectors, unpredicated)   |
| SQSUB      | Signed saturating subtract immediate   | SQSUB (immediate)                                         |
| SQSUB      | Signed saturating subtract vectors     | SQSUB (vectors, predicated) SQSUB (vectors, unpredicated) |
| SUB        | Subtract immediate                     | SUB (immediate)                                           |
| SUB        | Subtract vectors (predicated)          | SUB (vectors, predicated)                                 |
| SUB        | Subtract vectors (unpredicated)        | SUB (vectors, unpredicated)                               |
| SUBR       | Reversed subtract from immediate       | SUBR (immediate)                                          |
| SUBR       | Reversed subtract vectors              | SUBR (vectors)                                            |
| SXTB       | Signed byte extend                     | SXTB, SXTH,SXTW                                           |
| SXTH       | Signed halfword extend                 | SXTB, SXTH,SXTW                                           |
| SXTW       | Signed word extend                     | SXTB, SXTH,SXTW                                           |
| UABD       | Unsigned absolute difference           | UABD                                                      |
| UDIV       | Unsigned divide                        | UDIV                                                      |
| UDIVR      | Unsigned reversed divide               | UDIVR                                                     |
| UMAX       | Unsigned maximum with immediate        | UMAX(immediate)                                           |
| UMAX       | Unsigned maximum vectors               | UMAX(vectors)                                             |
| UMIN       | Unsigned minimum with immediate        | UMIN(immediate)                                           |
| UMIN       | Unsigned minimum vectors               | UMIN(vectors)                                             |
| UMULH      | Unsigned multiply returning high half  | UMULH(predicated) UMULH(unpredicated)                     |
| UQADD      | Unsigned saturating add immediate      | UQADD(immediate)                                          |
| UQADD      | Unsigned saturating add vectors        | UQADD(vectors, predicated) UQADD(vectors, unpredicated)   |
| UQSUB      | Unsigned saturating subtract immediate | UQSUB(immediate)                                          |
| UQSUB      | Unsigned saturating subtract vectors   | UQSUB(vectors, predicated) UQSUB(vectors, unpredicated)   |
| UXTB       | Unsigned byte extend                   | UXTB,UXTH,UXTW                                            |
| UXTH       | Unsigned halfword extend               |                                                           |
| UXTW       | Unsigned word extend                   | UXTB,UXTH,UXTW UXTB,UXTH,UXTW                             |

## C3.9.1.2 SVE Integer dot product

The Integer dot product instructions delimit the source vectors into groups of four 8-bit or 16-bit integer elements. Within each group of four elements, the elements in the first source vector are multiplied by the corresponding elements

in the second source vector. The resulting widened products are summed and added to the 32-bit or 64-bit element of the accumulator and destination vector that aligns with the group of four elements in the first source vector.

The indexed forms of these instructions specify a single, numbered, group of four elements within each 128-bit segment of the second source vector as the multiplier for all the groups of four elements within the corresponding 128-bit segment of the first source vector.

## Table C3-157 Integer dot product instructions

| Mnemonic   | Instruction                                                | See                   |
|------------|------------------------------------------------------------|-----------------------|
| SDOT       | Signed integer indexed dot product                         | SDOT (2-way, indexed) |
|            | Signed integer dot product                                 | SDOT (2-way, vectors) |
| SDOT       | Signed dot product by vector                               | SDOT (4-way, vectors) |
|            | Signed dot product by indexed elements                     | SDOT (4-way, indexed) |
| SUDOT      | Signed by unsigned integer dot product by indexed elements | SUDOT                 |
| UDOT       | Unsigned integer indexed dot product                       | UDOT(2-way, indexed)  |
|            | Unsigned integer dot product                               | UDOT(2-way, vectors)  |
| UDOT       | Unsigned dot product by vector                             | UDOT(4-way, vectors)  |
|            | Unsigned dot product by indexed elements                   | UDOT(4-way, indexed)  |
| USDOT      | Unsigned by signed integer dot product                     | USDOT(vectors)        |
|            | Unsigned by signed integer dot product by indexed elements | USDOT(indexed)        |

## C3.9.1.3 SVE Integer matrix multiply-accumulate

The Integer matrix multiply-accumulate instructions are implemented by FEAT\_I8MM.

The matrix multiply-accumulate instructions delimit source and destination vectors into 128-bit segments. The 128-bit segments are organized as follows:

- In the first source vector, a 2x8 matrix of 8-bit integers in row-by-row order.
- In the second source vector, an 8x2 matrix of 8-bit integers in column-by-column order.
- In the destination vector, a 2x2 matrix of 32-bit integers in row-by-row order.

One matrix multiplication is performed per vector segment and accumulated into the destination vector segment.

## Table C3-158 Integer matrix multiply operations

| Mnemonic   | Instruction                                                                  | See    |
|------------|------------------------------------------------------------------------------|--------|
| SMMLA      | Widening signed 8-bit integer matrix multiply-accumulate into 2x2 matrix     | SMMLA  |
| UMMLA      | Widening unsigned 8-bit integer matrix multiply-accumulate into 2x2 matrix   | UMMLA  |
| USMMLA     | Widening mixed sign 8-bit integer matrix multiply-accumulate into 2x2 matrix | USMMLA |

## C3.9.1.4 SVE Integer comparison

The Integer comparison instructions compare Active elements in the first source vector with the corresponding elements in a second vector or with an immediate value. The Boolean result of each comparison is placed in the corresponding element of the destination predicate. Inactive elements in the destination predicate register are set to FALSE. All integer comparisons set the N, Z, and C condition flags based on the predicate result, and set the V flag to zero.

The wide element variants of the compare instructions allow a packed vector of narrower elements to be compared with wider 64-bit elements. These instructions treat the second source vector as having a fixed 64-bit doubleword element size and compare each narrow element of the first source vector with the corresponding vertically-aligned wide element of the second source vector. For example, if the first source vector contained 8-bit byte elements, then 8-bit element[0] to element[7] of the first source vector are compared with 64-bit element[0] of the second source vector, 8-bit element[8] to element[15] with 64-bit element[1], and so on. All 64 bits of the wide elements are significant for the comparison, with the narrow elements being sign-extended or zero-extended to 64 bits as appropriate for the type of comparison.

Table C3-159 Integer comparison instructions

| Mnemonic   | Instruction                                           | See                                           |
|------------|-------------------------------------------------------|-----------------------------------------------|
| CMPEQ      | Compare signed equal to immediate                     | CMP<cc> (immediate) Equal                     |
| CMPEQ      | Compare signed equal to wide elements                 | CMP<cc> (wide elements) Equal                 |
| CMPEQ      | Compare signed equal to vector                        | CMP<cc> (vectors) Equal                       |
| CMPGE      | Compare signed greater than or equal to immediate     | CMP<cc> (immediate) Greater than or equal     |
| CMPGE      | Compare signed greater than or equal to wide elements | CMP<cc> (wide elements) Greater than or equal |
| CMPGE      | Compare signed greater than or equal to vector        | CMP<cc> (vectors) Greater than or equal       |
| CMPGT      | Compare signed greater than immediate                 | CMP<cc> (immediate) Greater than              |
| CMPGT      | Compare signed greater than wide elements             | CMP<cc> (wide elements) Greater than          |
| CMPGT      | Compare signed greater than vector                    | CMP<cc> (vectors) Greater than                |
| CMPHI      | Compare unsigned higher than immediate                | CMP<cc> (immediate) Higher                    |
| CMPHI      | Compare unsigned higher than wide elements            | CMP<cc> (wide elements) Higher                |
| CMPHI      | Compare unsigned higher than vector                   | CMP<cc> (vectors) Higher                      |
| CMPHS      | Compare unsigned higher than or same as immediate     | CMP<cc> (immediate) Higher or same            |
| CMPHS      | Compare unsigned higher than or same as wide elements | CMP<cc> (wide elements) Higher or same        |
| CMPHS      | Compare unsigned higher than or same as vector        | CMP<cc> (vectors) Higher or same              |
| CMPLE      | Compare signed less than or equal to immediate        | CMP<cc> (immediate) Less than or equal        |
| CMPLE      | Compare signed less than or equal to wide elements    | CMP<cc> (wide elements) Less than or equal    |
| CMPLE      | Compare signed less than or equal to vector           | CMPLE(vectors)                                |
| CMPLO      | Compare unsigned lower than immediate                 | CMP<cc> (immediate) Lower                     |
| CMPLO      | Compare unsigned lower than 64-bit wide elements      | CMP<cc> (wide elements) Lower                 |
| CMPLO      | Compare unsigned lower than vector                    | CMPLO(vectors)                                |
| CMPLS      | Compare unsigned lower or same as immediate           | CMP<cc> (immediate) Lower or same             |
| CMPLS      | Compare unsigned lower or same as wide elements       | CMP<cc> (wide elements) Lower or same         |
| CMPLS      | Compare unsigned lower or same as vector              | CMPLS (vectors)                               |
| CMPLT      | Compare signed less than immediate                    | CMP<cc> (immediate) Less than                 |
| CMPLT      | Compare signed less than wide elements                | CMP<cc> (wide elements) Less than             |
| CMPLT      | Compare signed less than vector                       | CMPLT (vectors)                               |
| CMPNE      | Compare not equal to immediate                        | CMP<cc> (immediate) Not equal                 |
| CMPNE      | Compare not equal to wide elements                    | CMP<cc> (wide elements) Not equal             |
| CMPNE      | Compare not equal to vector                           | CMP<cc> (vectors) Not equal                   |

## C3.9.2 SVE Vector address calculation

The Vector address calculation instructions compute vectors of addresses and addresses of vectors. This includes instructions to add a multiple of the current vector length or predicate register length, in bytes, to a general-purpose register.

The ADR instruction is an integer arithmetic operation that is used to calculate a vector of 64-bit or 32-bit addresses.

The ADR destination vector elements are computed by the addition of the corresponding elements in the source vectors, with an optional sign or zero extension and optional bitwise left shift of 1-3 bits applied to the final operands. This can be considered as the addition of a vector base and a scaled vector index.

The ADR instruction computes a vector of 32-bit addresses by the addition of a 32-bit base and a scaled 32-bit unsigned index. The ADR instruction computes a vector of 64-bit addresses by one of:

- Addition of a 64-bit base and a scaled 64-bit unsigned index.
- Addition of a 64-bit base and a scaled, zero-extended 32-bit index.
- Addition of a 64-bit base and a scaled, sign-extended 32-bit index.

## Table C3-160 Vector address calculation instructions

| Mnemonic   | Instruction                                                             | See   |
|------------|-------------------------------------------------------------------------|-------|
| ADDPL      | Add multiple of predicate register length, in bytes, to scalar register | ADDPL |
| ADDVL      | Add multiple of vector length, in bytes, to scalar register             | ADDVL |
| ADR        | Calculate vector of addresses                                           | ADR   |
| RDVL       | Read multiple of vector register length, in bytes, to scalar register   | RDVL  |

## C3.9.3 SVE Bitwise logical operations

The Bitwise logical operations instructions perform bitwise logical operations on vectors. Where operations are unpredicated, the operations are independent of the element size.

## Table C3-161 Bitwise logical operations

| Mnemonic   | Instruction                                          | See                         |
|------------|------------------------------------------------------|-----------------------------|
| AND        | Bitwise ANDvectors (predicated)                      | AND(vectors, predicated)    |
| AND        | Bitwise ANDvectors (unpredicated)                    | AND(vectors, unpredicated)  |
| AND        | Bitwise ANDwith immediate                            | AND(immediate)              |
| BIC        | Bitwise clear with vector (predicated)               | BIC (vectors, predicated)   |
| BIC        | Bitwise clear with vector (unpredicated)             | BIC (vectors, unpredicated) |
| BIC        | Bitwise clear using immediate                        | BIC (immediate)             |
| DUPM       | Broadcast bitmask immediate to vector (unpredicated) | DUPM                        |
| EON        | Bitwise exclusive-OR with inverted immediate         | EON                         |
| EOR        | Bitwise exclusive-OR vectors (predicated)            | EOR(vectors, predicated)    |
| EOR        | Bitwise exclusive-OR vectors (unpredicated)          | EOR(vectors, unpredicated)  |
| EOR        | Bitwise exclusive-OR with immediate                  | EOR(immediate)              |

| Mnemonic   | Instruction                       | See                        |
|------------|-----------------------------------|----------------------------|
| MOV        | Move bitmask immediate to vector  | MOV                        |
|            | Move vector register              | MOV(vector, unpredicated)  |
| NOT        | Bitwise invert vector             | NOT(vector)                |
| ORN        | Bitwise ORwith inverted immediate | ORN(immediate)             |
| ORR        | Bitwise ORvectors (predicated)    | ORR(vectors, predicated)   |
|            | Bitwise ORvectors (unpredicated)  | ORR(vectors, unpredicated) |
|            | Bitwise ORwith immediate          | ORR(immediate)             |

## C3.9.4 SVE Bitwise shift, reverse, and count

Bitwise shifts, reversals, and counts within vector elements.

Shift counts saturate at the number of bits per element, rather than being used modulo the element size. If modulo behavior is required, then the modulus must be computed separately.

The wide element variants of the bitwise shift instructions allow a packed vector of narrower elements to be shifted by wider 64-bit shift amounts. These instructions treat the second source vector as having a fixed 64-bit doubleword element size and shift each narrow element of the first source vector by the corresponding vertically-aligned wide element of the second source vector. For example, if the first source vector contained 8-bit byte elements, then 8-bitelement[0] to element[7] of the first vector are shifted by 64-bit element[0] of the second source vector, 8-bit element [8] to element[15] by 64-bit element[1], and so on. All 64 bits of the wide shift amount are significant.

Table C3-162 Bitwise shift, reverse, and count instructions

| Mnemonic   | Instruction                                            | See                               |
|------------|--------------------------------------------------------|-----------------------------------|
| ASR        | Arithmetic shift right by immediate (predicated)       | ASR (immediate, predicated)       |
| ASR        | Arithmetic shift right by immediate (unpredicated)     | ASR (immediate, unpredicated)     |
| ASR        | Arithmetic shift right by wide elements (predicated)   | ASR (wide elements, predicated)   |
| ASR        | Arithmetic shift right by wide elements (unpredicated) | ASR (wide elements, unpredicated) |
| ASR        | Arithmetic shift right by vector                       | ASR (vectors)                     |
| ASRD       | Arithmetic shift right for divide by immediate         | ASRD                              |
| ASRR       | Reversed arithmetic shift right by vector              | ASRR                              |
| CLS        | Count leading sign bits                                | CLS                               |
| CLZ        | Count leading zero bits                                | CLZ                               |
| CNT        | Count nonzero bits                                     | CNT                               |
| LSL        | Logical shift left by immediate (predicated)           | LSL (immediate, predicated)       |
| LSL        | Logical shift left by immediate (unpredicated)         | LSL (immediate, unpredicated)     |
| LSL        | Logical shift left by wide elements (predicated)       | LSL (wide elements, predicated)   |
| LSL        | Logical shift left by wide elements (unpredicated)     | LSL (wide elements, unpredicated) |
| LSL        | Logical shift left by vector                           | LSL (vectors)                     |
| LSLR       | Reversed logical shift left by vector                  | LSLR                              |
| LSR        | Logical shift right by immediate (predicated)          | LSR (immediate, predicated)       |
| LSR        | Logical shift right by immediate (unpredicated)        | LSR (immediate, unpredicated)     |

| Mnemonic   | Instruction                                         | See                               |
|------------|-----------------------------------------------------|-----------------------------------|
|            | Logical shift right by wide elements (predicated)   | LSR (wide elements, predicated)   |
|            | Logical shift right by wide elements (unpredicated) | LSR (wide elements, unpredicated) |
|            | Logical shift right by vector                       | LSR (vectors)                     |
| LSRR       | Reversed logical shift right by vector              | LSRR                              |
| RBIT       | Reverse bits                                        | RBIT                              |

## C3.9.5 SVE Vector floating-point operations

The following instructions operate on floating-point data within a vector.

## C3.9.5.1 SVE Floating-point arithmetic

The Floating-point arithmetic instructions perform arithmetic operations on vectors containing floating-point element values.

Table C3-163 Floating-point arithmetic instructions

| Mnemonic   | Instruction                                    | See                         |
|------------|------------------------------------------------|-----------------------------|
| FABD       | Floating-point absolute difference             | FABD                        |
| FABS       | Floating-point absolute value                  | FABS                        |
| FADD       | Floating-point add (immediate)                 | FADD(immediate)             |
| FADD       | Floating-point add (predicated)                | FADD(vectors, predicated)   |
| FADD       | Floating-point add (unpredicated)              | FADD(vectors, unpredicated) |
| FDIV       | Floating-point divide                          | FDIV                        |
| FDIVR      | Floating-point reversed divide                 | FDIVR                       |
| FMAX       | Floating-point maximum with immediate          | FMAX(immediate)             |
| FMAX       | Floating-point maximum vectors                 | FMAX(vectors)               |
| FMAXNM     | Floating-point maximum number with immediate   | FMAXNM(immediate)           |
| FMAXNM     | Floating-point maximum number vectors          | FMAXNM(vectors)             |
| FMIN       | Floating-point minimum with immediate          | FMIN (immediate)            |
| FMIN       | Floating-point minimum vectors                 | FMIN (vectors)              |
| FMINNM     | Floating-point minimum number with immediate   | FMINNM(immediate)           |
| FMINNM     | Floating-point minimum number vectors          | FMINNM(vectors)             |
| FMUL       | Floating-point multiply by immediate           | FMUL(immediate)             |
| FMUL       | Floating-point multiply vectors (predicated)   | FMUL(vectors, predicated)   |
| FMUL       | Floating-point multiply vectors (unpredicated) | FMUL(vectors, unpredicated) |
| FMULX      | Floating-point multiply-extended               | FMULX                       |
| FNEG       | Floating-point negate                          | FNEG                        |
| FRECPE     | Floating-point reciprocal estimate             | FRECPE                      |
| FRECPS     | Floating-point reciprocal step                 | FRECPS                      |
| FRECPX     | Floating-point reciprocal exponent             | FRECPX                      |

| Mnemonic   | Instruction                                     | See                          |
|------------|-------------------------------------------------|------------------------------|
| FRSQRTE    | Floating-point reciprocal square root estimate  | FRSQRTE                      |
| FRSQRTS    | Floating-point reciprocal square root step      | FRSQRTS                      |
| FSCALE     | Floating-point adjust exponent by vector        | FSCALE                       |
| FSQRT      | Floating-point square root                      | FSQRT                        |
| FSUB       | Floating-point subtract immediate               | FSUB (immediate)             |
| FSUB       | Floating-point subtract vectors (predicated)    | FSUB (vectors, predicated)   |
| FSUB       | Floating-point subtract vectors (unpredicated)  | FSUB (vectors, unpredicated) |
| FSUBR      | Floating-point reversed subtract from immediate | FSUBR (immediate)            |
| FSUBR      | Floating-point reversed subtract vectors        | FSUBR (vectors)              |

## C3.9.5.2 SVE Floating-point multiply accumulate

The Floating-point multiply accumulate instructions perform floating-point fused multiply-add or multiply-subtract operations and their negated forms. There are two groups of these instructions, as follows:

- Instructions where the result of the operation is written to the addend register.
- -Supported instructions are: FMLA, FMLS, FNMLA, FNMLS.
- Instructions where the result of the operation is written to the multiplicand register.
- -Supported instructions are: FMAD, FMSB, FNMAD, FNMSB.

## Table C3-164 Floating-point multiply accumulate instructions

| Mnemonic   | Instruction                                                                         | See                               |
|------------|-------------------------------------------------------------------------------------|-----------------------------------|
| FMLA       | Floating-point fused multiply-add vectors, writing to the addend                    | FMLA(indexed) FMLA(vectors)       |
| FMLS       | Floating-point fused multiply-subtract vectors, writing to the addend               | FMLS (indexed) FMLS (vectors)     |
| FNMLA      | Floating-point negated fused multiply-add vectors, writing to the addend            | FNMLA                             |
| FNMLS      | Floating-point negated fused multiply-subtract vectors, writing to the addend       | FNMLS                             |
| FMAD       | Floating-point fused multiply-add vectors, writing to the multiplicand              | FMAD                              |
| FMSB       | Floating-point fused multiply-subtract vectors, writing to the multiplicand         | FMLSLB (indexed) FMLSLB (vectors) |
| FNMAD      | Floating-point negated fused multiply-add vectors, writing to the multiplicand      | FNMAD                             |
| FNMSB      | Floating-point negated fused multiply-subtract vectors, writing to the multiplicand | FNMSB                             |

## C3.9.5.3 SVE Floating-point complex arithmetic

The Floating-point complex arithmetic instructions perform arithmetic on vectors containing floating-point complex numbers as interleaved pairs of elements, where the even-numbered elements contain the real components and the odd-numbered elements contain the imaginary components.

The FCADD instructions rotate the complex numbers in the second source vector by 90 degrees or 270 degrees in the direction from the positive real axis towards the positive imaginary axis, when considered in polar representation, before adding active pairs of elements to the corresponding elements of the first source vector in a destructive manner.

The FCMLA instructions perform a transformation of the operands to allow the creation of multiply-add or multiply-subtract operations on complex numbers by combining two of the instructions. The transformations performed are as follows:

- The complex numbers in the second source vector, considered in polar form, are rotated by 0 degrees or 180 degrees before multiplying by the duplicated real components of the first source vector.
- The complex numbers in the second source vector, considered in polar form, are rotated by 90 degrees or 270 degrees before multiplying by the duplicated imaginary components of the first source vector.

The resulting products are then added to the corresponding components of the destination and addend vector, without intermediate rounding.

Two FCMLA instructions can be used as follows:

```
FCMLA Zda.S, Pg/M, Zn.S, Zm.S, #A ... FCMLA Zda.S, Pg/M, Zn.S, Zm.S, #B
```

For example, some meaningful combinations of A and B are:

- A=0, B=90. In this case, the two vectors of complex numbers in Zn and Zm are multiplied and the products are added to the complex numbers in Zda.
- A=0, B=270. In this case, the conjugates of the complex numbers in Zn are multiplied by the complex numbers in Zm and the products are added to the complex numbers in Zda.
- A=180, B=270. In this case, the two vectors of complex numbers in Zn and Zm are multiplied and the products are subtracted from the complex numbers in Zda.
- A=180, B=90. In this case, the conjugates of the complex numbers in Zn are multiplied by the complex numbers in Zm and the products are subtracted from the complex numbers in Zda.

Note

The lack of intermediate rounding can give unexpected results in certain cases relative to a traditional sequence of independent multiply, add, and subtract instructions.

In addition, when using these instructions, the behavior of calculations such as ( ∞ + ∞ i) multiplied by (0+i) is (NaN+NaNi), rather than the result expected by ISO C, which is complex. The expectation is that these instructions are only used in situations where the effect of differences in the rounding and handling of infinities are not material to the calculation.

Table C3-165 Floating-point complex arithmetic instructions

| Mnemonic   | Instruction                                     | See            |
|------------|-------------------------------------------------|----------------|
| FCADD      | Floating-point complex add with rotate          | FCADD          |
| FCMLA      | Floating-point complex multiply-add with rotate | FCMLA(vectors) |

## C3.9.5.4 SVE Floating-point rounding and conversion

The Floating-point rounding and conversion instructions change floating-point size and precision, round floating-point to integral floating-point with explicit rounding mode, and convert floating-point to or from integer format.

Table C3-166 Floating-point rounding and conversion instructions

| Mnemonic   | Instruction                                                                 | See     |
|------------|-----------------------------------------------------------------------------|---------|
| BFCVT      | Floating-point down convert to BFloat16 format                              | BFCVT   |
| BFCVTNT    | Floating-point down convert and narrow to BFloat16 format (top, predicated) | BFCVTNT |

| Mnemonic   | Instruction                                                                   | See                                      |
|------------|-------------------------------------------------------------------------------|------------------------------------------|
| FCVT       | Floating-point convert precision                                              | FCVT                                     |
| FCVTZS     | Floating-point convert to signed integer, rounding toward zero                | FCVTZS                                   |
| FCVTZU     | Floating-point convert to unsigned integer, rounding toward zero              | FCVTZU                                   |
| FRINTA     | Floating-point round to integral value, to nearest with ties away from zero   | FRINT<r> Nearest with ties to away       |
| FRINTI     | Floating-point round to integral value, using the current rounding mode       | FRINT<r> Current mode                    |
| FRINTM     | Floating-point round to integral value, toward minus infinity                 | FRINT<r> Toward minus infinity           |
| FRINTN     | Floating-point round to integral value, to nearest with ties to even          | FRINT<r> Nearest with ties to even       |
| FRINTP     | Floating-point round to integral value, toward plus infinity                  | FRINT<r> Toward plus infinity            |
| FRINTX     | Floating-point round to integral value exact, using the current rounding mode | FRINT<r> Current mode signalling inexact |
| FRINTZ     | Floating-point round to integral value, toward zero                           | FRINT<r> Toward zero                     |
| SCVTF      | Signed integer convert to floating-point                                      | SCVTF                                    |
| UCVTF      | Unsigned integer convert to floating-point                                    | UCVTF                                    |

## C3.9.5.5 SVE Floating-point comparisons

The Floating-point comparison instructions compare active floating-point element values in the first source vector with corresponding elements in the second vector or with the immediate value +0.0. The Boolean result of each comparison is placed in the corresponding element of the destination predicate. Inactive elements in the destination predicate register are set to FALSE. Floating-point vector comparisons do not set the condition flags.

Table C3-167 Floating-point comparison instructions

| Mnemonic   | Instruction                                            | See                                       |
|------------|--------------------------------------------------------|-------------------------------------------|
| FACGE      | Floating-point absolute compare greater than or equal  | FAC<cc> - Greater than or equal           |
| FACGT      | Floating-point absolute compare greater than           | FAC<cc> - Greater than                    |
| FACLE      | Floating-point absolute compare less than or equal     | FACLE                                     |
| FACLT      | Floating-point absolute compare less than              | FACLT                                     |
| FCMEQ      | Floating-point compare equal to zero                   | FCM<cc> (zero) - Equal                    |
|            | Floating-point compare equal to vector                 | FCM<cc> (vectors) - Equal                 |
| FCMGE      | Floating-point compare greater than or equal to zero   | FCM<cc> (zero) - Greater than or equal    |
|            | Floating-point compare greater than or equal to vector | FCM<cc> (vectors) - Greater than or equal |
| FCMGT      | Floating-point compare greater than zero               | FCM<cc> (zero) - Greater than             |
|            | Floating-point compare greater than vector             | FCM<cc> (vectors) - Greater than          |
| FCMLE      | Floating-point compare less than or equal to zero      | FCM<cc> (zero) - Less than or equal       |
|            | Floating-point compare less than or equal to vector    | FCMLE(vectors)                            |
| FCMLT      | Floating-point compare less than zero                  | FCM<cc> (zero) - Less than                |
|            | Floating-point compare less than vector                | FCMLT (vectors)                           |
| FCMNE      | Floating-point compare not equal to zero               | FCM<cc> (zero) - Not equal                |
|            | Floating-point compare not equal to vector             | FCM<cc> (vectors) - Not equal             |
| FCMUO      | Floating-point unordered vectors                       | FCM<cc> (vectors) - Unordered             |

| Mnemonic   | Instruction   | See   |
|------------|---------------|-------|

## C3.9.5.6 SVE Floating-point transcendental acceleration

The Floating-point transcendental instructions accelerate calculations of sine, cosine, and exponential functions for vectors containing floating-point element values.

The trigonometric instructions accelerate the calculation of a polynomial series approximation for the sine and cosine functions. The exponential instruction accelerates the polynomial series calculation of the exponential function.

## Table C3-168 Floating-point transcendental instructions

| Mnemonic   | Instruction                                           | See    |
|------------|-------------------------------------------------------|--------|
| FTMAD      | Floating-point trigonometric multiply-add coefficient | FTMAD  |
| FTSMUL     | Floating-point trigonometric starting value           | FTSMUL |
| FTSSEL     | Floating-point trigonometric select coefficient       | FTSSEL |
| FEXPA      | Floating-point exponential accelerator                | FEXPA  |

## C3.9.5.7 SVE Floating-point indexed multiples

The Floating-point indexed multiples instructions multiply all floating-point elements within each 128-bit segment of the first source vector by the single numbered element within the corresponding segment of the second source vector.

For the FMLA and FMLS instructions, the products are destructively added or subtracted from the corresponding elements of the addend and destination vector, without intermediate rounding.

## Table C3-169 Floating-point indexed multiples instructions

| Mnemonic   | Instruction                                                | See            |
|------------|------------------------------------------------------------|----------------|
| FMLA       | Floating-point fused multiply-add by indexed elements      | FMLA(indexed)  |
| FMLS       | Floating-point fused multiply-subtract by indexed elements | FMLS (indexed) |
| FMUL       | Floating-point multiply by indexed elements                | FMUL(indexed)  |

## C3.9.5.8 SVE Floating-point matrix multiply-accumulate and companion instructions

The floating-point matrix multiply-accumulate and companion instructions facilitate matrix multiplication computation.

The matrix multiply-accumulate instructions delimit source and destination vectors into segments. The segments are organized as follows:

- In the first source vector, a 2x2 matrix in row-by-row order.
- In the second source vector, a 2x2 matrix in column-by-column order.
- In the destination vector, a 2x2 matrix in row-by-row order.

One matrix multiplication is performed per vector segment and accumulated into the destination vector segment. For the double-precision matrix multiply-accumulate instructions, the vector segment length and minimum vector length is 256 bits. Double-precision matrix multiply-accumulate instructions are not supported when the vector length is 128 bits. For the single-precision matrix multiply-accumulate instruction, the vector segment length is 128 bits.

The floating-point matrix multiply-accumulate instructions strictly define the order of accumulations, and the multiplications and additions are not fused, so intermediate rounding is performed after every multiplication and every addition.

The companion instructions support data rearrangements in vector registers as required by the double-precision matrix multiply-accumulate instructions.

The following table shows the floating-point matrix multiplication instructions and companion instructions that are implemented by FEAT\_F64MM:

## Table C3-170 Floating-point matrix multiply instructions

| Mnemonic    | Instruction                                                                  | See                            |
|-------------|------------------------------------------------------------------------------|--------------------------------|
| FMMLA       | Floating-point matrix multiply-accumulate into 2x2 matrix (double-precision) | FMMLA                          |
| LD1ROB      | Contiguous load and replicate thirty-two bytes, scalar plus scalar           | LD1ROB (scalar plus scalar)    |
| LD1ROB      | Contiguous load and replicate thirty-two bytes, scalar plus immediate        | LD1ROB (scalar plus immediate) |
| LD1ROD      | Contiguous load and replicate four doublewords, scalar plus scalar           | LD1ROD (scalar plus scalar)    |
| LD1ROD      | Contiguous load and replicate four doublewords, scalar plus immediate        | LD1ROD (scalar plus immediate) |
| LD1ROH      | Contiguous load and replicate sixteen halfwords, scalar plus scalar          | LD1ROH (scalar plus scalar)    |
| LD1ROH      | Contiguous load and replicate sixteen halfwords, scalar plus immediate       | LD1ROH (scalar plus immediate) |
| LD1ROW      | Contiguous load and replicate eight words, scalar plus scalar                | LD1ROW(scalar plus scalar)     |
| LD1ROW      | Contiguous load and replicate eight words, scalar plus immediate             | LD1ROW(scalar plus immediate)  |
| TRN1 , TRN2 | Interleave even or odd 128-bit elements from two vectors                     | TRN1, TRN2 (vectors)           |
| UZP1 , UZP2 | Concatenate even or odd 128-bit elements from two vectors                    | UZP1, UZP2 (vectors)           |
| ZIP1 , ZIP2 | Interleave 128-bit elements from two half vectors                            | ZIP1, ZIP2 (vectors)           |

The following table shows the floating-point matrix multiplication instruction, which is implemented by FEAT\_F32MM:

| Mnemonic   | Instruction                                                                  | See   |
|------------|------------------------------------------------------------------------------|-------|
| FMMLA      | Floating-point matrix multiply-accumulate into 2x2 matrix (single-precision) | FMMLA |

## C3.9.5.9 SVE BFloat16 floating-point multiply-add

The BFloat16 floating-point multiply-add instructions perform an implicit conversion of the bottom (even-numbered) or top (odd-numbered) BFloat16 source elements to IEEE 754 single-precision floating-point format before performing a fused multiply-add without intermediate rounding to the overlapping single-precision destination element. These instructions follow the normal floating-point behaviors that apply to single-precision arithmetic, controlled by the Effective value of the FPCR, and captured in the FPSR cumulative exception bits.

## Table C3-172 SVE BFloat16 floating-point multiply-add instructions

| Mnemonic   | Instruction                                                                                 | See                                 |
|------------|---------------------------------------------------------------------------------------------|-------------------------------------|
| BFMLALB    | BFloat16 floating-point widening multiply accumulate long bottom (vector and indexed forms) | BFMLALB(vectors) BFMLALB(indexed)   |
| BFMLALT    | BFloat16 floating-point widening multiply accumulate long top (vector and indexed forms)    | BFMLALT (vectors) BFMLALT (indexed) |

| Mnemonic   | Instruction                                                                            | See               |
|------------|----------------------------------------------------------------------------------------|-------------------|
| BFMLSLB    | BFloat16 floating-point multiply-subtract long from single-precision (bottom, indexed) | BFMLSLB (indexed) |
|            | BFloat16 floating-point multiply-subtract long from single-precision (bottom)          | BFMLSLB (vectors) |
| BFMLSLT    | BFloat16 floating-point multiply-subtract long from single-precision (top, indexed)    | BFMLSLT (indexed) |
|            | BFloat16 floating-point multiply-subtract long from single-precision (top)             | BFMLSLT (vectors) |

## C3.9.5.10 SVE BFloat16 floating-point dot product

The BFloat16 floating-point dot product instruction, BFDOT , performs an implicit conversion of vectors of BFloat16 input values to IEEE 754 single-precision floating-point format.

The BFloat16 dot product instructions delimit their source vectors into pairs of BFloat16 elements.

## Table C3-173 SVE BFloat16 floating-point dot product instructions

| Mnemonic   | Instruction                                                    | See                             |
|------------|----------------------------------------------------------------|---------------------------------|
| BFDOT      | BFloat16 floating-point dot product (vector and indexed forms) | BFDOT (vectors) BFDOT (indexed) |

## C3.9.5.11 SVE BFloat16 floating-point matrix multiply-accumulate

The BFloat16 floating-point matrix multiply-accumulate instruction, BFMMLA , is implemented by FEAT\_BF16.

This instruction delimits the source and destination vectors into 128-bit segments. The 128-bit segments are organized as follows:

- In the first source vector, a 2x4 matrix of BFloat16 values in row-by-row order.
- In the second source vector, a 4x2 matrix of BFloat16 values in column-by-column order.
- In the destination vector, a 2x2 matrix of single-precision values in row-by-row order.

One matrix multiplication is performed per source vector segment and accumulated into the corresponding destination vector segment. This corresponds to accumulating two 2-way BFloat16 widening dot products into each single-precision destination element, following the numeric behaviors described for BFDOT instruction in SVE BFloat16 floating-point dot product.

## Table C3-174 SVE BFloat16 floating-point matrix multiply instruction

| Mnemonic   | Instruction                                        | See    |
|------------|----------------------------------------------------|--------|
| BFMMLA     | BFloat16 floating-point matrix multiply-accumulate | BFMMLA |

## C3.9.5.12 SVE BFloat16 floating-point convert

The BFloat16 floating-point convert instructions perform accurately rounded down-conversion of IEEE 754 single-precision source vector elements to BFloat16 format.

The BFCVT instruction places its BFloat16 results in the bottom or even-numbered 16-bit elements of the destination vector, and sets the top or odd-numbered elements to zero.

The BFCVTNT instruction places its BFloat16 results in the top or odd-numbered 16-bit elements of the destination vector, leaving the bottom or even-numbered elements unchanged.

These instructions follow the normal floating-point behaviors that apply to single-precision arithmetic, controlled by the Effective value of the FPCR, and captured in the FPSR cumulative exception bits.

## Table C3-175 SVE BFloat16 floating-point convert instructions

| Mnemonic   | Instruction                                                          | See     |
|------------|----------------------------------------------------------------------|---------|
| BFCVT      | Floating-point down convert to BFloat16 format (predicated)          | BFCVT   |
| BFCVTNT    | Floating-point down convert and narrow to BFloat16 (top, predicated) | BFCVTNT |

## C3.9.6 Predicate operations

The Predicate instructions perform operations that manipulate the predicate registers.

Some of these instructions are insensitive to the predicate element size and specify an explicit byte element size qualifier, .B, but an assembler must accept any qualifier, or none.

## C3.9.6.1 SVE Predicate initialization

The Predicate initialization instructions initialize predicate elements.Predicate elements can be initialized to be FALSE, or to be TRUE when their element number is less than:

- Afixed number of elements from the following range: VL1-VL8, VL16, VL32, VL64, VL128 or VL256.
- The largest power of two elements, POW2.
- The largest multiple of three or four elements, MUL3 or MUL4.
- The number of accessible elements, ALL, which is implicitly a multiple of two.

Unspecified or out of range constraint encodings generate a predicate with values that are all FALSE and do not cause an Undefined Instruction exception.

## Table C3-176 Predicate initialization instructions

| Mnemonic   | Instruction                                                                      | See               |
|------------|----------------------------------------------------------------------------------|-------------------|
| PFALSE     | Set all predicate elements to FALSE                                              | PFALSE            |
| PTRUE      | Initialize predicate elements from named constraint                              | PTRUE (predicate) |
| PTRUES     | Initialize predicate elements from named constraint, setting the condition flags | PTRUES            |

## C3.9.6.2 SVE Predicate move operations

The Predicate move instructions operate on all bits of the predicate registers, implying a fixed, 1-bit predicate element size. The flag-setting variants set the N, Z, and C condition flags based on the predicate result, and set the V flag to zero. Because these instructions operate with a fixed, 1-bit element size, the Governing predicate for the flag-setting variants should be in the canonical form for a predicate element size in order to generate a meaningful set of condition flags for that element size.

## Table C3-177 Predicate move instructions

| Mnemonic   | Instruction                                   | See              |
|------------|-----------------------------------------------|------------------|
| SEL        | Select predicate elements from two predicates | SEL (predicates) |

| Mnemonic   | Instruction                                                         | See                                 |
|------------|---------------------------------------------------------------------|-------------------------------------|
| MOV        | Move predicate elements (predicated, merging)                       | MOV(predicate, predicated, merging) |
|            | Move predicate elements (predicated, zeroing)                       | MOV(predicate, predicated, zeroing) |
|            | Move predicate elements (unpredicated)                              | MOV                                 |
| MOVS       | Move predicate elements, setting the condition flags (predicated)   | MOVS(predicated)                    |
|            | Move predicate elements, setting the condition flags (unpredicated) | MOVS(unpredicated)                  |

## C3.9.6.3 SVE Predicate logical operations

The Predicate logical operation instructions perform bitwise logical operations on predicate registers that operate on all bits of the register, implying a fixed, 1-bit predicate element size. The flag-setting variants set the N, Z, and C condition flags based on the predicate result, and set the V flag to zero. Inactive elements in the destination Predicate register are set to zero, except for PTEST which does not specify a destination register. Because these instructions operate with a fixed, 1-bit element size, the Governing predicate for the flag-setting variants should be in the canonical form for a predicate element size in order to generate a meaningful set of condition flags for that element size.

## Table C3-178 Predicate logical operation instructions

| Mnemonic   | Instruction                                                  | See              |
|------------|--------------------------------------------------------------|------------------|
| AND        | Bitwise ANDpredicates                                        | AND(predicates)  |
| ANDS       | Bitwise ANDpredicates, setting the condition flags           | ANDS             |
| BIC        | Bitwise clear predicates                                     | BIC (predicates) |
| BICS       | Bitwise clear predicates, setting the condition flags        | BICS             |
| EOR        | Bitwise exclusive-OR predicates                              | EOR(predicates)  |
| EORS       | Bitwise exclusive-OR predicates, setting the condition flags | EORS             |
| NAND       | Bitwise NANDpredicates                                       | NAND             |
| NANDS      | Bitwise NANDpredicates, setting the condition flags          | NANDS            |
| NOR        | Bitwise NORpredicates                                        | NOR              |
| NORS       | Bitwise NORpredicates, setting the condition flags           | NORS             |
| NOT        | Bitwise invert predicate                                     | NOT(predicate)   |
| NOTS       | Bitwise invert predicate, setting the condition flags        | NOTS             |
| ORN        | Bitwise ORinverted predicate                                 | ORN(predicates)  |
| ORNS       | Bitwise ORinverted predicate, setting the condition flags    | ORNS             |
| ORR        | Bitwise ORpredicates                                         | ORR(predicates)  |
| ORRS       | Bitwise ORpredicates, setting the condition flags            | ORRS             |
| PTEST      | Test predicate value, setting the condition flags            | PTEST            |

## C3.9.6.4 FFR predicate handling

The FFR predicate handling instructions work with SVE First-fault and Non-fault loads using the FFR to determine which elements have been successfully loaded and which remain to be loaded on a subsequent iteration.

The RDFFRS instruction sets the N, Z, and C condition flags based on the predicate result, and sets the V flag to zero. Because these instructions operate with a fixed, 1-bit element size, the Governing predicate for the RDFFRS instruction should be in the canonical form for a predicate element size in order to generate a meaningful set of condition flags for that element size.

## Table C3-179 FFR predicate handling instructions

| Mnemonic   | Instruction                                                                                | See                  |
|------------|--------------------------------------------------------------------------------------------|----------------------|
| RDFFR      | Return predicate of successfully loaded elements (unpredicated)                            | RDFFR (unpredicated) |
|            | Return predicate of successfully loaded elements (predicated)                              | RDFFR (predicated)   |
| RDFFRS     | Return predicate of successfully loaded elements, setting the condition flags (predicated) | RDFFRS               |
| SETFFR     | Initialize the First-fault register to all TRUE                                            | SETFFR               |
| WRFFR      | Write a predicate register to the First-fault register                                     | WRFFR                |

## C3.9.6.5 Predicate count

The Predicate count instructions count either the number of Active predicate elements that are set to TRUE, or the number of elements implied by a named predicate constraint. The count can be placed in a general-purpose register, or used to increment or decrement a vector or general-purpose register.

Signed or unsigned saturating variants handle cases where, for example, an increment might cause a vectorized scalar loop index to overflow and therefore never satisfy a loop termination condition that compares it with a limit that is close to the maximum integer value.

The named predicate constraint limits the number of elements to:

- Afixed number of elements from the following range: VL1-VL8, VL16, VL32, VL64, VL128 or VL256.
- The largest power of two elements, POW2.
- The largest multiple of three or four elements, MUL3 or MUL4.
- The number of accessible elements, ALL, implicitly a multiple of two.

Unspecified or out of range predicate constraint encodings generate a zero element count and do not cause an Undefined Instruction exception.

## Table C3-180 Predicate count instructions

| Mnemonic   | Instruction                                                               | See                          |
|------------|---------------------------------------------------------------------------|------------------------------|
| CNTB       | Set scalar to multiple of 8-bit predicate constraint element count        | CNTB,CNTD,CNTH,CNTW          |
| CNTH       | Set scalar to multiple of 16-bit predicate constraint element count       | CNTB,CNTD,CNTH,CNTW          |
| CNTW       | Set scalar to multiple of 32-bit predicate constraint element count       | CNTB,CNTD,CNTH,CNTW          |
| CNTD       | Set scalar to multiple of 64-bit predicate constraint element count       | CNTB,CNTD,CNTH,CNTW          |
| CNTP       | Set scalar to the number of Active predicate elements that are TRUE       | CNTP (predicate)             |
| DECB       | Decrement scalar by multiple of 8-bit predicate constraint element count  | DECB,DECD,DECH,DECW (scalar) |
| DECH       | Decrement scalar by multiple of 16-bit predicate constraint element count | DECB,DECD,DECH,DECW (scalar) |
| DECH       | Decrement vector by multiple of 16-bit predicate constraint element count | DECD, DECH, DECW(vector)     |
| DECW       | Decrement scalar by multiple of 32-bit predicate constraint element count | DECB,DECD,DECH,DECW (scalar) |
| DECW       | Decrement vector by multiple of 32-bit predicate constraint element count | DECD, DECH, DECW(vector)     |

| Mnemonic   | Instruction                                                                                 | See                            |
|------------|---------------------------------------------------------------------------------------------|--------------------------------|
| DECD       | Decrement scalar by multiple of 64-bit predicate constraint element count                   | DECB,DECD,DECH,DECW (scalar)   |
|            | Decrement vector by multiple of 64-bit predicate constraint element count                   | DECD, DECH, DECW(vector)       |
| DECP       | Decrement scalar by the number of predicate elements that are TRUE                          | DECP (scalar)                  |
|            | Decrement vector by the number of Active predicate elements that are TRUE                   | DECP (vector)                  |
| INCB       | Increment scalar by multiple of 8-bit predicate constraint element count                    | INCB, INCD, INCH,INCW (scalar) |
| INCH       | Increment scalar by multiple of 16-bit predicate constraint element count                   | INCB, INCD, INCH,INCW (scalar) |
|            | Increment vector by multiple of 16-bit predicate constraint element count                   | INCD, INCH, INCW(vector)       |
| INCW       | Increment scalar by multiple of 32-bit predicate constraint element count                   | INCB, INCD, INCH,INCW (scalar) |
|            | Increment vector by multiple of 32-bit predicate constraint element count                   | INCD, INCH, INCW(vector)       |
| INCD       | Increment scalar by multiple of 64-bit predicate constraint element count                   | INCB, INCD, INCH,INCW (scalar) |
|            | Increment vector by multiple of 64-bit predicate constraint element count                   | INCD, INCH, INCW(vector)       |
| INCP       | Increment scalar by the number of predicate elements that are TRUE                          | INCP (scalar)                  |
|            | Increment vector by the number of predicate elements that are TRUE                          | INCP (vector)                  |
| SQDECB     | Signed saturating decrement scalar by multiple of 8-bit predicate constraint element count  | SQDECB                         |
| SQDECH     | Signed saturating decrement scalar by multiple of 16-bit predicate constraint element count | SQDECH(scalar)                 |
|            | Signed saturating decrement vector by multiple of 16-bit predicate constraint element count | SQDECH(vector)                 |
| SQDECW     | Signed saturating decrement scalar by multiple of 32-bit predicate constraint element count | SQDECW(scalar)                 |
|            | Signed saturating decrement vector by multiple of 32-bit predicate constraint element count | SQDECW(vector)                 |
| SQDECD     | Signed saturating decrement scalar by multiple of 64-bit predicate constraint element count | SQDECD(scalar)                 |
|            | Signed saturating decrement vector by multiple of 64-bit predicate constraint element count | SQDECD(vector)                 |
| SQDECP     | Signed saturating decrement scalar the number of predicate elements that are TRUE           | SQDECP (scalar)                |
|            | Signed saturating decrement vector by the number of predicate elements that are TRUE        | SQDECP (vector)                |
| SQINCB     | Signed saturating increment scalar by multiple of 8-bit predicate constraint element count  | SQINCB                         |
| SQINCH     | Signed saturating increment scalar by multiple of 16-bit predicate constraint element count | SQINCH (scalar)                |
|            | Signed saturating increment vector by multiple of 16-bit predicate constraint element count | SQINCH (vector)                |
| SQINCW     | Signed saturating increment scalar by multiple of 32-bit predicate constraint element count | SQINCW (scalar)                |
|            | Signed saturating increment vector by multiple of 32-bit predicate constraint element count | SQINCW (vector)                |

| Mnemonic   | Instruction                                                                                   | See             |
|------------|-----------------------------------------------------------------------------------------------|-----------------|
| SQINCD     | Signed saturating increment scalar by multiple of 64-bit predicate constraint element count   | SQINCD (scalar) |
| SQINCD     | Signed saturating increment vector by multiple of 64-bit predicate constraint element count   | SQINCD (vector) |
| SQINCP     | Signed saturating increment scalar by the number of predicate elements that are TRUE          | SQINCP (scalar) |
| SQINCP     | Signed saturating increment vector by the number of predicate elements that are TRUE          | SQINCP (vector) |
| UQDECB     | Unsigned saturating decrement scalar by multiple of 8-bit predicate constraint element count  | UQDECB          |
| UQDECH     | Unsigned saturating decrement scalar by multiple of 16-bit predicate constraint element count | UQDECH(scalar)  |
| UQDECH     | Unsigned saturating decrement vector by multiple of 16-bit predicate constraint element count | UQDECH(vector)  |
| UQDECW     | Unsigned saturating decrement scalar by multiple of 32-bit predicate constraint element count | UQDECW(scalar)  |
| UQDECW     | Unsigned saturating decrement vector by multiple of 32-bit predicate constraint element count | UQDECW(vector)  |
| UQDECD     | Unsigned saturating decrement scalar by multiple of 64-bit predicate constraint element count | UQDECD(scalar)  |
| UQDECD     | Unsigned saturating decrement vector by multiple of 64-bit predicate constraint element count | UQDECD(vector)  |
| UQDECP     | Unsigned saturating decrement scalar by the number of predicate elements that are TRUE        | UQDECP(scalar)  |
| UQDECP     | Unsigned saturating decrement vector by the number of predicate elements that are TRUE        | UQDECP(vector)  |
| UQINCB     | Unsigned saturating increment scalar by multiple of 8-bit predicate constraint element count  | UQINCB          |
| UQINCH     | Unsigned saturating increment scalar by multiple of 16-bit predicate constraint element count | UQINCH (scalar) |
| UQINCH     | Unsigned saturating increment vector by multiple of 16-bit predicate constraint element count | UQINCH (vector) |
| UQINCW     | Unsigned saturating increment scalar by multiple of 32-bit predicate constraint element count | UQINCW(scalar)  |
| UQINCW     | Unsigned saturating increment vector by multiple of 32-bit predicate constraint element count | UQINCW(vector)  |
| UQINCD     | Unsigned saturating increment scalar by multiple of 64-bit predicate constraint element count | UQINCD (scalar) |
| UQINCD     | Unsigned saturating increment vector by multiple of 64-bit predicate constraint element count | UQINCD (vector) |
| UQINCP     | Unsigned saturating increment scalar by the number of predicate elements that are TRUE        | UQINCP (scalar) |
| UQINCP     | Unsigned saturating increment vector by the number of predicate elements that are TRUE        | UQINCP (vector) |

## C3.9.7 Loop control

These instructions control counted vector loops and vector loops with data-dependent termination conditions. These instructions create a loop partition predicate with Active elements set to TRUE up to the point where the loop should

terminate, and FALSE thereafter. Two loop concepts are supported, simple loops and data-dependent loops.

## C3.9.7.1 Simple loops

An up-counting WHILE instruction that increments the value of the first scalar operand and compares the value with a second, fixed scalar operand. The instruction generates a destination predicate with all of the following characteristics:

- The predicate elements starting from the lowest numbered element are true while the comparison is true.
- The predicate elements thereafter, up to the highest numbered element, are false when the comparison becomes false.

All 32 bits or 64 bits of the scalar operands are significant for the purposes of comparison. The full 32-bit or 64-bit value of the first operand is incremented by 1 for each destination predicate element, irrespective of the element size. The first general-purpose register operand is not updated.

If all of the following occur, a comparison can never fail, resulting in an all-true predicate:

- The comparison includes an equality test.
- The second scalar operand is equal to the maximum integer value of the selected size and type of comparison.

The N, Z, C, and V condition flags are unconditionally set to control a subsequent conditional branch.

## Table C3-181 Single loop instructions

| Mnemonic   | Instruction                                                         | See                 |
|------------|---------------------------------------------------------------------|---------------------|
| WHILELE    | While incrementing signed scalar less than or equal to scalar       | WHILELE (predicate) |
| WHILELO    | While incrementing unsigned scalar lower than scalar                | WHILELO (predicate) |
| WHILELS    | While incrementing unsigned scalar lower than or the same as scalar | WHILELS (predicate) |
| WHILELT    | While incrementing signed scalar less than scalar                   | WHILELT (predicate) |

## C3.9.7.2 Data-independent loops

For data-dependent termination conditions, it is necessary to convert the result of a vector comparison into a loop partition predicate. The new partition truncates the current vector partition immediately before or after the first active TRUE comparison. The N, Z, C, and V condition flags are optionally set to control a subsequent conditional branch.

The BRKA instructions set active destination predicate elements to TRUE up to and including the first active TRUE element in their source predicate register, setting subsequent elements to FALSE.

The BRKB instructions set active destination predicate elements to TRUE up to but excluding the first active TRUE element in their source predicate register, setting subsequent elements to FALSE.

The BRKPA and BRKPB instructions propagate the result of a previous BRKB or BRKPB instruction, by setting their destination predicate register to all FALSE if the Last active element of their first source predicate register is not TRUE, but otherwise generate the destination predicate from their second source predicate as described for the BRKA and BRKB instructions.

The BRKN instructions propagate the result of a previous BRKB or BRKPB instruction by setting the destination predicate register to all FALSE if the Last active element of their first source predicate register is not TRUE, but otherwise leave the destination predicate unchanged. The destination and second source predicate must have been created by another instruction, such as RDFFR or WHILE .

## Table C3-182 Data-independent loop instructions

| Mnemonic   | Instruction                                                                                                 | See    |
|------------|-------------------------------------------------------------------------------------------------------------|--------|
| BRKA       | Break after the first true condition                                                                        | BRKA   |
| BRKAS      | Break after the first true condition, setting the condition flags                                           | BRKAS  |
| BRKB       | Break before the first true condition                                                                       | BRKB   |
| BRKBS      | Break before the first true condition, setting the condition flags                                          | BRKBS  |
| BRKN       | Propagate break to next partition                                                                           | BRKN   |
| BRKNS      | Propagate break to next partition, setting the condition flags                                              | BRKNS  |
| BRKPA      | Break after the first true condition, propagating from previous partition                                   | BRKPA  |
| BRKPAS     | Break after the first true condition, propagating from previous partition, setting the condition flags      | BRKPAS |
| BRKPB      | Break before the first true condition, propagating from the previous partition                              | BRKPB  |
| BRKPBS     | Break before the first true condition, propagating from the previous partition, setting the condition flags | BRKPBS |

## C3.9.7.3 Serialized operations

The Serialized operation instructions permit Active elements within a vector to be processed sequentially without unpacking the vector. The condition flags are unconditionally set to control a subsequent conditional branch.

## Table C3-183 Serialized operation instructions

| Mnemonic   | Instruction                               | See             |
|------------|-------------------------------------------|-----------------|
| PFIRST     | Set the First active element to TRUE      | PFIRST          |
| PNEXT      | Find next Active element                  | PNEXT           |
| CTERMEQ    | Compare and terminate loop when equal     | CTERMEQ,CTERMNE |
| CTERMNE    | Compare and terminate loop when not equal | CTERMEQ,CTERMNE |

## C3.9.8 SVE Move operations

## C3.9.8.1 Element move and broadcast

The Element move and broadcast instructions copy data from scalar registers, immediate values, and other vectors to all vector elements or only to Active vector elements. The copied data might be in an integer or floating-point format.

## Table C3-184 Element move and broadcast instructions

| Mnemonic   | Instruction                                             | See                                               |
|------------|---------------------------------------------------------|---------------------------------------------------|
| CPY        | Copy signed integer immediate to Active vector elements | CPY (immediate, merging) CPY (immediate, zeroing) |
|            | Copy general-purpose register to Active vector elements | CPY (scalar)                                      |
|            | Copy SIMD&FP scalar register to Active vector elements  | CPY (SIMD&FP scalar)                              |

| Mnemonic   | Instruction                                                     | See                                                                     |
|------------|-----------------------------------------------------------------|-------------------------------------------------------------------------|
| DUP        | Broadcast signed immediate to all vector elements               | DUP(immediate)                                                          |
| DUP        | Broadcast general-purpose register to all vector elements       | DUP(scalar)                                                             |
| FCPY       | Copy floating-point immediate to Active vector elements         | FCPY                                                                    |
| FDUP       | Broadcast floating-point immediate to all vector elements       | FDUP                                                                    |
| FMOV       | Move floating-point +0.0 to vector elements (unpredicated)      | FMOV(zero, unpredicated)                                                |
| FMOV       | Move floating-point +0.0 to vector elements (predicated)        | FMOV(zero, predicated)                                                  |
| FMOV       | Move floating-point immediate to vector elements (unpredicated) | FMOV(immediate, unpredicated)                                           |
| FMOV       | Move floating-point immediate to vector element (predicated)    | FMOV(immediate, predicated)                                             |
| MOV        | Move signed integer immediate to vector elements (unpredicated) | MOV(immediate, unpredicated)                                            |
| MOV        | Move signed integer immediate to vector elements (predicated)   | MOV(immediate, predicated, merging) MOV(immediate, predicated, zeroing) |
| MOV        | Move general-purpose register to vector elements (unpredicated) | MOV(scalar, unpredicated)                                               |
| MOV        | Move general-purpose register to vector elements (predicated)   | MOV(scalar, predicated)                                                 |
| MOV        | Move SIMD&FP scalar register to vector elements (unpredicated)  | MOV(SIMD&FP scalar, unpredicated)                                       |
| MOV        | Move SIMD&FP scalar register to vector elements (predicated)    | MOV(SIMD&FP scalar, predicated)                                         |
| MOV        | Move vector register (unpredicated)                             | MOV(vector, unpredicated)                                               |
| MOV        | Move vector register (predicated)                               | MOV(vector, predicated)                                                 |
| SEL        | Select vector elements from two vectors                         | SEL (predicates) SEL (vectors)                                          |

## C3.9.8.2 Element permute and shuffle

The Element permute and shuffle instructions move data between different vector elements, or between vector elements and scalar registers.

These instructions perform the following operations:

- Conditionally extract the Last active element of a vector or the following element.
- -The supported instructions are CLASTA and CLASTB .
- Unconditionally extract the Last active element of a vector or the following element.
- -The supported instructions are LASTA and LASTB .
- Variable permute instructions where the permutation is determined by the values in a predicate register or a table of element index values.
- -The supported instructions are COMPACT , SPLICE , and TBL .
- Fixed permute instructions where the form of the permutation is encoded in the instruction.
- -The supported instructions are: DUP , EXT , INSR , REV , REVB , REVH , REVW , SUNPKHI , SUNPKLO , TRN1 , TRN2 , UUNPKHI , UUNPKLO , UZP1 , UZP2 , ZIP1 , and ZIP2 .

## Table C3-185 Element permute and shuffle instructions

| Mnemonic   | Instruction                                                                             | See                     |
|------------|-----------------------------------------------------------------------------------------|-------------------------|
| CLASTA     | Conditionally extract element after the Last active element to general-purpose register | CLASTA (scalar)         |
|            | Conditionally extract element after the Last active element to SIMD&FP scalar           | CLASTA (SIMD&FP scalar) |

| Mnemonic   | Instruction                                                               | See                               |
|------------|---------------------------------------------------------------------------|-----------------------------------|
|            | Conditionally extract element after the Last active element to vector     | CLASTA (vectors)                  |
| CLASTB     | Conditionally extract Last active element to general-purpose register     | CLASTB (scalar)                   |
| CLASTB     | Conditionally extract Last active element to SIMD&FP scalar               | CLASTB (SIMD&FP scalar)           |
| CLASTB     | Conditionally extract Last active element to vector                       | CLASTB (vectors)                  |
| LASTA      | Extract element after the Last active element to general-purpose register | LASTA (scalar)                    |
| LASTA      | Extract element after the Last active element to SIMD&FP scalar           | LASTA (SIMD&FP scalar)            |
| LASTB      | Extract Last active element to general-purpose register                   | LASTB (scalar)                    |
| LASTB      | Extract Last active element to SIMD&FP scalar                             | LASTA (SIMD&FP scalar)            |
| COMPACT    | Copy Active vector elements to lower-numbered elements                    | COMPACT                           |
| SPLICE     | Splice two vectors under predicate control                                | SPLICE                            |
| TBL        | Programmable table lookup using vector of element indexes                 | TBL                               |
| DUP        | Broadcast indexed vector element                                          | DUP(indexed)                      |
| EXT        | Extract vector from pair of vectors                                       | EXT                               |
| INSR       | Insert general-purpose register into shifted vector                       | INSR (scalar)                     |
| INSR       | Insert SIMD&FP scalar register into shifted vector                        | INSR (SIMD&FP scalar)             |
| MOV        | Move indexed element or SIMD&FP scalar to vector (unpredicated)           | MOV(SIMD&FP scalar, unpredicated) |
| MOV        | Move SIMD&FP scalar register to vector elements (predicated)              | MOV(SIMD&FP scalar, predicated)   |
| REV        | Reverse all elements in vector                                            | REV(vector)                       |
| REVB       | Reverse 8-bit bytes in elements                                           | REVB,REVH,REVW                    |
| REVH       | Reverse 16-bit halfwords in elements                                      | REVB,REVH,REVW                    |
| REVW       | Reverse 32-bit words in elements                                          | REVB,REVH,REVW                    |
| TRN1       | Interleave even elements from two vectors                                 | TRN1, TRN2 (vectors)              |
| TRN2       | Interleave odd elements from two vectors                                  | TRN1, TRN2 (vectors)              |
| UZP1       | Concatenate even elements from two vectors                                | UZP1, UZP2 (vectors)              |
| UZP2       | Concatenate odd elements from two vectors                                 | UZP1, UZP2 (vectors)              |
| ZIP1       | Interleave elements from low halves of two vectors                        | ZIP1, ZIP2 (vectors)              |
| ZIP2       | Interleave elements from high halves of two vectors                       | ZIP1, ZIP2 (vectors)              |

## C3.9.8.3 Unpacking instructions

The Unpacking instructions unpack half of the elements from the source vector register or predicate register, widen the unpacked elements to twice the width, and place the result in the destination register.

## Table C3-186 Unpacking instructions

| Mnemonic   | Instruction                                              | See              |
|------------|----------------------------------------------------------|------------------|
| SUNPKHI    | Unpack and sign-extend elements from high half of vector | SUNPKHI, SUNPKLO |
| SUNPKLO    | Unpack and sign-extend elements from low half of vector  | SUNPKHI, SUNPKLO |
| UUNPKHI    | Unpack and zero-extend elements from high half of vector | UUNPKHI,UUNPKLO  |
| UUNPKLO    | Unpack and zero-extend elements from low half of vector  | UUNPKHI,UUNPKLO  |

| Mnemonic   | Instruction                                           | See              |
|------------|-------------------------------------------------------|------------------|
| PUNPKHI    | Unpack and widen elements from high half of predicate | PUNPKHI, PUNPKLO |
| PUNPKLO    | Unpack and widen elements from low half of predicate  | PUNPKHI, PUNPKLO |

## C3.9.8.4 Predicate permute

The Predicate instructions are used to move and permute predicate elements. These instructions generally mirror the fixed vector permutes to allow predicates to follow their data. The permutes move all of the bits in a predicate element, not just the canonical bits.

## Table C3-187 Predicate instructions

| Mnemonic   | Instruction                                            | See                     |
|------------|--------------------------------------------------------|-------------------------|
| REV        | Reverse all elements in predicate                      | REV(predicate)          |
| TRN1       | Interleave even elements from two predicates           | TRN1, TRN2 (predicates) |
| TRN2       | Interleave odd elements from two predicates            | TRN1, TRN2 (predicates) |
| UZP1       | Select even elements from two predicates               | UZP1, UZP2 (predicates) |
| UZP2       | Select odd elements from two predicates                | UZP1, UZP2 (predicates) |
| ZIP1       | Interleave elements from low halves of two predicates  | ZIP1, ZIP2 (predicates) |
| ZIP2       | Interleave elements from high halves of two predicates | ZIP1, ZIP2 (predicates) |

## C3.9.9 Index vector generation

The INDEX instruction initializes a vector horizontally by setting its first element to an integer value, and then repeatedly incrementing it by a second integer value to generate the subsequent elements. Each integer value can be specified as a signed immediate or a general-purpose register.

## Table C3-188 Index instructions

| Mnemonic   | Instruction                                                                              | See                       |
|------------|------------------------------------------------------------------------------------------|---------------------------|
| INDEX      | Create index vector starting from and incremented by immediates                          | INDEX (immediates)        |
| INDEX      | Create index vector starting from immediate and incremented by general-purpose register  | INDEX (scalars)           |
| INDEX      | Create index vector starting from general-purpose register and incremented by immediate  | INDEX (scalar, immediate) |
| INDEX      | Create index vector starting from immediate and incremented by general-purpose registers | INDEX (immediate, scalar) |

## C3.9.10 Move prefix

The MOVPRFX (predicated) instruction is a predicated vector move that can be combined with a predicated destructive instruction that immediately follows it, in program order, to create a single constructive operation, or to convert an instruction with merging predication to use zeroing predication.

The MOVPRFX (unpredicated) instruction is an unpredicated vector move that can be combined with a predicated or unpredicated destructive instruction that immediately follows it, in program order, to create a single constructive operation.

The Operational information section of an SVE instruction description indicates whether or not an instruction can be predictably prefixed by a MOVPRFX instruction. If the Operational information of an SVE instruction description does not mention MOVPRFX or if the section does not exist, then the instruction cannot be predictably prefixed by a MOVPRFX instruction.

The prefixed instruction that immediately follows a MOVPRFX instruction in program order must be an implemented SVE instruction that can be predictably prefixed by a MOVPRFX instruction, or an A64 HLT instruction, or an A64 BRK instruction. For an SVE instruction that can be predictably prefixed by a MOVPRFX instruction, all of the following apply:

- The destination register field implicitly specifies one of the source operands, which means that it is a destructive binary or ternary vector operation or unary operation with merging predication, excluding MOVPRFX .
- The destination register is the same as the MOVPRFX destination register.
- The prefixed instruction does not use the MOVPRFX destination register in any of its other source register fields, even if it has a different name but refers to the same architectural register state. For example, Z1, V1, and D1 all refer to the same architectural register.
- If the MOVPRFX instruction is predicated, then the prefixed instruction is predicated using the same Governing predicate register, and the maximum encoded element size is the same as the MOVPRFX element size, excluding the fixed-size 64-bit elements of the wide elements form of bitwise shift and integer compare operations.
- If the MOVPRFX instruction is unpredicated, then the prefixed instruction can use any Governing predicate register and element size, or it can be unpredicated. A predicated MOVPRFX cannot be used with an unpredicated instruction.

If the instruction that follows a MOVPRFX instruction is not an implemented SVE instruction that can be predictably prefixed by a MOVPRFX instruction, the two instructions behave in one of the following CONSTRAINED UNPREDICTABLE ways:

- Either or both instructions can execute with their individually described effects.
- Either instruction can generate an Undefined Instruction exception.
- Either or both instructions can execute as a NOP .
- The second instruction can execute with an UNKNOWN value for any of its source registers.
- Any register that is written by either or both instructions can be set to an unknown value.
- Acontrol flow instruction that writes the PC can set the PC to an unknown value.

## Table C3-189 Move prefix instructions

| Mnemonic   | Instruction                | See                   |
|------------|----------------------------|-----------------------|
| MOVPRFX    | Move prefix (predicated)   | MOVPRFX(predicated)   |
|            | Move prefix (unpredicated) | MOVPRFX(unpredicated) |

Unless the combination of a constructive operation with merging predication is specifically required, it is strongly recommended that, for performance reasons, software should prefer to use the zeroing form of predicated MOVPRFX or the unpredicated MOVPRFX instruction.

When a MOVPRFX instruction is executed, except for PMU events SVE\_MOVPRFX\_SPEC, SVE\_MOVPRFX\_Z\_SPEC, SVE\_MOVPRFX\_M\_SPEC, and SVE\_MOVPRFX\_U\_SPEC, 0x807C -0x807F , it is IMPLEMENTATION DEFINED for each execution of the instruction whether or not any Performance Monitor counts the instruction. This can vary dynamically for each execution of the same instruction.

When a microarchitectural operation is executed because of a MOVPRFX instruction, except for PMU events SVE\_MOVPRFX\_SPEC, SVE\_MOVPRFX\_Z\_SPEC, SVE\_MOVPRFX\_M\_SPEC, and SVE\_MOVPRFX\_U\_SPEC, 0x807C -0x807F , it is IMPLEMENTATION DEFINED for each execution of the operation whether or not the Performance Monitor counts the operation. This can vary dynamically for each execution of the same instruction.

## C3.9.10.1 MOVPRFX instruction behavior in self-hosted debug

A MOVPRFX instruction can legally prefix a BRK or HLT instruction.

If a hardware breakpoint is programmed with the address of a legal MOVPRFX instruction, when any of the following events occur, the hardware breakpoint generates a Breakpoint exception:

- The MOVPRFX instruction is committed for execution.
- The combined MOVPRFX and Prefixed instruction is committed for execution.

If a hardware breakpoint is programmed with the address of an illegal MOVPRFX instruction or a Prefixed instruction, when any of the MOVPRFX instruction and Prefixed instruction are committed for execution, it is CONSTRAINED UNPREDICTABLE whether or not the hardware breakpoint generates a Breakpoint exception.

If a single-step is performed for a MOVPRFX instruction, it is CONSTRAINED UNPREDICTABLE whether the PE steps over the pair of instructions or steps over only the MOVPRFX instruction.

## C3.9.11 Reduction operations

## C3.9.11.1 Horizontal reductions

The Horizontal reduction instructions perform arithmetic horizontally across Active elements of a single source vector and deliver a scalar result.

The floating-point horizontal accumulating sum instruction, FADDA , operates strictly in order of increasing element number across a vector, using the scalar destination register as a source for the initial value of the accumulator. This preserves the original program evaluation order where non-associativity is required.

The other floating-point reductions calculate their result using a recursive pair-wise algorithm that does not preserve the original program order, but permits increased parallelism for code that does not require strict order of evaluation.

Integer reductions are fully associative, and the order of evaluation is not specified by the architecture.

Table C3-190 Horizontal reduction instructions

| Mnemonic   | Instruction                                                                                       | See     |
|------------|---------------------------------------------------------------------------------------------------|---------|
| ANDV       | Bitwise ANDreduction, treating Inactive elements as all ones                                      | ANDV    |
| EORV       | Bitwise EORreduction, treating Inactive elements as zero                                          | EORV    |
| FADDA      | Floating-point add strictly-ordered reduction, accumulating in scalar, ignoring Inactive elements | FADDA   |
| FADDV      | Floating-point add recursive reduction, treating Inactive elements as +0.0                        | FADDV   |
| FMAXNMV    | Floating-point maximum number recursive reduction, treating Inactive elements as the default NaN  | FMAXNMV |
| FMAXV      | Floating-point maximum recursive reduction, treating Inactive elements as negative infinity       | FMAXV   |
| FMINNMV    | Floating-point minimum number recursive reduction, treating Inactive elements as the default NaN  | FMINNMV |
| FMINV      | Floating-point minimum recursive reduction, treating Inactive elements as positive infinity       | FMINV   |
| ORV        | Bitwise ORreduction, treating Inactive elements as zero                                           | ORV     |
| SADDV      | Signed add reduction, treating Inactive elements as zero                                          | SADDV   |
| SMAXV      | Signed maximum reduction, treating Inactive elements as the minimum signed integer                | SMAXV   |
| SMINV      | Signed minimum reduction, treating Inactive elements the maximum signed integer                   | SMINV   |
| UADDV      | Unsigned add reduction, treating Inactive elements as zero                                        | UADDV   |
| UMAXV      | Unsigned maximum reduction, treating Inactive elements as zero                                    | UMAXV   |
| UMINV      | Unsigned minimum reduction, treating Inactive elements as the maximum unsigned integer            | UMINV   |